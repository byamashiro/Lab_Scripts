# Gnuplot script file for plotting data
# 

set terminal png nocrop enhanced size 900,700 font 'arial,18'

set out '2nsgauss.png'

set multiplot
set size 1,1
#set tics font ", 30"
set origin 0,0 #origin of plot
set title 'Pulse Amplitude Histogram (2ns)'
set ylabel "Amplitude (counts)"
set xlabel "Channel Number"
set xr [0:2050]
set yr [0:1000]
set key top right
set bar small
set grid


# function = range ? equation : second range ? second function equation : 0 elsewhere



# both (single) gaussians
#h(x) = 0<=x && x<=o4 ? A4*exp(-0.5*((x-o4)/s4)**2)+c4 : o4<x && x<=2500 ? A5*exp(-((x-o5)/s5)**2)+c5 : 0 
#h(x) = 0<=x && x<=1150 ? A4*exp(-0.5*((x-o4)/s4)**2)+c4 : 1150<x && x<=2500 ? A5*exp(-((x-o5)/s5)**2)+c5 : 0 

h(x) = 0<=x && x<=1200 ? A4*exp(-0.5*((x-o4)/s4)**2)+c4 : o5<x && x<=2500 ? A5*exp(-((x-o5)/s5)**2)+c5 : 0
A4=600;# height
o4=1100;# peak center
c4=3;# continuum
s4=50;# width
A5=600;
o5=1100;
c5=0;
s5=50; # width of curve, right of center
fit [800:2000] h(x) 'sol.dat' u 1:2 via A4,o4,s4,c4,A5,s5,c5,o5

g(x) = 0<=x && x<=472 ? A3*exp(-0.5*((x-o3)/s3)**2)+c3 : o3a<x && x<=900 ? A3a*exp(-((x-o3a)/s3a)**2)+c3a : 0
A3=950;
o3=350;
c3=3;
s3=50;
A3a=900;
o3a=400;
c3a=0;
s3a=50;
fit [0:1270] g(x) 'sol.dat' u 1:2 via A3,o3,s3,c3,A3a,o3a,s3a,c3a


#double gaussian
f(x) = A1*exp(-0.5*((x-o1)/s1)**2)+A2*exp(-0.5*((x-o2)/s2)**2)+c;
A1=600;
A2=900;
o1=1100;
o2=400;
s1=50;
s2=50;
c=3;
fit f(x) 'sol.dat' u 1:2 via A1,o1,s1,A2,o2,s2,c


# fit lines to leading edges
f1(x)=a1*x+b1
fit [260:450] f1(x) "sol.dat" u 1:2 via a1, b1
f2(x)=a2*x+b2
fit [950:1100] f2(x) "sol.dat" u 1:2 via a2, b2


plot 'sol.dat' u 1:2:($2**0.5) pt 1 lc rgb 'blue' ps 0.5 t '' w yerrorbars,\
	h(x) lt 3 lw 3 lc rgb '#B22222' t 'Second Peak', \
	g(x) lt 4 lw 3 lc rgb '#32CD32' t 'First Peak'


#, \f(x) lt 5 lc rgb 'black' t 'Double Gaussian'
#f1(x) lt 1 lc rgb '#00FF00' t 'Start Signal',\
#f2(x) lt 2 lc rgb '#FF0000' t 'Stop Signal', \
     
set grid
unset multiplot