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

def Omux_output(a,b,s):
    return or_table[and_table[a.value][not_table[s.value].value].value][and_table[b.value][s.value].value]

def Cmux_output(a,b,s):
    return or_table[or_table[and_table[a.value][not_table[s.value].value].value][and_table[b.value][s.value].value].value][and_table[a.value][b.value].value]


def unify_consecutive(arr):


    unified = [arr[0]]  # Start with the first element

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:  # Check if current value is different from the previous
            unified.append(arr[i])

    return unified
def mux(a, b, s):
    #print(f"{a, b, s} mux")
    return a if s == 0 else b

def get_longest(o_1,o_2,o_3):
    if len(o_1) > len(o_2):
        if len(o_1) > len(o_3):
            return o_1
    elif len(o_2) > len(o_3):
        return o_2
    return o_3

def Mux_D(a,b,s):
    if len(a) == 1 and len(b) == 1 and len(s) == 1:
        #print(f"{a[0],b[0],s[0]}\n")
        return [mux(a[0],b[0],s[0])]
    elif len(a) == 0 or len(b) == 0 or len(s) == 0:
        #print ("empty")
        return []

    #print(f"{a,b,s}")
    option1 = Mux_D(a[1:],b,s)
    #print(f"mux of option 1 {option1}")
    option1.insert(0,mux(a[0],b[0],s[0]))
    option1 = unify_consecutive(option1)
    #print("sending option 2")
    option2 = Mux_D(a,b[1:],s)
    option2.insert(0,mux(a[0],b[0],s[0]))
    option2 = unify_consecutive(option2)
    option3 = Mux_D(a, b, s[1:])
    option3.insert(0, mux(a[0], b[0], s[0]))
    option3 = unify_consecutive(option3)
    #print(f"{option1} option1 {a,b,s}")
    #print(f"{option2} option2 {a,b,s}")
    #print(f"{option3} option3 {a,b,s}")

    option = get_longest(option1,option2,option3)
    #print(f"{option} final")
    #print("\n")

    #return option1

    if all(i==0 for i in option):
        return [0]
    elif all(i==1 for i in option):
        return [1]
    elif option[0] == 0 and option[-1] == 0 and not all(i==0 for i in option):
        return [0,1,0]
    elif option[0] == 1 and option[-1] == 1 and not all(i==1 for i in option):
        return [1,0,1]
    elif option[0] == 0 and option[-1] == 1:
        if len(option) == 2:
            return [0,1]
        else:
            return [0,1,0,1]
    elif option[0] == 1 and option[-1] == 0:
        if len(option) == 2:
            return [1,0]
        else:
            return [1,0,1,0]
    return []



def New_Dmux_output(a,b,s):
    #return or_table[and_table[or_table[a.value][s.value].value][b.value].value][and_table[or_table[b.value][not_table[s.value].value].value][a.value].value]
    return or_table[and_table[a.value][not_table[s.value].value].value][and_table[b.value][or_table[a.value][s.value].value].value]
def Dmux_output(a,b,s):
    return or_table[and_table[or_table[a.value][s.value].value][b.value].value][and_table[or_table[b.value][not_table[s.value].value].value][a.value].value]


def convert_to_arr(enum):
    mapping = {
        DynamicEnum._0_E: [0],
        DynamicEnum._010_E: [0, 1, 0],
        DynamicEnum._10_E: [1, 0],
        DynamicEnum._1010_E: [1, 0, 1, 0],
        DynamicEnum._1_E: [1],
        DynamicEnum._101_E: [1, 0, 1],
        DynamicEnum._01_E: [0, 1],
        DynamicEnum._0101_E: [0, 1, 0, 1],
    }
    return mapping[enum]
def convert_to_enum(arr):
    reverse_mapping = {
        (0,): DynamicEnum._0_E,
        (0, 1, 0): DynamicEnum._010_E,
        (1, 0): DynamicEnum._10_E,
        (1, 0, 1, 0): DynamicEnum._1010_E,
        (1,): DynamicEnum._1_E,
        (1, 0, 1): DynamicEnum._101_E,
        (0, 1): DynamicEnum._01_E,
        (0, 1, 0, 1): DynamicEnum._0101_E,
    }
    return reverse_mapping[tuple(arr)]

