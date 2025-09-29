* =============================================================================
* Circuit    : 2-to-1 Multiplexer
* Description: OR[AND[a, NOT[s]], AND[b, s]]
* =============================================================================

.subckt MUX gnd a b s out vdd
  * Invert s to get s'
  XNOT gnd s s_inv vdd NOT

  * First AND: a * s'
  XAND1 gnd a s_inv and1_out vdd AND2

  * Second AND: b * s
  XAND2 gnd b s and2_out vdd AND2

  * OR: Combine the two AND outputs
  XOR gnd and1_out and2_out out vdd OR
.ends MUX

.inc ./and2.inc  * Ensure and2.inc is included
.inc ./nand2.inc
.inc ./inv.inc
.inc ./or.inc
