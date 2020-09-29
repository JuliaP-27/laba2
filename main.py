import threading
import time

def solution_1():
    def printList(carteg):
        print(carteg)

    for x in range(4):
        thread = threading.Thread(target=printList,args=[range(x)])
        print(f"Thread '{x+1}' is starting")
        thread.start()

def solution_2():
    first_matrix = []
    second_matrix = []


    i=0
    while True:
        print(f"Enter {i+1} row in matrix, if you wahna stop clear input")
        inp = input()
        if(inp == ""):
            break
        inp = inp.split(' ')
        first_matrix.append(inp)
        i+=1

    for x in range(len(first_matrix[0])):
        print(f"Enter {x + 1} row in second matrix")
        inp = input()
        inp = inp.split(' ')
        second_matrix.append(inp)
        i += 1

    def getMatrixColumn(matrix, id):
        column = []
        for row in matrix:
            column.append(row[id])
        return column

    def multRowMatrix(state, row, column):
        result = 0
        for x in range(len(row)):
            result +=int(row[x])*int(column[x])
        result_matrix[state].append(result)

    result_matrix = []

    for p in range(len(first_matrix)):
        result_matrix.append([])

    for row in range(len(first_matrix)):
        for col in range(len(second_matrix)):
            thread = threading.Thread(target=multRowMatrix, args=(row,first_matrix[row],getMatrixColumn(second_matrix,col)))
            thread.start()
            thread.join()

    for row in result_matrix:
        print(row)

def solution_3():
    def reading(state):
        try:
            fileRead = open(f"expression/in_{state}.txt", "r")
        except:
            print("File not found!!!")
            return

        string = fileRead.read()
        string = string.split()

        op = string[0]
        a = int(string[1])
        b = int(string[2])

        result = 0
        if(op == '+'):
            result = a + b
        elif(op == '-'):
            result = a - b
        elif(op == '*'):
            result = a * b
        elif(op == '/'):
            result = a / b
        results[state] = result

    countOfFile = 4
    results = []

    for x in range(countOfFile):
        results.append(0)
        thread = threading.Thread(target=reading, args=[x])
        thread.start()

    time.sleep(2)
    result = 0
    for x in range(len(results)):
        result += results[x]

    fileWrite = open("out.txt","w")
    fileWrite.write(str(result))

solutions = {
    1:solution_1,
    2:solution_2,
    3:solution_3
}

while True:
    print("Enter the num of solution...")
    inp = input()
    if(inp == "stop"):
        quit()
    try:
        solutions[int(inp)]()
    except:
        print("Wrong solution")