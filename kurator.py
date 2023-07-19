f = open('35.txt')
n, k = map(int, f.readline().split())
res = []
for i in range(n):
    money = int(f.readline())
    nomer = i + 1
    if (nomer)**0.5 == int(nomer**0.5):
        res.append(money)
res.sort(reverse = True)
print(sum(res[:k]))
        
