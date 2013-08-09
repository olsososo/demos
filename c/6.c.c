#include <stdio.h>

void Exchg3(int &x, int &y)
{
    int tmp = x;
    x = y;
    y = tmp;
    printf("x = %d,y = %d\n", x, y);
}

main()
{
    int a = 4;
    int b = 6;
    Exchg3(a, b);
    printf("a = %d, b = %d\n", a, b);
    return(0);
}

