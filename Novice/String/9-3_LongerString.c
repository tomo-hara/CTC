#include <stdio.h>

unsigned int ct_strlen(char *str)
{
    unsigned int len = 0;
    while (*str++ != '\x00')
        len++;
    return (len);
}

int main(void)
{
    char s1[20];
    char s2[20];
    scanf("%s%s", s1, s2);
    
    unsigned int s1_len = ct_strlen(s1);
    unsigned int s2_len = ct_strlen(s2);
    if (s1_len > s2_len)
        printf("%s %d", s1, s1_len);
    else if (s1_len < s2_len)
        printf("%s %d", s2, s2_len);
    else
        printf("same");
    return 0;
}