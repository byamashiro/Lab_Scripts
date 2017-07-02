# Gnuplot script file for plotting data
# 

set terminal png nocrop enhanced size 900,700 font 'arial,18'

set out 'muAl.png'

set multiplot
set size 1,1
#set tics font ", 30"
set origin 0,0 #origin of plot
set title "Absorption of Aluminium"
set ylabel "Normalized Integration"
set xlabel "Thickness (cm)"
#set xr [.4:1.4]
#set yr [0:.6]
#set yr [-500000:8000000]
set autoscale y
set autoscale x
#set logscale x
#set logscale y
set key bottom right
set bar small
set grid
f(x) = m*x+b
fit f(x) "mu.dat" using 1:2 via m,b

g(x) = m1*x+b1
fit g(x) "mu.dat" using 1:3 via m1,b1

plot 'mu.dat' u 1:2 w points ps 2 t '',\
	'mu.dat' using 1:3 w points ps 2 title '',\
	f(x) lw 2 lc rgb "green" t 'Cesium',\
	g(x) lw 2 lc rgb "red" t 'Cobalt'
#=============mini plot=============      
set grid
unset multiplot