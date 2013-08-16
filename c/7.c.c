#include <stdio.h>

long factorial(int n)
{
	int result = 1;
	
	while(n>0)
	{
		result *= n;
		n -= 1;
	}

	return result;
}

void main()
{
	int result;

	result = factorial(4);

	printf("%d\n",result);
}
