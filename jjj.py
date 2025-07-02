while True:
    user_input = input("enter numbers seperated by space")
    LIST=[int(x) for x in user_input.split()]
    a=0
    n=0
    max_num=LIST[0]
    min_num=LIST[0]
    for x in LIST:
        a=+x
        n+=1
        if x>max_num:
            max_num=x
        if x<min_num:
            min_num=x


    print("average=",a/n)  
    print("maximum=",max_num)          

    print("minimum=",min_num)
    print("sorted list=", sorted(LIST))

    O=input('DO YOU WANT TO DO MORE(Y/N)')
    if O!="Y":
        break
        