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
    if(x.value % 2 == 0):
        for y in DynamicEnum:
            if (y.value % 2 == 0):
                for z in DynamicEnum:
                    if (z.value % 2 == 0):
                        if(x.value % 4 + y.value % 4 + z.value % 4 <= 2):
                            if((or_table[x.value][and_table[y.value][z.value].value].value != and_table[or_table[x.value][y.value].value][or_table[x.value][z.value].value].value) or
                                (and_table[x.value][or_table[y.value][z.value].value].value != or_table[and_table[x.value][y.value].value][and_table[x.value][z.value].value].value)):
                                flag = True
                                print(f"Distribute Mismatch found!")
                                print(f"x: {x.name} ({x.value}), y: {y.name} ({y.value}), z: {z.name} ({z.value})")
                                print(f"{or_table[x.value][and_table[y.value][z.value].value].value} != {and_table[or_table[x.value][y.value].value][or_table[x.value][z.value].value].value}")
                                print(f"OR {and_table[x.value][or_table[y.value][z.value].value].value} != {or_table[and_table[x.value][y.value].value][and_table[x.value][z.value].value].value}")
                                break

                if ((not_table[or_table[x.value][y.value].value].value != and_table[not_table[x.value].value][not_table[y.value].value].value) or
                        (not_table[and_table[x.value][y.value].value].value != or_table[not_table[x.value].value][not_table[y.value].value].value)):
                    flag = True
                    print(f"Demorgan Mismatch found!")
                    print(f"x: {x.name} ({x.value}), y: {y.name} ({y.value})")
                    print(f"{not_table[or_table[x.value][y.value].value].value} != {and_table[not_table[x.value].value][not_table[y.value].value].value}")
                    print(f"OR {not_table[and_table[x.value][y.value].value].value} != {or_table[not_table[x.value].value][not_table[y.value].value].value}")
                    break


if not flag:
    print("Demorgan holds for all cases!")
