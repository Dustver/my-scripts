#include <stdio.h>
#include <time.h>
void function(){
  clock_t time_start= clock();
	for(int i = 0; i < 50000000000000; i++);
  clock_t time_end = clock() - time_start;
  printf("%f", (double)time_end / CLOCKS_PER_SEC);
}
int main()
{
	function();

    return 0;
}
