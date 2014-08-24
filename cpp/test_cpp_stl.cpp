#include <iostream>
#include <iomanip>
#include <ctime>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
  int n = atoi(argv[1]);

  time_t start = clock();

  vector<double> x;
  x.reserve(n);

  for (int i = 0; i < n; ++i)
    x.push_back(rand());

  vector< vector<double> > a;
  a.reserve(n);

  for (int i = 0; i < n; ++i) {

    vector<double> row;
    row.reserve(n);

    for (int j = 0; j < n; ++j)
      row.push_back(rand());

    a.push_back(row);
  }

  vector<double> y;
  y.reserve(n);

  for (int i = 0; i < n; ++i)
    y.push_back(0.0);

  time_t end = clock();

  cout << "*** C++ (STL) ***:  Construction = " << setprecision(6)
       << (double)(end - start)/CLOCKS_PER_SEC << " sec" << endl;

  start = clock();

  for (int i = 0; i < n; ++i)
    for (int j = 0; j < n; ++j)
      y[i] += a[i][j]*x[j];

  end = clock();

  cout << "*** C++ (STL) ***:  Computation = " << setprecision(6)
       << (double)(end - start)/CLOCKS_PER_SEC << " sec" << endl;
}
