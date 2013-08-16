#include <stdio.h>

int * find_int(int key,int array[],int len)
{
	int i;
	for(i = 0;i < len;i += 1)
	{
		if(array[i] == key)
			return &array[i];
	}
}


void main()
{
	int array[] = {1,2,3,4,5,6};
	int key = 6;
	int *p;
	
	p = find_int(key,array,6);
	
	printf("%d\n",*p);
}
