n = int(input())

i = 0
l = 0
while i < n:
    battle = input()
    if 'CD' in battle:
        l += 1
    i += 1
print(n-l)