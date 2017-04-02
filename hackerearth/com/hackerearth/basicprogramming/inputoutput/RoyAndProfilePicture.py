# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/roy-and-profile-picture/

l = int(input())
n = int(input())

for i in range(n):
    w, h = input().split(' ')
    w = int(w)
    h = int(h)

    if w < l or h < l:
        print('UPLOAD ANOTHER')
    elif w != h:
        print('CROP IT')
    else:
        print('ACCEPTED')
