#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char* argv[])
{
  int i, j, k;

  int n = atoi(argv[1]);
  int m = 20;

  time_t start = clock();

  double** b = malloc(m*sizeof(double*));

  for (i = 0; i < n; ++i) {

    b[i] = malloc(n*sizeof(double));

    for (j = 0; j < n; ++j)
      b[i][j] = i + j + 2;
  }

  double** a = malloc(n*sizeof(double*));

  for (i = 0; i < n; ++i) {

    a[i] = malloc(n*sizeof(double));

    for (j = 0; j < n; ++j)
      a[i][j] = 1.0/(i + j + 1.0);
  }

  time_t end = clock();

  printf("*** C ***:  Construction = %.6f sec\n",
	 (double)(end - start)/CLOCKS_PER_SEC);

  start = clock();

  for (k = 0; k < n-1; ++k)
    for (i = k+1; i < n; ++i) {
      a[i][k] /= a[k][k];
      for (j = k+1; j < n; ++j)
	a[i][j] -= a[i][k]*a[k][j];
    }

  end = clock();

  printf("*** C ***:  Factorization = %.6f sec\n",
	 (double)(end - start)/CLOCKS_PER_SEC);

  start = clock();

  double** x = malloc(m*sizeof(double*));

  for (i = 0; i < n; ++i)
    x[i] = malloc(n*sizeof(double));

  double s;

  for (k = 0; k < m; ++k) {

    x[k][0] = b[k][0];
    for (i = 1; i < n; ++i) {
      s = 0.0;
      for (int j = 0; j < i-1; ++j)
	s += a[i][j]*x[k][j];
      x[k][i] = b[k][i] - s;
    }

    x[k][n-1] /= a[n-1][n-1];
    for (i = n-2; i > -1; --i) {
      s = 0.0;
      for (j= i+1; j < n; ++j)
	s += a[i][j]*x[k][j];
      x[k][i] = (x[k][i] - s)/a[i][i];
    }
  }

  end = clock();

  printf("*** C ***:  Substitution = %.6f sec\n",
	 (double)(end - start)/CLOCKS_PER_SEC);

  for (i = 0; i < n; ++i)
    free(a[i]);

  for (i = 0; i < m; ++i) {
    free(b[i]);
    free(x[i]);
  }

  free(b);
  free(a);
  free(x);
}
