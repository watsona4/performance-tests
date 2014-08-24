#include <iostream>
#include <iomanip>
#include <ctime>

using namespace std;

int main(int argc, char* argv[])
{
  int n = atoi(argv[1]);

  time_t start = clock();

  double* x = new double[n];

  for (int i = 0; i < n; ++i)
    x[i] = rand();

  double** a = new double*[n];

  for (int i = 0; i < n; ++i) {

    a[i] = new double[n];

    for (int j = 0; j < n; ++j)
      a[i][j] = rand();
  }

  double* y = new double[n];

  for (int i = 0; i < n; ++i)
    y[i] = 0.0;

  time_t end = clock();

  cout << "*** C++ (array) ***:  Construction = " << setprecision(6)
       << (double)(end - start)/CLOCKS_PER_SEC << " sec" << endl;

  start = clock();

  for (int i = 0; i < n; ++i)
    for (int j = 0; j < n; ++j)
      y[i] += a[i][j]*x[j];

  end = clock();

  cout << "*** C++ (array) ***:  Computation = " << setprecision(6)
       << (double)(end - start)/CLOCKS_PER_SEC << " sec" << endl;

  delete x;
  delete y;
  
  for (int i = 0; i < n; ++i)
    delete a[i];

  delete a;
}
