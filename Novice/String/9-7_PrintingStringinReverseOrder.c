#include <stdio.h>

int main(void)
{
    char str[4][21];
    int i = 0;
    while (i < 4)
        scanf("%[^\n]", str[i++]);
        
    while (i)
        printf("%s\n", str[--i]);
    return 0;
}
/*
위와 같이 구현해보았는데, 원하는 결과값이 나오지 않습니다.
fgets()의 구현은 아래와 같이 했어요. 개행말고는 차이가 없어야 할 것이라 생각하는데 무엇을 놓친걸까요..?
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
