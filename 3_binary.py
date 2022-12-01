"""
Gamma rate = most common bit
epsilon rate = least common bit
multiply to get power consumption
"""

def main():

    file = open("3_input.txt", "r")
    lines = file.readlines()

    binarylist = []
    gamma_rate = ""
    epsilon_rate = ""

    for line in lines:
        binarylist.append(line)

    for col in range(len(binarylist[0])-1):
        zerocount = 0
        onecount = 0
        for row in binarylist:
                if row[col] == "1":
                    zerocount += 1
                else:
                    onecount += 1
        if zerocount > onecount:
            gamma_rate += "0"
        else:
            gamma_rate += "1"
    

    for col in range(len(binarylist[0])-1):
        zerocount = 0
        onecount = 0
        for row in binarylist:
                if row[col] == "1":
                    zerocount += 1
                else:
                    onecount += 1
        if zerocount < onecount:
            epsilon_rate += "0"
        else:
            epsilon_rate += "1"

    print(int(gamma_rate, 2)*int(epsilon_rate, 2))
    

if __name__ == '__main__':
    main()
    