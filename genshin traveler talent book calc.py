#조합해서 필요한 특성 책 수량만큼 구할 수 있는지
#지금 위에서 필요한걸 아래에 요구해서 가능한지 알아보는 방식으로 했는데
#그냥 아래에서 먼저 위에 물어서 잉여물을 주는식으로 해야겠다
#어차피 물어볼 단계가 많은것도 아니고...
#이렇게 하는 목적은 3단계는 안되더라도 2단계는 레벨업에 쓰이는 만큼 조합 가능하면 특성레벨 얼마나 올릴수 있나 확인하게

#그리고 특성 적용해서 계산하는것도 ...

#ver 1.0

def mix_book(now_book, need_book, surplus_book, mix_cnt, book_name):

    tf = True

    if need_book[1] > 0: #2단계 책이 부족한경우
        if  surplus_book[0]//3 >= need_book[1]:
            mix_cnt[0] += need_book[1]
            surplus_book[0] = surplus_book[0] - need_book[1]*3
            now_book[0] = now_book[0] - need_book[1]*3
            now_book[1] = now_book[1] + need_book[1]
            need_book[1] = 0
        else:
            tf = False


    if need_book[2] > 0: #3단계 책이 부족한경우
        if surplus_book[1]//3 >= need_book[2]: #2단계 책 잉여분만으로도 커버 가능한 경우
                    mix_cnt[1] += need_book[2]
                    surplus_book[1] = surplus_book[1] - need_book[2]*3
                    now_book[1] = now_book[1] - need_book[2]*3
                    now_book[2] = now_book[2] + need_book[2]
                    need_book[2] = 0
        else:
            if (surplus_book[1] + surplus_book[0]//3)//3 >= need_book[2]: #영혼까지 끌어모으면 가능한 경우
                mix_cnt[0] += (need_book[2]*3 - surplus_book[1])
                mix_cnt[1] += need_book[2]
                surplus_book[0] = surplus_book[0] - (need_book[2]*3 - surplus_book[1])*3
                now_book[0] = now_book[0] - (need_book[2]*3 - surplus_book[1])*3
                now_book[1] = now_book[1] - surplus_book[1]
                surplus_book[1] = 0
                now_book[2] = now_book[2] + need_book[2]
                need_book[2] = 0
            else: #영혼까지 끌어모아도 안되는 경우
                tf = False
            
    if need_book[0] > 0: #1단계 책이 부족한경우
        tf=False
    
    return tf


def limit_level(now_lv, goal_lv, buse, poong, cg, goal_buse, goal_poong, goal_cg, book_state):
        #           2단계       3단계        4단계      5단계       6단계       7단계       8단계       9단계         10단계
    goal_book = ["buse 1 3", "poong 2 2", "cg 2 4", "buse 2 6", "poong 2 9", "cg 3 4", "buse 3 6", "poong 3 12", "cg 3 16"]
        #           0번          1번         2번         3번          4번       5번         6번          7번         8번
    goal_mora = [12500, 17500, 25000, 30000, 37500, 120000, 260000, 450000, 700000]

    book_name = ["부세", "풍아", "천광"]
    talent_name = ["평타", "전투스킬", "원소폭발"]
    book_name_cnt = 0
    sum_mora = 0

    now_books = [buse, poong, cg]
    goal_books = [goal_buse, goal_poong, goal_cg]

    #여기서 할 것 부족한 상태에서 얼마나 찍을 수 있는가
    #나중에 우선순위 값 줘서 뭐부터 올릴지....
    #지금은 평타->전투->폭발 순

    #일단 조합 안하고 넘긴 애부터 조합해버리자
    for state in book_state:
        if state == True: #책이 충분한 경우는 넘기고
            pass
        else: #모자라서 조합안하고 그냥 넘긴건 여기서 잉여분만큼 조합해서 올리고
            for i in range(0,2):
                if now_books[book_name_cnt][i] > goal_books[book_name_cnt][i]:
                    surplus = now_books[book_name_cnt][i] - goal_books[book_name_cnt][i]
                    now_books[book_name_cnt][i+1] = now_books[book_name_cnt][i+1] + surplus//3
                    now_books[book_name_cnt][i] = goal_books[book_name_cnt][i] + surplus%3
        book_name_cnt +=1


    for i in range(0,3):
        lvup_state = True
        lv_cnt = now_lv[i]+1
        front_lv = now_lv[i] #범위 앞
        back_lv = goal_lv[i] #범위 뒤

        if front_lv == back_lv or back_lv == 0 or back_lv == 1:
            print("{0}특성은 설정대로 레벨업 하지 않고 넘어갑니다".format(talent_name[i]))
            continue

        for j in range(front_lv-1, back_lv-1):
            book, lv, ea = goal_book[j].split(" ")
            lv = int(lv)
            ea = int(ea)

            if book == "buse":
                if buse[lv-1] - ea >= 0:
                    buse[lv-1] = buse[lv-1] - ea
                    sum_mora += goal_mora[j]
                else:
                    print("{0}레벨업에 실패했습니다. {1}특성은 현재 {2}까지 레벨업 가능합니다".format(lv_cnt, talent_name[i], lv_cnt-1))
                    lvup_state = False
                    continue
            elif book == "poong":
                if poong[lv-1] - ea >= 0:
                    poong[lv-1] = poong[lv-1] - ea
                    sum_mora += goal_mora[j]
                else:
                    print("{0}레벨업에 실패했습니다. {1}특성은 현재 {2}까지 레벨업 가능합니다".format(lv_cnt, talent_name[i], lv_cnt-1))
                    lvup_state = False
                    continue
            else:
                if cg[lv-1] - ea >= 0:
                    cg[lv-1] = cg[lv-1] - ea
                    sum_mora += goal_mora[j]
                else:
                    print("{0}레벨업에 실패했습니다. {1}특성은 현재 {2}까지 레벨업 가능합니다".format(lv_cnt, talent_name[i], lv_cnt-1))
                    lvup_state = False
                    continue
            lv_cnt += 1

        if lvup_state == True:
            print("{0}특성은 목표한 {1}레벨업까지 가능합니다".format(talent_name[i], back_lv))

    for i in range(0,3):
        print("레벨 업 후 남은 책은 {0}의 가르침 {1}권, 인도 {2}권, 철학 {3}권 입니다".
        format(book_name[i], now_books[i][0], now_books[i][1], now_books[i][2]))
    print("특성 레벨 업에 필요한 모라는 총 {0}모라 입니다".format(sum_mora))
    
def try_domain(books):
    return max(sum([books[2]*9, books[1]*3, books[0]])//8, 1)






#값 = 유저가 소유한 [1단계, 2단계, 3단계] 부세, 풍아, 천광, /  현재 [무기, 전투, 폭발] 특성레벨, 목표 특성레벨
def calc_book(buse, poong, cg, now_lv, goal_lv): 

    #목표
    goal_buse = [0, 0, 0]
    goal_poong = [0, 0, 0]
    goal_cg = [0, 0, 0]
    goal_books = [goal_buse, goal_poong, goal_cg]

    #필요
    need_buse = [0, 0, 0]
    need_poong = [0, 0, 0]
    need_cg = [0, 0, 0]
    need_books = [need_buse, need_poong, need_cg]

    #잉여
    surplus_buse = []
    surplus_poong = []
    surplus_cg = []
    surplus_books = [surplus_buse, surplus_poong, surplus_cg]

    mix_cnt_buse = [0,0]
    mix_cnt_poong = [0,0]
    mix_cnt_cg = [0,0]

    book_state = [False, False, False] #부세, 풍아, 천광 순
    book_name = ["부세", "풍아", "천광"]

    
    #               2단계       3단계        4단계      5단계       6단계       7단계       8단계       9단계         10단계
    goal_book = ["buse 1 3", "poong 2 2", "cg 2 4", "buse 2 6", "poong 2 9", "cg 3 4", "buse 3 6", "poong 3 12", "cg 3 16"]
        #           0번          1번         2번         3번          4번       5번         6번          7번         8번

    #유저가 설정한 레벨까지 필요한 책 계산
    for i in range(0,3):
        front_lv = now_lv[i] #범위 앞
        back_lv = goal_lv[i] #범위 뒤

        if front_lv == back_lv or back_lv == 0 or back_lv == 1: continue

        for j in range(front_lv-1, back_lv-1):
            book, lv, ea = goal_book[j].split(" ")
            lv = int(lv)
            ea = int(ea)

            if book == "buse":
                goal_buse[lv-1] = goal_buse[lv-1] + ea
            elif book == "poong":
                goal_poong[lv-1] = goal_poong[lv-1] + ea
            else:
                goal_cg[lv-1] = goal_cg[lv-1] + ea

    #부족한 책 수량 계산
    for i in range(0,3):
        need_buse[i] = max(goal_buse[i] - buse[i], 0)
        need_poong[i] = max(goal_poong[i] - poong[i], 0)
        need_cg[i] = max(goal_cg[i] - cg[i], 0)

    #잉여 책 수량 계산
    for i in range(0,3):
        surplus_buse.append(max(buse[i] - goal_buse[i], 0))
        surplus_poong.append(max(poong[i] - goal_poong[i], 0))
        surplus_cg.append(max(cg[i] - goal_cg[i], 0))

    #현 상태 출력
    print("소요되는 책은 부세의 가르침 {0}권, 인도 {1}권, 철학 {2}권 입니다".format(goal_buse[0], goal_buse[1], goal_buse[2]))
    print("부족한 책은 부세의 가르침 {0}권, 인도 {1}권, 철학 {2}권 입니다".format(need_buse[0], need_buse[1], need_buse[2]))
    print("잉여 책은 부세의 가르침 {0}권, 인도 {1}권, 철학 {2}권 입니다\n".format(surplus_buse[0], surplus_buse[1], surplus_buse[2]))

    print("소요되는 책은 풍아의 가르침 {0}권, 인도 {1}권, 철학 {2}권 입니다".format(goal_poong[0], goal_poong[1], goal_poong[2]))
    print("부족한 책은 풍아의 가르침 {0}권, 인도 {1}권, 철학 {2}권 입니다".format(need_poong[0], need_poong[1], need_poong[2]))
    print("잉여 책은 풍아의 가르침 {0}권, 인도 {1}권, 철학 {2}권 입니다\n".format(surplus_poong[0], surplus_poong[1], surplus_poong[2]))

    print("소요되는 책은 천광의 가르침 {0}권, 인도 {1}권, 철학 {2}권 입니다".format(goal_cg[0], goal_cg[1], goal_cg[2]))
    print("부족한 책은 천광의 가르침 {0}권, 인도 {1}권, 철학 {2}권 입니다".format(need_cg[0], need_cg[1], need_cg[2]))
    print("잉여 책은 천광의 가르침 {0}권, 인도 {1}권, 철학 {2}권 입니다\n".format(surplus_cg[0], surplus_cg[1], surplus_cg[2]))

    if need_buse.count(0) == 3: #부족한 게 전부 0이라 조합이 필요없음
        book_state[0] = True 
    else: #부족한 게 있음
        book_state[0] = mix_book(buse, need_buse, surplus_buse, mix_cnt_buse, "buse")

    if need_poong.count(0) == 3: #부족한 게 전부 0이라 조합이 필요없음
        book_state[1] = True 
    else: #부족한 게 있음
        book_state[1] = mix_book(poong, need_poong, surplus_poong, mix_cnt_poong, "poong")

    if need_cg.count(0) == 3: #부족한 게 전부 0이라 조합이 필요없음
        book_state[2] = True 
    else: #부족한 게 있음
        book_state[2] = mix_book(cg, need_cg, surplus_cg, mix_cnt_cg, "cg")

    
    if False not in book_state:
        print("목표 특성 레벨까지 레벨 업이 가능합니다")
        
    else:
        print("목표 특성 레벨까지 레벨 업이 불가능합니다")
        book_name_cnt = 0

    book_name_cnt = 0
    for mix_cnt in [mix_cnt_buse, mix_cnt_poong, mix_cnt_cg]:
        if book_state[book_name_cnt] == True and mix_cnt.count(0) != 2:
            print("{0}의 가르침을 {1}개 소모하여 인도를 {2}권 만들어야 합니다".format(book_name[book_name_cnt], mix_cnt[0]*3, mix_cnt[0]))
            print("{0}의 인도를 {1}개 소모하여 철학을 {2}권 만들어야 합니다".format(book_name[book_name_cnt], mix_cnt[1]*3, mix_cnt[1]))
        else:
            if book_state[book_name_cnt] == True and mix_cnt.count(0) == 2:
                print("{0}는 합성이 불필요합니다".format(book_name[book_name_cnt]))
            else:
                print("{0}는 재료가 부족합니다".format(book_name[book_name_cnt]))
        book_name_cnt += 1

    print("")

    book_name_cnt = 0
    sum_try = 0
    for state in book_state:
        if state == False:
            sum_try += try_domain(need_books[book_name_cnt])
        book_name_cnt += 1
    print("부족한 수량만큼 최소 {0}번의 비경을 도전해야합니다. 소모 레진은 {1}입니다\n".format(sum_try, sum_try*20))


    #일단 남는거 다 조합해서 얼마나 레벨 올릴수 있을까?
    limit_level(now_lv, goal_lv, buse, poong, cg, goal_buse, goal_poong, goal_cg, book_state)




def main():
    # 현재 책 수량 단계가 낮을수록 리스트 앞에 있음
    now_buse = [17, 22, 10] #리얼
    # now_buse = [9, 18, 12] #테스트용 
    now_poong = [66, 61, 14]
    now_cg = [10, 9, 10]

    now_lv = [1,1,1]
    goal_lv = [1,9,9]

    print("무기, 전투, 폭발 순으로 현재 특성 레벨은 {0}, {1}, {2} 이 설정됐고".format(now_lv[0], now_lv[1], now_lv[2]))
    print("무기, 전투, 폭발 순으로 목표 특성 레벨은 {0}, {1}, {2} 이 설정됐습니다\n".format(goal_lv[0], goal_lv[1], goal_lv[2]))

    print("현재 부세의 가르침 {0}권, 인도 {1}권, 철학 {2}권 보유 중으로 설정되었습니다".format(now_buse[0], now_buse[1], now_buse[2]))
    print("현재 풍아의 가르침 {0}권, 인도 {1}권, 철학 {2}권 보유 중으로 설정되었습니다".format(now_poong[0], now_poong[1], now_poong[2]))
    print("현재 천광의 가르침 {0}권, 인도 {1}권, 철학 {2}권 보유 중으로 설정되었습니다".format(now_cg[0], now_cg[1], now_cg[2]))

    print("")

    #값 = 유저가 소유한 [1단계, 2단계, 3단계] 부세, 풍아, 천광, /  현재 [무기, 전투, 폭발] 특성레벨, 목표 특성레벨
    calc_book(now_buse, now_poong, now_cg, now_lv, goal_lv)

main()

#행추 캐릭터 특성 소재 합성 시 25%의 확률로 일부 합성 재료를 반환한다.
#합성 계산할 때 합성횟수 * 0.25 하고 정수부분을 재료에 포함시키는 공식으로

#유라 캐릭터 특성 소재 합성 시 10%의 확률로 생산량의 2배를 획득한다.
#마찬가지 합성횟수 * 0.1의 정수부분만 상위단계 재료수에 추가
#특성 책

#모나 무기 돌파 소재 합성 시 25%의 확률로 일부 합성 재료를 반환한다.
#아야카 무기 돌파 소재를 합성 시 10%의 확률로 생산량의 2배를 획득한다.
#알베도 무기 돌파 소재를 합성 시 10%의 확률로 생산량의 2배를 획득한다.
#비경 소재

#설탕 캐릭터와 무기의 육성 소재를 합성 시 10%의 확률로 생산량의 2배를 획득한다.
#필드 몹에서 얻는 재료





#리사 포션 합성 시 20%의 확률로 일부 합성 재료를 반환한다...


    




""" 나중에 데이터 구조 바꾸면 ...

    for need in [need_buse, need_poong, need_cg]:

        count_lv = 3

        for i in reversed(need):
            if i == 0: pass
            else:
                mix_book()

"""
"""
    for count_lv in [3,2,1]:
        if need_buse[count_lv-1] == 0:
            pass
        elif book_state[0] == True:
            if (mix_book(buse, need_buse, surplus_buse, count_lv, "부세")):
                print("\n부세는 조합으로 필요수량을 맞출 수 있습니다")
                print("조합 후 책의 현황입니다. 가르침 {0}권, 인도 {1}권, 철학 {2}권"
                    .format(buse[0], buse[1], buse[2]))
                print("특성레벨을 올린 후 현황입니다. 가르침 {0}권, 인도 {1}권, 철학 {2}권\n"
                    .format(buse[0]-goal_buse[0], buse[1]-goal_buse[1], buse[2]-goal_buse[2]))
            else:
                book_state[0] = False
                print("부세는 조합으로 필요수량을 맞출 수 없습니다\n")
                print("조합으로 부족분을 채우려면 가르침 {0}권을 모으거나\n".format(need_buse[2]*9 + need_buse[1]*3) + 
                    "가르침 {0}권, 인도 {1}권을 모아야 합니다\n"
                    .format(need_buse[0], need_buse[1] + need_buse[2]*3))
                print("최고난도 비경 기준으로 레진 20당 1단계 재료 8개 만큼의 가치를 보장하여 얻을 수 있습니다")
                print("따라서 최대 {0}번의 특성 비경 도전 ({1}레진 소모)이 필요합니다\n"
                        .format((need_buse[2]*9 + need_buse[1]*3)//8, ((need_buse[2]*9 + need_buse[1]*3)//8)*20) )

        if need_poong[count_lv-1] == 0:
            pass
        elif book_state[1] == True:
            if (mix_book(poong, need_poong, surplus_poong, count_lv, "풍아")):
                print("\n풍아는 조합으로 필요수량을 맞출 수 있습니다")
                print("조합 후 책의 현황입니다. 가르침 {0}권, 인도 {1}권, 철학 {2}권"
                    .format(poong[0], poong[1], poong[2]))
                print("특성레벨을 올린 후 현황입니다. 가르침 {0}권, 인도 {1}권, 철학 {2}권\n"
                    .format(poong[0]-goal_poong[0], poong[1]-goal_poong[1], poong[2]-goal_poong[2]))
            else:
                book_state[1] = False
                print("풍아는 조합으로 필요수량을 맞출 수 없습니다\n")
                print("조합으로 부족분을 채우려면 가르침 {0}권을 모으거나\n".format(need_poong[2]*9 + need_poong[1]*3) + 
                    "가르침 {0}권, 인도 {1}권을 모아야 합니다\n"
                    .format(need_poong[0], need_poong[1] + need_poong[2]*3))
                print("최고난도 비경 기준으로 레진 20당 1단계 재료 8개 만큼의 가치를 보장하여 얻을 수 있습니다")
                print("따라서 최대 {0}번의 특성 비경 도전 ({1}레진 소모)이 필요합니다\n"
                        .format((need_poong[2]*9 + need_poong[1]*3)//8, ((need_poong[2]*9 + need_poong[1]*3)//8)*20) )


        if need_cg[count_lv-1] == 0:
            pass
        elif book_state[2] == True:
            if (mix_book(cg, need_cg, surplus_cg, count_lv, "천광")):
                print("\n천광은 조합으로 필요수량을 맞출 수 있습니다")
                print("조합 후 책의 현황입니다. 가르침 {0}권, 인도 {1}권, 철학 {2}권"
                    .format(cg[0], cg[1], cg[2]))
                print("특성레벨을 올린 후 현황입니다. 가르침 {0}권, 인도 {1}권, 철학 {2}권\n"
                    .format(cg[0]-goal_cg[0], cg[1]-goal_cg[1], cg[2]-goal_cg[2]))
            else:
                book_state[2] = False
                print("천광은 조합으로 필요수량을 맞출 수 없습니다\n")
                print("조합으로 부족분을 채우려면 가르침 {0}권을 모으거나\n".format(need_cg[2]*9 + need_cg[1]*3) + 
                    "가르침 {0}권, 인도 {1}권을 모아야 합니다\n"
                    .format(need_cg[0], need_cg[1] + need_cg[2]*3))
                print("최고난도 비경 기준으로 레진 20당 1단계 재료 8개 만큼의 가치를 보장하여 얻을 수 있습니다")
                print("따라서 최대 {0}번의 특성 비경 도전 ({1}레진 소모)이 필요합니다\n"
                        .format((need_cg[2]*9 + need_cg[1]*3)//8, ((need_cg[2]*9 + need_cg[1]*3)//8)*20) )
"""

"""

def old_mix_book(now_book, need_book, surplus_book, lv, book_name):

    if lv == 1: #1단계 재료인 경우
        if now_book[lv-1] >= need_book[lv-1]:
            return True
        else:
            print("{0}단계의 재료가 부족합니다.".format(lv))
            return False

    else: #2, 3단계 재료인 경우

        if surplus_book[lv-2] >= need_book[lv-1]*3:
            print("{0}의 {1}단계 재료를 {2}개 소모하여 {3}단계 재료를 {4}개 제작합니다."
                    .format(book_name, lv-1, need_book[lv-1]*3, lv, need_book[lv-1]))
            now_book[lv-2] = now_book[lv-2] - need_book[lv-1]*3
            now_book[lv-1] = now_book[lv-1] + need_book[lv-1]
            return True
        else:
            temp_low_need = need_book[lv-2]
            need_book[lv-2] = need_book[lv-2] + need_book[lv-1]*3 - surplus_book[lv-2]
            if (mix_book(now_book, need_book, surplus_book, lv-1, book_name)):
                print("{0}의 {1}단계 재료를 {2}개 소모하여 {3}단계 재료를 {4}개 제작합니다."
                    .format(book_name, lv-1, need_book[lv-1]*3, lv, need_book[lv-1]))
                need_book[lv-2] = 0
                now_book[lv-2] = now_book[lv-2] - need_book[lv-1]*3
                now_book[lv-1] = now_book[lv-1] + need_book[lv-1]
                return True            
            else:
                need_book[lv-2] = temp_low_need
                print("{0}단계의 재료가 부족합니다.".format(lv))
                return False
"""