def convert_to_arr(enum):
    mapping = {
        DynamicEnum._0_E: [0],
        DynamicEnum._010_E: [0, 1, 0],
        DynamicEnum._10_E: [1, 0],
        DynamicEnum._1010_E: [1, 0, 1, 0],
        DynamicEnum._1_E: [1],
        DynamicEnum._101_E: [1, 0, 1],
        DynamicEnum._01_E: [0, 1],
        DynamicEnum._0101_E: [0, 1, 0, 1],
    }
    return mapping[enum]

def convert_to_text(enum):
    mapping = {
        DynamicEnum._0_E: "0",
        DynamicEnum._010_E: "010",
        DynamicEnum._10_E: "10",
        DynamicEnum._1010_E: "1010",
        DynamicEnum._1_E: "1",
        DynamicEnum._101_E: "101",
        DynamicEnum._01_E: "01",
        DynamicEnum._0101_E: "0101",
    }
    return mapping[enum]


def check_equal(muxer, Mux_main):
    if muxer != Mux_main:
        return "\\cellcolor{red!25}"
    return ""

def check_regular(mux):
    if line.a.value % 2 == 0 and line.b.value % 2 == 0 and line.s.value % 2 == 0:
        return "\\cellcolor{green!25}"
    return ""

class MUX_Calc:
    def __init__(self, a: DynamicEnum, b: DynamicEnum, s: DynamicEnum):
        # Initialize inputs
        self.a = a
        self.b = b
        self.s = s

        # Initialize outputs (DynamicEnum type)
        self.Omux = Omux_output(a,b,s)
        self.Cmux = Cmux_output(a,b,s)
        self.Dmux = Dmux_output(a,b,s)
        self.newDmux = New_Dmux_output(a,b,s)
        self.MUX_D = convert_to_enum(Mux_D(convert_to_arr(a),convert_to_arr(b),convert_to_arr(s)))

    def __str__(self):
        """String representation of the system state."""
        return (
            f"Inputs: a={convert_to_text(self.a)}, b={convert_to_text(self.b)}, s={convert_to_text(self.s)} - "
            f"Outputs: Omux={convert_to_text(self.Omux)}, "
            f"Cmux={convert_to_text(self.Cmux)}, "
            f"Old Dmux={convert_to_text(self.Dmux)}, "
            f"New Dmux={convert_to_text(self.newDmux)}, "
            f"MUX_D={convert_to_text(self.MUX_D)}"
        )


print(Mux_D([0,1],[0,1],[0,1]))

mux_list = []

for a in DynamicEnum:
    for b in DynamicEnum:
        for s in DynamicEnum:
            mux_temp = MUX_Calc(a,b,s)
            mux_list.append(mux_temp)
            print(mux_temp)

            #print(f"For ({convert_to_text(a),convert_to_text(b),convert_to_text(s)}) - Omux = {convert_to_text(Omux_output(a,b,s))}, Cmux = {convert_to_text(Cmux_output(a,b,s))}, Dmux = {convert_to_text(Dmux_output(a,b,s))}, MUX_D = {convert_to_text(convert_to_enum(Mux_D(convert_to_arr(a),convert_to_arr(b),convert_to_arr(s))))}")

index = 1
for line in mux_list:
    text = f"{index}&{check_regular(line)}$({convert_to_text(line.a)},{convert_to_text(line.b)},{convert_to_text(line.s)})$ &{check_equal(line.Omux,line.MUX_D)}{convert_to_text(line.Omux)} & {check_equal(line.Cmux,line.MUX_D)}{convert_to_text(line.Cmux)} & {check_equal(line.Dmux,line.MUX_D)}{convert_to_text(line.Dmux)}  & {check_equal(line.newDmux,line.MUX_D)}{convert_to_text(line.newDmux)} & {convert_to_text(line.MUX_D)}\\\\"
    if("red" in text):
        print(text)
        print("\\hline")
        index = index + 1







