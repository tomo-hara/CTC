""" Write a code that outputs the starting index of a substring, 
if the objective string exists as a substring of a given input string. 
Assume that the index starts from 0. """

""" The first line contains the input string and the second line 
contains the objective string. """

import sys

input_str = input()
target_str = input()


# input_str의 s_idx1에서 e_idx1 까지의 문자열과
# output_str의 s_idx2에서 e_idx2 까지의 문자열과 일치하는지를 비교합니다.
def is_match(s_idx1, e_idx1, s_idx2, e_idx2):
    for i, j in zip(range(s_idx1, e_idx1 + 1), range(s_idx2, e_idx2 + 1)):
        if input_str[i] != target_str[j]:
            return False
    
    return True


input_len, target_len = len(input_str), len(target_str)

# 입력 문자열의 각 문자를 시작점으로 하여 목적 문자열을 만들 수 있는지 확인합니다.
for i in range(input_len):
    # input_str의 i 부터 i + target_len - 1까지의 원소가
    # target_len의 0부터 target_len - 1 까지의 원소와
    # 정확히 일치하는지 확인합니다.

    # 만약 input_str의 끝 원소인 i + target_len - 1 번째가
    # 존재하지 않는다면 비교를 하지 않습니다.
    if i + target_len - 1 >= input_len:
        continue
    
    if is_match(i, i + target_len - 1, 0, target_len - 1):
         # 모든 문자에 대하여 매칭이 된 경우:
        print(i)
        sys.exit(0)

# 매칭이 되지 않는 경우:
print(-1)