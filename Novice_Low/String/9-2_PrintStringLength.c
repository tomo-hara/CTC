#include <stdio.h>

int main(void)
{
    char s1[100];
    char s2[100];
    scanf("%s", s1);
    scanf("%s", s2);
    int s1_len = 0;
    while (s1[s1_len] != '\0')
        s1_len++;
    int s2_len = 0;
    while (s2[s2_len] != '\0')
        s2_len++;
    printf("%d", s1_len + s2_len);
    return 0;
}