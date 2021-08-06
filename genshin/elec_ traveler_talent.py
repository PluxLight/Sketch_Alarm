# 추가할 기능
# 1. 데이터 구조 바꾸기 리스트 -> 딕셔너리
# 2. 특성 적용해서 계산하는것도 ...
# 3. 재료 부족한 상황에서 현재 어디까지 올릴 수 있는지 계산할 떄 어떤 특성 우선순위로 둘지 설정하는 기능

#ver 1.0

def mix_book(book_dict):

    result = True

    if book_dict['need'][1] > 0: #2단계 책이 부족한경우
        if  book_dict['surplus'][0]//3 >= book_dict['need'][1]:
            book_dict['mix_cnt'][0] += book_dict['need'][1]
            book_dict['surplus'][0] = book_dict['surplus'][0] - book_dict['need'][1]*3
            book_dict['now'][0] = book_dict['now'][0] - book_dict['need'][1]*3
            book_dict['now'][1] = book_dict['now'][1] + book_dict['need'][1]
            book_dict['need'][1] = 0
        else:
            result = False


    if book_dict['need'][2] > 0: #3단계 책이 부족한경우
        if book_dict['surplus'][1]//3 >= book_dict['need'][2]: #2단계 책 잉여분만으로도 커버 가능한 경우
                book_dict['mix_cnt'][1] += book_dict['need'][2]
                book_dict['surplus'][1] = book_dict['surplus'][1] - book_dict['need'][2]*3
                book_dict['now'][1] = book_dict['now'][1] - book_dict['need'][2]*3
                book_dict['now'][2] = book_dict['now'][2] + book_dict['need'][2]
                book_dict['need'][2] = 0
        else:
            if (book_dict['surplus'][1] + book_dict['surplus'][0]//3)//3 >= book_dict['need'][2]: #영혼까지 끌어모으면 가능한 경우
                book_dict['mix_cnt'][0] += (book_dict['need'][2]*3 - book_dict['surplus'][1])
                book_dict['mix_cnt'][1] += book_dict['need'][2]
                book_dict['surplus'][0] = book_dict['surplus'][0] - (book_dict['need'][2]*3 - book_dict['surplus'][1])*3
                book_dict['now'][0] = book_dict['now'][0] - (book_dict['need'][2]*3 - book_dict['surplus'][1])*3
                book_dict['now'][1] = book_dict['now'][1] - book_dict['surplus'][1]
                book_dict['surplus'][1] = 0
                book_dict['now'][2] = book_dict['now'][2] + book_dict['need'][2]
                book_dict['need'][2] = 0
            else: #영혼까지 끌어모아도 안되는 경우
                result = False
            
    if book_dict['need'][0] > 0: #1단계 책이 부족한경우
        result=False
    
    return result


def limit_level(now_lv, goal_lv, books):

        #           2단계       3단계        4단계      5단계       6단계       7단계       8단계       9단계         10단계
    goal_book = ["buse 1 3", "poong 2 2", "cg 2 4", "buse 2 6", "poong 2 9", "cg 3 4", "buse 3 6", "poong 3 12", "cg 3 16"]
        #           0번          1번         2번         3번          4번       5번         6번          7번         8번
    goal_mora = [12500, 17500, 25000, 30000, 37500, 120000, 260000, 450000, 700000]

    talent_name = ["평타", "전투스킬", "원소폭발"]
    sum_mora = 0

    #여기서 할 것 부족한 상태에서 얼마나 찍을 수 있는가
    #나중에 우선순위 값 줘서 뭐부터 올릴지....
    #지금은 평타->전투->폭발 순

    #일단 조합 안하고 넘긴 애부터 조합해버리자
    for book in books.keys():
        if books[book]['state'] == True: #책이 충분한 경우는 넘기고
            pass
        else: #모자라서 조합안하고 그냥 넘긴건 여기서 잉여분만큼 조합해서 올리고
            for i in range(0,2):
                if books[book]['now'][i] > books[book]['goal'][i]: #현재 책이 목표 책 수량보다는 많으면
                    surplus = books[book]['now'][i] - books[book]['goal'][i]
                    books[book]['now'][i+1] = books[book]['now'][i+1] + surplus//3
                    books[book]['now'][i] = books[book]['goal'][i] + surplus%3


    for i in range(0,3):
        lvup_state = True
        lv_cnt = now_lv[i]+1
        front_lv = now_lv[i] #범위 앞
        back_lv = goal_lv[i] #범위 뒤

        if front_lv == back_lv or back_lv == 0 or back_lv == 1:
            print(f"{talent_name[i]}특성은 설정대로 레벨 업 하지 않고 넘어갑니다")
            continue

        for j in range(front_lv-1, back_lv-1):
            book, lv, ea = goal_book[j].split(" ")
            lv = int(lv)
            ea = int(ea)

            if books[book]['now'][lv-1] - ea >= 0:
                books[book]['now'][lv-1] = books[book]['now'][lv-1] - ea
                sum_mora += goal_mora[j]
            else:
                print(f"{lv_cnt}레벨 업에 실패했습니다. {talent_name[i]}특성은 현재 {lv_cnt-1}까지 레벨 업 가능합니다")
                lvup_state = False
                continue

            lv_cnt += 1

        if lvup_state == True:
            print(f"{talent_name[i]}특성은 목표한 {back_lv}레벨까지 가능합니다")

    print()

    for book in books:
        print(f"레벨 업 후 남은 책은 {books[book]['name']}의 가르침 {books[book]['now'][0]}권, 인도 {books[book]['now'][1]}권, 철학 {books[book]['now'][2]}권 입니다")
    print(f"\n특성 레벨 업에 필요한 모라는 총 {sum_mora}모라 입니다")
    

def try_domain(books):
    return max(sum([books[2]*9, books[1]*3, books[0]])//8, 1)






#값 = 유저가 소유한 [1단계, 2단계, 3단계] 부세, 풍아, 천광, /  현재 [무기, 전투, 폭발] 특성레벨, 목표 특성레벨
def calc_book(buse, poong, cg, now_lv, goal_lv): 

    #목표
    books = {
        'buse' : {
            'now' : [buse[0], buse[1], buse[2]],
            'goal' : [0, 0, 0],
            'need' : [0, 0, 0],
            'surplus' : [0, 0, 0],
            'mix_cnt' : [0, 0],
            'state' : False,
            'name' : "부세"
        },
        'poong' : {
            'now' : [poong[0], poong[1], poong[2]],
            'goal' : [0, 0, 0],
            'need' : [0, 0, 0],
            'surplus' : [0, 0, 0],
            'mix_cnt' : [0, 0],
            'state' : False,
            'name' : "풍아"
        },
        'cg' : {
            'now' : [cg[0], cg[1], cg[2]],
            'goal' : [0, 0, 0],
            'need' : [0, 0, 0],
            'surplus' : [0, 0, 0],
            'mix_cnt' : [0, 0],
            'state' : False,
            'name' : "천광"
        }
    }
    
    #               2단계       3단계        4단계      5단계       6단계       7단계       8단계       9단계         10단계
    goal_book = ["buse 1 3", "poong 2 2", "cg 2 4", "buse 2 6", "poong 2 9", "cg 3 4", "buse 3 6", "poong 3 12", "cg 3 16"]
        #           0번          1번         2번         3번          4번       5번         6번          7번         8번

    sum_try = 0

    #유저가 설정한 레벨까지 필요한 책 계산
    for i in range(0,3):
        front_lv = now_lv[i] #범위 앞
        back_lv = goal_lv[i] #범위 뒤

        if front_lv == back_lv or back_lv == 0 or back_lv == 1: continue

        for j in range(front_lv-1, back_lv-1):
            book, lv, ea = goal_book[j].split(" ")
            lv = int(lv)
            ea = int(ea)

            books[book]['goal'][lv-1] += ea

    #부족한 책 수량 계산 겸 잉여분 계산
    for book in books.keys():
        books[book]['need'][0] = max(books[book]['goal'][0] - books[book]['now'][0], 0)
        books[book]['need'][1] = max(books[book]['goal'][1] - books[book]['now'][1], 0)
        books[book]['need'][2] = max(books[book]['goal'][2] - books[book]['now'][2], 0)
        
        books[book]['surplus'][0] = max(books[book]['now'][0] - books[book]['goal'][0], 0)
        books[book]['surplus'][1] = max(books[book]['now'][1] - books[book]['goal'][1], 0)
        books[book]['surplus'][2] = max(books[book]['now'][2] - books[book]['goal'][2], 0)

        #현 상태 출력
        print(f"소요되는 책은 {books[book]['name']}의 가르침 {books[book]['goal'][0]}권, 인도 {books[book]['goal'][1]}권, 철학 {books[book]['goal'][2]}권 입니다")
        print(f"부족한 책은 {books[book]['name']}의 가르침 {books[book]['need'][0]}권,  인도 {books[book]['need'][1]}권, 철학 {books[book]['need'][2]}권 입니다\n")
        # print(f"잉여 책은 {books[book]['name']}의 가르침 {books[book]['surplus'][0]}권, 인도 {books[book]['surplus'][1]}권, 철학 {books[book]['surplus'][2]}권 입니다\n")


    for book in books.keys():
        if books[book]['need'].count(0) == 3: #부족한 게 전부 0이라 조합이 필요없음
            books[book]['state'] = True
        else: #부족한 게 있음
            books[book]['state'] = mix_book(books[book])

    
    

    for book in books.keys():
        if books[book]['state'] == True and books[book]['mix_cnt'].count(0) != 2: #레벨 업이 가능하고, 조합이 필요한 경우
            if books[book]['mix_cnt'][0] != 0: print(f"{books[book]['name']}의 가르침을 {books[book]['mix_cnt'][0]*3}개 소모하여 인도를 {books[book]['mix_cnt'][0]}권 만들어야 합니다")
            if books[book]['mix_cnt'][1] != 0: print(f"{books[book]['name']}의 인도를 {books[book]['mix_cnt'][1]*3}개 소모하여 철학을 {books[book]['mix_cnt'][1]}권 만들어야 합니다\n")
        else:
            if books[book]['state'] == True and books[book]['mix_cnt'].count(0) == 2: #레벨 업이 가능하고, 조합이 필요없는 경우
                print(f"{books[book]['name']} 은/는 합성이 불필요합니다")
            else:                                                       #재료가 부족해 레벨 업이 불가능한 경우
                print(f"{books[book]['name']} 은/는 재료가 부족합니다")
                sum_try += try_domain(books[book]['need'])

    if True == books['buse']['state'] and True == books['poong']['state'] and True == books['cg']['state']:
        print("\n목표 특성 레벨까지 레벨 업이 가능합니다")
    else:
        print("\n목표 특성 레벨까지 레벨 업이 불가능합니다")
        print(f"부족한 수량만큼 최대 {sum_try}번의 비경을 도전해야합니다. 소모 레진은 {sum_try*20}입니다\n")


    #일단 남는거 다 조합해서 얼마나 레벨 올릴수 있을까?
    limit_level(now_lv, goal_lv, books)


if __name__=="__main__":
    # 현재 책 수량 단계가 낮을수록 리스트 앞에 있음
    now_buse = [17, 22, 10] #리얼
    # now_buse = [9, 18, 12] #테스트용 
    now_poong = [0, 30, 10]
    now_cg = [10, 9, 10]

    now_lv = [1,1,1]
    goal_lv = [1,9,9]

    print(f"무기, 전투, 폭발 순으로 현재 특성 레벨은 {now_lv[0]}, {now_lv[1]}, {now_lv[2]} 이 설정됐고")
    print(f"무기, 전투, 폭발 순으로 목표 특성 레벨은 {goal_lv[0]}, {goal_lv[1]}, {goal_lv[2]} 이 설정됐습니다\n")

    print(f"현재 부세의 가르침 {now_buse[0]}권, 인도 {now_buse[1]}권, 철학 {now_buse[2]}권 보유 중으로 설정되었습니다")
    print(f"현재 풍아의 가르침 {now_poong[0]}권, 인도 {now_poong[1]}권, 철학 {now_poong[2]}권 보유 중으로 설정되었습니다")
    print(f"현재 천광의 가르침 {now_cg[0]}권, 인도 {now_cg[1]}권, 철학 {now_cg[2]}권 보유 중으로 설정되었습니다\n")


    #값 = 유저가 소유한 [1단계, 2단계, 3단계] 부세, 풍아, 천광, /  현재 [무기, 전투, 폭발] 특성레벨, 목표 특성레벨
    calc_book(now_buse, now_poong, now_cg, now_lv, goal_lv)

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