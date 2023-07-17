# defining registers and instructions
Register32bit = {"eax": 0, "ebx": 0, "ecx": 0, "edx": 0}
Register16bit = {"ax": 0, "bx": 0, "cx": 0, "dx": 0}
Register8bit = {"ah": 0, "al": 0, "bh": 0,
                "bl": 0, "ch": 0, "cl": 0, "dh": 0, "dl": 0}

eax = {"eax": Register32bit["eax"], "ax": Register16bit["ax"],
       "ah": Register8bit["ah"], "al": Register8bit["al"]}
ebx = {"ebx": Register32bit["ebx"], "bx": Register16bit["bx"],
       "bh": Register8bit["bh"], "bl": Register8bit["bl"]}
ecx = {"ecx": Register32bit["ecx"], "cx": Register16bit["cx"],
       "ch": Register8bit["ch"], "cl": Register8bit["cl"]}
edx = {"edx": Register32bit["edx"], "dx": Register16bit["dx"],
       "dh": Register8bit["dh"], "dl": Register8bit["dl"]}
# defining flags
carryFlag = False
zeroFlag = False
negativeFlag = False
overflowFlag = False


# removing free spaces and lines to have a cleaner assembly code
def remove_space(text: str):
    while "\n\n" in text:
        text = text.replace("\n\n", "\n")

    while "  " in text:
        text = text.replace("  ", " ")

    text = text.replace(" ", ",")
    while ",," in text:
        text = text.replace(",,", ",")

    return text.split('\n')

# evaluate the instruction


def evaluate_Instruction(instruction):
    if instruction == "add":
        return "add"
    elif instruction == "or":
        return "or"
    elif instruction == "and":
        return "and"
    elif instruction == "sub":
        return "sub"
    elif instruction == "mov":
        return "mov"
    elif instruction == "xor":
        return "xor"
    else:
        print("Wrong input!\nInvalid instruction!")

#  8bit registers


def calculate_8bit(num1, num2):
    global zeroFlag
    global carryFlag
    global negativeFlag
    global overflowFlag
    if instruction == "add":
        num2 += num1
        if num2 == 0:
            zeroFlag = True
        if num2 >= 255:
            carryFlag = True
        if num2 >= 127 or num2 <= -128:
            overflowFlag = True
        if num2 < 0:
            negativeFlag = True
            carryFlag = True

    elif instruction == "or" or instruction == "xor":
        num2 = num1 | num2
        if num2 == 0:
            zeroFlag = True
        if num2 >= 255:
            carryFlag = True
        if (num2 >= 127) or (num2 <= -128):
            overflowFlag = True
        if num1 < 0:
            negativeFlag = True
            carryFlag = True

    elif instruction == "and":
        num2 = num1 & num2
        if num2 == 0:
            zeroFlag = True
        if num2 >= 255:
            carryFlag = True
        if num2 >= 127 or num2 <= -128:
            overflowFlag = True
        if num2 < 0:
            negativeFlag = True
            carryFlag = True
    elif instruction == "sub":
        num2 -= num1
        if num2 == 0:
            zeroFlag = True
        if num2 >= 255:
            carryFlag = True
        if num2 >= 127 or num2 <= -128:
            overflowFlag = True
        if num2 < 0:
            negativeFlag = True
            carryFlag = True
    elif instruction == "mov":
        num2 = num1
        if num2 == 0:
            zeroFlag = True

    return zeroFlag, carryFlag, overflowFlag, negativeFlag, num1, num2

#  16bit registers


def calculate_16bit(num1, num2):
    global zeroFlag
    global carryFlag
    global negativeFlag
    global overflowFlag
    if instruction == "add":
        num2 += num1
        if num2 == 0:
            zeroFlag = True
        if num2 >= (2**16) - 1 or num2 <= 0:
            carryFlag = True
        if num2 >= (2**15) - 1 or num2 <= -(2**15):
            overflowFlag = True
        if num2 < 0:
            negativeFlag = True

    elif instruction == "or" or instruction == "xor":
        num2 = num1 | num2
        if num2 == 0:
            zeroFlag = True
        if num2 >= (2**16) - 1 or num2 < 0:
            carryFlag = True
        if (num2 >= (2**15) - 1) or (num2 < -(2**15)):
            overflowFlag = True
        if num2 < 0:
            negativeFlag = True

    elif instruction == "and":
        num2 = num1 & num2
        if num2 == 0:
            zeroFlag = True
        if num2 >= (2**16) - 1 or num2 < 0:
            carryFlag = True
        if num2 >= (2**15) - 1 or num2 <= -(2**15):
            overflowFlag = True
        if num2 < 0:
            negativeFlag = True
    elif instruction == "sub":
        num2 -= num1
        if num2 == 0:
            zeroFlag = True

    elif instruction == "mov":
        num2 = num1
        if num2 == 0:
            zeroFlag = True
    return zeroFlag, carryFlag, overflowFlag, negativeFlag, num1, num2

