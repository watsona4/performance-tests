program test_fortran

  integer :: n, i, j, k
  double precision, allocatable :: b(:,:), a(:,:), x(:,:)
  double precision :: s
  real :: start, end
  integer, parameter :: m = 20
  character*30 :: n_str

  call getarg(1, n_str)
  read (n_str,*) n

  call cpu_time(start)

  allocate(b(n,m), a(n,n))

  do j=1,m
     do i=1,n
        b(j,i) = i + j
     enddo
  enddo

  do j=1,n
     do i=1,n
        a(j,i) = 1.0/(i + j - 1.0)
     enddo
  enddo

  call cpu_time(end)
  
  write(*,'("*** Fortran 90 ***:  Construction = ",f10.6," sec")') end - start

  call cpu_time(start)

  do k=1,n-1
     do i=k+1,n
        a(k,i) = a(k,i)/a(k,k)
        do j=k+1,n
           a(j,i) = a(j,i) - a(k,i)*a(j,k)
        enddo
     enddo
  enddo

  call cpu_time(end)

  write(*,'("*** Fortran 90 ***:  Factorization = ",f10.6," sec")') end - start

  call cpu_time(start)

  allocate(x(n,m))

  do k=1,m

     x(1,k) = b(1,k)
     do i=2,n
        s = 0d0
        do j=1,i-1
           s = s + a(j,i)*x(j,k)
        enddo
        x(j,k) = b(i,k) - s
     enddo

     x(n,k) = x(n,k)/a(n,n)
     do i=n-1,-1,1
        s = 0d0
        do j=i+1,n
           s = s + a(j,i)*x(j,k)
        enddo
        x(i,k) = (x(i,k) - s)/a(i,i)
     enddo

  enddo

  call cpu_time(end)

  write(*,'("*** Fortran 90 ***:  Substitution = ",f10.6," sec")') end - start

  deallocate(b,a,x)

end program test_fortran
