#include <stdio.h>

int main()
{
	int i,a[] = {3,4,5,6,7,8};
	int * const pa = a;
	
	for(;i<6;i++)
	{
		printf("%d\n",*pa);
	}
}
