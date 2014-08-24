import java.lang.String;
import java.util.*;

public class test_java_arraylist {

    public static void main(String[] args) {

	int n = Integer.parseInt(args[0]);

	long start = System.currentTimeMillis();

	ArrayList<Double> x = new ArrayList<Double>();

	for (int i = 0; i < n; ++i)
	    x.add(Math.random());

	ArrayList<ArrayList<Double>> a = new ArrayList<ArrayList<Double>>();

	for (int i = 0; i < n; ++i) {

	    ArrayList<Double> row = new ArrayList<Double>();

	    for (int j = 0; j < n; ++j)
		row.add(Math.random());

	    a.add(row);
	}

	ArrayList<Double> y = new ArrayList<Double>();

	for (int i = 0; i < n; ++i)
	    y.add(0.0);

	long end = System.currentTimeMillis();

	System.out.format("*** Java (arraylist) ***:  Construction = %.6f sec\n",
			  (double)(end - start)/1000);

	start = System.currentTimeMillis();
	
	for (int i = 0; i < n; ++i)
	    for (int j = 0; j < n; ++j)
		y.set(i, y.get(i) + a.get(i).get(j)*x.get(j));

	end = System.currentTimeMillis();

	System.out.format("*** Java (arraylist) ***:  Computation = %.6f sec\n",
			  (double)(end - start)/1000);
    }
}
