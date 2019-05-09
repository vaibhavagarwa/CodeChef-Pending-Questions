Question Link: https://www.codechef.com/MAY19B/problems/MATCHS

Problem is how to use conter to decide which ended game as his last turn


for i in range(0, int(input())):
    n, p = 0, 1
    a, b = input().split()
    a = int(a)
    b = int(b)
    cnt=0

    while a!=0 or b!=0:
        cnt+=1
        print ("Upt a and b", a,b)
        if a==b:
            #cnt+=1
            break
        if a>b:
            if a%b==0:
                #cnt += 1
                break
            else:
                a=a-b
                continue
        if b>a:
            if b%a==0:
                #cnt += 1
                break
            else:
                b=b-a
            continue

    print (cnt)
