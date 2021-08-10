import datetime as dt

MAX_LEZHIN = 160
LEZHIN = 20
LEZHIN_CON = 40

#레진 8분마다 1씩 충전
#시간단위는 분으로 



def time_clac():
    # time_goal = dt.datetime(2021,8,11,10,30,0).strftime('%Y-%m-%d %H:%M:%S')
    # time_now = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f'{MAX_LEZHIN}')

    time_goal = dt.datetime(2021,8,11,10,30,0)
    time_now = dt.datetime.now()

    print('지금 시간 : ' + str(time_now))
    print('목표 시간 : ' + str(time_goal))

    lezhin_now = 73
    lezhin_goal = 155
    lezhin_con_now = 5 #현재 농축레진
    lezhin_con_goal = 5 #목표 시간에 보유할 농축레진
    time_plus = 0
    lezhin_surplus = 0

    print(f"\n현재 레진 : {lezhin_now}\
            \n목표 레진 : {lezhin_goal}\
            \n현재 농레 : {lezhin_con_now}\
            \n목표 농레 : {lezhin_con_goal}\n")

    lezhin_con_need = max(lezhin_con_goal - lezhin_con_now, 0)
    if lezhin_con_need != 0:
        if lezhin_now>=40:
            print(f'현재 보유중인 레진 {lezhin_now-lezhin_now%40}를 소모하여 농축 레진 {lezhin_now//40}개를 생성합니다')
            lezhin_con_now += lezhin_now//40
            lezhin_now = lezhin_now%40
            lezhin_con_need = max(lezhin_con_goal - lezhin_con_now, 0)
        time_plus = lezhin_con_need*40*8

    time_plus += lezhin_goal * 8

    time_start_charge = time_goal - dt.timedelta(minutes=time_plus)
    print(f'충전 시작 시간 : {time_start_charge}  단, 이 때 레진이 0 이라고 가정\n')
    time_surplus = time_start_charge - time_now
    print(f'잉여 시간 : {time_surplus}')
    time_sur = str(time_surplus).split(':')


    
    if (time_sur[0][0] == '-'):
        print("Not Have Time Surplus")
    else:
        lezhin_surplus = ( (int(time_sur[0]) * 60) + int(time_sur[1]) )//8
        # print('잉여 레진 : ' + str(lezhin_surplus))
        print(f'잉여 레진 : {lezhin_surplus + lezhin_now} (목표 시간전까지 모을 수 있는 레진 양)')

        lezhin_surplus += lezhin_now
        if lezhin_surplus%20 > MAX_LEZHIN-lezhin_goal:
            print(f'잉여 레진이 비경 등으로 레진을 소모하여도 과하게 남으므로 일부 시간을 조정합니다\n')
            time_sup = (LEZHIN-lezhin_surplus%20)*8
            time_start_charge = time_start_charge + dt.timedelta(minutes=time_sup)
            print(f'{LEZHIN-lezhin_surplus%20}레진을 더 모아 레진을 전부 소모합니다')
            print(f'충전 시작 시간은 {time_start_charge}로 조정됐으며')
            temp = time_goal - time_start_charge
            print(temp)
            temp = str(temp).split(':')
            temp = int(temp[0])*60 + int(temp[1])
            temp = temp//8
            print(f'예상 충전량은 {temp}입니다')

        print()


if __name__ == "__main__":
    time_clac()