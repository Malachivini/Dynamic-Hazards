from enum import Enum

class DynamicEnum(Enum):
    _0_E = 0
    _010_E = 1
    _10_E = 2
    _1010_E = 3
    _1_E = 4
    _101_E = 5
    _01_E = 6
    _0101_E = 7

def lower_rep(d_enum):
    arr = [DynamicEnum._010_E,DynamicEnum._010_E,DynamicEnum._1010_E,DynamicEnum._1010_E,DynamicEnum._101_E,DynamicEnum._101_E,DynamicEnum._0101_E,DynamicEnum._0101_E]
    return arr[d_enum.value]

or_table = [
    [DynamicEnum._0_E,      DynamicEnum._010_E,     DynamicEnum._10_E,      DynamicEnum._1010_E,    DynamicEnum._1_E,       DynamicEnum._101_E,     DynamicEnum._01_E,    DynamicEnum._0101_E],
    [DynamicEnum._010_E,    DynamicEnum._010_E,     DynamicEnum._1010_E,    DynamicEnum._1010_E,    DynamicEnum._1_E,       DynamicEnum._101_E,     DynamicEnum._0101_E,  DynamicEnum._0101_E],
    [DynamicEnum._10_E,     DynamicEnum._1010_E,    DynamicEnum._10_E,      DynamicEnum._1010_E,    DynamicEnum._1_E,       DynamicEnum._101_E,     DynamicEnum._101_E,   DynamicEnum._101_E],
    [DynamicEnum._1010_E,   DynamicEnum._1010_E,    DynamicEnum._1010_E,    DynamicEnum._1010_E,    DynamicEnum._1_E,       DynamicEnum._101_E,     DynamicEnum._101_E,   DynamicEnum._101_E],
    [DynamicEnum._1_E,      DynamicEnum._1_E,       DynamicEnum._1_E,       DynamicEnum._1_E,       DynamicEnum._1_E,       DynamicEnum._1_E,       DynamicEnum._1_E,     DynamicEnum._1_E],
    [DynamicEnum._101_E,    DynamicEnum._101_E,     DynamicEnum._101_E,     DynamicEnum._101_E,     DynamicEnum._1_E,       DynamicEnum._101_E,     DynamicEnum._101_E,   DynamicEnum._101_E],
    [DynamicEnum._01_E,     DynamicEnum._0101_E,    DynamicEnum._101_E,     DynamicEnum._101_E,     DynamicEnum._1_E,       DynamicEnum._101_E,     DynamicEnum._01_E,    DynamicEnum._0101_E],
    [DynamicEnum._0101_E,   DynamicEnum._0101_E,    DynamicEnum._101_E,     DynamicEnum._101_E,     DynamicEnum._1_E,       DynamicEnum._101_E,     DynamicEnum._0101_E,  DynamicEnum._0101_E],
]

and_table = [
    [DynamicEnum._0_E,      DynamicEnum._0_E,       DynamicEnum._0_E,       DynamicEnum._0_E,       DynamicEnum._0_E,       DynamicEnum._0_E,       DynamicEnum._0_E,       DynamicEnum._0_E],
    [DynamicEnum._0_E,      DynamicEnum._010_E,     DynamicEnum._010_E,     DynamicEnum._010_E,     DynamicEnum._010_E,     DynamicEnum._010_E,     DynamicEnum._010_E,     DynamicEnum._010_E],
    [DynamicEnum._0_E,      DynamicEnum._010_E,     DynamicEnum._10_E,      DynamicEnum._1010_E,    DynamicEnum._10_E,      DynamicEnum._1010_E,    DynamicEnum._010_E,     DynamicEnum._010_E],
    [DynamicEnum._0_E,      DynamicEnum._010_E,     DynamicEnum._1010_E,    DynamicEnum._1010_E,    DynamicEnum._1010_E,    DynamicEnum._1010_E,    DynamicEnum._010_E,     DynamicEnum._010_E],
    [DynamicEnum._0_E,      DynamicEnum._010_E,     DynamicEnum._10_E,      DynamicEnum._1010_E,    DynamicEnum._1_E,       DynamicEnum._101_E,     DynamicEnum._01_E,      DynamicEnum._0101_E],
    [DynamicEnum._0_E,      DynamicEnum._010_E,     DynamicEnum._1010_E,    DynamicEnum._1010_E,    DynamicEnum._101_E,     DynamicEnum._101_E,     DynamicEnum._0101_E,    DynamicEnum._0101_E],
    [DynamicEnum._0_E,      DynamicEnum._010_E,     DynamicEnum._010_E,     DynamicEnum._010_E,     DynamicEnum._01_E,      DynamicEnum._0101_E,    DynamicEnum._01_E,      DynamicEnum._0101_E],
    [DynamicEnum._0_E,      DynamicEnum._010_E,     DynamicEnum._010_E,     DynamicEnum._010_E,     DynamicEnum._0101_E,    DynamicEnum._0101_E,    DynamicEnum._0101_E,    DynamicEnum._0101_E],
]

