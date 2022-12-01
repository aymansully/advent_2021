def main():
    
    file = open("1_input.txt", "r")
    lines = file.readlines()
    # sonar_new = 0
    sonar_old = 0
    increase_count = 0

    for line in lines:
        sonar_new = int(line)
        if sonar_old != 0:
            # compare
            if sonar_new > sonar_old:
                increase_count += 1

        sonar_old = sonar_new
    print(increase_count)

if __name__ == '__main__':
    main()
        