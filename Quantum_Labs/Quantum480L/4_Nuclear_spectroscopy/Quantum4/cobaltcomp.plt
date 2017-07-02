# Gnuplot script file for plotting data
# 

set terminal png nocrop enhanced size 900,700 font 'arial,18'

set out 'cocomp.png'

set multiplot
set size 1,1
#set tics font ", 30"
set origin 0,0 #origin of plot
set title "Gaussian fits for Co^{60}"
set ylabel "Amplitude (counts)"
set xlabel "Channel Number"
set xr [0:1000]
set yr [0:500]
#set yr [-500000:8000000]
#set autoscale y
#set autoscale x
#set logscale x
#set logscale y
set key top right
set bar small
set grid

PI=3.14;
a=100;
b=540;
c=500;

f(x) = a * (exp((-(x-b)**2)/(2*c**2)))+m1*x+b1
fit [500:610] f(x) "newcobalt.Spe" using 0:1 via a,b,c,m1,b1


f1(x) = A1*exp(-0.5*((x-o1)/s1)**2)+(e1*x*x)+(d1*x)+c1 + A2*exp(-0.5*((x-o2)/s2)**2)
A1=247;# height
o1=713;# peak center
c1=145;# continuum
s1=50;# width
d1=50;
e1=50;
A2=162;# height
o2=813;# peak center
c2=78;# continuum
s2=100;# width
fit [610:900] f1(x) "newcobalt.Spe" u 0:1 via A1,o1,s1,c1,d1,e1,A2,o2,s2



plot  "newcobalt.Spe" using 0:1:($1**0.5) title 'Co^{60}' lc rgb "blue" lw 1 with yerrorbars,\
	[500:610] f(x) lc rgb "green" lw 3 t 'Compton Edge',\
	[620:900] f1(x) lc rgb "red" lw 3 t 'Photopeak 1 and 2'
	
	
#=============mini plot=============      
set grid
unset multiplot