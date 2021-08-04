def af(a):
    a[1] = 0



def main():

    book = dict()

    print(type(book))

    book['buse'] = {'now':[0,1,2], 'goal':[3,4,5], 'need':[6,7,8], 'surplus':[9,0,10]}

    print(book)
    print()
    print(book['buse'])
    print()
    print(book['buse']['now'])
    print()
    print(book['buse']['now'][1])

    book['buse']['now'][1] = 2
    print()
    print(book['buse']['now'])

    
    book['poonga'] = {'now':[2,0,1], 'goal':[3,4,5], 'need':[6,7,8], 'surplus':[9,0,10]}

    print(book, end='\n\n')

    print(book.values())


main()