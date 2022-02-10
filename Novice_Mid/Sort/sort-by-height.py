## src : https://www.codetree.ai/missions/5/concepts/41/problems/sort-by-height/description
## 정렬 - 키를 기준으로 정렬

n = int(input())
assert 1 <= n <= 10
people = [] # List[tuple(str, int, int)]
for _ in range(n):
	name, height, weight = input().split()
	assert 1<= len(name) <= 10
	assert 100 <= int(height) <= 200
	assert 20 <= int(weight) <= 100
	people.append( ( name, int(height), int(weight) ) )

people.sort(key=lambda x: x[1])

for name, height, weight in people:
	 print(name, height, weight)