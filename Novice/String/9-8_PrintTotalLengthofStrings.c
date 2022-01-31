#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

#define WORD_MAX (10)
#define TRUE (1)
#define FALSE (0)

int ct_is_alphabetic(char c)
{
	if ((c & 0x40) && (c &= 0x1f) && c < 27)
		return (TRUE);
	return (FALSE);
}

int ct_is_space(char c)
{
	if (c == ' ')
		return (TRUE);
	return (FALSE);
}

unsigned int ct_word_len(char *str)
{
	unsigned int len = 0;
	while (*str != '\x00')
	{
		if (ct_is_alphabetic(*str) || ct_is_space(*str))
			len++;
		str++;
	}
	return (len);
}

int main(void)
{
	/* to do:
	WORD_LEN 동적할당 
	*/

	char **s = (char **)malloc(sizeof(char *) * WORD_MAX);

	int i = 0;
	while (i < 10)
		scanf("%s", *(s + i++));
	printf("%s", s[0]);
	return 0;
}

// Hello Code Tree My Name Is Will Nice To Meet You : 38

/* 간단 버전 */
#include <stdio.h>
#include <string.h>

#define WORD_MAX 10

int main() {
	
	char arr[WORD_MAX][20];

	for (int i = 0; i < WORD_MAX; i++) {
		scanf("%s", arr[i]);
	}
    unsigned int len = 0;
	for (int i = 0; i < WORD_MAX; i++) {
		len += strlen(arr[i]);
	}
    printf("%u", len);

	return 0;
}