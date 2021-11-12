# -*- coding: utf-8 -*-
"""MiniMaxMidgameEndgameBlack.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FfLto4uXeEANOFZF8Sdo9u7NDOS7eo6c
"""

import sys

#@title MAIN
#take command line arguments
if(len(sys.argv) != 4) :
    print(sys.argv[0], ": takes 3 arguments, not ", len(sys.argv)-1, ".")
    print("Expecting arguments: inputposition.txt outputposition.txt depth??.")
    sys.exit()

inputposition = str(sys.argv[1])
outputposition = str(sys.argv[2])
depth = int(sys.argv[3])

f = open(inputposition, 'r+')
inputposition= f.read()
f.close()


inputposition= [token for token in inputposition]
print('inputposition:', inputposition)
print('outputposition:', outputposition)
print('depth:', depth)

#@title NEIGHBORS
def neighbors(position):
  if (position == 0):
    return [1,2,6]
  elif (position == 1):
    return [0,11]
  elif (position == 2):
    return [3,4,7]
  elif (position == 3):
    return [2,10]
  elif (position == 4):
    return [2,5,12]
  elif (position == 5):
    return [4,9]
  elif (position == 6):
    return [0, 7,18]
  elif (position == 7):
    return [2,6,8,15]
  elif (position == 8):
    return [4,7,12]
  elif (position == 9):
    return [5,10,14]
  elif (position == 10):
    return [3,9,11,17]
  elif (position == 11):
    return [1,10,20]
  elif (position == 12):
    return [8,13]
  elif (position == 13):
    return [12,14,16]
  elif (position == 14):
    return [9,13]
  elif (position == 15):
    return [7,16]
  elif (position == 16):
    return [13,15,17,19]
  elif (position == 17):
    return [10,16]
  elif (position == 18):
    return [6,19]
  elif (position == 19):
    return [16,18,20]
  elif (position == 20):
    return [11,19]
  else:
    return [-1]

#@title CLOSEMILL
def closeMill(position, board):
  true=1
  false=0
  error=-1

  C= board[position]
  if (C == 'x'):
    return -1
  
  if (position == 0):
    if (board[6] == C and board[18] == C) or (board[2]==C and board[4]==C):
      return true
    return false

  elif (position == 1):
    if (board[11] == C and board[20] == C):
      return true
    return false

  elif (position == 2):
    if (board[0] == C and board[4] == C) or (board[7]==C and board[15]==C):
      return true
    return false

  elif (position == 3):
    if (board[10] == C and board[17] == C):
      return true
    return false

  elif (position == 4):
    if (board[2] == C and board[0] == C) or (board[7]==C and board[15]==C):
      return true
    return false

  elif (position == 5):
    if (board[9] == C and board[14] == C):
      return true
    return false

  elif (position == 6):
    if (board[7] == C and board[8] == C) or (board[0]==C and board[18]==C):
      return true
    return false
  
  elif (position == 7):
    if (board[6] == C and board[8] == C) or (board[2]==C and board[15]==C):
      return true
    return false
  
  elif (position == 8):
    if (board[6] == C and board[7] == C) or (board[4]==C and board[12]==C):
      return true
    return false

  elif (position == 9):
    if (board[10] == C and board[11] == C) or (board[5]==C and board[14]==C):
      return true
    return false

  elif (position == 10):
    if (board[9] == C and board[11] == C) or (board[3]==C and board[17]==C):
      return true
    return false

  elif (position == 11):
    if (board[9] == C and board[10] == C) or (board[1]==C and board[20]==C):
      return true
    return false

  elif (position == 12):
    if (board[4] == C and board[8] == C) or (board[13]==C and board[14]==C):
      return true
    return false

  elif (position == 13):
    if (board[16] == C and board[19] == C) or (board[12]==C and board[14]==C):
      return true
    return false

  elif (position == 14):
    if (board[3] == C and board[10] == C) or (board[12]==C and board[13]==C):
      return true
    return false

  elif (position == 15):
    if (board[2] == C and board[7] == C) or (board[16]==C and board[17]==C):
      return true
    return false

  elif (position == 16):
    if (board[13] == C and board[19] == C) or (board[15]==C and board[17]==C):
      return true
    return false

  elif (position == 17):
    if (board[3] == C and board[10] == C) or (board[15]==C and board[16]==C):
      return true
    return false

  elif (position == 18):
    if (board[6] == C and board[0] == C) or (board[19]==C and board[20]==C):
      return true
    return false

  elif (position == 19):
    if (board[13] == C and board[16] == C) or (board[18]==C and board[20]==C):
      return true
    return false

  elif (position == 20):
    if (board[1] == C and board[11] == C) or (board[18]==C and board[19]==C):
      return true
    return false

  else:
    return -1

#@title PRINTPICTUREBOARD
def printpictureboard(board): #purely for debugging\
  print("a\t b\t c\t d\t e\t f\t g\t")
  print(f"{board[18]}________________________{board[19]}____________________________{board[20]}")
  print(f"|                          |                        |")
  print(f"|                          |                        |")
  print(f"|                          |                        |")
  print(f"|               {board[15]}______   {board[16]} _________{board[17]}        |" )
  print(f"|               |          |          |              |")
  print(f"|               |          |          |              |")
  print(f"|               |     {board[12]} ___{board[13]}  {board[14]} |              |")
  print(f"|               |     |         |    |              |")
  print(f"|{board[6]}__________ {board[7]}________|{board[8]}       |{board[9]}____{board[10]}____________ |{board[11]}")
  print(f"|               |     |         |    |              |")
  print(f"|               |     |{board[4]} _______{board[5]}|              |")
  print(f"|               |    /               |              |")
  print(f"|               |  /                 |              |")
  print(f"|               |{board[2]}___________________{board[3]}|              |")
  print(f"|             /                                     |")
  print(f"|         /                                         |")
  print(f"|      /                                            |")
  print(f"|   /                                               |")
  print(f"|{board[0]}/__________________________________________________{board[1]} ")  

  return

