def mix_book(books):

    result = True

    if books['need'][1] > 0: #2단계 책이 부족한경우
        if  books['surplus'][0]//3 >= books['need'][1]:
            books['mix_cnt'][0] += books['need'][1]
            books['surplus'][0] = books['surplus'][0] - books['need'][1]*3
            books['now'][0] = books['now'][0] - books['need'][1]*3
            books['now'][1] = books['now'][1] + books['need'][1]
            books['need'][1] = 0
        else:
            result = False


    if books['need'][2] > 0: #3단계 책이 부족한경우
        if books['surplus'][1]//3 >= books['need'][2]: #2단계 책 잉여분만으로도 커버 가능한 경우
                books['mix_cnt'][1] += books['need'][2]
                books['surplus'][1] = books['surplus'][1] - books['need'][2]*3
                books['now'][1] = books['now'][1] - books['need'][2]*3
                books['now'][2] = books['now'][2] + books['need'][2]
                books['need'][2] = 0
        else:
            if (books['surplus'][1] + books['surplus'][0]//3)//3 >= books['need'][2]: #영혼까지 끌어모으면 가능한 경우
                books['mix_cnt'][0] += (books['need'][2]*3 - books['surplus'][1])
                books['mix_cnt'][1] += books['need'][2]
                books['surplus'][0] = books['surplus'][0] - (books['need'][2]*3 - books['surplus'][1])*3
                books['now'][0] = books['now'][0] - (books['need'][2]*3 - books['surplus'][1])*3
                books['now'][1] = books['now'][1] - books['surplus'][1]
                books['surplus'][1] = 0
                books['now'][2] = books['now'][2] + books['need'][2]
                books['need'][2] = 0
            else: #영혼까지 끌어모아도 안되는 경우
                result = False
            
    if books['need'][0] > 0: #1단계 책이 부족한경우
        result=False
    
    return result


def limit_level(books, ta_lv):

            #단계 2  3  4  5  6  7  8   9  10
            #등급 1  2  2  2  2  3  3   3  3
            #칸  0  1  2  3  4  5  6   7   8 
    goal_book = [3, 2, 4, 6, 9, 4, 6, 12, 16]
    
    goal_mora = [12500, 17500, 25000, 30000, 37500, 120000, 260000, 450000, 700000]

    talent_name = ["평타", "전투스킬", "원소폭발"]
    sum_mora = 0

    #여기서 할 것 부족한 상태에서 얼마나 찍을 수 있는가
    #나중에 우선순위 값 줘서 뭐부터 올릴지....
    #지금은 평타->전투->폭발 순


    for i in range(0,2):
        if books['now'][i] > books['goal'][i]: #현재 책이 목표 책 수량보다는 많으면
            surplus = books['now'][i] - books['goal'][i]
            books['now'][i+1] = books['now'][i+1] + surplus//3
            books['now'][i] = books['goal'][i] + surplus%3

    print(f"싹 다 조합하면 {books['name']}의 가르침 {books['now'][0]}권, 인도 {books['now'][1]}권, 철학 {books['now'][2]}권 입니다\n")


    for i in range(0,3):
        lvup_state = True
        lv_cnt = ta_lv['now'][i]+1
        front_lv = ta_lv['now'][i] #범위 앞
        back_lv = ta_lv['goal'][i] #범위 뒤

        if front_lv == back_lv or back_lv == 0 or back_lv == 1:
            print(f"{talent_name[i]}특성은 설정대로 레벨 업 하지 않고 넘어갑니다")
            continue

        for j in range(front_lv-1, back_lv-1):
            ea = goal_book[j]
            if j < 1:
                lv = 1
            elif j >= 1 and j < 5:
                lv = 2
            else:
                lv = 3

            if books['now'][lv-1] - ea >= 0:
                books['now'][lv-1] = books['now'][lv-1] - ea
                sum_mora += goal_mora[j]
            else:
                print(f"{lv_cnt}레벨 업에 실패했습니다. {talent_name[i]}특성은 현재 {lv_cnt-1}까지 레벨 업 가능합니다")
                lvup_state = False
                break

            lv_cnt += 1

        if lvup_state == True:
            print(f"{talent_name[i]}특성은 목표한 {back_lv}레벨까지 가능합니다")

    print()

    print(f"레벨 업 후 남은 책은 {books['name']}의 가르침 {books['now'][0]}권, 인도 {books['now'][1]}권, 철학 {books['now'][2]}권 입니다")
    print(f"\n특성 레벨 업에 필요한 모라는 총 {sum_mora}모라 입니다")
    

def try_domain(books):
    return max(sum([books[2]*9, books[1]*3, books[0]])//8, 1)


def sim_calc(books, ta_lv):
            #단계 2  3  4  5  6  7  8   9  10
            #등급 1  2  2  2  2  3  3   3  3
            #칸  0  1  2  3  4  5  6   7   8 
    goal_book = [3, 2, 4, 6, 9, 4, 6, 12, 16]
    sum_try = 0

    for i in range(0,3):
        front_lv = ta_lv['now'][i] #범위 앞
        back_lv = ta_lv['goal'][i] #범위 뒤

        if front_lv == back_lv or back_lv == 0 or back_lv == 1: continue

        for j in range(front_lv-1, back_lv-1):
            ea = goal_book[j]
            if j < 1:
                lv = 1
            elif j >= 1 and j < 5:
                lv = 2
            else:
                lv = 3

            books['goal'][lv-1] += ea

    #1-9까지 1성 3개 2성 21개 3성 22
    #1-10까지 1성 3개 2성 21개 3성 38
    #1-9 2개에 1-10 하나면 1성 9개 2성 63개 3성 82

    #부족한 책 수량 계산 겸 잉여분 계산    
    books['need'][0] = max(books['goal'][0] - books['now'][0], 0)
    books['need'][1] = max(books['goal'][1] - books['now'][1], 0)
    books['need'][2] = max(books['goal'][2] - books['now'][2], 0)
    
    books['surplus'][0] = max(books['now'][0] - books['goal'][0], 0)
    books['surplus'][1] = max(books['now'][1] - books['goal'][1], 0)
    books['surplus'][2] = max(books['now'][2] - books['goal'][2], 0)

    #현 상태 출력
    print(f"소유중인 책인 {books['name']}의 가르침 {books['now'][0]}권, 인도 {books['now'][1]}권, 철학 {books['now'][2]}권 입니다")
    print(f"소요되는 책은 {books['name']}의 가르침 {books['goal'][0]}권, 인도 {books['goal'][1]}권, 철학 {books['goal'][2]}권 입니다")
    print(f"부족한 책은 {books['name']}의 가르침 {books['need'][0]}권,  인도 {books['need'][1]}권, 철학 {books['need'][2]}권 입니다\n")
    # print(f"잉여 책은 {books['name']}의 가르침 {books['surplus'][0]}권, 인도 {books['surplus'][1]}권, 철학 {books['surplus'][2]}권 입니다\n")

    if books['need'].count(0) == 3: #부족한 게 전부 0이라 조합이 필요없음
        books['state'] = True
        print("필요한건 전부 갖췄음")
    else: #부족한 게 있음
        print("부족함")
        books['state'] = mix_book(books)

    
    

    if books['state'] == True and books['mix_cnt'].count(0) != 2: #레벨 업이 가능하고, 조합이 필요한 경우
        if books['mix_cnt'][0] != 0: print(f"{books['name']}의 가르침을 {books['mix_cnt'][0]*3}개 소모하여 인도를 {books['mix_cnt'][0]}권 만들어야 합니다")
        if books['mix_cnt'][1] != 0: print(f"{books['name']}의 인도를 {books['mix_cnt'][1]*3}개 소모하여 철학을 {books['mix_cnt'][1]}권 만들어야 합니다\n")
    else:
        if books['state'] == True and books['mix_cnt'].count(0) == 2: #레벨 업이 가능하고, 조합이 필요없는 경우
            print(f"{books['name']} 은/는 합성이 불필요합니다")
        else:                                                       #재료가 부족해 레벨 업이 불가능한 경우
            print(f"{books['name']} 은/는 재료가 부족합니다")
            sum_try += try_domain(books['need'])

    if True == books['state']:
        print("\n목표 특성 레벨까지 레벨 업이 가능합니다")
    else:
        print("\n목표 특성 레벨까지 레벨 업이 불가능합니다")
        print(f"부족한 수량만큼 최대 {sum_try}번의 비경을 도전해야합니다. 소모 레진은 {sum_try*20}입니다\n")


    # #일단 남는거 다 조합해서 얼마나 레벨 올릴수 있을까?
    limit_level(books, ta_lv)


    
    return 0


if __name__ == "__main__":

    books = {
        'now' : [62, 53, 16],
        # 'now' : [0, 0, 0],
        'goal': [0, 0, 0],
        'need': [0, 0, 0],
        'surplus': [0, 0, 0],
        'mix_cnt': [0, 0],
        'state': False,
        'name': '천광'
    }

    talent_lv = {
        'now' : [1, 1, 1],
        'goal' : [9, 9, 10]
    }

    sim_calc(books, talent_lv)
