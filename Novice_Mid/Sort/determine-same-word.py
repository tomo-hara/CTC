## src : https://www.codetree.ai/missions/5/concepts/41/problems/determine-same-word
## 정렬 - 순서를 바꾸었을 때 같은 단어인지 판별하기
from typing import List

def is_equal_string(a : List[str], b : List[str]) -> bool:
	if len(a) != len(b):
		return False
	a.sort()
	b.sort()
	for elem_a, elem_b in zip(a, b):
		if elem_a != elem_b:
			return False
	return True

string_a = input()
string_b = input()
print("Yes") if (is_equal_string(list(string_a), list(string_b))) else print("No")

# # #
import sys

ASCII_NUM = 128
count = [0] * ASCII_NUM

str1 = input()
str2 = input()
for char1 in str1:
	count[ord(char1)] += 1
for char2 in str2:
	count[ord(char2)] -= 1

for i in range(ASCII_NUM):
	if count[i] != 0:
		print("No")
		sys.exit(0)
print("Yes")