      program test_fortran

      integer :: n, i, j, k
      double precision :: b(10000,20), a(10000,10000), x(10000,20), s
      real :: start, finish
      integer, parameter :: m = 20
      character*30 :: n_str

      call getarg(1, n_str)
      read (n_str,*) n

      call cpu_time(start)

      do 10 i=1,m
         do 11 j=1,n
            b(j,i) = i + j
 11      continue
 10   continue

      do 12 i=1,n
         do 13 j=1,n
            a(j,i) = 1.0/(i + j - 1.0)
 13      continue
 12   continue

      call cpu_time(finish)
      
      write(*,'("*** Fortran 77 ***:  Construction = ",f10.6," sec")')
     c     finish - start

      call cpu_time(start)

      do 20 k=1,n-1
         do 21 i=k+1,n
            a(k,i) = a(k,i)/a(k,k)
            do 22 j=k+1,n
               a(j,i) = a(j,i) - a(k,i)*a(j,k)
 22         continue
 21      continue
 20   continue

      call cpu_time(finish)

      write(*,'("*** Fortran 77 ***:  Factorization = ",f10.6," sec")')
     c     finish - start

      call cpu_time(start)
      
      do 30 k=1,m
         
         x(1,k) = b(1,k)
         do 31 i=2,n
            s = 0d0
            do 32 j=1,i-1
               s = s + a(j,i)*x(j,k)
 32         continue
            x(j,k) = b(i,k) - s
 31      continue
         
         x(n,k) = x(n,k)/a(n,n)
         do 33 i=n-1,-1,1
            s = 0d0
            do 34 j=i+1,n
               s = s + a(j,i)*x(j,k)
 34         continue
            x(i,k) = (x(i,k) - s)/a(i,i)
 33      continue
         
 30   continue
      
      call cpu_time(finish)

      write(*,'("*** Fortran 77 ***:  Substitution = ",f10.6," sec")')
     c     finish - start
      
      end program test_fortran
