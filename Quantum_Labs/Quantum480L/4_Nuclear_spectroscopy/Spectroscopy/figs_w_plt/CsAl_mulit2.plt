set terminal png nocrop enhanced size 900,700 font 'arial,15'
set out 'CsAl2.png'
#set terminal pngcairo size 600, 900
#set output 'CsAl2.png'

set grid

set lmargin at screen 0.1
set rmargin at screen 0.95
set xr [50:2050]
set yr [0:500]

TOP=0.95
DY = 0.29

#set multiplot
set multiplot layout 3, 1 title "^{137}Cs with Al Absorber\n" font "arial,18"
set offset 0,0,graph 0.05, graph 0.05



unset ylabel
set tmargin at screen TOP-2*DY
set bmargin at screen TOP-3*DY#+0.02
set ytics 0, 150, 500 nomirror font 'arial,15'

# xlabel
set label 'Channel Number' at screen 0.55, 0.01 center front font 'arial,18'
set xtics 0, 500, 2000 font 'arial,15'

plot 'Al56mm.Spe' u 0:1:($1**0.5) pt 4 lc rgb 'orange' ps 0.5 t '56mm' w yerrorbars



set xtics format ''
unset xlabel
set ylabel 'Counts' offset 2 font 'arial,18'
set tmargin at screen TOP-DY
set bmargin at screen TOP-2*DY
set ytics 0, 150, 500 nomirror font 'arial,15'
plot 'Al25mm.Spe' u 0:1:($1**0.5) pt 3 lc rgb '#32CD32' ps 0.5 t '25mm' w yerrorbars



unset ylabel
set tmargin at screen TOP
set bmargin at screen TOP-DY
set ytics 0, 150, 500 nomirror font 'arial,15'
plot 'Al12mm.Spe' u 0:1:($1**0.5) pt 2 lc rgb '#0000FF' ps 0.5 t '12mm' w yerrorbars

unset multiplot; set output

