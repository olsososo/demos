#include <stdio.h>

int main()
{
	int i=0,a[] = {2,4,5,6,7,8,3,4,5};

	for(i=0;i<9;i++)
	{
		printf("%d\n",*(a+i));
	}
}
