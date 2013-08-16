#include <stdio.h>

main()
{
	/*struct SIMPLE {
		int a;
		char b;
		float c;
	}

	struct SIMPLE x;
	struct SIMPLE y[20],*z;
	*/

	struct SIMPLE {
		int 	a;
		char 	b;
		float	c;
	};

	struct SIMPLE x;
	struct SIMPLE y[20],*z;

	struct COMPLEX {
		float 	f;
		int 	a[20];
		long 	*lp;
		struct SIMPLE s;
		struct SIMPLE sa[10];
		struct SIMPLE *sp;
	};
	
	struct SIMPLE s = {
		1,'a',3.14
	};
	
	union {
		float 	f;
		int 	i;
	} fi;

	fi.i = 3;

	printf("%f\n",fi.f);

}
