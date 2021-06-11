#!/usr/bin/python3.7

# for encoding games as base64 strings
import base64

# contains the logic for the game of quatro
class Board:
    
    # constructor
    def __init__(self):
        # array representing the 16 tiles
        self.board=[None]*16
        # the selected piece
        self.selection=None
        # the current player
        self.white=True
        # all possible ways to have pieces in a row
        self.paths=[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[0,4,8,12],
                [1,5,9,13],[2,6,10,14],[3,7,11,15],[0,5,10,15],[3,6,9,12]]
        # maps tuple of atrribute, value to pretty representation
        self.attribute_map = {(1,0):"hollow",(1,1):"solid",(2,0):"short",(2,1):"tall",
                (4,0):"square",(4,1):"round",(8,0):"dark",(8,1):"light"}
        # maps integer representation of piece to pretty representaion
        self.pretty_map = {None:"  ",0:" 0",1:" 1",2:" 2",3:" 3",4:" 4",5:" 5",6:" 6",7:" 7",
                8:" 8",9:" 9",10:"10",11:"11",12:"12",13:"13",14:"14",15:"15"}
        # all possible unique board permutations
        self.board_permutations=[
                {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11,12:12,13:13,14:14,15:15},
                {0:12,1:8,2:4,3:0,4:13,5:9,6:5,7:1,8:14,9:10,10:6,11:2,12:15,13:11,14:7,15:3},
                {0:15,1:14,2:13,3:12,4:11,5:10,6:9,7:8,8:7,9:6,10:5,11:4,12:3,13:2,14:1,15:0},
                {0:3,1:7,2:11,3:15,4:2,5:6,6:10,7:14,8:1,9:5,10:9,11:13,12:0,13:4,14:8,15:12},
                {0:12,1:13,2:14,3:15,4:8,5:9,6:10,7:11,8:4,9:5,10:6,11:7,12:0,13:1,14:2,15:3},
                {0:3,1:2,2:1,3:0,4:7,5:6,6:5,7:4,8:11,9:10,10:9,11:8,12:15,13:14,14:13,15:12},
                {0:15,1:11,2:7,3:3,4:14,5:10,6:6,7:2,8:13,9:9,10:5,11:1,12:12,13:8,14:4,15:0},
                {0:0,1:4,2:8,3:12,4:1,5:5,6:9,7:13,8:2,9:6,10:10,11:14,12:3,13:7,14:11,15:15}]
        # all possible unique attribute possitions
        self.attribute_permutations=[
            (0,1,2,3),(0,1,3,2),(0,2,1,3),(0,2,3,1),(0,3,1,2),(0,3,2,1),(1,0,2,3),(1,0,3,2),
            (1,2,0,3),(1,2,3,0),(1,3,0,2),(1,3,2,0),(2,0,1,3),(2,0,3,1),(2,1,0,3),(2,1,3,0),
            (2,3,0,1),(2,3,1,0),(3,0,1,2),(3,0,2,1),(3,1,0,2),(3,1,2,0),(3,2,0,1),(3,2,1,0)]
    
    def are_equivalent(self, other):
        return False

    def from_notation(self, note):
        return False

    # place the selected piece, throws exception if invalid
    def place(self, square):
        if(self.check_square(square)):
            self.board[square]=self.selection
            self.selection = None
        else:
            raise Exception("illegal sqaure")

    # select a piece, change player's turn
    def select(self, piece):
        if(not self.selection is None):
            raise Exception("must place piece")
        if(self.check_piece(piece)):
            self.selection=piece
            self.white = not self.white
        else:
            raise Exception("illegal selection")

    # return true if piece has not yet been placed
    def check_piece(self, piece):
        if(piece<0 or piece>15):
            return False
        for i in range(16):
            if(piece==self.board[i]):
                return False
        return True

    # return true if square is unoccupied
    def check_square(self, square):
        if(self.board[square]!=None):
            return False
        if(square<0 or square>15):
            return False
        return True

    # determine wheter the last move caused the position to be a win
    def check(self):
        flag=False
        for path in self.paths:
            a = self.board[path[0]]
            b = self.board[path[1]]
            c = self.board[path[2]]
            d = self.board[path[3]]
            if(a==None or b==None or c==None or d==None):
                continue
            for x in [1,2,4,8]:
                aa = a&x
                bb = b&x
                cc = c&x
                dd = d&x
                if(aa==bb and aa==cc and aa==dd):
                    flag=True
        return flag

    # pretty print the board to the console
    def print(self):
        print("\u250c\u2500\u2500\u252c\u2500\u2500\u252c\u2500\u2500\u252c\u2500\u2500\u2510")
        print("\u2502"+self.pretty_map[self.board[12]]+"\u2502"+self.pretty_map[self.board[13]]+"\u2502"+self.pretty_map[self.board[14]]+"\u2502"+self.pretty_map[self.board[15]]+"\u2502")
        print("\u251c\u2500\u2500\u253c\u2500\u2500\u253c\u2500\u2500\u253c\u2500\u2500\u2524")
        print("\u2502"+self.pretty_map[self.board[8]]+"\u2502"+self.pretty_map[self.board[9]]+"\u2502"+self.pretty_map[self.board[10]]+"\u2502"+self.pretty_map[self.board[11]]+"\u2502")
        print("\u251c\u2500\u2500\u253c\u2500\u2500\u253c\u2500\u2500\u253c\u2500\u2500\u2524")
        print("\u2502"+self.pretty_map[self.board[4]]+"\u2502"+self.pretty_map[self.board[5]]+"\u2502"+self.pretty_map[self.board[6]]+"\u2502"+self.pretty_map[self.board[7]]+"\u2502")
        print("\u251c\u2500\u2500\u253c\u2500\u2500\u253c\u2500\u2500\u253c\u2500\u2500\u2524")
        print("\u2502"+self.pretty_map[self.board[0]]+"\u2502"+self.pretty_map[self.board[1]]+"\u2502"+self.pretty_map[self.board[2]]+"\u2502"+self.pretty_map[self.board[3]]+"\u2502")
        print("\u2514\u2500\u2500\u2534\u2500\u2500\u2534\u2500\u2500\u2534\u2500\u2500\u2518")