xor_table = [
    [DynamicEnum._0_E,      DynamicEnum._010_E,     DynamicEnum._10_E,      DynamicEnum._1010_E,    DynamicEnum._1_E,       DynamicEnum._101_E,     DynamicEnum._01_E,      DynamicEnum._0101_E],
    [DynamicEnum._010_E,    DynamicEnum._010_E,     DynamicEnum._1010_E,    DynamicEnum._1010_E,    DynamicEnum._101_E,     DynamicEnum._101_E,     DynamicEnum._0101_E,    DynamicEnum._0101_E],
    [DynamicEnum._10_E,     DynamicEnum._1010_E,    DynamicEnum._010_E,     DynamicEnum._010_E,     DynamicEnum._01_E,      DynamicEnum._0101_E,    DynamicEnum._101_E,     DynamicEnum._101_E],
    [DynamicEnum._1010_E,   DynamicEnum._1010_E,    DynamicEnum._010_E,     DynamicEnum._010_E,     DynamicEnum._0101_E,    DynamicEnum._0101_E,    DynamicEnum._101_E,     DynamicEnum._101_E],
    [DynamicEnum._1_E,      DynamicEnum._101_E,     DynamicEnum._01_E,      DynamicEnum._0101_E,    DynamicEnum._0_E,       DynamicEnum._010_E,     DynamicEnum._10_E,      DynamicEnum._1010_E],
    [DynamicEnum._101_E,    DynamicEnum._101_E,     DynamicEnum._0101_E,    DynamicEnum._0101_E,    DynamicEnum._010_E,     DynamicEnum._010_E,     DynamicEnum._1010_E,    DynamicEnum._1010_E],
    [DynamicEnum._01_E,     DynamicEnum._0101_E,    DynamicEnum._101_E,     DynamicEnum._101_E,     DynamicEnum._10_E,      DynamicEnum._1010_E,    DynamicEnum._010_E,     DynamicEnum._010_E],
    [DynamicEnum._0101_E,   DynamicEnum._0101_E,    DynamicEnum._101_E,     DynamicEnum._101_E,     DynamicEnum._1010_E,    DynamicEnum._1010_E,    DynamicEnum._010_E,     DynamicEnum._010_E],
]

not_table = [DynamicEnum._1_E,      DynamicEnum._101_E,     DynamicEnum._01_E,      DynamicEnum._0101_E,    DynamicEnum._0_E,       DynamicEnum._010_E,     DynamicEnum._10_E,      DynamicEnum._1010_E]

flag = False

for x in DynamicEnum:
    for y in DynamicEnum:

        if ((or_table[x.value][y.value].value - or_table[lower_rep(x).value][lower_rep(y).value].value) > 0 or
                (and_table[x.value][y.value].value - and_table[lower_rep(x).value][lower_rep(y).value].value) > 0):


            flag = True
            print(f"Mismatch found!")
            print(f"x: {x.name} ({x.value}), y: {y.name} ({y.value})")
            print(or_table[x.value][y.value])
            print(or_table[lower_rep(x).value][lower_rep(y).value])
            print(and_table[x.value][y.value])
            print(and_table[lower_rep(x).value][lower_rep(y).value])
    if flag:
        break

    if (not_table[x.value].value - not_table[lower_rep(x).value].value) > 0:
        flag = True
        print(f"Mismatch found!")
        print(f"x: {x.name} ({x.value})")
        print(not_table[x.value])
        print(not_table[lower_rep(x).value])
        break

if not flag:
    print("Monotonicity holds for all cases!")
