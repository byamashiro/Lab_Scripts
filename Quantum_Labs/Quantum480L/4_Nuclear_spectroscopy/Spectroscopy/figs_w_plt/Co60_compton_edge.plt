# Gnuplot script file for plotting data
# 

set terminal png nocrop enhanced size 900,700 font 'arial,18'

set out 'Co60_gnuplot.png'

FILE_NAMES = 'newcobalt.Spe'

#set tics font ", 30"
set origin 0,0 #origin of plot
set title '^{60}Co'
set ylabel "Amplitude (counts)"
set xlabel "Channel Number"
set xr [0:2050]
set yr [0:800]
#set key top right
#set bar small
set grid

q(x) = A3*exp(-0.5*((x-o3)/s3)**2)+c3
A3=247;# height
o3=713;# peak center
c3=145;# continuum
s3=50;# width
fit [636:766] q(x) FILE_NAMES u 0:1 via A3,o3,s3,c3

p(x) = A4*exp(-0.5*((x-o4)/s4)**2)+c4
A4=162;# height
o4=813;# peak center
c4=78;# continuum
s4=50;# width
fit [766:900] p(x) FILE_NAMES u 0:1 via A4,o4,s4,c4

plot FILE_NAMES u 0:1:($1**0.5) pt 1 lc rgb '#0000FF' ps 0.5 t '0cm data' w yerrorbars, \
	q(x) lt 2 lc rgb '#32CD32' t 'Gaussian: 0cm', \
	p(x) lt 3 lc rgb '#32CD32' t 'Gaussian: 0cm'


unset grid
