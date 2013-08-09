#include <stdio.h>

void Exchg(int *px,int *py)
{
	int tmp = *px;
	*px = *py;
	*py = tmp;

	printf("*px = %d,*py = %d\n",*px,*py);
}


int main()
{
	int a = 4;
	int b = 6;

	Exchg(&a,&b);

	printf("a = %d,b = %d\n",a,b);

	return(0);
}
