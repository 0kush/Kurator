f = open('35.txt')
n, k = map(int, f.readline().split())
bank = []
for i in range(n):
    money = int(f.readline())
    bank.append([money, 0])
    
for j in range(1, n + 1):
    for i in range(n):
        if (i + 1) % j == 0:
            if bank[i][1] == 0:
                bank[i][1] = 1
            else:
                bank[i][1] = 0
res = []
for i in range(n):
    if bank[i][1] == 1:
        res.append(bank[i][0])
res.sort(reverse = True)
print(sum(res[:k]))
                
