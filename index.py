from queue import Full
import numpy as py 
from colorama import Fore, Back, Style, init
from state import *
from game import *
from tkinter import *
from tkinter import simpledialog, messagebox
from dfs import *

class player:
   def __init__(self,array1,array2,arraygoal):
    #   self.master=master
      self.arr1=array1
      self.arr2=array2
      self.arrgoal=array3goul
      self.initstate=State(array1,array2,array3goul,None)
      
   def move_player(self):
      new_state=self.initstate
      new_state.printS()
      while (not new_state.chickGoal()):
            inp=input("enter 1 or 2 or 3 or 4: ")
            inp=int(inp)
            new_state=new_state.move(inp)
            new_state.printS()
            # print("-- his perent --")
            # print(new_state.getperent().printS())
            # print("*"*20)
      if(new_state.chickGoal):
          print("SUCCESS")
            # messagebox.showinfo("تهانينا!", "Success")
            
      
# start application
if __name__ == "__main__": 
    gamee=game(2)
    array1=gamee.funarr1()
    array2=gamee.funarr2()
    array3goul=gamee.funarr3()
    print("/"*30)
    # s=State(array1,array2,array3goul,None)
    # d=DFS(s)
    
    # listpathstate=d.moveDFS()
    # for state in listpathstate:
    #     state.printS()
    
    player1=player(array1,array2,array3goul)
    player1.move_player()
    # root.mainloop()

           



