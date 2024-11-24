import os

import matplotlib.pyplot as plt

def assignments():
    value = []
    asmt = inputs("What is the assignment name: ")
    asmts = open("data/assignments.txt")
    for id in asmts:
        if asmt == id.strip():
            id = asmts.readline().strip()
            break
    for files in os.listdir("data/submissions"):
        grade = open(f"data/submissions/{files}")
        test = grade.read().strip().split("|")
        if id == test[1]:
            value.append(int(test[2]))
    return value
def menu():
    print("1. Student grade\n"
          "2. Assignment statistics\n"
          "3. Assignment graph\n")
def main():
    menu()
    opt = int(input("Enter your selection: "))
    total = 0
    count = 0
    if opt == 1:
        student = input("What is the student's name: ")
        file = open("data/students.txt")
        for line in file:
            if student == line[3:].strip():
                stu_id = line[:3]
                for files in os.listdir("data/submissions"):
                    grades = open(f"data/submissions/{files}")
                    test = grades.read()
                    if stu_id == test[:3].strip():
                        asmt = test.strip().split("|")
                        asmts = open("data/assignments.txt")
                        for id in asmts:
                            if asmt[1] == id.strip():
                                weight = asmts.readline()
                                total += int(asmt[2]) * int(weight)
                        count += int(weight)
                    grades.close()
                avg = total / count
                print(f"{round(avg)}%")
        file.close()
    elif opt == 2:
        value = assignments()
        value.sort()
        for num in value:
            total += num
            count += 1
        avg = total / count
        print(f"Min: {value[0]}%\n"
              f"Average: {int(avg)}%\n"
              f"Max: {value[-1]}%\n")
    elif opt == 3:
        value = assignments()
        plt.hist(value, bins=[0, 25, 50, 75, 100])
        plt.show()
    else:
        print("Invalid Selection\n")

if __name__ == "__main__":
    main()
