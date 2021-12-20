def hill(n) :
    k = n - 1 # here n is 5, so 5 -1 = 4 which is k

    for i in range(0 , n) :
        for j in range(0 , k):
            print(end = " ")

        k = k - 1 # here k which is 4 is - by 1 so we could get new k as 3

        for j in range (0, i + 1) :
            print("*" , end = " ")

        print("\r")

hill(5)

