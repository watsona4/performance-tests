import time
import subprocess
import re
import math
from prettytable import PrettyTable

batches = 1
n_per_batch = 1

size = 800

#########################################################################

def average(x):
    return float(sum(x))/len(x)

#########################################################################

def stdev(x):
    if len(x) == 1: return 0.0
    return (sum(map(lambda v: v**2, x)) - len(x)*average(x)**2)/ \
        (len(x) - 1)

#########################################################################

def run_test(s):

    e_const = re.compile('\*\*\* .* \*\*\*:  Construction = (.*) sec')
    e_fact = re.compile('\*\*\* .* \*\*\*:  Factorization = (.*) sec')
    e_subs = re.compile('\*\*\* .* \*\*\*:  Substitution = (.*) sec')

    const_times = []
    fact_times = []
    subs_times = []

    for b in xrange(batches):

        const_time = 0.0
        fact_time = 0.0
        subs_time = 0.0

        for i in xrange(n_per_batch):

            p = subprocess.Popen(s.split(), stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)

            out = p.communicate()[0]

            for line in out.split('\n'):
                if line: print 'b = %d, i = %d, %s' % (b, i, line)
                m = e_const.search(line)
                if m: const_time += float(m.group(1))
                m = e_fact.search(line)
                if m: fact_time += float(m.group(1))
                m = e_subs.search(line)
                if m: subs_time += float(m.group(1))

        const_times.append(const_time/n_per_batch)
        fact_times.append(fact_time/n_per_batch)
        subs_times.append(subs_time/n_per_batch)

    const_time = average(const_times)
    fact_time = average(fact_times)
    subs_time = average(subs_times)

    const_time_var = stdev(const_times)
    fact_time_var = stdev(fact_times)
    subs_time_var = stdev(subs_times)

    return (const_time, fact_time, subs_time)

#########################################################################

result = []

# # Test Python (list)

# times = run_test('python test_python_lu.py %d' % size)

# print '*** Python (list) ***:  Construction time = %.6g' % times[0]
# print '*** Python (list) ***:  Factorization time = %.6g' % times[1]
# print '*** Python (list) ***:  Substitution time = %.6g' % times[2]

# result.append(('Python (list)', times[0], times[1], times[2], sum(times)))

# # Test Python (NumPy)

# times = run_test('python test_numpy_lu.py %d' % size)

# print '*** Python (NumPy) ***:  Construction time = %.6g' % times[0]
# print '*** Python (NumPy) ***:  Factorization time = %.6g' % times[1]
# print '*** Python (NumPy) ***:  Substitution time = %.6g' % times[2]

# result.append(('Python (NumPy)', times[0], times[1], times[2], sum(times)))

# # Test Python (SciPy)

# times = run_test('python test_scipy_lu.py %d' % size)

# print '*** Python (SciPy) ***:  Construction time = %.6g' % times[0]
# print '*** Python (SciPy) ***:  Factorization time = %.6g' % times[1]
# print '*** Python (SciPy) ***:  Substitution time = %.6g' % times[2]

# result.append(('Python (SciPy)', times[0], times[1], times[2], sum(times)))

# Test C

subprocess.Popen(['gcc','-Ofast','test_c_lu.c','-o','test_c_lu']).wait()

times = run_test('./test_c_lu %d' % size)

print '*** C ***:  Construction time = %.6g' % times[0]
print '*** C ***:  Factorization time = %.6g' % times[1]
print '*** C ***:  Substitution time = %.6g' % times[2]

result.append(('C', times[0], times[1], times[2], sum(times)))

# Test C OpenMP

subprocess.Popen('gcc -Ofast -fopenmp test_c_lu_mp.c -o test_c_lu_mp -L/usr/local/lib'.split()).wait()

times = run_test('./test_c_lu_mp %d' % size)

print '*** C OpenMP ***:  Construction time = %.6g' % times[0]
print '*** C OpenMP ***:  Factorization time = %.6g' % times[1]
print '*** C OpenMP ***:  Substitution time = %.6g' % times[2]

result.append(('C OpenMP', times[0], times[1], times[2], sum(times)))

# # Test C++ (array)

# subprocess.Popen(['g++','-Ofast','test_cpp_array_lu.cpp','-o','test_cpp_array_lu']).wait()

# times = run_test('./test_cpp_array_lu %d' % size)

# print '*** C++ (array) ***:  Construction time = %.6g' % times[0]
# print '*** C++ (array) ***:  Factorization time = %.6g' % times[1]
# print '*** C++ (array) ***:  Substitution time = %.6g' % times[2]

# result.append(('C++ (array)', times[0], times[1], times[2], sum(times)))

# # Test C++ (STL)

# subprocess.Popen(['g++','-Ofast','test_cpp_stl_lu.cpp','-o','test_cpp_stl_lu']).wait()

# times = run_test('./test_cpp_stl_lu %d' % size)

# print '*** C++ (STL) ***:  Construction time = %.6g' % times[0]
# print '*** C++ (STL) ***:  Factorization time = %.6g' % times[1]
# print '*** C++ (STL) ***:  Substitution time = %.6g' % times[2]

# result.append(('C++ (STL)', times[0], times[1], times[2], sum(times)))

# # Test Fortran 77

# subprocess.Popen(['gfortran','-Ofast','test_f77_lu.f','-o','test_f77_lu']).wait()

