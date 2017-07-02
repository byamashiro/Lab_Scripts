# Gnuplot script file for plotting data
# 

set terminal png nocrop enhanced size 900,700 font 'arial,18'

set out 'Na22_gnuplot.png'

FILE_NAMES = 'newsodium.Spe'

#set tics font ", 30"
set origin 0,0 #origin of plot
set title '^{22}Na'
set ylabel "Amplitude (counts)"
set xlabel "Channel Number"
set auto x
set auto y
set xr [0:2050]
set yr [0:500]
#set key top right
#set bar small
set grid



g(x) = A4*exp(-0.5*((x-o4)/s4)**2)+c4
A4=250;# height
o4=300;# peak center
c4=5;# continuum
s4=50;# width
fit [250:400] g(x) FILE_NAMES u 0:1 via A4,o4,s4,c4

plot FILE_NAMES u 0:1:($1**0.5) pt 1 lc rgb '#0000FF' ps 0.5 t '0cm data' w yerrorbars, \
	g(x) lw 3 lt 3 lc rgb '#32CD32' t 'Gaussian: 0cm'


unset grid
unset multiplot