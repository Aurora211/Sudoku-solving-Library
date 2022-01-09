from sudoku import sudoku

obj = sudoku()

for item in range(0,9):
    obj.setLineData(item, input("Line"+str(item)+": "))
print("="*20)
print("Start Solving Problem...")
print(obj.solve())
obj.printProblem()
