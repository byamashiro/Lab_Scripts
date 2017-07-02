# Gnuplot script file for plotting data
# 

set terminal png nocrop enhanced size 900,700 font 'arial,18'

set out 'calib2.png'

set multiplot
set size 1,1
#set tics font ", 30"
set origin 0,0 #origin of plot
set title "Calibration: MCA Peak Channel vs. Energy"
set ylabel "Peak Channel"
set xlabel "Energy (MeV)"
set xr [.2:1.6]
#set yr [0:600]
#set yr [-500000:8000000]
set autoscale y
#set autoscale x
#set logscale x
#set logscale y
set key top right
set bar small
set grid
f(x) = m*x+b
#g(x) = q*x+c
#h(x) = j*x+d
#f(x) = a*x**2 + b*x + c          # define a quadratic function
#fit f(x) 'zat.dat' via a,b,c    # compute the coefficients a,b,c

fit f(x) "calib2.dat" using 1:2:3 via m,b
#fit g(x) "ams.dat" using 6:7 via q,c
#fit h(x) "ams.dat" using 1:5 via j,d

#f1(x)=a1*x+b1
#fit [260:450] f1(x) "sol.dat" u 1:2 via a1, b1
#f2(x)=a2*x+b2
#fit [950:1100] f2(x) "sol.dat" u 1:2 via a2, b2


plot f(x) lw 2 lc rgb "green" t '',\
	"calib2.dat" using 1:2:3 title '' lc rgb "blue" ps 2 lw 3 pt 1 with yerrorbars,\
	'calib2.dat' u 1:2:4 with labels font "10" offset 1.3,-.8,0 tc rgb "black" t ''

#=============mini plot=============      
set grid
unset multiplot