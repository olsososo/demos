#include <stdio.h>

int main()
{
	char a,*pa;
	a = 10;
	pa = &a;
	*pa = 20;
	*&a = 30;
	printf("%d\n",a);
}
