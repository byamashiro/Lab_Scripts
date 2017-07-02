#angle	nofilt	angle error	nofilterr	filt	angle error	filterr

set terminal pngcairo nocrop enhanced size 900,700 font 'arial,20'
set out 't1ish.png'

set title "Heavy Mineral Oil T1"
set ylabel "Peak Voltage (V)" offset 1,6,0
set xlabel "Time (s)" offset 28,.5,0
set mxtics 5
set mytics 4

set xr [-0.001:.065]
#set yr []

#f(x) = a*(1-2*exp(-x/b))
f(x) = a*(1-b*exp(-x/c))
fit f(x) 't1.dat' using 1:2 via a,b,c

set samples 100000

set style line 102 lt 0 lc rgb "black" lw 1
set grid ls 102 



plot "t1.dat" using 1:2:3 with yerrorbars lw 2 pt 6 ps 2 lc rgb 'blue' t '',\
	f(x) lc rgb 'red' lw 2 t ''