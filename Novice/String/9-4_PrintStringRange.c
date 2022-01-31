#include <stdio.h>
#include <string.h>

int main(void)
{
    char str[32];
    scanf("%[^\n]s", str); //s 유무의 차이는 모름. 앞에 붙이면 Null terminate는 됨.
    str[10] = '\x00';
    printf("%s", (str + 2));
    return 0;
}

int main() {

	char str[20];
	fgets(str, 20, stdin);

	str[10] = '\0';
	printf("%s\n", &str[2]);

	return 0;

}
