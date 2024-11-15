from state import *
import numpy as py
from game import *

class DFS:
    def __init__(self,state):
        self.initState=state
        
    def moveDFS(self):
        stack =[self.initState];
        visited =set()
        while stack:
            nodestate=stack.pop(0)
            if nodestate in visited:
                continue
            print("/"*20)
            print("add")
            nodestate.printS()
            print(nodestate.chickGoal())
            if(nodestate.chickGoal()):
                print("true")
                print(nodestate.chickGoal())
                break
            visited.add(nodestate)
            # print(nodestate.chickGoal())
            if(nodestate.chickGoal()):
                print("enter")
                path=[nodestate]
                while(nodestate.getperent!=None):
                    nodestate=nodestate.getperent
                    path.append(nodestate)
                    print("jj")
                    nodestate.printS()
                path.reverse()
                return path
            
            else :
                listchild=nodestate.nextState2()
                for n in listchild:
                    if not(n in visited):
                        stack.append(n)

        return visited            
        

if __name__ == "__main__": 
    gamee=game(1)
    array1=gamee.funarr1()
    array2=gamee.funarr2()
    array3goul=gamee.funarr3()
    print("/"*30)
    s=State(array1,array2,array3goul,None)
    d=DFS(s)
    
    listpathstate=d.moveDFS()
    # print(listpathstate)
    # for state in listpathstate:
    #     print("*"*30)
    #     state.printS()  
    #     print("/"*20)  

    print(len(listpathstate))        

# def checkmovedown(self, posA, posB, posC,array, exitA, exitB):
    #     if  posA[0].size > 0 and posA[1].size > 0  :
    #         rowA, colA = posA[0][0], posA[1][0]
    #         max_rowA = rowA + 1
    #         while array[max_rowA][colA] != "■" and array[max_rowA][colA] != "B" and array[max_rowA][colA] != "C":
    #            max_rowA += 1
    #         max_rowA -= 1
    #         a = self.goalsquare[rowA][colA]
    #         if a == "A" :
    #             array[rowA][colA] = "□"  
    #             array[max_rowA][colA] = "□"
    #             self.goalsquare[rowA][colA] ="□"
    #         elif a == "B":
    #             array[rowA][colA] = "b"  
    #             array[max_rowA][colA] = "A"
    #         elif a == "C":
    #             array[rowA][colA] = "c" 
    #             array[max_rowA][colA] = "A"    
    #         else:
    #             array[rowA][colA] = "□"
    #             array[max_rowA][colA] = "A"

    #         #  ////////
    #     if posB[0].size > 0 and posB[1].size > 0:
    #         rowB, colB = posB[0][0], posB[1][0]
    #         max_rowB = rowB + 1
    #         while array[max_rowB][colB] != "■" and array[max_rowB][colB] != "A" and array[max_rowB][colB] != "C" :
    #             max_rowB += 1
    #         max_rowB -= 1
    #         b = self.goalsquare[rowB][colB]
    #         if b == "A":
    #             array[rowB][colB] = "a"
    #             array[max_rowB][colB] = "B"
    #         elif b == "B":
    #             array[rowB][colB] = "□"
    #             array[max_rowB][colB] = "□"
    #             self.goalsquare[rowB][colB] ="□"
    #         elif b == "C":
    #             array[rowB][colB] = "c"
    #             array[max_rowB][colB] = "B"    
    #         else:
    #             array[rowB][colB] = "□"
    #             array[max_rowB][colB] = "B"

    #         #  ////////
    #     if posC[0].size > 0 and posC[1].size > 0:
    #         rowC, colC = posC[0][0], posC[1][0]
    #         max_rowC = rowC + 1
    #         while array[max_rowC][colC] != "■" and array[max_rowC][colC] != "A" and array[max_rowC][colC] != "B":
    #             max_rowC += 1
    #         max_rowC -= 1
    #         c = self.goalsquare[rowC][colC]
    #         if c == "A" :
    #             array[rowC][colC] = "a"
    #             array[max_rowC][colC] = "C"
    #         elif c == "B" :
    #             array[rowC][colC] = "b"
    #             array[max_rowC][colC] = "C"
    #         elif c == "C":
    #             array[rowC][colC] = "□"
    #             array[max_rowC][colC] = "□" 
    #             self.goalsquare[rowC][colC] ="□"   
    #         else:
    #             array[rowC][colC] = "□"
    #             array[max_rowC][colC] = "C"

    #     return array
   