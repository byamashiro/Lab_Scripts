#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <unistd.h>
#include <string.h>

/***********************************************************
 *
 * rebin.c - simple rebinner, reads from stdin, outs to stdout.  
 *           Copyright(c) 2013 Kevin Croker for Physics 481L
 *           GPL v3 License
 *
 *           Assumes (data has been sorted and bin number is first 
 *           column value) OR (row number)
 *
 *           CAVEAT handles at most 1024 bytes of garbage per line
 * 
 ******************************************** *****************/

const char *usage = "Usage: %s bin_width [format_specifier]\n";

int main(int argc, char **argv) {

  float datum;
  float width;
  char *fmtspec = 0;
  int oldrows, bin;
  float binContents;
  char buffer[1024];

  // Make sure they specified at least a bin width
  if(argc < 2 || argc > 3) {

    printf(usage, argv[0]);
    return 1;
  }
  
  // Parse it into a float
  width = atof(argv[1]);
  if(width <= 0.0) {

    printf("Bad parsed width %f\n", width);
    return 2;
  }

  // Did they give a format spec?
  if(argc == 3) {
    printf("Not yet implemented\n");
    return 3;
  }
  else
    fmtspec = "%f";
  
  // Keep track of rows
  bin = 0;
  
  while(!feof(stdin)) {

    for(oldrows = 0; oldrows < width; ++oldrows) {
      
      // Try to read a line
      if(scanf(fmtspec, &datum) <= 0) {
	
	// Bitch
	if(scanf("%s", buffer) <= 0)
	  fprintf(stderr, "Bad row %d, no contents read (width not multiple of data quantity?)\n", bin*(int)width+oldrows);
	else
	  fprintf(stderr, "Bad row %d: \"%s\"\n", bin*(int)width+oldrows, buffer);

	continue;
      }
      else {
	
	// Accumulate
	binContents += datum;
      }
    }
    
    // Output, with explicit width for clarity
    printf("%f\t%f\n", width*bin, binContents);
    ++bin;
    binContents = 0.0;
  }
  
  return 0;
}
  