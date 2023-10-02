str_n = input()
n = int(str_n)
i = 0
frequency = [0] * 10
a = list(map(int, input().split()))

sum_val = 0
for c in a:
    if c>10:
        sum_val+=1
    else:
        frequency[c] = frequency[c] + 1
        i += 1

i = 0
while i < 10:
    if frequency[i] != 0:
        sum_val = sum_val + min(abs(frequency[i] - i),frequency[i])
    i += 1

print(sum_val)
