# Gnuplot script file for plotting data
# 

set terminal png nocrop enhanced size 900,700 font 'arial,18'

set out 'nacomp.png'

set multiplot
set size 1,1
#set tics font ", 30"
set origin 0,0 #origin of plot
set title "Gaussian fits for Na^{22}"
set ylabel "Amplitude (counts)"
set xlabel "Channel Number"
set xr [0:900]
set yr [0:200]
#set yr [-500000:8000000]
#set autoscale y
#set autoscale x
#set logscale x
#set logscale y
set key top right
set bar small
set grid

PI=3.14;
#a=50;
#b=100;
#c=30;
#f(x) = a * (exp((-(x-b)**2)/(2*c**2)))+d
#fit [40:240] f(x) "newsodium.Spe" using 0:1 via a,b,c,d

j=200;
k=310;
l=50;
g(x) = j * (exp((-(x-k)**2)/(2*l**2)))+a7*x+b7
fit [240:900] g(x) "newsodium.Spe" using 0:1 via j,k,l,a7,b7

#m+(a7*(x-b7)**2+c7)
a1=100;
b1=610;
c1=30;
f1(x) = a1 * (exp((-(x-b1)**2)/(2*c1**2)))+a2*x+b2
fit [400:900] f1(x) "newsodium.Spe" using 0:1 via a1,b1,c1,a2,b2

j1=100;
k1=800;
l1=30;
g1(x) = j1 * (exp((-(x-k1)**2)/(2*l1**2)))+a3*x+b3
fit [500:900] g1(x) "newsodium.Spe" using 0:1 via j1,k1,l1,a3,b3




plot  "newsodium.Spe" using 0:1:($1**0.5) title 'Na^{22}' lc rgb "blue" lw 1 with yerrorbars,\
	[250:380] g(x) lw 3 lc rgb "red" t 'Annihilation Peak',\
	[500:660] f1(x) lw 3 lc rgb "green" t 'Photopeak Compton Edge',\
	[720:850] g1(x) lw 3 lc rgb "yellow" t 'Photopeak'
#	f(x) lw 3 t 'Annilation Compton Edge',\
#=============mini plot=============      
set grid
unset multiplot