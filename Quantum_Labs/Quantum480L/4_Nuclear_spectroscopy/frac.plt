# Gnuplot script file for plotting data
# 

set terminal png nocrop enhanced size 900,700 font 'arial,18'

set out 'frac.png'

set multiplot
set size 1,1
#set tics font ", 30"
set origin 0,0 #origin of plot
set title "Fractional Energy Resolution"
set ylabel "Energy Resolution (  E/E)"
set xlabel "Energy (MeV)"
set xr [.4:1.4]
set yr [0:.6]
#set yr [-500000:8000000]
#set autoscale y
#set autoscale x
#set logscale x
#set logscale y
set key top right
set bar small
set grid
#f(x) = m*x+b
#g(x) = q*x+c
#h(x) = j*x+d
f(x) = a*x**b;
fit f(x) 'frac.dat' via a,b

#fit f(x) "calib2.dat" using 1:2:3 via m,b
#fit g(x) "ams.dat" using 6:7 via q,c
#fit h(x) "ams.dat" using 1:5 via j,d

#f1(x)=a1*x+b1
#fit [260:450] f1(x) "sol.dat" u 1:2 via a1, b1
#f2(x)=a2*x+b2
#fit [950:1100] f2(x) "sol.dat" u 1:2 via a2, b2


plot 'frac.dat' u 1:2:3 with labels font "10" offset 1.3,-1,0 tc rgb "black" t '',\
	"frac.dat" using 1:2 title '' lc rgb "blue" ps 2 lw 3 pt 1 with points
#=============mini plot=============      
set grid
unset multiplot