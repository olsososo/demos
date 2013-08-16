#include <stdio.h>

long
factorial(int n)
{
	if(n <= 0)
		return 1;
	else
		return n*factorial(n-1);
}

void main(void)
{
	int result;

	result = factorial(4);

	printf("%d\n",result);
}
