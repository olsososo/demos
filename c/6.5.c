#include <stdio.h>

int main()
{
	int i,*pa,a[] = {3,4,5,6,7,8};
	pa = a;
	
	for(;i<6;i++)
	{
		printf("%d\n",*pa);
		pa++;
	}
}
