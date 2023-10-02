n=input()
a = list(map(int, input().split()))
count = 0
flag=True
while flag:
    for n in a:
        if n%2==1:
           flag=False
           continue
    a = list(map(lambda x: x/2, a))
    count+=1
print(count-1)