#include <stdio.h>

int main()
{
	int i1 = 30;
	int i2 = 40;
	const int *pi = &i1;
	pi = &i2;
	
	i2 = 80;
	printf("%d\n",*pi);
}
