# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/palindrome-check-2/

input_word = input()

is_palindrome = True

for i, j in zip(range(len(input_word) // 2), reversed(range(len(input_word) // 2 + 1, len(input_word)))):
    if input_word[i] != input_word[j]:
        is_palindrome = False
        break

if is_palindrome:
    print("YES")
else:
    print("NO")
