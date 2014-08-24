import java.lang.String;

public class test_java {

    public static void main(String[] args) {

	int n = Integer.parseInt(args[0]);

	long start = System.currentTimeMillis();

	double[] x = new double[n];

	for (int i = 0; i < n; ++i)
	    x[i] = Math.random();

	double[][] a = new double[n][n];

	for (int i = 0; i < n; ++i)
	    for (int j = 0; j < n; ++j)
		a[i][j] = Math.random();

	double[] y = new double[n];

	for (int i = 0; i < n; ++i)
	    y[i] = 0.0;

	long end = System.currentTimeMillis();

	System.out.format("*** Java (array) ***:  Construction = %.6f sec\n",
			  (double)(end - start)/1000);

	start = System.currentTimeMillis();
	
	for (int i = 0; i < n; ++i)
	    for (int j = 0; j < n; ++j)
		y[i] += a[i][j]*x[j];

	end = System.currentTimeMillis();

	System.out.format("*** Java (array) ***:  Computation = %.6f sec\n",
			  (double)(end - start)/1000);
    }
}
