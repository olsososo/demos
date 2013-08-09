#include <stdio.h>

int main()
{
	int i = 5;
	int *pi;
	int **ppi;

	pi = &i;
	ppi = &pi;

	printf("*pi = %d\n",*pi);
	printf("**pi = %d\n",**ppi);
}
