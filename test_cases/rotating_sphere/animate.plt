set terminal gif animate
set title "Rotating sphere"
set output 'motion.gif'

do for [i=0:100] {
    splot sprintf("sphere.%.4d", i) using 1:2:3 with points title "t=${i*6.283185307179586}"
}