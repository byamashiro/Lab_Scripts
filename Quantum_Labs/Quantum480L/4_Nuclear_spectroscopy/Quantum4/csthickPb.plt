# Gnuplot script file for plotting data
# 

set terminal png nocrop enhanced size 900,700 font 'arial,18'

set out 'csthickpb.png'

set multiplot
set size 1,1
#set tics font ", 30"
set origin 0,0 #origin of plot
set title "Pb Thickness for Cesium Isotope"
set ylabel "Amplitude (counts)"
set xlabel "Channel Number"
set xr [0:950]
set yr [0:600]
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
#f(x) = a*x**2 + b*x + c          # define a quadratic function
#fit f(x) 'zat.dat' via a,b,c    # compute the coefficients a,b,c

#fit f(x) "sol.dat" using 4:5 via m,b
#fit g(x) "ams.dat" using 6:7 via q,c
#fit h(x) "ams.dat" using 1:5 via j,d

#f1(x)=a1*x+b1
#fit [260:450] f1(x) "sol.dat" u 1:2 via a1, b1
#f2(x)=a2*x+b2
#fit [950:1100] f2(x) "sol.dat" u 1:2 via a2, b2


plot  "Cs137_0cm_180s.Spe" using 0:1:($1**0.5) title '0 cm' lc rgb "red" lw 1 with yerrorbars,\
	"Cs137_0.644cmPb_180s.Spe" using 0:1:($1**0.5) title '0.644 cm' lc rgb "purple" lw 1 with yerrorbars,\
	"Cs137_1.91cmPb_180s.Spe" using 0:1:($1**0.5) title '1.91 cm' lc rgb "green" lw 1 with yerrorbars

#=============mini plot=============      
set grid
unset multiplot