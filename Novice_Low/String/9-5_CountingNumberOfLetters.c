#include <stdio.h>
#include <string.h>

int main(void)
{
    char str[101];
    char niddle;
	char *p_str = str;

    fgets(str, 100, stdin);
    scanf("%c", &niddle);
    int cnt = 0;
    while (*p_str != '\x00')
    {
        if (*p_str == niddle)
            cnt++;
        p_str++;
    }
    printf("%d", cnt);
    return 0;
}