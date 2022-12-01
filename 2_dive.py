"""
forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.
"""

def main():

    depth = 0
    h_pos = 0


    file = open("2_input.txt", "r")
    lines = file.readlines()

    for line in lines:
        splitline = line.split(" ")

        if splitline[0] == "forward":
            h_pos += int(splitline[1])
        elif splitline[0] == "up":
            depth -= int(splitline[1])
        elif splitline[0] == "down":
            depth += int(splitline[1])
    print(h_pos*depth)

if __name__ == '__main__':
    main()
    