# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/modify-the-string/https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/modify-the-string/

input_word = input()

output_word = ''

for char in input_word:
    if ord(char) < 91:
        output_word += chr(ord(char) + 32)
    else:
        output_word += chr(ord(char) - 32)

print(output_word)