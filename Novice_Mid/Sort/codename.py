## src : https://www.codetree.ai/missions/5/concepts/41/problems/code-name/introduction
## 객체 - 코드네임

#1 : 튜플
codes = []
for _ in range(5):
    name, score = tuple(input().split())
    codes.append((name, int(score)))

min_idx = 0
for  i in range(1, 5):
    if codes[i][1] < codes[min_idx][1]:
        min_idx = i

print(codes[min_idx][0], codes[min_idx][1])

#1 : 튜플 (언패킹 - 가독성 높이기)
codes = []
for _ in range(5):
    name, score = tuple(input().split())
    codes.append((name, int(score)))

min_idx = 0
for  i in range(1, 5):
    name, score = codes[i]
    min_name, min_score = codes[min_idx]
    if score < min_score:
        min_idx = i

min_name, min_score = codes[min_idx]
print(min_name, min_score)

#2 : 클래스
class Code:
    def __init__(self, name, score):
        self.name = name
        self.score = score

codes = []
for _ in range(5):
    name, score = tuple(input().split())
    codes.append(Code(name, int(score)))

min_idx = 0
for  i in range(1, 5):
    if codes[i].score < codes[min_idx].score:
        min_idx = i

print(codes[min_idx].name, codes[min_idx].score)
str.upp