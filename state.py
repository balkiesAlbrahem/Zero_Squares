import numpy as py
from colorama import Fore, Back, Style, init
import copy


class State:
    def __init__(self,array1,array2,arlist3goal,instate):
        self.boald=array1
        self.colorsquare=array2
        self.goalsquare=arlist3goal
        self.perentstate=instate
        #   مشان المقارنة الاوبجكتات 
    def __eq__(self, other):
        return (py.array_equal(self.colorsquare, other.colorsquare) and
                py.array_equal(self.goalsquare, other.goalsquare))
    
    def __hash__(self):
        return hash((self.colorsquare.tobytes(), self.goalsquare.tobytes()))        
        # result1=py.where(self.colorsquare=="A")
        # result2=py.where(self.colorsquare=="B")

    def getperent(self):
        return self.perentstate
        
    def nowpstate(self):
        return State(self.boald,self.colorsquare,self.goalsquare,self.perentstate)
    
    def chickGoal(self):
        return py.array_equal(self.colorsquare,self.goalsquare)

# //////////////////////////////////////////////////////

#    RIGHT 
    def checkmoveright(self, posA, posB,posC,array0,exitA,exitB):
        x=copy.deepcopy(self.goalsquare)
        array =array0
        listmovechar=[]
        if posA[0].size > 0 and posA[1].size > 0:
            rowA, colA = posA[0][0], posA[1][0]
            max_colA=colA-1
            while array[rowA][max_colA]!="■" and array[rowA][max_colA]!="B"  and array[rowA][max_colA]!="C" and x[rowA][max_colA]!="A":
                max_colA-=1
            if(x[rowA][max_colA]=="A"):
                max_colA
            else:        
                max_colA+=1 
            listmovechar.append((rowA,colA,max_colA,"A")) 
        # ////////////////
        if posB[0].size > 0 and posB[1].size > 0 :
            rowB, colB = posB[0][0], posB[1][0] 
            max_colB=colB-1
            while array[rowB][max_colB]!="■" and array[rowB][max_colB]!="A" and array[rowB][max_colB]!="C" and x[rowB][max_colB]!="B":
                max_colB-=1 
            if( x[rowB][max_colB]=="B"):
                max_colB
            else:        
                max_colB+=1 
            listmovechar.append((rowB,colB,max_colB,"B"))
                # //////////
        if posC[0].size > 0 and posC[1].size > 0 :
            rowC, colC = posC[0][0], posC[1][0] 
            max_colC=colC-1
            while array[rowC][max_colC]!="■" and array[rowC][max_colC]!="A" and array[rowC][max_colC]!="B" and x[rowC][max_colC]!="C":
                max_colC-=1
            if(x[rowC][max_colC]=="C") :
                max_colC
            else:        
                max_colC+=1 
            listmovechar.append((rowC,colC,max_colC,"C"))  

        for row,col,colmax,chare in listmovechar:
            array[row][colmax]=chare

            if (x[row][col]=="A"):
                if col!=colmax:
                    array[row][col]="a"
            elif (x[row][col]=="B"):
                if col!=colmax:
                    array[row][col]="b"
            elif (x[row][col]=="C"):
                if col!=colmax:
                   array[row][col]="c"
            else:
                if col!=colmax:
                    array[row][col]="□"  
            
            if (x[row][colmax]==chare):
                x[row][colmax]="□"
                array[row][colmax]="□"
        # for n in listmovechar:
        #     print(n)         
        return array ,x
    

# /////////////////////
    def moveright(self, posA, posB,posC,array,exitA,exitB):
        perentstat=self.nowpstate()
        array ,x= self.checkmoveright(posA, posB,posC,array,exitA,exitB)
        s=State(self.boald,array,x,perentstat)
        return s
    

# /////////////////////////////////////////////////////////////////

