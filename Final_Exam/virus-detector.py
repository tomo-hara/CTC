# src : https://www.codetree.ai/problems/virus-detector
# 기말고사 - 바이러스 검사

n = int(input())
consumers = list(map(int, input().split()))
l, m = tuple(map(int, input().split()))

total_cnt = 0
for consumer in consumers:
    cnt = 0
    consumer -= l
    cnt += 1
    while consumer <= 0:
        consumer -= m
        cnt += 1
    total_cnt += cnt
print(total_cnt)