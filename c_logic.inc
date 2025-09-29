* c_logic.inc
* C(x,y,w,z) with tunable, local delays on the K term (w AND z) only.
* C = [y' AND ((x' AND K) OR (x AND K))] OR [y AND ((x' AND K) OR (x AND (w OR z')))]
* K = (x' AND y) OR (w AND x) OR (y AND z') OR (w AND z) OR (w AND y)
* Ports: gnd x y w z out vdd
* Params: CD_W = cap to ground on w-delay buffer, CD_Z = same for z-delay buffer.

.subckt clogicD gnd x y w z out vdd params: CD_W=0 CD_Z=0

* Inverters for complements reused elsewhere
Xnx gnd x x_n vdd inv
Xny gnd y y_n vdd inv
Xnz gnd z z_n vdd inv

*-------------------------------
* Local delay only on (w AND z)
* w -> inv -> node -> C -> inv -> w_del  (polarity preserved)
* z -> inv -> node -> C -> inv -> z_del
*-------------------------------
Xwbuf1 gnd w wbuf1 vdd inv
Cdw1   wbuf1 gnd {CD_W}
Xwbuf2 gnd wbuf1 w_del vdd inv

Xzbuf1 gnd z zbuf1 vdd inv
Cdz1   zbuf1 gnd {CD_Z}
Xzbuf2 gnd zbuf1 z_del vdd inv

*-------------------------------
* Build K = k1 OR k2 OR k3 OR (w_del AND z_del) OR k5
*-------------------------------
* k1 = x' AND y
Xk1 gnd x_n y   k1 vdd and2
* k2 = w AND x (uses original w)
Xk2 gnd w   x   k2 vdd and2
* k3 = y AND z'
Xk3 gnd y   z_n k3 vdd and2
* k4del = w_del AND z_del   <-- delayed-only path
Xk4 gnd w_del z_del k_wz vdd and2
* k5 = w AND y  (uses original w)
Xk5 gnd w   y   k5 vdd and2

Xk12    gnd k1  k2   k12    vdd or
Xk34    gnd k3  k_wz k34    vdd or
Xk1234  gnd k12 k34  k1234  vdd or
Xkfinal gnd k1234 k5  K      vdd or

* Shared terms
* (x' AND K)
Xa1 gnd x_n K a1 vdd and2
* (x AND K)
Xa2 gnd x   K a2 vdd and2
* (w OR z')
Xw_or_zn gnd w z_n w_or_zn vdd or

* term1 = y' AND ( (x' AND K) OR (x AND K) )
Xa1_or_a2 gnd a1 a2 a12_or vdd or
Xterm1    gnd y_n a12_or term1 vdd and2

* term2 = y AND ( (x' AND K) OR ( x AND (w OR z') ) )
Xa3 gnd x w_or_zn a3 vdd and2
Xa1_or_a3 gnd a1 a3 a13_or vdd or
Xterm2    gnd y  a13_or term2 vdd and2

* Final output
Xout gnd term1 term2 out vdd or

.ends clogicD
