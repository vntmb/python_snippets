# This takes in values and sorts them using the bubble sort algorithm
values = [1,373, 12, 372, 32, 54, 12]

def main():
    run = 1
    while run < len(values)-1:
        count = 0
        #print("To go through " + str(len(values)-run))
        while count < len(values)-run:
            if values[count+1] < values[count]:
                values[count], values[count+1] = values[count+1], values[count]
            count += 1
        run +=1 
    print(values)

if __name__ == "__main__":
    main()