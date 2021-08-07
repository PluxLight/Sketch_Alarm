def af(a):
    print(a)



def main():

    buse = [17, 22, 10] #리얼
    # buse = [9, 18, 12] #테스트용 
    poong = [66, 61, 14]
    cg = [10, 9, 10]

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

    for i in books.keys():
        print(books[i]['need'][0])


main()