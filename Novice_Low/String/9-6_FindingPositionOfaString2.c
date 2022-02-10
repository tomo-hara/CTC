#include <stdio.h>

// char *ct_strstr(const char *s1, const char *s2)
// {
// 	int i;
// 	while (*s1 != '\x00')
// 	{
// 		i = 0;
// 		while (*s1 == *s2)
// 		{
// 			i++;
// 			s2++;
// 			if (*s2 == '\x00')
// 				return (s1);
// 		}
// 		s1++;
// 	}
// 	return (NULL);
// }

// char *ct_strchr(const char *s1, const char c)
// {
// 	while (*s1 != '\x00')
// 	{
// 		if (*s1 == c)
// 			return s1;
// 		s1++;
// 	}
// 	return NULL;
// }

int ct_strchr34(const char *s1, const char c)
{
	if (*(s1 + 2) == c || *(s1 + 3) == c)
		return (1);
	return (0);
}

int main(void)
{
    char arr[5][20] = { "apple", "banana", "grape", "blueberry", "orange" };
    char niddle;

	scanf("%c", &niddle);
	int cnt = 0;
	int i = 0;
    while (i < 5)
	{
		if (ct_strchr34(arr[i], niddle))
		{
			printf("%s\n", arr[i]);
			cnt++;
		}
		i++;
	}
	printf("%d", cnt);
	return 0;
}