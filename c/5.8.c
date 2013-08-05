#include <stdio.h>

int func()
{
	static int counter = 1;
	return ++counter;
}

main(void)
{
	int c = func();
	printf("%d\n",c);
}
