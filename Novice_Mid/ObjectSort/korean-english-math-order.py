# src : https://www.codetree.ai/missions/5/concepts/41/problems/korean-english-math-order
# 객체 정렬 - 국영수 순이지

class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())

given_inputs = [
    tuple(input().split())
    for _ in range(n)
]
students = [
    Student(name, int(kor), int(eng), int(math))
    for (name, kor, eng, math) in given_inputs
]
students.sort(key=lambda x: (-x.kor, -x.eng, -x.math))

for student in students:
    print(student.name, student.kor, student.eng, student.math)