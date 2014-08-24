using System;
using System.Collections.Generic;

public class test_cs_arraylist {
  
  public static void Main(string[] args) {
    
    int n = Convert.ToInt32(args[0]);

    DateTime start = DateTime.Now;

    Random rand = new Random();

    List<double> x = new List<double>(n);

    for (int i = 0; i < n; ++i)
      x.Add(rand.NextDouble());

    List<List<double>> a = new List<List<double>>(n);

    for (int i = 0; i < n; ++i)
      {
	List<double> row = new List<double>(n);

	for (int j = 0; j < n; ++j)
	  row.Add(rand.NextDouble());

	a.Add(row);
      }

    List<double> y = new List<double>(n);
    
    for (int i = 0; i < n; ++i)
      y.Add(0.0);

    DateTime end = DateTime.Now;

    Console.WriteLine("*** C# (array) ***:  Construction = {0:F6} sec",
		      end.Subtract(start).TotalSeconds);

    start = DateTime.Now;
	
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
     	y[i] += a[i][j]*x[j];
    
    end = DateTime.Now;
    
    Console.WriteLine("*** C# (array) ***:  Computation = {0:F6} sec",
		      end.Subtract(start).TotalSeconds);
  }
}
