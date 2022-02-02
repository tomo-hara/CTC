# 미해결

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

char str[1001], sub_str[1001];

// input_str의 s_idx1에서 e_idx1 까지의 문자열과
// output_str의 s_idx2에서 e_idx2 까지의 문자열과 일치하는지를 비교합니다.
bool IsMatch(int s_idx1, int e_idx1, int s_idx2, int e_idx2) {
    int i = s_idx1;
    int j = s_idx2;
    while (i <= e_idx1 && j <= e_idx2) {
        if(str[i] != sub_str[j])
            return false;
        i++;
        j++;
    }

    return true;
}

int main() {
    scanf("%s", str);
	scanf("%s", sub_str);

    int str_len = strlen(str);
    int sub_str_len = strlen(sub_str);

    // 입력 문자열의 각 문자를 시작점으로 하여 목적 문자열을 만들 수 있는지 확인합니다.
    for(int i = 0; i < str_len; i++) {
        // str[ i 부터 i + sub_str_len - 1]까지
        // sub_str_len[ 0부터 sub_str_len - 1 ]까지
        
        // 만약 str[ i + target_len - 1 ]
		// 존재하지 않는다면 비교를 하지 않습니다.
        if(i + sub_str_len - 1 >= str_len)
            continue;
        
        if(IsMatch(i, i + sub_str_len - 1, 0, sub_str_len - 1)) {
            // 모든 문자에 대하여 매칭이 된 경우:
            printf("%d", i);
            return 0;
        }
    }

    // 매칭이 되지 않는 경우:
    printf("-1");
    return 0;
}