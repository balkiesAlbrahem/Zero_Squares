from state import *
import numpy as py
from game import *

class DFS:
    def __init__(self, state):
        self.initState = state
        self.visited = set()

    def moveDFS(self, state, path):
        if state.chickGoal():
            path.append(state)
            return path, self.visited

        self.visited.add(state)

        listchild = state.nextState2()
        for child in listchild:
            if child not in self.visited:
                path.append(state)

                result = self.moveDFS(child, path)
                if result:  
                    return result

                path.pop()

        return None  

if __name__ == "__main__":
    gamee = game(3)
    array1 = gamee.funarr1()
    array2 = gamee.funarr2()
    array3goul = gamee.funarr3()

    print("  -----  DFS (Recursive) -----   ")
    s = State(array1, array2, array3goul, None)
    d = DFS(s)
    listpathstate = []
    result = d.moveDFS(s, listpathstate)

    if result:
        listpathstate, listvisitedstate = result
        for state in listpathstate:
            state.printS()
            print("/" * 20)
        print(f"number of state in path is  {len(listpathstate)}")
        print(f"number of state in visited is  {len(listvisitedstate)}")
    else:
        print("No solution found.")
