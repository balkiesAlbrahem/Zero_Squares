from state import *
import numpy as py
from game import *

class BFS:
    def __init__(self,state):
        self.initState=state
        
    def moveBFS(self):
        queue =[self.initState];
        visited =set()
        while queue:
            nodestate=queue.pop(0)
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
                        queue.append(n)

                    
        

if __name__ == "__main__": 
    gamee=game(3)
    array1=gamee.funarr1()
    array2=gamee.funarr2()
    array3goul=gamee.funarr3()
    print("   -------- BFS --------   ")
    s=State(array1,array2,array3goul,None)
    d=BFS(s)
    listpathstate ,listvisitedstate =d.moveBFS()
    for state in listpathstate:
        state.printS()  
        print("/"*20)  
    print(f"number of state in path is  {len(listpathstate)}")        
    print(f"number of state in visited is  {len(listvisitedstate)}")        


   