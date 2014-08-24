import java.lang.String;

public class test_java_lu {

    public static void main(String[] args) {

	int n = Integer.parseInt(args[0]);
	int m = 20;

	long start = System.currentTimeMillis();

	double[][] b = new double[m][n];

	for (int i = 0; i < m; ++i)
	    for (int j = 0; j < n; ++j)
		b[i][j] = i + j + 2;

	double[][] a = new double[n][n];

	for (int i = 0; i < n; ++i)
	    for (int j = 0; j < n; ++j)
		a[i][j] = 1.0/(i + j + 1.0);

	long end = System.currentTimeMillis();

	System.out.format("*** Java (array) ***:  Construction = %.6f sec\n",
			  (double)(end - start)/1000);

	start = System.currentTimeMillis();
	
	for (int k = 0; k < n-1; ++k)
	    for (int i = k+1; i < n; ++i) {
		a[i][k] /= a[k][k];
		for (int j = k+1; j < n; ++j)
		    a[i][j] -= a[i][k]*a[k][j];
	    }

	end = System.currentTimeMillis();

	System.out.format("*** Java (array) ***:  Factorization = %.6f sec\n",
			  (double)(end - start)/1000);

	start = System.currentTimeMillis();

	double[][] x = new double[m][n];
	
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

	end = System.currentTimeMillis();

	System.out.format("*** Java (array) ***:  Substitution = %.6f sec\n",
			  (double)(end - start)/1000);
    }
}
