# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 11:17:29 2023

@author: Janin
"""
import time

class Puissance:
    
    def __init__(self, board=None, player="R"): #player jaune J ou rouge R
        """this is a state of the game: board configuration plus player's turn"""
        if board is None:
            self.board = [[' ' for i in range(12)] for j in range(6)] #12 colonnes 6 lignes
        else:
            self.board = board
        self.player = player
    
    def Print_Board(self):
        for i in range(6):
            print(self.board[i]) #print chaque ligne sur une ligne
            print()
        print()
        if not self.Terminal():
             print("Next player:", self.player)

        
    def Actions(self):
        """self is the state of the board which is a 6x12 matrix along with which player's turn it is
        returns the possible actions to take so possible spots --> liste of columns that can be filled"""
        return [column for column in range(12)  if self.board[0][column]==" "] #its enough to check wether first row is empty to know that this action is possible
        
    def Result(self,a):
        """a is a column, we implement the action a on self, so we "drop" pin until not empty case"""
        board_res=[row[:] for row in self.board]
        for row in range(5,-1,-1): #on parcourt a l'envers jusqu'a premiere case vide
            if board_res[row][a]==" ":
                board_res[row][a]=self.player
                break
        return Puissance(board_res,"R" if self.player=="J" else "J") #returns the new state with the next's player's turn
                
    def Terminal(self):
        """ returns true if somoene won or if the board is full, False if not (no need to check wether pions available this will be managed in gameplay code"""
        #rows
        for row in range(6):       
            for i in range(9):
                if self.board[row][i]!=' ' and self.board[row][i]==self.board[row][i+1] and self.board[row][i+1]==self.board[row][i+2] and self.board[row][i+2]==self.board[row][i+3]:
                    return True
        #columns
        for column in range(12):   
            for i in range(3):
                if self.board[i][column]!=' ' and self.board[i][column]==self.board[i+1][column] and self.board[i+1][column]==self.board[i+2][column] and self.board[i+2][column]==self.board[i+3][column]:
                    return True
                
        #diagonals left to right
        for i in range(3):        
            for j in range(9):
                if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3] != " ":
                    return True
                
        #diagonals right to left
        for i in range(3):         
            for j in range(3, 12):
                if self.board[i][j] == self.board[i + 1][j - 1] == self.board[i + 2][j - 2] == self.board[i + 3][j - 3] != " ":
                    return True
    
        return not any(' ' in row for row in self.board) #if space then return false if full returns true cause end game


    def Utility(self):
        """return 1 if R wins, -1 if he loses and 0 if its a tie"""
        #res=0
        #rows
        for row in range(6):       
            for i in range(9):
                if self.board[row][i]!=' ' and self.board[row][i]==self.board[row][i+1] and self.board[row][i+1]==self.board[row][i+2] and self.board[row][i+2]==self.board[row][i+3]:
                    if self.board[row][i]=="R":
                        return 1
                    else:
                        return -1
        #columns
        for column in range(12):   
            for i in range(3):
                if self.board[i][column]!=' ' and self.board[i][column]==self.board[i+1][column] and self.board[i+1][column]==self.board[i+2][column] and self.board[i+2][column]==self.board[i+3][column]:
                    if self.board[i][column]=="R":
                        return 1
                    else:
                        return -1
                
        #diagonal left to right
        for i in range(3):        
            for j in range(9):
                if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3] != " ":
                    if self.board[i][j]=="R":
                        return 1
                    else:
                        return -1
                
        #diagonal right to left
        for i in range(3):         
            for j in range(3, 12):
                if self.board[i][j] == self.board[i + 1][j - 1] == self.board[i + 2][j - 2] == self.board[i + 3][j - 3] != " ":
                    if self.board[i][j]=="R":
                        return 1
                    else:
                        return -1
        return 0

    
