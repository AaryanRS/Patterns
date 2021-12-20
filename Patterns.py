rows = 5
n = 6

for i in range(rows, 0 , -1 ) :
    n -= 1

    for j in range(0 , n ) :
        print(n , end = " ")

    print('\r')