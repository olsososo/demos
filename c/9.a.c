#include <stdio.h>

size_t
len(char *string)
{
	int length = 0;
	
	while(*string++ != '\0')
	{
		length++;
	}

	return length;
}

void main()
{
	int length;
	char message[] = "helloworld";

	length = len(message);

	printf("%d\n",length);
}
