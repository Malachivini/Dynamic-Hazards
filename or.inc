.subckt OR gnd i1 i2 o vdd
  XNOR gnd i1 i2 t1 vdd NOR2
  XINV gnd t1 o vdd INV
.ends OR

.inc ./nor2.inc
.inc ./inv.inc
