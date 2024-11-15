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
            nodestate=stack.pop()
            if nodestate in visited:
                continue
            visited.add(nodestate)
            if(nodestate.chickGoal()):
                path=[nodestate]
                while(not nodestate.getperent() is None):
                    nodestate=nodestate.getperent()
                    path.append(nodestate)
                path.reverse()
                return path ,visited 
            
            else :
                listchild=nodestate.nextState2()
                for n in listchild:
                    if not(n in visited):
                        stack.append(n)

                    
        

if __name__ == "__main__": 
    gamee=game(3)
    array1=gamee.funarr1()
    array2=gamee.funarr2()
    array3goul=gamee.funarr3()
    print("  -----  DFS -----   ")
    s=State(array1,array2,array3goul,None)
    d=DFS(s)
    listpathstate ,listvisitedstate =d.moveDFS()
    for state in listpathstate:
        state.printS()  
        print("/"*20)  
    print(f"number of state in path is  {len(listpathstate)}")        
    print(f"number of state in visited is  {len(listvisitedstate)}")        


   