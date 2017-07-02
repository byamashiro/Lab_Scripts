# Gnuplot script file for plotting data
# 

set terminal png nocrop enhanced size 900,700 font 'arial,18'

set out 'cscomp.png'

set multiplot
set size 1,1
#set tics font ", 30"
set origin 0,0 #origin of plot
set title "Gaussian fits for Cs^{137}"
set ylabel "Amplitude (counts)"
set xlabel "Channel Number"
set xr [0:900]
set yr [0:4000]
#set yr [-500000:8000000]
#set autoscale y
#set autoscale x
#set logscale x
#set logscale y
set key top right
set bar small
set grid

PI=3.14;
a=150;
b=280;
c=10;
f(x) = a * (exp((-(x-b)**2)/(2*c**2)))+m1*x+b1
fit [260:320] f(x) "newcesium.Spe" using 0:1 via a,b,c,m1,b1

PI=3.14;
j=350;
k=410;
l=50;
#g(x) = j * (exp((-(x-k)**2)/(2*l**2)))+m2*x+b2
#fit [300:900] g(x) "newcesium.Spe" using 0:1 via j,k,l,m2,b2

g(x) = A1*exp(-0.5*((x-o1)/s1)**2)+(e1*x*x)+(d1*x)+c1# + A2*exp(-0.5*((x-o2)/s2)**2)
A1=3500;# height
o1=400;# peak center
c1=145;# continuum
s1=70;# width
d1=60;
e1=70;
#A2=162;# height
#o2=813;# peak center
#c2=78;# continuum
#s2=100;# width
fit [320:590] g(x) "newcesium.Spe" u 0:1 via A1,o1,s1,c1,d1,e1#,A2,o2,s2


plot  "newcesium.Spe" using 0:1:($1**0.5) title 'Cs^{137}' lc rgb "blue" lw 1 with yerrorbars,\
	[260:330] f(x) lw 3 lc rgb "green" t 'Compton Edge',\
	[340:500] g(x) lw 3 lc rgb "red" t 'Photopeak'

#=============mini plot=============      
set grid
unset multiplot