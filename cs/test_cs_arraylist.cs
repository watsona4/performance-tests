using System;
using System.Collections;

public class test_cs_arraylist {
  
  public static void Main(string[] args) {
    
    int n = Convert.ToInt32(args[0]);

    DateTime start = DateTime.Now;

    Random rand = new Random();

    ArrayList x = new ArrayList(n);

    for (int i = 0; i < n; ++i)
      x.Add(rand.NextDouble());

    ArrayList a = new ArrayList(n*n);

    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
    	a.Add(rand.NextDouble());

    ArrayList y = new ArrayList(n);
    
    for (int i = 0; i < n; ++i)
      y.Add(0.0);

    DateTime end = DateTime.Now;

    Console.WriteLine("*** C# (array) ***:  Construction = {0:F6} sec",
		      end.Subtract(start).TotalSeconds);

    start = DateTime.Now;
	
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
     	y[i] = Convert.ToDouble(y[i]) + Convert.ToDouble(a[i*n+j])*
	  Convert.ToDouble(x[j]);
    
    end = DateTime.Now;
    
    Console.WriteLine("*** C# (array) ***:  Computation = {0:F6} sec",
		      end.Subtract(start).TotalSeconds);
  }
}
