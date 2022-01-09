import copy

class sudoku:
    # 初始问题矩阵
    problem = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]

    # 输出当前问题矩阵
    def printProblem(self):
        print("Current Problem Map")
        for row in self.problem:
            for item in row:
                if item == 0:
                    print(" ", end="")
                else:
                    print(item, end="")
            print("\n", end="")
    
    # 获取单元格值
    def getValueOf(self,x,y):
        return self.problem[x][y]

    # 设置单个单元值
    def setData(self,x,y,value):
        if x not in range(0,9) or y not in range(0,9):
            print("Position is not valid!")
            return False
        self.problem[x][y] = value
        return True
    
    # 设置一行单元值
    def setLineData(self,x,value):
        if len(value) != 9:
            print("Length of line data is not valid!")
            return False
        if x not in range(0,9):
            print("Line index is not valid!")
            return False
        index = 0
        for item in value:
            if item in ["1","2","3","4","5","6","7","8","9"]:
                self.problem[x][index] = int(item)
            else:
                self.problem[x][index] = 0
            index = index + 1
        return True

    # 检测单元格内值是否合理
    def checkSingle(self,x,y):
        if x not in range(0,9) or y not in range(0,9):
            print("Position is not valid!")
            return False
        if self.problem[x][y] not in range(1,10):
            print("Current position does not filled yet!")
            return False
        value = self.problem[x][y]
        #line check
        check = -1
        for item in range(0,9):
            if self.problem[x][item] == value:
                check = check + 1
        if check > 0:
            return "Found"
        #row check
        check = -1
        for item in range(0,9):
            if self.problem[item][y] == value:
                check = check + 1
        if check > 0:
            return "Found"
        #box check
        check = -1
        box_x = x // 3
        box_y = y // 3
        for row in range(0,3):
            for line in range(0,3):
                if self.problem[3 * box_x + row][3 * box_y + line] == value:
                    check = check + 1
        if check > 0:
            return "Found"
        return True

    # 获取指定单元格所有可能值
    def getPosibleNumbers(self,x,y):
        if x not in range(0,9) or y not in range(0,9):
            print("Position is not valid!")
            return False
        if self.problem[x][y] != 0:
            print("This cell has already filled!")
            return False
        posibleNumbers = []
        for item in range(1,10):
            self.setData(x,y,item)
            if self.checkSingle(x,y) == True:
                posibleNumbers.append(item)
            self.setData(x,y,0)
        return posibleNumbers
    
    # 获取空单元格坐标
    # 默认获取所有空单元格坐标
    # 非1值输出第一个空单元格坐标
    def getBlankCell(self,mode = 1):
        blankCell = []
        for row in range(0,9):
            for line in range(0,9):
                if self.problem[row][line] == 0:
                    if mode != 1:
                        return [row,line]
                    else:
                        blankCell.append([row,line])
        return blankCell
    
    # 找到第一个只有一可能值的单元格并填入值
    def fillOnlySelectionCell(self):
        blankCell = self.getBlankCell()
        if blankCell == []:
            return False
        for item in blankCell:
            posibleNumber = self.getPosibleNumbers(item[0],item[1])
            if posibleNumber != False and len(posibleNumber) == 1:
                self.setData(item[0],item[1],posibleNumber[0])
                return True
        return False
    
    # 检查是否存在无解单元格
    def checkUnsolvableCell(self):
        blankCell = self.getBlankCell()
        if blankCell == []:
            return False
        for item in blankCell:
            posibleNumber = self.getPosibleNumbers(item[0],item[1])
            if posibleNumber != False and posibleNumber == []:
                return True
        return False
    
    # 求解主函数 === 求解主函数
    def solve(self):
        while self.fillOnlySelectionCell():
            pass
        if self.getBlankCell() == []:
            print("Problem Solved.")
            return True
        return self.testWrong()

    # 试错递归
    def testWrong(self,pos=[-1,-1]):
        temp = copy.deepcopy(self.problem)
        priCell = self.getBlankCell(0)
        if pos != [-1,-1]:
            priCell = pos
        posibleNumber = self.getPosibleNumbers(priCell[0],priCell[1])
        for item in posibleNumber:
            self.problem = copy.deepcopy(temp)
            self.setData(priCell[0],priCell[1],item)
            if self.getBlankCell() == []:
                print("Problem Solved.")
                return "Solved"
            if self.checkUnsolvableCell():
                continue
            while self.fillOnlySelectionCell():
                pass
            if self.getBlankCell() == []:
                print("Problem Solved.")
                return "Solved"
            if self.checkUnsolvableCell():
                continue
            if self.testWrong(self.getBlankCell(0)) == "Solved":
                return "Solved"
        self.problem = copy.deepcopy(temp)
        return False
