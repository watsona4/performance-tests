import time
import subprocess
import re
import math
from prettytable import PrettyTable

batches = 1
n_per_batch = 1

size = 4000

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
    e_comp = re.compile('\*\*\* .* \*\*\*:  Computation = (.*) sec')

    const_times = []
    comp_times = []

    for b in xrange(batches):

        const_time = 0.0
        comp_time = 0.0

        for i in xrange(n_per_batch):

            p = subprocess.Popen(s.split(), stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)

            out = p.communicate()[0]

            for line in out.split('\n'):
                if line: print 'b = %d, i = %d, %s' % (b, i, line)
                m = e_const.search(line)
                if m: const_time += float(m.group(1))
                m = e_comp.search(line)
                if m: comp_time += float(m.group(1))

        const_times.append(const_time/n_per_batch)
        comp_times.append(comp_time/n_per_batch)

    const_time = average(const_times)
    comp_time = average(comp_times)

    const_time_var = stdev(const_times)
    comp_time_var = stdev(comp_times)

    return (const_time, comp_time)

#########################################################################

result = []

# Test Python

(const_time,comp_time) = run_test('python test_python.py %d' % size)

print '*** Python ***:  Construction time = %.6g' % const_time
print '*** Python ***:  Computation time = %.6g' % comp_time

result.append(('Python', const_time, comp_time, const_time+comp_time))

# Test Numpy

(const_time,comp_time) = run_test('python test_numpy.py %d' % size)

print '*** Numpy ***:  Construction time = %.6g' % const_time
print '*** Numpy ***:  Computation time = %.6g' % comp_time

result.append(('Numpy', const_time, comp_time, const_time+comp_time))

# Test C

subprocess.Popen(['gcc','-O3','test_c.c','-o','test_c']).wait()

(const_time,comp_time) = run_test('./test_c %d' % size)

print '*** C ***:  Construction time = %.6g' % const_time
print '*** C ***:  Computation time = %.6g' % comp_time

result.append(('C', const_time, comp_time, const_time+comp_time))

# Test C OpenMP

subprocess.Popen(['gcc','-O3','-fopenmp','test_c_mp.c','-o','test_c_mp']).wait()

(const_time,comp_time) = run_test('./test_c_mp %d' % size)

print '*** C OpenMP ***:  Construction time = %.6g' % const_time
print '*** C OpenMP ***:  Computation time = %.6g' % comp_time

result.append(('C OpenMP', const_time, comp_time, const_time+comp_time))

# Test C++ (array)

subprocess.Popen(['g++','-O3','test_cpp_array.cpp','-o','test_cpp_array']).wait()

(const_time,comp_time) = run_test('./test_cpp_array %d' % size)

print '*** C++ (array) ***:  Construction time = %.6g' % const_time
print '*** C++ (array) ***:  Computation time = %.6g' % comp_time

result.append(('C++ (array)', const_time, comp_time, const_time+comp_time))

# Test C++ (STL)

subprocess.Popen(['g++','-O3','test_cpp_stl.cpp','-o','test_cpp_stl']).wait()

(const_time,comp_time) = run_test('./test_cpp_stl %d' % size)

print '*** C++ (STL) ***:  Construction time = %.6g' % const_time
print '*** C++ (STL) ***:  Computation time = %.6g' % comp_time

result.append(('C++ (STL)', const_time, comp_time, const_time+comp_time))

# Test Fortran 77

subprocess.Popen(['gfortran','-O3','test_f77.f','-o','test_f77']).wait()

(const_time,comp_time) = run_test('./test_f77 %d' % size)

print '*** Fortran 77 ***:  Construction time = %.6g' % const_time
print '*** Fortran 77 ***:  Computation time = %.6g' % comp_time

result.append(('Fortran 77', const_time, comp_time, const_time+comp_time))

# Test Fortran 90

subprocess.Popen(['gfortran','-O3','test_fortran.f90','-o','test_fort']).wait()

(const_time,comp_time) = run_test('./test_fort %d' % size)

print '*** Fortran 90 ***:  Construction time = %.6g' % const_time
print '*** Fortran 90 ***:  Computation time = %.6g' % comp_time

result.append(('Fortran 90', const_time, comp_time, const_time+comp_time))

# Test Java arrays

subprocess.Popen(['javac','test_java.java']).wait()

(const_time,comp_time) = run_test('java test_java %d' % size)

print '*** Java (array) ***:  Construction time = %.6g' % const_time
print '*** Java (array) ***:  Computation time = %.6g' % comp_time

result.append(('Java (array)', const_time, comp_time, const_time+comp_time))

# Test Java vector

subprocess.Popen(['javac','test_java_generics.java']).wait()

(const_time,comp_time) = run_test('java test_java_generics %d' % size)

print '*** Java (vector) ***:  Construction time = %.6g' % const_time
print '*** Java (vector) ***:  Computation time = %.6g' % comp_time

result.append(('Java (vector)', const_time, comp_time, const_time+comp_time))

# Test Java arraylist

subprocess.Popen(['javac','test_java_arraylist.java']).wait()

(const_time,comp_time) = run_test('java test_java_arraylist %d' % size)

print '*** Java (arraylist) ***:  Construction time = %.6g' % const_time
print '*** Java (arraylist) ***:  Computation time = %.6g' % comp_time

result.append(('Java (arraylist)', const_time, comp_time, const_time+comp_time))

# Test C# array

subprocess.Popen('gmcs test_cs.cs'.split()).wait()

(const_time,comp_time) = run_test('mono test_cs.exe %d' % size)

print '*** C# (array) ***:  Construction time = %.6g' % const_time
print '*** C# (array) ***:  Computation time = %.6g' % comp_time

result.append(('C# (array)', const_time, comp_time, const_time+comp_time))

# Test C# arraylist

subprocess.Popen('gmcs test_cs_arraylist.cs'.split()).wait()

(const_time,comp_time) = run_test('mono test_cs_arraylist.exe %d' % size)

print '*** C# (arraylist) ***:  Construction time = %.6g' % const_time
print '*** C# (arraylist) ***:  Computation time = %.6g' % comp_time

result.append(('C# (arraylist)', const_time, comp_time, const_time+comp_time))

# Test C# list

subprocess.Popen('gmcs test_cs_list.cs'.split()).wait()

(const_time,comp_time) = run_test('mono test_cs_list.exe %d' % size)

print '*** C# (list) ***:  Construction time = %.6g' % const_time
print '*** C# (list) ***:  Computation time = %.6g' % comp_time

result.append(('C# (list)', const_time, comp_time, const_time+comp_time))

# Output results sorted by construction time

result.sort(key=lambda x: x[1])

pt = PrettyTable(['Solver','Construction','Computation','Total'])

for res in result:
    pt.add_row([res[0], '%.6f'%res[1], '%.6f'%res[2], '%.6f'%res[3]])

print pt

# Output results sorted by computation time

result.sort(key=lambda x: x[2])

pt = PrettyTable(['Solver','Construction','Computation','Total'])

for res in result:
    pt.add_row([res[0], '%.6f'%res[1], '%.6f'%res[2], '%.6f'%res[3]])

print pt

# Output results sorted by total time

result.sort(key=lambda x: x[3])

pt = PrettyTable(['Solver','Construction','Computation','Total'])

for res in result:
    pt.add_row([res[0], '%.6f'%res[1], '%.6f'%res[2], '%.6f'%res[3]])

print pt
