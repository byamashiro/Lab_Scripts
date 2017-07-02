# Gnuplot script file for plotting data
# 

set terminal pngcairo nocrop enhanced size 900,700 font 'arial,18'

set out 'muonlifetime.png'

set multiplot
set size 1,1
#set tics font ", 30"
set origin 0,0 #origin of plot
set title "Muon Lifetime"
set ylabel "Amplitude (counts)"
set xlabel "Channel Number"
set xr [100:1000]
#set yr [0:20]
#set yr [-500000:8000000]
#set autoscale y
#set autoscale x
#set logscale x
set logscale y
set key top right
set bar small
set grid

PI=3.14;
a=5;
m=250; #b=250;
s=3; #c=1;

#f(x) = a * (exp((-(x-b)**2)/(2*c**2))) #+m1*x+b1
#fit f(x) "group2muondata_2016.Spe" using 0:1 via a,b,c #,m1,b1

f(x) = a/(2*PI*s**2)**0.5*exp(-(x-m)**2/(2*s**2)) 
#fit f(x) "group2muondata_2016.Spe" using 0:1 via s,m,a

#bw = 1.0
#bin(x,width)=width*floor(x/width)
#plot 'group2muondata_2016.Spe' using (bin($1,bw)):(1.0) smooth frequency with boxes

plot "muondata2.dat" using 1:2:($2**0.5) title 'Muons' lc rgb "blue" lw 1 with yerrorbars
#f(x) lc rgb "green" lw 3 t 'Compton Edge'
#	[620:900] f1(x) lc rgb "red" lw 3 t 'Photopeak 1 and 2'
	
	
#=============mini plot=============      
set grid
unset multiplot