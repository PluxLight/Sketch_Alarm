import datetime as dt

#레진 8분마다 1씩 충전
#시간단위는 분으로 



def time_clac():
    # time_goal = dt.datetime(2021,8,11,10,30,0).strftime('%Y-%m-%d %H:%M:%S')
    # time_now = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    time_goal = dt.datetime(2021,8,11,10,30,0)
    time_now = dt.datetime.now()

    print('지금 시간 : ' + str(time_now))
    print('목표 시간 : ' + str(time_goal))

    lezhin_now = 60
    lezhin_goal = 155
    lezhin_con_now = 5 #현재 농축레진
    lezhin_con_goal = 5 #목표 시간에 보유할 농축레진
    time_plus = 0

    print(f"\n현재 레진 : {lezhin_now}\
            \n목표 레진 : {lezhin_goal}\
            \n현재 농레 : {lezhin_con_now}\
            \n목표 농레 : {lezhin_con_goal}\n")

    lezhin_con_need = max(lezhin_con_goal - lezhin_con_now, 0)
    if lezhin_con_need != 0:
        time_plus = lezhin_con_need*40*8

    time_plus += lezhin_goal * 8

    time_start_charge = time_goal - dt.timedelta(minutes=time_plus)
    print('충전 시작 시간 : ' + str(time_start_charge) + ' 단, 이 때 레진이 0 이라고 가정\n')
    time_surplus = time_start_charge - time_now
    print('잉여 시간 : ' + str(time_surplus))
    time_sur = str(time_surplus).split(':')
    # print(time_sur[0], time_sur[1])
    # print(time_sur[0][0])
    if (time_sur[0][0] == '-'):
        print("Not Have Time Surplus")
    else:
        lezhin_surplus = ( (int(time_sur[0]) * 60) + int(time_sur[1]) )//8
        # print('잉여 레진 : ' + str(lezhin_surplus))
        print(f'잉여 레진 : {lezhin_surplus} (목표 시간전까지 모을 수 있는 레진 양)')


if __name__ == "__main__":
    time_clac()