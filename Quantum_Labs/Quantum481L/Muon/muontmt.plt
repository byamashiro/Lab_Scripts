set autoscale x
set xlabel 'Voltage'
set ylabel 'Log counts'
unset logscale x
set logscale y

plot "muon.dat" using 1:2:($2**.5) t '' with yerrorbars,\
	"muon.dat" using 1:3:($3**.5) t '' with yerrorbars,\
	"muon.dat" using 1:4:($4**.5) t '' with yerrorbars,\
	"muon.dat" using 1:5:($5**.5) t '' with yerrorbars,\
	"muon.dat" using 1:6:($6**.5) t '' with yerrorbars,\
	"muon.dat" using 1:7:($7**.5) t '' with yerrorbars,\
	"muon.dat" using 1:2 t 'PMT A 100s' with lines,\
	"muon.dat" using 1:3 t 'PMT B 60s' with lines,\
	"muon.dat" using 1:4 t 'PMT C 60s' with lines,\
	"muon.dat" using 1:5 t 'PMT D 60s' with lines,\
	"muon.dat" using 1:6 t 'PMT A 60s' with lines,\
	"muon.dat" using 1:7 t 'PMT A 60s(50mV)' with lines
	
replot
##HV	PMT_A_100s	PMT_B_60s	PMT_C_60s	PMT_D_60s