#   LEFT
    def checkmoveleft(self, posA, posB,posC,array0,exitA,exitB):
        x=copy.deepcopy(self.goalsquare)
        array=array0
        listmovechar=[]
        if posA[0].size > 0 and posA[1].size > 0 :
            rowA, colA = posA[0][0], posA[1][0]
            max_colA=colA
            while array[rowA][max_colA]!="■" and array[rowA][max_colA]!="B"  and array[rowA][max_colA]!="C" and x[rowA][max_colA]!="A":
               max_colA+=1 
            if(x[rowA][max_colA]=="A"):
                max_colA
            else:       
                max_colA-=1 
            listmovechar.append((rowA,colA,max_colA,"A")) 
       
        #   ///////////////////// 
        if posB[0].size > 0 and posB[1].size > 0:
            rowB, colB = posB[0][0], posB[1][0]
            max_colB=colB
            while array[rowB][max_colB]!="■" and array[rowB][max_colB]!="A"  and array[rowB][max_colB]!="C" and x[rowB][max_colB]!="B" :
                max_colB+=1 
            if(x[rowB][max_colB]=="B"):
                max_colB
            else:          
                max_colB-=1
            listmovechar.append((rowB,colB,max_colB,"B")) 

        #    /////////////
        if posC[0].size > 0 and posC[1].size > 0:
            rowC, colC = posC[0][0], posC[1][0]
            max_colC = colC
            while array[rowC][max_colC]!="■" and array[rowC][max_colC]!="A" and array[rowC][max_colC]!="B" and x[rowC][max_colC]!="C" :
                max_colC+=1  
            if(x[rowC][max_colC]=="C"):
                max_colC
            else:         
                max_colC-=1
            listmovechar.append((rowC,colC,max_colC,"C"))

        for row,col,colmax,chare in listmovechar:
            array[row][colmax]=chare

            if (x[row][col]=="A"):
                if col!=colmax:
                    array[row][col]="a"
            elif (x[row][col]=="B"):
                if col!=colmax:
                    array[row][col]="b"
            elif (x[row][col]=="C"):
                if col!=colmax:
                    array[row][col]="c"
            else:
                if col!=colmax:
                    array[row][col]="□"  
            
            if (x[row][colmax]==chare):
                x[row][colmax]="□"
                array[row][colmax]="□"
        # for n in listmovechar:
        #     print(n)     

        return array ,x

# 
    def moveleft(self, posA, posB,posC,array,exitA,exitB):
        perentstat=self.nowpstate()
        array,x= self.checkmoveleft( posA, posB,posC,array,exitA,exitB)
        s=State(self.boald,array,x,perentstat)
        return s

# ////////////////////////////////////////////////////////////
#   UP 
    def checkmoveup(self, posA, posB,posC,array0,exitA,exitB):
        x=copy.deepcopy(self.goalsquare)
        array=array0
        listmovechar=[]
        if posA[0].size > 0 and posA[1].size > 0:
            rowA, colA = posA[0][0], posA[1][0]
            max_rowA=rowA-1
            while array[max_rowA][colA]!="■" and array[max_rowA][colA]!="B" and array[max_rowA][colA]!="C" and x[max_rowA][colA]!="A":
                max_rowA-=1
            if(x[max_rowA][colA]=="A"):
                max_rowA
            else:        
                max_rowA+=1
            listmovechar.append((rowA,max_rowA,colA,"A")) 

        # ///////////
        if posB[0].size > 0 and posB[1].size > 0:
            rowB, colB = posB[0][0], posB[1][0]
            max_rowB=rowB-1
            while array[max_rowB][colB]!="■" and array[max_rowB][colB]!="A" and array[max_rowB][colB]!="C" and x[max_rowB][colB]!="B":
               max_rowB-=1 
            if(x[max_rowB][colB]=="B"):
                max_rowB
            else:        
                max_rowB+=1  
            listmovechar.append((rowB,max_rowB,colB,"B"))

        # ///////////
        if posC[0].size > 0 and posC[1].size > 0:
            rowC, colC = posC[0][0], posC[1][0]
            max_rowC=rowC-1
            while array[max_rowC][colC]!="■" and array[max_rowC][colC]!="A" and array[max_rowC][colC]!="B" and x[max_rowC][colC]!="C":
               max_rowC-=1 
            if(x[max_rowC][colC]=="C"):
                max_rowC
            else:        
                max_rowC+=1  
            listmovechar.append((rowC,max_rowC,colC,"C"))
            
        for row,rowmax,col,chare in listmovechar:
            array[rowmax][col]=chare
            if(x[row][col]=="A"):
                if row!=rowmax:
                    array[row][col]="a"
            elif(x[row][col]=="B"):
                if row!=rowmax:
                    array[row][col]="b"
            elif(x[row][col]=="C"):
                if row!=rowmax:
                    array[row][col]="c"
            else:
                if row!=rowmax :
                    array[row][col]="□"            
            if (x[rowmax][col]==chare):
                x[rowmax][col]="□"
                array[rowmax][col]="□"

        return array ,x


    def moveup(self, posA, posB,posC,array,exitA,exitB):
        perentstat=self.nowpstate()
        array,x= self.checkmoveup( posA, posB,posC,array,exitA,exitB)
        s=State(self.boald,array,x,perentstat)
        return s

    #  down
    
    def checkmovedown(self, posA, posB, posC, array0, exitA, exitB):
        x=copy.deepcopy(self.goalsquare)
        array=array0
        listmovechar=[]
        if posA[0].size > 0 and posA[1].size > 0:
            rowA, colA = posA[0][0], posA[1][0]
            max_rowA = rowA + 1
            while array[max_rowA][colA] != "■" and array[max_rowA][colA] != "B" and array[max_rowA][colA] != "C" and x[max_rowA][colA]!="A":
                max_rowA += 1
            if (x[max_rowA][colA]=="A"):
                max_rowA 
            else:    
                max_rowA -= 1
            listmovechar.append((rowA,max_rowA,colA,"A"))

        if posB[0].size > 0 and posB[1].size > 0:
            rowB, colB = posB[0][0], posB[1][0]
            max_rowB = rowB + 1
            while array[max_rowB][colB] != "■" and array[max_rowB][colB] != "A" and array[max_rowB][colB] != "C" and x[max_rowB][colB]!="B":
                max_rowB += 1
            if(x[max_rowB][colB]=="B"):
                max_rowB 
            else :        
                max_rowB -= 1
            listmovechar.append((rowB,max_rowB,colB,"B"))

        if posC[0].size > 0 and posC[1].size > 0:
            rowC, colC = posC[0][0], posC[1][0]
            max_rowC = rowC + 1
            while array[max_rowC][colC] != "■" and array[max_rowC][colC] != "A" and array[max_rowC][colC] != "B" and x[max_rowC][colC]!="C":
                max_rowC += 1
            if(x[max_rowC][colC]=="C"):
                max_rowC 
            else:    
                max_rowC -= 1
            listmovechar.append((rowC,max_rowC,colC,"C"))

        for row,rowmax,col,chare in listmovechar:
            array[rowmax][col]=chare
            if(x[row][col]=="A"):
                if row!=rowmax:
                    array[row][col]="a"
            elif(x[row][col]=="B"):
                if row!=rowmax:
                    array[row][col]="b"
            elif(x[row][col]=="C"):
                if row!=rowmax:
                    array[row][col]="c"
            else:
                if row!=rowmax :
                    array[row][col]="□"            
            if (x[rowmax][col]==chare):
                x[rowmax][col]="□"
                array[rowmax][col]="□"     

        return array  ,x  

    def movedown(self, posA,posB,posC,array,exitA,exitB):
        perentstat=self.nowpstate()
        array,x= self.checkmovedown( posA, posB,posC,array,exitA,exitB)
        s=State(self.boald,array,x,perentstat)
        return s

