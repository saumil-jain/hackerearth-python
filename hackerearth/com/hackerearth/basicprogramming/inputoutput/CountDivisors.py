# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/count-divisors/

input_line = input()
l, r, k = input_line.split(' ')
l, r, k = int(l), int(r), int(k)

lower_quo = l // k
upper_quo = r // k
lower_rem = l % k

if lower_rem == 0:
    ans = upper_quo - lower_quo + 1
else:
    ans = upper_quo - lower_quo

print(ans)
