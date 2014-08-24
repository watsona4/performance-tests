using System;

public class test_cs {
  
  public static void Main(string[] args) {
    
    int n = Convert.ToInt32(args[0]);

    DateTime start = DateTime.Now;

    Random rand = new Random();

    double[] x = new double[n];

    for (int i = 0; i < n; ++i)
      x[i] = rand.NextDouble();

    double[,] a = new double[n,n];

    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
    	a[i,j] = rand.NextDouble();

    double[] y = new double[n];
    
    for (int i = 0; i < n; ++i)
      y[i] = 0.0;

    DateTime end = DateTime.Now;

    Console.WriteLine("*** C# (array) ***:  Construction = {0:F6} sec",
		      end.Subtract(start).TotalSeconds);

    start = DateTime.Now;
	
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
     	y[i] += a[i,j]*x[j];
    
    end = DateTime.Now;
    
    Console.WriteLine("*** C# (array) ***:  Computation = {0:F6} sec",
		      end.Subtract(start).TotalSeconds);
  }
}
