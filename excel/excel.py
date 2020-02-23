#Using python to write data into Excel

import os
import sys
import time
import re
import win32api, win32con
from win32com.client import Dispatch
from os import listdir
from os.path import isfile,join

class consol:
    def __init__(self):
        self.xlws=''
        self.branch=''
        self.cc=''
        self.xlapp=''
        self.matrix=[]
        self.xlwb=''

    def excel(self, workbook, worksheetnum):
        self.xlapp=Dispatch("Excel.Application")
        self.xlapp.visible=False
        self.xlwb=self.xlapp.Workbooks.Open(workbook)
        self.xlws=self.xlwb.Worksheets(worksheetnum)
        print(self.xlws.name)
        '''
        for x in range(1,14):
            worksheetnum=x
            print(x)
            self.xlws=self.xlwb.Worksheets(worksheetnum)
            print(self.xlws.name)
        '''

    def escape(self):
        self.xlwb.Save()
        self.xlapp.Quit()

    def getWS(self):
        return self.xlws

    def setBranch(self, startrow, startcol):
        print("setBranch")
        xlws=self.xlws
        #print(xlws.name)
        #print("here1")
        xlcell=xlws.Cells(startrow,startcol)   
        self.branch=xlcell.Value

    def setCC(self, row, col):
        print("setCC")
        xlws=self.xlws
        xlcell=xlws.Cells(row,col)   
        self.cc=xlcell.Value

    def getBranch(self):
        return self.branch

    def getCC(self):
        return self.cc

    def isando(self, branchcol, cccol, GLcodecol, startBudcol, numBudgetcols, startrow, numrows):
        I=["CostCentre1","CostCentre2","CostCentre3","CostCentre4"]
        numBudgetcols=numBudgetcols+1
        xlws=self.xlws
        print("isando")
        Branch=self.getBranch()
        CC=self.getCC()
        w=13
        rowM=0
        rowN=0

        for row in range(startrow,numrows):
            branch=xlws.Cells(row,branchcol).Value
            cc=xlws.Cells(row,cccol).Value
            if(branch==Branch):
                for c in I:
                    if(cc==c):
                        pass
                    else:
                        rowM=rowM+1

        rowM=rowM+10

        endBudcol=startBudcol+numBudgetcols-1
        self.matrix=[[0 for x in range (w)] for y in range(rowM)]
        for row in range(startrow,numrows):
            branch=xlws.Cells(row,branchcol).Value
            cc=xlws.Cells(row,cccol).Value
            if(branch==Branch):
                match=0
                for c in I:
                    if(cc==c):
                        match=1
                
                if(match==0):
                    rowN=rowN+1
                    GLcode=xlws.Cells(row,GLcodecol).Value
                    colN=0
                    self.matrix[rowN][colN]=GLcode
                    for col in range(startBudcol,endBudcol):
                        colN=colN+1
                        Budgetval=xlws.Cells(row,col).Value
                        self.matrix[rowN][colN]=Budgetval
                        #print(Budgetval)   

    def readC(self, branchcol, cccol, GLcodecol, startBudcol, numBudgetcols, startrow, numrows):
        numBudgetcols=numBudgetcols+1
        xlws=self.xlws
        print("readC")
        Branch=self.getBranch()
        CC=self.getCC()
        w=13
        rowM=0
        rowN=0

        for row in range(startrow,numrows):
            branch=xlws.Cells(row,branchcol).Value
            cc=xlws.Cells(row,cccol).Value
            if((branch==Branch)and(cc==CC)):
                rowM=rowM+1

        rowM=rowM+10

        endBudcol=startBudcol+numBudgetcols-1
        self.matrix=[[0 for x in range (w)] for y in range(rowM)]
        for row in range(startrow,numrows):
            branch=xlws.Cells(row,branchcol).Value
            cc=xlws.Cells(row,cccol).Value
            if((branch==Branch)and(cc==CC)):
                rowN=rowN+1
                GLcode=xlws.Cells(row,GLcodecol).Value
                colN=0
                self.matrix[rowN][colN]=GLcode
                for col in range(startBudcol,endBudcol):
                    colN=colN+1
                    Budgetval=xlws.Cells(row,col).Value
                    self.matrix[rowN][colN]=Budgetval
                    #print(Budgetval)
                
    def readB(self, branchcol, GLcodecol, startBudcol, numBudgetcols, startrow, numrows):
        numBudgetcols=numBudgetcols+1
        xlws=self.xlws
        print("readB")
        Branch=self.getBranch()
        w=13
        h=numrows
        rowM=0
        rowN=0

        for row in range(startrow,numrows):
            branch=xlws.Cells(row,branchcol).Value 
            if(branch==Branch):
                    rowM=rowM+1

        rowM=rowM+10

        endBudcol=startBudcol+numBudgetcols-1
        self.matrix=[[0 for x in range (w)] for y in range(rowM)]
        for row in range(startrow,numrows):
            branch=xlws.Cells(row,branchcol).Value             
            if(branch==Branch):
                rowN=rowN+1
                GLcode=xlws.Cells(row,GLcodecol).Value
                #print("equal branch")
                #print(GLcode)
                colN=0 
                self.matrix[rowN][colN]=GLcode
                for col in range(startBudcol,endBudcol):
                    colN=colN+1
                    Budgetval=xlws.Cells(row,col).Value
                    self.matrix[rowN][colN]=Budgetval
                    #print(Budgetval)

    def getMatrix(self):
        return self.matrix

    def write(self, row, column):
        print("write")
        xlws=self.xlws
        m=[]
        m=self.getMatrix()
        nextRow=row
        row_count=xlws.Rows.Count
        for cell_value in range(1,row_count):
            #print(xlws)
            c=xlws.Cells(cell_value,column).Value
            #print(c)
            if(c<>None):
                #print("passed")
                #print(cell_value)
                pass
            else:
                print("broke")
                #print(cell_value)
                break
        nextRow=cell_value
        print(nextRow)
        
        for v in m:
            nextCol=column
            for x in v:
                xlws.Cells(nextRow,nextCol).Value=x
                nextCol=nextCol+1
            nextRow=nextRow+1
        

mypath="c:\\Budgets - Patryk\\"
finalbudget="c:\\consolSBS.xlsx"
#branch
#worksheet=6
row=3
column=3
worksheet=12

startrow=10
branchcol=4
GLcodecol=2
startBudcol=21
numBudgetcols=12
numrows=2306

ccrow=4
cccol=4
ccol=5

#data
#worksheet=2
rowW=1
colW=1
#budget
#column=20
r=0
c=consol()
onlyfiles=[f for f in listdir(mypath) if isfile(join(mypath,f))]
for files in onlyfiles:
    print(files)
    fullFileR=mypath+files
    fullFileW=finalbudget
    c.excel(fullFileR, worksheet)
    c.setBranch(row, column)
    Branch=c.getBranch()
    #print(Branch)
    if(Branch=="Brach1"):
        c.setCC(ccrow,cccol)
        isando=c.getCC()
        if(isando==None):
            c.isando(branchcol, ccol, GLcodecol, startBudcol, numBudgetcols, startrow, numrows)
        else:
            c.readC(branchcol, ccol, GLcodecol, startBudcol, numBudgetcols, startrow, numrows)
    else:
        c.readB(branchcol, GLcodecol, startBudcol, numBudgetcols, startrow, numrows)
    m=c.getMatrix()
    #print(len(m))
    c.escape()
    c.excel(fullFileW, 1)
    c.write(rowW, colW)
    c.escape()
