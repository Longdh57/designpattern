def outerFunction():
    x = "Hello Long Dao"

    def innerFunction():
        nonlocal x              # khai bao x la bien nonlocal
        x = "Hello all!"
        print("inner:", x)      # print gia tri cua x o trong ham innerFunction

    innerFunction()             # run ham innerFunction
    print("outer:", x)          # print gia tri cua x o trong ham outerFunction

outerFunction()