#  32bit registers


def calculate_32bit(num1, num2):
    global zeroFlag
    global carryFlag
    global negativeFlag
    global overflowFlag
    if instruction == "add":
        num2 += num1
        if num2 == 0:
            zeroFlag = True
        if num2 >= (2**32) - 1 or num2 < 0:
            carryFlag = True
        if num2 >= (2**31) - 1 or num2 <= -(2**31):
            overflowFlag = True
        if num2 < 0:
            negativeFlag = True

    elif instruction == "or" or instruction == "xor":
        num2 = num1 | num2
        if num2 == 0:
            zeroFlag = True
        if num2 >= (2**32) - 1 or num2 < 0:
            carryFlag = True
        if (num2 >= (2**31) - 1) or (num2 <= -(2**31)):
            overflowFlag = True
        if num2 < 0:
            negativeFlag = True

    elif instruction == "and":
        num2 = num1 & num2
        if num2 == 0:
            zeroFlag = True
        if num2 > (2**32) - 1 or num2 < 0:
            carryFlag = True
        if num2 >= (2**31) - 1 or num2 <= -(2**31):
            overflowFlag = True
        if num2 < 0:
            negativeFlag = True
    elif instruction == "sub":
        num2 -= num1
        if num2 == 0:
            zeroFlag = True
        if num2 >= (2**32) - 1 or num2 < 0:
            carryFlag = True
        if num2 >= (2**31) - 1 or num2 <= -(2**31):
            overflowFlag = True
        if num2 < 0:
            negativeFlag = True
    elif instruction == "mov":
        num2 = num1
        if num2 == 0:
            zeroFlag = True

    return zeroFlag, carryFlag, overflowFlag, negativeFlag, num1, num2

# this function syncs all the registers from one family


def sync_reg():
    global eax, ebx, ecx, edx
    value = ''
    for i in eax.keys():
        for j in Register32bit.keys():
            if(i == j):
                eax[j] = int("{:32b}".format(Register32bit[i]))
        for j in Register16bit.keys():
            if(i == j):
                eax[j] = int("{:16b}".format(Register16bit[i]))
        for j in Register8bit.keys():
            if(i == j):
                eax[j] = int("{:8b}".format(Register8bit[i]))
        if(eax[i] != 0):
            value = "{:032b}".format(int(str(eax[i]), 2))
            eax["eax"] = int(value[0:32])
            Register32bit["eax"] = int(str(eax["eax"]), 2)
            eax["ax"] = int(value[16:32])
            Register16bit["ax"] = int(str(eax["ax"]), 2)
            eax["ah"] = int(value[16:24])
            Register8bit["ah"] = int(str(eax["ah"]), 2)
            eax["al"] = int(value[24:32])
            Register8bit["al"] = int(str(eax["al"]), 2)
            break
    for i in ebx.keys():
        for j in Register32bit.keys():
            if(i == j):
                ebx[j] = Register32bit[i]
        for j in Register16bit.keys():
            if(i == j):
                ebx[j] = Register16bit[i]
        for j in Register8bit.keys():
            if(i == j):
                ebx[j] = Register8bit[i]
        if(ebx[i] != 0):
            value = "{:032b}".format(ebx[i])
            ebx["ebx"] = int(value[0:32])
            Register32bit["ebx"] = int(str(ebx["ebx"]), 2)
            ebx["bx"] = int(value[16:32])
            Register16bit["bx"] = int(str(ebx["bx"]), 2)
            ebx["bh"] = int(value[16:24])
            Register8bit["bh"] = int(str(ebx["bh"]), 2)
            ebx["bl"] = int(value[24:32])
            Register8bit["bh"] = int(str(ebx["bl"]), 2)
            break
    for i in ecx.keys():
        for j in Register32bit.keys():
            if(i == j):
                ecx[j] = Register32bit[i]
        for j in Register16bit.keys():
            if(i == j):
                ecx[j] = Register16bit[i]
        for j in Register8bit.keys():
            if(i == j):
                ecx[j] = Register8bit[i]
        if(ecx[i] != 0):
            value = "{:032b}".format(ecx[i])
            ecx["ecx"] = int(value[0:32])
            Register32bit["ecx"] = int(str(ebx["ecx"]), 2)
            ecx["cx"] = int(value[16:32])
            Register16bit["cx"] = int(str(ebx["cx"]), 2)
            ecx["ch"] = int(value[16:24])
            Register8bit["ch"] = int(str(ebx["ch"]), 2)
            ecx["cl"] = int(value[24:32])
            Register8bit["cl"] = int(str(ebx["cl"]), 2)
            break
    for i in edx.keys():
        for j in Register32bit.keys():
            if(i == j):
                edx[j] = Register32bit[i]
        for j in Register16bit.keys():
            if(i == j):
                edx[j] = Register16bit[i]
        for j in Register8bit.keys():
            if(i == j):
                edx[j] = Register8bit[i]
        if(edx[i] != 0):
            value = "{:032b}".format(edx[i])
            edx["edx"] = int(value[0:32])
            Register32bit[ecx] = int(str(ecx["ecx"]), 2)
            edx["dx"] = int(value[16:32])
            Register16bit["dx"] = int(str(ecx["dx"]), 2)
            edx["dh"] = int(value[16:24])
            Register8bit["dh"] = int(str(ecx["dh"]), 2)
            edx["dl"] = int(value[24:32])
            Register8bit["dl"] = int(str(ecx["dl"]), 2)
            break


