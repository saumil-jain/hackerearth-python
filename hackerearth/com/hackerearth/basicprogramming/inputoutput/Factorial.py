# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-factorial/

n = int(input())

ans = 1

while n > 0:
    ans *= n
    n -= 1

print(ans)