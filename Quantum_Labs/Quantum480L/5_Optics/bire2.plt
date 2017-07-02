# Gnuplot script file for plotting data
# 
set terminal png nocrop enhanced size 900,700 font 'arial,18'

set out 'bire2.png'

#set size 1,1
#set tics font ", 30"
#set origin 0,0 #origin of plot
set title "Birefringence of Decreasing from Zero"
set ylabel "Intensity (V)"
set xlabel "Angle(Degrees)"


#set xr [0:360]
#set yr [0:.15]
#set yr [-500000:8000000]
set autoscale y
set autoscale x
#set logscale x
#set logscale y
set key top right
set bar small
set grid

f1(x)=a1*((x-b1)**2) + c1
a1=1
b1=293
fit f1(x) 'bire.dat' u 4:5 via a1,b1,c1

plot	"bire.dat" using 4:5:6 title 'Measured Voltages' lc rgb "red" ps 2 lw 3 pt 1 with yerrorbars,\
	f1(x) t '' lw 2 lc rgb 'green'

#=============mini plot=============      
set grid
unset multiplot