program test_fortran

  integer :: n, i, j
  double precision, allocatable :: x(:), a(:,:), y(:)
  real :: start, end
  character*30 :: n_str

  call getarg(1, n_str)
  read (n_str,*) n

  call cpu_time(start)

  allocate(x(n), a(n,n), y(n))

  do i=1,n
     call random_number(x(i))
  enddo

  do j=1,n
     do i=1,n
        call random_number(a(i,j))
     enddo
  enddo

  y(:) = 0d0

  call cpu_time(end)
  
  write(*,'("*** Fortran 90 ***:  Construction = ",f10.6," sec")') end - start

  call cpu_time(start)

  do j=1,n
    do i=1,n
      y(i) = y(i) + a(i,j)*x(j)
    enddo
  enddo

  call cpu_time(end)

  write(*,'("*** Fortran 90 ***:  Computation = ",f10.6," sec")') end - start

  deallocate(x,a,y)

end program test_fortran
