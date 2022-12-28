def productof(n):
    sum=1
    for i in str(n-1):
        sum*=int(i)
    print(sum)
n=int(input())
productof(n)
