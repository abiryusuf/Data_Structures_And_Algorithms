

def sum(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num
print(sum(5))

x = [6, 7, 8, 9]
def total(num):
    sum = 0
    ave = 0
    for i in num:
        sum += i
    return sum/len(num)
print(total(x))