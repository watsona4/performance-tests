      program test_fortran

      integer :: n, i, j
      double precision :: x(10000), a(10000,10000), y(10000)
      real :: start, finish
      character*30 :: n_str

      call getarg(1, n_str)
      read (n_str,*) n

      call cpu_time(start)

      do 10 i=1,n
         x(i) = rand()
 10   continue

      do 20 j=1,n
         do 30 i=1,n
            a(i,j) = rand()
 30      continue
 20   continue

      y(:) = 0d0

      call cpu_time(finish)
      
      write(*,'("*** Fortran 77 ***:  Construction = ",f10.6," sec")')
     c     finish - start

      call cpu_time(start)

      do 40 j=1,n
         do 50 i=1,n
            y(i) = y(i) + a(i,j)*x(j)
 50      continue
 40   continue

      call cpu_time(finish)

      write(*,'("*** Fortran 77 ***:  Computation = ",f10.6," sec")')
     c     finish - start
      
      end program test_fortran
