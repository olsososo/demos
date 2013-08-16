#include <stdio.h>

void
cpy(char *buffer,char const *string)
{
	while((*buffer++ = *string++) != '\0')
		;
}

void main()
{
	char buf[] = "hello";
	char str[] = "world";
	
	cpy(buf,str);

	printf("%s\n",buf);
}
