#include <stdio.h>

main()
{
	int a = 112;
	int *b = &a;
	*b = 100;
	printf("%d\n",a);
}
/*
main()
{
	int a,b;
	int *point_1,*point_2;
	scanf("%d,%d",&a,&b);

	point_1 = &a;
	point_2 = &b;

	printf("%d,%d\n",*point_1,*point_2);
}*/
