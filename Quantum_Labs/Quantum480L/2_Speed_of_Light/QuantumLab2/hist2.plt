set title "Counts vs Channel Number"
set xlabel "Channel Number"
set ylabel "Counts"
set xrange [0:2250]
set yrange [0:1000]
set pointsize 2
set bar small
set grid
#set key below

f(x) = a1*x+b1
g(x) = a2*x+b2
fit [250:450] f(x) 'hist2.dat' using 1:2 via a1, b1
fit [900:1100] g(x) 'hist2.dat' using 1:2 via a2, b2
plot "hist2.dat" using 1:2 with lines title '',\
f(x) with lines title 'y1 = (4.663 +/- 0.051)x + (-1205 +/- 18)',\
g(x) with lines title 'y2 = (2.724 +/- 0.035)x + (-2451 +/- 35)'