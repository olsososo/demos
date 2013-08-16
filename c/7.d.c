#include <stdio.h>
#include <stdarg.h>

int
average(int n_values,...)
{
	va_list var_arg;
	int count;
	int sum = 0;

	va_start(var_arg,n_values);
	
	for(count = 0;count < n_values;count += 1)
	{
		sum += va_arg(var_arg,int);
	}

	va_end(var_arg);
	
	printf("%d\n",sum);
}

int
main()
{
	
	average(5,5,5,5,5,5);
	
}
