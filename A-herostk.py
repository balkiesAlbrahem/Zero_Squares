from state import *
import numpy as py
from game import *
import heapq  

class AStar:
    def __init__(self, state):
        self.initState = state

    def moveAStar(self):
        priority_queue = [(0, id(self.initState), self.initState)]
        visited = set()
        cost_dict = {self.initState: 0} 

        while priority_queue:
            current_f_cost, _, nodestate = heapq.heappop(priority_queue)

            if nodestate in visited:
                continue
            visited.add(nodestate)

            if nodestate.chickGoal():
                path = [nodestate]
                while nodestate.getperent() is not None:
                    nodestate = nodestate.getperent()
                    path.append(nodestate)
                path.reverse()
                return path, visited, cost_dict[nodestate]

            listchild = nodestate.nextState2()
            for n in listchild:
                g_cost = cost_dict[nodestate] + 1  # التكلفة الفعلية للوصول للحالة الجديدة
                h_cost = n.heuristic()  # القيمة الهيرستيكية
                f_cost = g_cost + h_cost

                if n not in visited or g_cost < cost_dict.get(n, float('inf')):
                    cost_dict[n] = g_cost
                    heapq.heappush(priority_queue, (f_cost, id(n), n))

if __name__ == "__main__":
    gamee = game(3)
    array1 = gamee.funarr1()
    array2 = gamee.funarr2()
    array3goul = gamee.funarr3()

    print("  -----  A* -----   ")
    s = State(array1, array2, array3goul, None)
    a_star = AStar(s)
    listpathstate, listvisitedstate, total_cost = a_star.moveAStar()

    for state in listpathstate:
        state.printS()
        print("/" * 20)

    print(f"Number of states in path: {len(listpathstate)}")
    print(f"Number of states visited: {len(listvisitedstate)}")
    print(f"Total cost: {total_cost}")
