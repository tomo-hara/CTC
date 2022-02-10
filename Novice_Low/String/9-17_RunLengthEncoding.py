''' Given an input string AA, write a code that returns the Run Length Encoded string for the input string. Run Length Encoding is a simple form of lossless data compression that runs on sequences with the same value occurring many consecutive times.
For example, if string AA is aaabbbbcbb, the Run Length Encoded String is a3b4c1b2, as a appears 3 times, b appears 4 times, c appears 1 time and b appears 2 times, sequentially.
Given an input string AA, write a code that returns the Run Length Encoded string for the input string. '''


string = input()
cnt = 1
res = ""

for i in range(1, len(string)):
	if (string[i - 1] == string[i]):
		cnt += 1
	else:
		res += "".join([string[i-1], str(cnt)])
		cnt = 1
res += "".join([string[-1], str(cnt)])

total_cnt = 0
total_cnt += len(res)
print(total_cnt)
print(res)

# 밤과 새벽에 걸친 오답코드(Jan 31 ~ Feb 1) : A# 를 넘어가는 경우(10개 이상 압축)에 대해 처리하지 못함
string = input()
cnt = 1
res = []

for i in range(1, len(string)):
	if (string[i - 1] == string[i]):
		cnt += 1
	else:
		res.append([string[i-1], cnt])
		cnt = 1
res.append([string[-1], cnt])
total_cnt = 0
for idx in range(len(res)):
	total_cnt += len(res[idx])
print(total_cnt)
for idx in range(len(res)):
	print(res[idx][0], res[idx][1], sep="", end="")
