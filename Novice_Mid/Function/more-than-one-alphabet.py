# src : https://www.codetree.ai/missions/5/concepts/39/problems/more-than-one-alphabet
# Call by - 2개 이상의 알파벳

import sys

string = input()
# cnt_arr = [0] * 26 # lower alpha
for i in range(1, len(string)):
    if string[i] != string[0]:
        print("Yes")
        sys.exit(0)
print("No")