limit=int(input("Enter the limit :"))


def rever_star(i):
    for i in range (i,0,-1):
        print('*' * i)


rever_star(limit)