#  ////******************** //////////////// 
#   MOVE FOR ANYWHERE
    def move(self,value):
        result1=py.where(self.colorsquare=="A")
        result2=py.where(self.colorsquare=="B")
        result3=py.where(self.colorsquare=="C")
        if result1:
            exitresultA=True
        else:
            exitresultA=False    
              
        if result2:
            exitresultB=True 
        else:
            exitresultB=False

        copy_array=copy.deepcopy(self.colorsquare)
        match value :
            case 1:
                s=self.moveright(result1,result2,result3,copy_array,exitresultA,exitresultB)
                return s
            
            case 2:
                s=self.moveleft(result1,result2,result3,copy_array,exitresultA,exitresultB)
                return s
            
            case 3:
                s=self.moveup(result1,result2,result3,copy_array,exitresultA,exitresultB)
                return s
            
            case 4:
                s=self.movedown(result1,result2,result3,copy_array,exitresultA,exitresultB)
                return s
              
            case _:
                print("anywhere")

     
    def nextState(self):
        sonstate=[]
        r=self.move(1) 
        sonstate.append(r)
        l=self.move(2)
        sonstate.append(l)
        u=self.move(3)
        sonstate.append(u)
        d=self.move(4)
        sonstate.append(d)
        return sonstate
    

    def nextState2(self):
        sonstate=[]
        r=self.move(1) 
        if r!=self.nowpstate():
            sonstate.append(r)
        l=self.move(2)
        if l!=self.nowpstate():
            sonstate.append(l)
        u=self.move(3)
        if u!=self.nowpstate():
            sonstate.append(u)
        # sonstate.append(u)
        d=self.move(4)
        if d!=self.nowpstate():
            sonstate.append(d)
        # sonstate.append(d)
        return sonstate
        
    
    
        

#   JUST PRINT 
    def printS(self):
        for i in range(len(self.colorsquare)):
            for j in range(len(self.colorsquare[i])):
                if(self.colorsquare[i][j]!="□" or self.colorsquare[i][j]!="■"):
                    print(Fore.BLUE+self.colorsquare[i][j]+Fore.BLACK,end=" ")
                else:    
                    print(self.colorsquare[i][j],end=' ')  
            print("")      
        
        

    