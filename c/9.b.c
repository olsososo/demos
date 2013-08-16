#include <stdio.h>
#include <string.h>


char *
my_strrstr(char const *s1,char const *s2)
{
	register char * last;
	register char * current;

	last = NULL;

}


main()
{
	char s[] = "Golden Global View";
	char *p;

	p = strchr(s,'V');
	
	printf("%s",p);
}
