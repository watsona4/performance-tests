import java.lang.String;
import java.util.*;

public class test_java_generics {

    public static void main(String[] args) {

	int n = Integer.parseInt(args[0]);

	long start = System.currentTimeMillis();

	Vector<Double> x = new Vector<Double>();

	for (int i = 0; i < n; ++i)
	    x.add(Math.random());

	Vector<Vector<Double>> a = new Vector<Vector<Double>>();

	for (int i = 0; i < n; ++i) {

	    Vector<Double> row = new Vector<Double>();

	    for (int j = 0; j < n; ++j)
		row.add(Math.random());

	    a.add(row);
	}

	Vector<Double> y = new Vector<Double>();

	for (int i = 0; i < n; ++i)
	    y.add(0.0);

	long end = System.currentTimeMillis();

	System.out.format("*** Java (vector) ***:  Construction = %.6f sec\n",
			  (double)(end - start)/1000);

	start = System.currentTimeMillis();
	
	for (int i = 0; i < n; ++i)
	    for (int j = 0; j < n; ++j)
		y.set(i, y.get(i) + a.get(i).get(j)*x.get(j));

	end = System.currentTimeMillis();

	System.out.format("*** Java (vector) ***:  Computation = %.6f sec\n",
			  (double)(end - start)/1000);
    }
}
