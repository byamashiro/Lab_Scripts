# Gnuplot script file for plotting data
# 

set terminal png nocrop enhanced size 900,700 font 'arial,18'

set out 'Co60__doub_gauss_quad_back.png'

FILE_NAMES = 'newcobalt.Spe'

#set tics font ", 30"
set origin 0,0 #origin of plot
set title '^{60}Co'
set ylabel "Amplitude (counts)"
set xlabel "Channel Number"
set xr [0:2050]
set yr [0:600]
#set key top right
#set bar small
set grid


f(x) = A1*exp(-0.5*((x-o1)/s1)**2)+(e1*x*x)+(d1*x)+c1 + A2*exp(-0.5*((x-o2)/s2)**2)
A1=247;# height
o1=713;# peak center
c1=145;# continuum
s1=50;# width
d1=50;
e1=50;
A2=162;# height
o2=813;# peak center
c2=78;# continuum
s2=100;# width
fit [630:900] f(x) FILE_NAMES u 0:1 via A1,o1,s1,c1,d1,e1,A2,o2,s2



plot FILE_NAMES u 0:1:($1**0.5) pt 1 lc rgb '#0000FF' ps 0.5 t '0cm data' w yerrorbars, \
	[636:900] f(x) lw 3 lt 2 lc rgb 'green' t 'Gaussian: 0cm'



unset grid




