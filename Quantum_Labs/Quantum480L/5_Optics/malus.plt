# Gnuplot script file for plotting data
# 

set terminal png nocrop enhanced size 900,700 font 'arial,18'

set out 'malus.png'

set multiplot
set size 1,1
#set tics font ", 30"
set origin 0,0 #origin of plot
set title "Malus's Law"
set ylabel "Intensity (V)"
set xlabel "Angle(Degrees)"
#set xr [.2:1.6]
#set yr [0:600]
#set yr [-500000:8000000]
set autoscale y
set autoscale x
#set logscale x
#set logscale y
set key top right
set bar small
set grid
f(x) =I * cos((pi/180)*(x-k))**2 + d
I=10
k=270
d=0
fit f(x) "malus.dat" using 1:2 via I, k, d

#f1(x) =a1*(x-b1)**2 + c1
#a1=1
#b1=180
#fit [155:205] f1(x) "malus.dat" using 1:2 via a1, b1, c1


plot	"malus.dat" using 1:2:3 title 'Measured Voltages' lc rgb "blue" ps 2 lw 3 pt 1 with yerrorbars,\
	f(x) t 'Cos^2(x) Fit' lw 2 lc rgb 'red'
#	f1(x)

#=============mini plot=============      
set grid
unset multiplot