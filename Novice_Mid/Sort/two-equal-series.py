## src : https://www.codetree.ai/missions/5/concepts/41/problems/two-equal-series
## 정렬 - 두 개의 동일한 수열

# import sys
# input = sys.readline().rstrip()
n = int(input())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

if arr_a == arr_b:
	print("Yes")
else:
	print("No")