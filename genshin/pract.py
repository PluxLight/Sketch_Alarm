def domain():

    da = dict()
    print(type(da))

    da = {1 : {}}

    print(da)

    da[1] = {'saram':'in'}

    print(da)
    print(da[1])

    # da[1] = da[1] + {'mob':'ear'}

    temp = {}

    for i in da[1].keys():
        # print(i)
        # da[1] = {i:da[1][i], 'mob':'ear'}
        temp[i] = da[1][i]

    temp['mob'] = 'ear'

    da[1] = temp

    print(da)

    temp = 0

    print(da)




    return 0




if __name__ == "__main__":
    domain()