# read file and split by lines
with open("code.txt", "r") as file:
    myString = file.read()
    myList = remove_space(myString)

    # splitting line-inputs to operators,values and instructions.
    # for in range of every  line
    for i in range(len(myList)):
        if myList[i] != '':
            # it lowers the registers and split them by ','
            operators = myList[i].split(",")
            operator1: str = operators[1].lower().strip()
            operator2: str = operators[2].lower().strip()
            # it lowers the instructions
            instruction = evaluate_Instruction(operators[0].lower())
        # puting value of register in num1 & num2
        if (operator1 in Register32bit.keys()) and (operator2 in Register32bit.keys()):
            num2 = int(Register32bit[operator1])
            num1 = int(Register32bit[operator2])
            zeroFlag, carryFlag, overflowFlag, negativeFlag, num1, num2 = calculate_32bit(
                num1, num2)
            Register32bit[operator1] = num1
            Register32bit[operator2] = num2
        elif(operator1 in Register16bit.keys()) and (operator2 in Register16bit.keys()):
            num2 = int(Register16bit[operator1])
            num1 = int(Register16bit[operator2])
            zeroFlag, carryFlag, overflowFlag, negativeFlag, num1, num2 = calculate_16bit(
                num1, num2)
            Register16bit[operator1] = num1
            Register16bit[operator2] = num2
        elif (operator1 in Register8bit.keys()) and (operator2 in Register8bit.keys()):
            num2 = int(Register8bit[operator1])
            num1 = int(Register8bit[operator2])
            zeroFlag, carryFlag, overflowFlag, negativeFlag, num1, num2 = calculate_8bit(
                num1, num2)
            Register8bit[operator1] = num1
            Register8bit[operator2] = num2
        elif (operator1 in Register8bit.keys()):
            num1 = int(operator2)
            num2 = int(Register8bit[operator1])
            zeroFlag, carryFlag, overflowFlag, negativeFlag, num1, num2 = calculate_8bit(
                num1, num2)
            Register8bit[operator1] = num2
        elif (operator1 in Register16bit.keys()):
            num1 = int(operator2)
            num2 = int(Register16bit[operator1])
            zeroFlag, carryFlag, overflowFlag, negativeFlag, num1, num2 = calculate_16bit(
                num1, num2)
            Register16bit[operator1] = num2
        elif (operator1 in Register32bit.keys()):
            num1 = int(operator2)
            num2 = int(Register32bit[operator1])
            zeroFlag, carryFlag, overflowFlag, negativeFlag, num1, num2 = calculate_32bit(
                num1, num2)
            Register32bit[operator1] = num2
        else:
            print("Error detected.")
        sync_reg()

    with open("answer.txt", "w") as file:
        file.write("zeroFlag: " + str(zeroFlag) + "\t | carryFlag: " + str(carryFlag) + "\noverflowFlag : " + str(overflowFlag)
                   + "\t | negativeFlag: " + str(negativeFlag)+"\n")
        file.write("eax:" + str(Register32bit["eax"]) + "\t ebx:" + str(Register32bit["ebx"]) + "\t ecx:"
                   + str(Register32bit["ecx"]) + "\t edx:" + str(Register32bit["edx"])+"\n")
        file.write("ax:" + str(Register16bit["ax"]) + "\t bx:" + str(Register16bit["bx"]) + "\t cx:" + str(Register16bit["cx"])
                   + "\t dx:" + str(Register16bit["dx"])+"\n")
        file.write("ah :" + str(Register8bit["ah"]) + " al :" + str(Register8bit["al"]) + "\nbh :" + str(
            Register8bit["bh"]) + " bl :"
            + str(Register8bit["bl"]) + "\nch : " + str(Register8bit["ch"]) + " cl :" + str(Register8bit["cl"]) +
            "\ndh : " + str(Register8bit["dh"]) + " dl : " + str(Register8bit["dl"])+"\n")