# times = run_test('./test_f77_lu %d' % size)

# print '*** Fortran 77 ***:  Construction time = %.6g' % times[0]
# print '*** Fortran 77 ***:  Factorization time = %.6g' % times[1]
# print '*** Fortran 77 ***:  Substitution time = %.6g' % times[2]

# result.append(('Fortran 77', times[0], times[1], times[2], sum(times)))

# # Test Fortran 90

# subprocess.Popen(['gfortran','-Ofast','test_fortran_lu.f90','-o','test_fortran_lu']).wait()

# times = run_test('./test_fortran_lu %d' % size)

# print '*** Fortran 90 ***:  Construction time = %.6g' % times[0]
# print '*** Fortran 90 ***:  Factorization time = %.6g' % times[1]
# print '*** Fortran 90 ***:  Substitution time = %.6g' % times[2]

# result.append(('Fortran 90', times[0], times[1], times[2], sum(times)))

# # Test Java arrays

# subprocess.Popen(['javac','test_java_lu.java']).wait()

# times = run_test('java test_java_lu %d' % size)

# print '*** Java (array) ***:  Construction time = %.6g' % times[0]
# print '*** Java (array) ***:  Factorization time = %.6g' % times[1]
# print '*** Java (array) ***:  Substitution time = %.6g' % times[2]

# result.append(('Java (array)', times[0], times[1], times[2], sum(times)))

# # Test Java vector

# subprocess.Popen(['javac','test_java_generics.java']).wait()

# times = run_test('java test_java_generics %d' % size)

# print '*** Java (vector) ***:  Construction time = %.6g' % times[0]
# print '*** Java (vector) ***:  Factorization time = %.6g' % times[1]
# print '*** Java (vector) ***:  Substitution time = %.6g' % times[2]

# result.append(('Java (vector)', times[0], times[1], times[2], sum(times)))

# # Test Java arraylist

# subprocess.Popen(['javac','test_java_arraylist.java']).wait()

# times = run_test('java test_java_arraylist %d' % size)

# print '*** Java (arraylist) ***:  Construction time = %.6g' % times[0]
# print '*** Java (arraylist) ***:  Factorization time = %.6g' % times[1]
# print '*** Java (arraylist) ***:  Substitution time = %.6g' % times[2]

# result.append(('Java (arraylist)', times[0], times[1], times[2], sum(times)))

# # Test C# array

# subprocess.Popen('gmcs test_cs_lu.cs'.split()).wait()

# times = run_test('mono test_cs_lu.exe %d' % size)

# print '*** C# (array) ***:  Construction time = %.6g' % times[0]
# print '*** C# (array) ***:  Factorization time = %.6g' % times[1]
# print '*** C# (array) ***:  Substitution time = %.6g' % times[2]

# result.append(('C# (array)', times[0], times[1], times[2], sum(times)))

# # Test C# arraylist

# subprocess.Popen('gmcs test_cs_arraylist.cs'.split()).wait()

# times = run_test('mono test_cs_arraylist.exe %d' % size)

# print '*** C# (arraylist) ***:  Construction time = %.6g' % times[0]
# print '*** C# (arraylist) ***:  Factorization time = %.6g' % times[1]
# print '*** C# (arraylist) ***:  Substitution time = %.6g' % times[2]

# result.append(('C# (arraylist)', times[0], times[1], times[2], sum(times)))

# # Test C# list

# subprocess.Popen('gmcs test_cs_list.cs'.split()).wait()

# times = run_test('mono test_cs_list.exe %d' % size)

# print '*** C# (list) ***:  Construction time = %.6g' % times[0]
# print '*** C# (list) ***:  Factorization time = %.6g' % times[1]
# print '*** C# (list) ***:  Substitution time = %.6g' % times[2]

# result.append(('C# (list)', times[0], times[1], times[2], sum(times)))

# Output results sorted by construction time

result.sort(key=lambda x: x[1])

pt = PrettyTable(['Solver','Construction','Factorization','Substitution','Total'])

for res in result:
    pt.add_row([res[0], '%.6f'%res[1], '%.6f'%res[2], '%.6f'%res[3], '%.6f'%res[4]])

print '\nResults Sorted by Construction Time:\n', pt

# Output results sorted by factorization time

result.sort(key=lambda x: x[2])

pt = PrettyTable(['Solver','Construction','Factorization','Substitution','Total'])

for res in result:
    pt.add_row([res[0], '%.6f'%res[1], '%.6f'%res[2], '%.6f'%res[3], '%.6f'%res[4]])

print '\nResults Sorted by Factorization Time:\n', pt

# Output results sorted by substitution time

result.sort(key=lambda x: x[3])

pt = PrettyTable(['Solver','Construction','Factorization','Substitution','Total'])

for res in result:
    pt.add_row([res[0], '%.6f'%res[1], '%.6f'%res[2], '%.6f'%res[3], '%.6f'%res[4]])

print '\nResults Sorted by Substitution Time:\n', pt

# Output results sorted by total time

result.sort(key=lambda x: x[4])

pt = PrettyTable(['Solver','Construction','Factorization','Substitution','Total','Ratio'])

for res in result:
    pt.add_row([res[0], '%.6f'%res[1], '%.6f'%res[2], '%.6f'%res[3], '%.6f'%res[4], '%.2f'%(res[4]/result[0][4])])

print '\nResults Sorted by Total Time:\n', pt