def minimax(state, alpha, beta, depth):
    if depth == 0 or state.Terminal():
        return None, heuristic_evaluation(state)

    if state.player == "R":
        max_eval = -float('inf')
        best_action = None

        for action in sorted(state.Actions(), key=lambda a: heuristic_sort(a, state)):
            new_state = state.Result(action)
            _, eval = minimax(new_state, alpha, beta, depth - 1)

            if eval > max_eval:
                max_eval = eval
                best_action = action

            alpha = max(alpha, eval)
            if beta <= alpha:
                break

        return best_action, max_eval

    else:
        min_eval = float('inf')
        best_action = None

        for action in sorted(state.Actions(), key=lambda a: heuristic_sort(a, state)):
            new_state = state.Result(action)
            _, eval = minimax(new_state, alpha, beta, depth - 1)

            if eval < min_eval:
                min_eval = eval
                best_action = action

            beta = min(beta, eval)
            if beta <= alpha:
                break

        return best_action, min_eval
    

def heuristic_sort(action, state):
    # Simple heuristic for sorting columns
    # Prioritize the center columns
    center_column = abs(action - 5)
    return -abs(center_column - 5)

def heuristic_evaluation(state):
    """returns a higher score for a state that has to be more prioritized by checkinig and analyzing windows of for spots in a row"""
    score = 0

    # Check horizontal configurations
    for row in range(6):
        for col in range(9):
            window = [state.board[row][col + i] for i in range(4)]
            score += evaluate_window(window)

    # Check vertical configurations
    for col in range(12):
        for row in range(3):
            window = [state.board[row + i][col] for i in range(4)]
            score += evaluate_window(window)

    # Check diagonal (left to right) configurations
    for row in range(3):
        for col in range(9):
            window = [state.board[row + i][col + i] for i in range(4)]
            score += evaluate_window(window)

    # Check diagonal (right to left) configurations
    for row in range(3):
        for col in range(3, 12):
            window = [state.board[row + i][col - i] for i in range(4)]
            score += evaluate_window(window)

    return score

def evaluate_window(window):
    """attributes a score for a window of 4 spots, the more in a row the more the score has impact (+ or -)"""
    player_count = window.count("R")
    opponent_count = window.count("J")

    if player_count == 4:
        return 100  # Winning configuration for the AI
    elif opponent_count == 4:
        return -100  # Winning configuration for the opponent
    elif player_count == 3 and window.count(" ") == 1:
        return 5  # AI has three in a row with an empty space
    elif opponent_count == 3 and window.count(" ") == 1:
        return -5  # Opponent has three in a row with an empty space
    elif player_count == 2 and window.count(" ") == 2:
        return 2  # AI has two in a row with two empty spaces
    elif opponent_count == 2 and window.count(" ") == 2:
        return -2  # Opponent has two in a row with two empty spaces
    else:
        return 0  # No significant configuration

    
def GamePlay():
    
    #setup de la partie
    First_Player=input("Quelle joueur commence? (R pour IA, J pour autre):  ")
    while First_Player!="R" and First_Player!="J":
        First_Player=input("ERREUR!\nChoisir R pour IA, J pour autre:  ")
    state=Puissance(None,First_Player)
    state.Print_Board()
    total_ai_time=0
    
    #lancement de la partie avec 21 tours maximum pour chaque joueur
    if First_Player=="R":
        for tour in range(21):
            if not state.Terminal():
                #AI's turn: "R"
                start=time.time()
                action,_=minimax(state, -float('inf'), float('inf'), 5)
                state=state.Result(action)
                state.Print_Board()
                end=time.time()
                print("AI took this much time:", end - start)
                print("AI played:", action)
                total_ai_time+=(end-start)

            
            if not state.Terminal():   
                #Player's turn: "J"
                action=int(input("choisi une colonne de ton choix (index. 0 a 11):  "))
                state=state.Result(action)
                state.Print_Board()
            
            else:
                break
    if First_Player=="J":
        for tour in range(21):
            
            if not state.Terminal():   
                #Player's turn: "J"
                action=int(input("choisi une colonne de ton choix (index. 0 a 11):  "))
                state=state.Result(action)
                state.Print_Board()
                
            if not state.Terminal():
                 #AI's turn: "R"
                start=time.time()
                action,_=minimax(state, -float('inf'), float('inf'),5)
                state=state.Result(action)
                state.Print_Board()
                end=time.time()
                print("AI took this much time:", end - start)
                print("AI played:", action)
                total_ai_time+=(end-start)

            
            else:
                break
            
    #fin de la partie
    res=state.Utility()
    if res==1:
        print("I WIN !")
    elif res==-1:
        print("YOU WIN !")
    else:
        print("ITS A TIE !")
        
    print("total AI play time: ", total_ai_time)
