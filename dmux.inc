* custom_logic.inc
* Implements: ((a + s) * b) + (not(s) * a)
* Ports: gnd a b s out vdd

.subckt custom_logic gnd a b s out vdd

* Invert s
Xinv gnd s s_inv vdd inv
Cdelay s_inv gnd 200fF

* OR gate: a + s -> or_out
Xor1 gnd a s or_raw vdd or

* Buffered OR using 2 inverters to maintain logic level
Xbuf1 gnd or_raw or_buf1 vdd inv
C1 or_buf1 gnd 1500fF

Xbuf2 gnd or_buf1 or_out vdd inv
C2 or_out gnd 1000fF



* AND gate: (a + s) * b -> and1_out
Xand1 gnd or_out b and1_out vdd and2


* AND gate: not(s) * a -> and2_out
Xand2 gnd s_inv a and2_out vdd and2

* Final OR: and1_out + and2_out -> out
Xor2 gnd and1_out and2_out out vdd or

.ends custom_logic
