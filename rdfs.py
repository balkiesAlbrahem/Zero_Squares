# from state import *
# import numpy as py
# from game import *
from state import *
from game import *

class DFS:
    def init(self, state):
        self.initState = state
        self.visited = set() 
    
    def moveDFS_recursive(self, nodeState):
        if nodeState.chickGoal():
            path = [nodeState]
            while nodeState.getperent() is not None: 
                nodeState = nodeState.getperent()
                path.append(nodeState)
            path.reverse()
            return path, self.visited
        
        self.visited.add(nodeState)
        
        children = nodeState.nextState2()
        for child in children:
            if child not in self.visited:
                result = self.moveDFS_recursive(child)
                if result:  
                    return result
        
        return None  

if __name__ == "main": 
    gamee = game(3)
    array1 = gamee.funarr1()
    array2 = gamee.funarr2()
    array3goul = gamee.funarr3()
    
    print("  -----  DFS -----   ")
    s = State(array1, array2, array3goul, None)
    d = DFS(s)
    result = d.moveDFS_recursive(d.initState)
    
    if result:
        listpathstate, listvisitedstate = result
        for state in listpathstate:
            state.printS()
            print("/" * 20)
        print(f"Number of states in path: {len(listpathstate)}")
        print(f"Number of states visited: {len(listvisitedstate)}")
    else:
        print("No solution found!")



