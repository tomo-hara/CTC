#include <stdio.h>

int main(void)
{
    char str[4][21];
    int i = 0;
    while (i < 4)
        scanf("%s[^\n]", str[i++]);
        
    while (i)
        printf("%s\n", str[--i]);
    return 0;
}
/*
위와 같이 구현해보았는데, 원하는 결과값이 나오지 않습니다. - scanf("%[^\n]")
다음과 같이 변경하면 정상작동 - scanf("%s[^\n]")

fgets()의 구현은 아래와 같이 - 문자열 중간에 공백이 있는 경우 권장
*/
#include <stdio.h>
int main(void)
{
    char str[4][21];
    int i = 0;
    while (i < 4)
        fgets(str[i++], 20 + 1, stdin);
    printf("%s\n", str[--i]);
    while (i)
        printf("%s", str[--i]);
    return 0;
}
