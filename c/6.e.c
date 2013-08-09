#include <stdio.h>

void find(char array[],char search,char *pa)
{
	int i;

	for(i=0;*(array+i)!=0;i++)
	{
		if(*(array+i) == search)
		{
			pa = array + i;
			break;

		}else if(*(array + i) ==0)
		{
			pa = 0;
			break;
		} 
	}
}


int main()
{
	char str[] = {"abcdefghijklmnopqrstuvwxyz0"};
	char search = 'd';
	char *p = 0;

	find(str,search,p);

	if(p == 0)
	{
		printf("not found!\n");
	
	}else
	{
		printf("found,p = %d\n",p);
	}
}
