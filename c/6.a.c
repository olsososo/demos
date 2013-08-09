#include <stdio.h>

void Exchg(int x,int y)
{
	int tmp;
	tmp = x;
	x = y;
	y = tmp;
	printf("x = %d,y = %d\n",x,y);
}

int main()
{	
	int a = 4,b = 6;
	Exchg(a,b);
	printf("a = %d,b = %d\n",a,b);
	return(0);
}
