"""
Gamma rate = most common bit
epsilon rate = least common bit
multiply to get power consumption
"""
def count_digits(i, binarylist):
    zerocount = 0
    onecount = 0
    for row in binarylist:
        if row[i] == "0":
            zerocount += 1
        else:
            onecount += 1
    return zerocount, onecount

def scan_and_add(binarylist, CO2, zeromajor, i):
    templist = []
    # digit = []
    if CO2 is True: 
        digit = ["1","0"] # for CO2
    else:
        digit = ["0","1"] # for Oxygen

    if zeromajor == True:
        for row in binarylist:
            if row[i] == digit[0]:
                templist.append(row)
    if templist != []:
            binarylist = templist        
    else:
        for row in binarylist:
            if row[i] == digit[1]:
                templist.append(row)
        if templist != []:
            binarylist = templist        

    return binarylist
            

def twelve_loop(binarylist, CO2):
    for col in range(12):
        zerocount, onecount = count_digits(col, binarylist)
        if zerocount > onecount:
            binarylist = scan_and_add(binarylist, CO2, True, col)
        elif zerocount < onecount:




def main2():
    file = open("3_input.txt", "r")
    lines = file.readlines()

    binaryOxygen = []
    binaryCO2 = []
    oxygenrating = ""
    CO2rating = ""

    for line in lines:
        binaryOxygen.append(line.strip())
        binaryCO2.append(line.strip())
    
    twelve_loop(binaryOxygen, False)
    twelve_loop(binaryCO2, True)
    

def main():

    file = open("3_input.txt", "r")
    lines = file.readlines()

    binaryOxygen = []
    binaryCO2 = []
    oxygenrating = ""
    CO2rating = ""

    for line in lines:
        binaryOxygen.append(line.strip())
        binaryCO2.append(line.strip())

    for col in range(12):
        zerocount = 0
        onecount = 0
        templist = []
        for row in binaryOxygen:
                if row[col] == "0":
                    zerocount += 1
                else:
                    onecount += 1

        if zerocount > onecount:
            for row in binaryOxygen:
                if row[col] == "0": # only keep the most common
                    templist.append(row)
            if templist != []:
                binaryOxygen = templist

        else: # less or equal
            for row in binaryOxygen:
                if row[col] == "1": # only keep the most common
                    templist.append(row)
            if templist != []:
                binaryOxygen = templist
        
        if len(binaryOxygen) == 1:
            oxygenrating = binaryOxygen[0]
            break
        
    for col in range(12):
        zerocount = 0
        onecount = 0
        templist = []
        for row in binaryCO2:
                if row[col] == "0":
                    zerocount += 1
                else:
                    onecount += 1
        if zerocount < onecount: 
            for row in binaryCO2:
                if row[col] == "0": # only keep the least common
                    templist.append(row)
            if templist != []:
                binaryCO2 = templist

        else:
            for row in binaryCO2:
                if row[col] == "1": # only keep the least common
                    templist.append(row)
            if templist != []:
                binaryCO2 = templist
                
        if len(binaryCO2) == 1:
            CO2rating = binaryCO2[0]
            break

    if oxygenrating != "" and CO2rating != "":
        print(int(oxygenrating, 2)*int(CO2rating, 2))
    else:
        print("error")
    

if __name__ == '__main__':
    main()
    