# interactive game between two human players
class Game:

    # constructor
    def __init__(self):
        # notation
        self.note=""
        # the board
        self.board=Board()


    def from_notation(self, note):
        self.note=note
        self.board=self.board.from_notation(note)

    def select_piece_interactive(self):
                    piece=int(input("select piece:\t"))
                    while(not self.board.check_piece(piece)):
                        piece=int(input("illegal selction\nselect piece:\t"))
                    self.board.select(piece)
                    self.append_notation(piece)
    
    def select_square_interactive(self):
                    square=int(input("select square:\t"))
                    while(not self.board.check_square(square)):
                        square=int(input("illegal selction\nselect square:\t"))
                    self.board.place(square)
                    self.append_notation(square)
    
    #def select_piece(self, piece):
    #                if(self.board.check_piece(piece)):
    #                    self.board.select(piece)
    #                self.append_notation(piece)
    #                    return
    #                self.append_notation(piece)
    
    #def select_square_interactive(self):
    #                square=int(input("select square:\t"))
    #                while(not self.board.check_square(square)):
    #                    square=int(input("illegal selction\nselect square:\t"))
    #                self.board.place(square)
    #                self.append_notation(square)

    def play(self):
        self.board.print()
        while True:
            if(self.white):
                print("white has the move")
                if(self.select):
                    # white select piece
                    self.select_piece()
                    self.select=not self.select
                    self.white=not self.white
                else:
                    # white place piece
                    self.select_square()
                    self.board.print()
                    if(self.board.check()):
                        print("win for white")
                        break
                    self.select=not self.select
            else:
                print("black has the move")
                if(self.select):
                    # black select piece
                    self.select_piece()
                    self.select=not self.select
                    self.white=not self.white
                else:
                    # black place piece
                    self.select_square()
                    self.board.print()
                    if(self.board.check()):
                        print("win for black")
                        break
                    self.select=not self.select


    def turn(self, square, piece):
        move = self.note
        if(not self.note==""):
            #logic for placing piece here
            return None
        # logic for selecting piece here
        if(self.board.check_piece(piece)):
            return move + "{:x}".format(piece)
        else:
            return None








    
def generate(stage):
    if(stage==0):
        root = Game()
        path = "database/" "{:02d}".format(stage) + "/" + filename_encode(root.note) + ".txt"
        print("opening path " + path)
        f = open(path, "w")
        f.write("u")
        for i in range(16):
            node = root.turn(None, i)
            if(not node is None):
                print(i)
                print(node)
                print(filename_encode(node))
                print()
                f.write("\n" + filename_encode(node)+ "\nu")
        f.close()

def filename_encode(x):
    if(x==""):
        return "===="
    flag=False
    if(len(x)%2==1):
        flag=True
    if(flag):
        x = "0" + x
    _bytes = bytes.fromhex(x)
    urlbytes = base64.urlsafe_b64encode(_bytes)
    urlstring = str(urlbytes, "utf-8")
    return urlstring

def filename_decode(x):
    urlbytes = bytes(x, "utf-8")
    _bytes = base64.urlsafe_b64decode(urlbytes)
    hexstring = _bytes.hex()
    return hexstring

        

#game = Game()
#game.play()

generate(0)
#print(filename_decode(filename_encode("")))

