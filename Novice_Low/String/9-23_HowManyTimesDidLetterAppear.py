""" Write a program that outputs how many time 'ee', 'eb' appears in the given string. """

string = input()

cnt1 = 0
cnt2 = 0
for i in range(len(string) - 1):
    if string[i] == 'e' and string[i+1] == 'e':
        cnt1 += 1
    if string[i] == 'e' and string[i+1] == 'b':
        cnt2 += 1
print(cnt1, cnt2, sep=" ")

# 오답 코드 : eee 를 두번으로 계산하지 못함
string = input()

print(string.count("ee"), end=" ")
print(string.count("eb"))