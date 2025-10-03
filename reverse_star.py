def rever_star(i):
    for i in range (i,0,-1):
        print('*' * i)



def forward_str(i):
    for i in range(0,i+1,1):
        print('*' * i)

limit=int(input("Enter the limit :"))
ch=int(input("Choices \n1:Ascending Start\n2:Descending Star\nEnter your choice:"))
if ch==1:
   forward_str(limit)
elif ch==2:
    rever_star(limit)
else:
    print("Invalid Input")       
    #######################