# Problem: C - Barking Password - https://codeforces.com/gym/588094/problem/C

import sys
password = input()
n = int(input())
words = [input() for _ in range(n)]
flag_1 = False
flag_2 = False
 
for word in words:
    if password == word:
        print("YES")
        sys.exit()
 
    if word[0] == password[1]:
        flag_1 = True
 
    if word[1] == password[0]:
        flag_2 = True
    
if flag_1 and flag_2:
    print("YES")
else:
    print("NO")