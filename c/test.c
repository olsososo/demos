#include "2.8.c"

int main(void)
{
	printf("%d",c);
	func();
}

int func(void)
{
	extern int b;
	printf("%d\n",b);
}

