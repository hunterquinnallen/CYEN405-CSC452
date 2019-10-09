#include <stdio.h>
#include <time.h> 
#include "mpi.h"
int main(int argc, char *argv[]) {
	int rank, size;
	clock_t start, end;
	start = clock();
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	printf("Hello hqa001 or Hunter A from #%d of %d!\n", rank, size);
	end = clock();
	double t = (double) (end-start)/CLOCKS_PER_SEC;
	printf("Time elapsed is %f secs.\n", t);
	MPI_Finalize();
	return 0;
}