def flipBoard(board):
  newboard=board
  for i in range(0, len(newboard)):
    if (newboard[i] == 'B'):
      newboard[i] = 'W'
    elif (newboard[i] == 'W'):
      newboard[i] = 'B'
  return board

def takecount(board, token):
  count=0
  for i in board:
    if (i == token):
      count += 1
  return count

#@title GENERATEHOPPING
def GenerateHopping(board):
  newboards=[]
  newboard=[]

  for i in range(len(board)):
    newboard= board.copy()
    
    if (board[i] == 'W'): #the current index of the hopping piece
      for j in range(len(board)):
        if (board[j] == 'x'): #the location it will hop to
          newboard=board
          newboard[j] == 'W'
          newboard[i] == 'x'
          newboards.append(newboard)
  return newboards

#@title GENERATEREMOVE
def GenerateRemove(board):
  newboards= []
  newboard= []

  for i in range(len(board)):
    newboard= board.copy()

    if (newboard[i] == 'B'):
      if (not (closeMill(i, newboard) )  ):
        newboard[i] = 'x'
        newboards.append(newboard)
  
  if (len(newboards) ==0): #i.e nothing can be removed.
    print("Nothing can be removed!")
    return newboards
  return newboards

#@title GENERATEMOVE
def GenerateMove(board):
  newboards=[]
  newboard=[]

  for i in range(len(board)): #index of the pawn being moved
    newboard= board.copy()
    adjacents= []

    if (board[i] == 'W'):
      adjacents= neighbors(i) #an array of adjacent spots, regardless of position
      #print("ADJACENTS OF", i,":", adjacents)
      for j in adjacents: #the location it will move to
        #print(i,j)
        if (board[j] == 'x'):
          print("MOVE FOUND", i, j)
          newboard[j] = 'W'
          newboard[i]= 'x'
          if (closeMill(j, newboard)):
            print("Calling GENREMOVE!")
            morepositions= GenerateRemove(newboard)
            for position in morepositions:
              newboards.append(position)
          else:
            newboards.append(newboard)
  return newboards

def GenerateMovesMidgameEndgame(board):
  if (takecount(board, "W") == 3):
    return GenerateHopping(board)
  else:
    return GenerateMove(board)

def StaticEstimationMidgameEndgame(board):
  numwhitepieces= takecount(board, 'W')
  numblackpieces= takecount(board, 'B')

  flipped= flipBoard(board.copy())
  opponentmoves= GenerateMove(flipped)
  if (numwhitepieces <= 2):
    return -10000
  elif (numblackpieces <= 2):
    return 10000
  if (len(opponentmoves) == 0):
    return 10000
  else:
    return (1000 * (numwhitepieces - numblackpieces) - len(opponentmoves))

def printboard(board):
  retstring=""
  for i in board:
    retstring += i
  return retstring

globalcounter=0 #this counts how many times minimax was called
globalerror=0

#@title MINIMAXMIDGAMENDGAME
def miniMaxMidgameEndgame(tree, maxdepth, isMaximizing, currentdepth):
  global globalcounter
  globalcounter += 1
  print("Examining position: ", tree.position, "at depth", currentdepth)
  if (currentdepth == maxdepth):
    staticeval= StaticEstimationMidgameEndgame(tree.position)
    tree.evaluation= staticeval
    print("LEAF NODE WITH EVAL", staticeval)
    return staticeval
  else:
    #two cases: maximizing or not
    if (not (isMaximizing)):
      blackside= []
      blackside= flipBoard(tree.position.copy())
      L= GenerateMove(blackside)
      #PHASE 1: BUILD TREE
      for m in L:
        print("M:", m)
        m= flipBoard(m)
        print("M:", m)
        newnode= Tree([], m, 0)
        print("Child found: ", newnode.position)
        tree.children.append(newnode)

      #PHASE 2: EVALUATE TREE
      L_evals=[]
      for child in tree.children:
        L_evals.append(miniMaxMidgameEndgame(child, maxdepth, not (isMaximizing), currentdepth + 1))
      tree.evaluation = min(L_evals)

    if (isMaximizing):
      L= GenerateMove(tree.position)
      #create a new tree node for every node in L and append it to the current tree nodes children.
      #PHASE 1: BUILD TREE
      for m in L:
        print("M:", m)
        newnode= Tree([], m, 0)
        print("Child found: ", newnode.position)
        tree.children.append(newnode)

      #PHASE 2: EVALUATE TREE
      L_evals=[]
      for child in tree.children:
        L_evals.append(miniMaxMidgameEndgame(child, maxdepth, not (isMaximizing), currentdepth + 1))
      tree.evaluation = max(L_evals)
      
  return tree.evaluation

class Tree:
  def __init__(self, children=[], position=[], evaluation=-69):
      self.children=children #an array of Tree objects
      self.position=position #char array
      self.evaluation=evaluation

root= Tree([], inputposition, depth)

evals=miniMaxMidgameEndgame(root, depth, False, 0) #tree, max, ismax, curr
print("EVALUATION:", root.evaluation, "AFTER CALLING MINIMAX", globalcounter,"TIMES")
runningbest= -999999
bestposition= []
for e in root.children:
  print(e.position, e.evaluation)
  if (e.evaluation > runningbest):
    runningbest= e.evaluation
    bestposition= (e.position).copy()

print("BEST POSITION: ", bestposition)

f = open(outputposition, "a")
f.write("".join(bestposition))
f.close()