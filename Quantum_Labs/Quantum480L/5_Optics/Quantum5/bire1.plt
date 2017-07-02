# Gnuplot script file for plotting data
# 
set terminal png nocrop enhanced size 900,700 font 'arial,18'

set out 'bire1.png'

#set size 1,1
#set tics font ", 30"
#set origin 0,0 #origin of plot
set title "Birefringence of Increasing from Zero"
set ylabel "Intensity (V)"
set xlabel "Angle(Degrees)"


#set xr [0:360]
#set yr [0:.15]
#set yr [-500000:8000000]
set autoscale y
set autoscale x
#set logscale x
#set logscale y
set key bottom right
set bar small
set grid

f(x)=a*((x-b)**2)+c
#f(x)=a+b*x+c*x**2
a=1
b=70
fit f(x) 'bire.dat' u 1:2 via a,b,c


plot	"bire.dat" using 1:2:3 title 'Measured Voltages' lc rgb "blue" ps 2 lw 3 pt 1 with yerrorbars,\
	f(x) t '' lw 2 lc rgb 'green'

#=============mini plot=============      
set grid
unset multiplot