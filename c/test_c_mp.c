#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char* argv[])
{
  int i, j;

  int n = atoi(argv[1]);

  time_t start = clock();

  double* x = malloc(n*sizeof(double));

  for (i = 0; i < n; ++i)
    x[i] = rand();

  double** a = malloc(n*sizeof(double*));

  for (i = 0; i < n; ++i) {

    a[i] = malloc(n*sizeof(double));

    for (j = 0; j < n; ++j)
      a[i][j] = rand();
  }

  double* y = malloc(n*sizeof(double));

  for (i = 0; i < n; ++i)
    y[i] = 0.0;

  time_t end = clock();

  printf("*** C OpenMP ***:  Construction = %.6f sec\n",
	 (double)(end - start)/CLOCKS_PER_SEC);

  start = clock();

#pragma omp parallel shared(x,y,a,n) private(i,j)
  {
#  pragma omp for schedule(dynamic,chunk) nowait
    for (i = 0; i < n; ++i)
      for (j = 0; j < n; ++j)
	y[i] += a[i][j]*x[j];
  }

  end = clock();

  printf("*** C OpenMP ***:  Computation = %.6f sec\n",
	 (double)(end - start)/CLOCKS_PER_SEC);

  free(x);
  free(y);
  
  for (i = 0; i < n; ++i)
    free(a[i]);

  free(a);
}
