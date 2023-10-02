s = input()

x=s.split("R")

while "" in x:
    x.remove("")

print(len(x))

for abc in x:
    i=0
    while i<len(abc):
        print('L',end='')
        i+=1
    i=0
    while i<len(abc):
        print('R',end='')
        i+=1
    print()