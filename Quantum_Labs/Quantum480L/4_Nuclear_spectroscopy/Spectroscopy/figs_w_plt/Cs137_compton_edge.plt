# Gnuplot script file for plotting data
# 

set terminal png nocrop enhanced size 900,700 font 'arial,18'

set out 'Cs137_gnuplot.png'

FILE_NAMES = 'newcesium.Spe'

#set tics font ", 30"
set origin 0,0 #origin of plot
set title '^{137}Cs'
set ylabel "Amplitude (counts)"
set xlabel "Channel Number"
set xr [0:2050]
set yr [0:6000]
#set key top right
#set bar small
set grid



h(x) = A4*exp(-0.5*((x-o4)/s4)**2)+c4
A4=4000;# height
o4=480;# peak center
c4=10;# continuum
s4=80;# width
fit [400:500] h(x) FILE_NAMES u 0:1 via A4,o4,s4,c4

plot FILE_NAMES u 0:1:($1**0.5) pt 1 lc rgb '#0000FF' ps 0.5 t '0cm data' w yerrorbars, \
	h(x) lw 3 lt 3 lc rgb '#32CD32' t 'Gaussian: 0cm'


unset grid
unset multiplot