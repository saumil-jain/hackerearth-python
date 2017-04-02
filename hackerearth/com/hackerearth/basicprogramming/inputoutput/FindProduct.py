# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-product/

size = int(input())
input_array = input()

input_array = input_array.split(' ', maxsplit=size)

input_array = [int(i) for i in input_array]

ans = 1

for i in input_array:
    ans = (ans * i) % (10 ** 9 + 7)

print(ans)
