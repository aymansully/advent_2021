def main():
    
    file = open("1_input.txt", "r")
    lines = file.readlines()
    # sonar_new = 0
    sonar_old = 0
    sonar_list = []
    increase_count = 0

    for line in lines:
        sonar_list.append(int(line))

    for count, sonar in enumerate(sonar_list):
        if count - 1 >= 0 and count < len(sonar_list)-1: 
            sonar_new = sonar_list[count-1] + sonar_list[count] + sonar_list[count+1]
            if sonar_old != 0:
                if sonar_new > sonar_old:
                    increase_count += 1
            sonar_old = sonar_new
            
    print(increase_count)

if __name__ == '__main__':
    main()
        