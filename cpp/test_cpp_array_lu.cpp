#include <iostream>
#include <iomanip>
#include <ctime>

using namespace std;

int main(int argc, char* argv[])
{
  int n = atoi(argv[1]);
  int m = 20;

  time_t start = clock();

  double** b = new double*[m];

  for (int i = 0; i < m; ++i) {

    b[i] = new double[n];

    for (int j = 0; j < n; ++j)
      b[i][j] = i + j + 2;
  }

  double** a = new double*[n];

  for (int i = 0; i < n; ++i) {

    a[i] = new double[n];

    for (int j = 0; j < n; ++j)
      a[i][j] = 1.0/(i + j + 1.0);
  }

  time_t end = clock();

  cout << "*** C++ (array) ***:  Construction = " << setprecision(6)
       << (double)(end - start)/CLOCKS_PER_SEC << " sec" << endl;

  start = clock();

  for (int k = 0; k < n-1; ++k)
    for (int i = k+1; i < n; ++i) {
      a[i][k] /= a[k][k];
      for (int j = k+1; j < n; ++j)
	a[i][j] -= a[i][k]*a[k][j];
    }

  end = clock();

  cout << "*** C++ (array) ***:  Factorization = " << setprecision(6)
       << (double)(end - start)/CLOCKS_PER_SEC << " sec" << endl;

  start = clock();

  double** x = new double*[m];
  for (int i = 0; i < m; ++i)
    x[i] = new double[n];

  for (int k = 0; k < m; ++k) {

    x[k][0] = b[k][0];
    for (int i = 1; i < n; ++i) {
      double s = 0.0;
      for (int j = 0; j < i-1; ++j)
	s += a[i][j]*x[k][j];
      x[k][i] = b[k][i] - s;
    }

    x[k][n-1] /= a[n-1][n-1];
    for (int i = n-2; i > -1; --i) {
      double s = 0.0;
      for (int j= i+1; j < n; ++j)
	s += a[i][j]*x[k][j];
      x[k][i] = (x[k][i] - s)/a[i][i];
    }
  }

  end = clock();

  cout << "*** C++ (array) ***:  Substitution = " << setprecision(6)
       << (double)(end - start)/CLOCKS_PER_SEC << " sec" << endl;

  for (int i = 0; i < m; ++i)
    delete b[i];

  delete b;

  for (int i = 0; i < n; ++i)
    delete a[i];

  delete a;

  for (int i = 0; i < m; ++i)
    delete x[i];

  delete x;
}
