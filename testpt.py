def af(a):
    print(a)



def main():

    # buse = [17, 22, 10] #리얼
    # # buse = [9, 18, 12] #테스트용 
    # poong = [66, 61, 14]
    # cg = [10, 9, 10]

    # books = {
    #     'buse' : {
    #         'now' : [buse[0], buse[1], buse[2]],
    #         'goal' : [0, 0, 0],
    #         'need' : [0, 0, 0],
    #         'surplus' : [0, 0, 0],
    #         'mix_cnt' : [0, 0],
    #         'state' : False,
    #         'name' : "부세"
    #     },
    #     'poong' : {
    #         'now' : [poong[0], poong[1], poong[2]],
    #         'goal' : [0, 0, 0],
    #         'need' : [0, 0, 0],
    #         'surplus' : [0, 0, 0],
    #         'mix_cnt' : [0, 0],
    #         'state' : False,
    #         'name' : "풍아"
    #     },
    #     'cg' : {
    #         'now' : [cg[0], cg[1], cg[2]],
    #         'goal' : [0, 0, 0],
    #         'need' : [0, 0, 0],
    #         'surplus' : [0, 0, 0],
    #         'mix_cnt' : [0, 0],
    #         'state' : False,
    #         'name' : "천광"
    #     }
    # }

    # for i in books.keys():
    #     print(books[i]['need'][0])

    """ 무기를 1에서 90까지 돌파하는데 비경 재료를 모으려면 몇판을 돌아야할까"""

    #비경 최고레벨 기준 레진 20당 한판에 1등급 2.21 2등급 2.40 3등급 0.64 4등급 0.07 개 드랍된다고 함
    # 3 9 9 4
    # 3+9*3+9*3*3+4*3*3*3
    # 3 + 27 + 81 + 108 = 219
    # 1성재료 219개 쯤하는 가치
    cnt = 0 #비경 돈 횟수
    now = [0, 0, 0, 0]
    goal = [3, 9, 9, 4]
    while True:
        cnt +=1
        now[0] += 2.21
        now[1] += 2.4
        now[2] += 0.64
        now[3] += 0.07

        if now[0] >= goal[0] and now[1] >= goal[1] and now[2] >= goal[2] and now[3] >= goal[3]: break

        if now[0] >= goal[0]:
            surplus = now[0] - goal[0]
            now[1] += surplus//3
            now[0] = goal[0] + surplus%3

        if now[1] >= goal[1]:
            surplus = now[1] - goal[1]
            now[2] += surplus//3
            now[1] = goal[1] + surplus%3

        if now[2] >= goal[2]:
            surplus = now[2] - goal[2]
            now[3] += surplus//3
            now[2] = goal[2] + surplus%3

    print(cnt,"\n")
    print(now)

    ads = 2.2/3 * 12/11 + 1.97
    print(ads)
    ads = ads/3 * 12/11
    print(ads)
    ads = ads + 0.24
    print(ads,"\n")

    cnt = 0 #비경 돈 횟수
    now = [62, 53, 16]
    goal = [9, 63, 82]
    while True:
        cnt +=1
        now[0] += 2.2
        now[1] += 1.97
        now[2] += 0.24

        if now[0] >= goal[0] and now[1] >= goal[1] and now[2] >= goal[2]: break

        if now[0] >= goal[0]:
            surplus = now[0] - goal[0]
            now[1] += surplus//3
            now[0] = goal[0] + surplus%3

        if now[1] >= goal[1]:
            surplus = now[1] - goal[1]
            now[2] += surplus//3
            now[1] = goal[1] + surplus%3


    print(cnt,"\n")
    print(now)





main()