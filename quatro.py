#!/usr/bin/python3.7

class Board:
    
    def __init__(self):
        self.board=[None]*16
        self.paths=[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[0,4,8,12],[1,5,9,13],[2,6,10,14],[3,7,11,15],[0,5,10,15],[3,6,9,12]]
        self.map = {(1,0):"hollow",(1,1):"solid",(2,0):"short",(2,1):"tall",(4,0):"square",(4,1):"round",(8,0):"dark",(8,1):"light"}
        self.pretty = {None:"  ",0:" 0",1:" 1",2:" 2",3:" 3",4:" 4",5:" 5",6:" 6",7:" 7",8:" 8",9:" 9",10:"10",11:"11",12:"12",13:"13",14:"14",15:"15"}
        
    def place(self, piece, square):
        if(self.board[square]!=None):
            raise Exception("square is already occupied")
        if(piece<0 or piece>15):
            raise Exception("invalid piece")
        if(square<0 or square>15):
            raise Exception("invalid square")
        for i in range(16):
            if(piece==self.board[i]):
                raise Exception("piece already in use")
        self.board[square]=piece

    def check_piece(self, piece):
        if(piece<0 or piece>15):
            return False
        for i in range(16):
            if(piece==self.board[i]):
                return False
        return True

    def check_square(self, square):
        if(self.board[square]!=None):
            return False
        if(square<0 or square>15):
            return False
        return True

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
                    y=0
                    if(aa!=0):
                        y=1
                    flag=True
                    print("the pieces are:", [a,b,c,d])
                    pte
                    print("the squares are:", path)
                    attribute=self.map[(x,y)]
                    print("the attribute is:", attribute)
        return flag

    def print(self):
        print("\u250c\u2500\u2500\u252c\u2500\u2500\u252c\u2500\u2500\u252c\u2500\u2500\u2510")
        print("\u2502"+self.pretty[self.board[12]]+"\u2502"+self.pretty[self.board[13]]+"\u2502"+self.pretty[self.board[14]]+"\u2502"+self.pretty[self.board[15]]+"\u2502")
        print("\u251c\u2500\u2500\u253c\u2500\u2500\u253c\u2500\u2500\u253c\u2500\u2500\u2524")
        print("\u2502"+self.pretty[self.board[8]]+"\u2502"+self.pretty[self.board[9]]+"\u2502"+self.pretty[self.board[10]]+"\u2502"+self.pretty[self.board[11]]+"\u2502")
        print("\u251c\u2500\u2500\u253c\u2500\u2500\u253c\u2500\u2500\u253c\u2500\u2500\u2524")
        print("\u2502"+self.pretty[self.board[4]]+"\u2502"+self.pretty[self.board[5]]+"\u2502"+self.pretty[self.board[6]]+"\u2502"+self.pretty[self.board[7]]+"\u2502")
        print("\u251c\u2500\u2500\u253c\u2500\u2500\u253c\u2500\u2500\u253c\u2500\u2500\u2524")
        print("\u2502"+self.pretty[self.board[0]]+"\u2502"+self.pretty[self.board[1]]+"\u2502"+self.pretty[self.board[2]]+"\u2502"+self.pretty[self.board[3]]+"\u2502")
        print("\u2514\u2500\u2500\u2534\u2500\u2500\u2534\u2500\u2500\u2534\u2500\u2500\u2518")

    #def toPiece(self, x):
        #if(x<0 or x>15):
            #raise Exception("x is not a valid integer")
        
        
#board = Board()
#board.place(0,0)
#board.place(1,1)
#board.place(2,2)
#board.place(11,3)
#print(board.check())


class Game:

    def __init__(self):
        self.note=""
        self.white=True
        self.select=True
        self.selection=None
        self.board=Board()

    def select_piece(self):
                    piece=int(input("select piece:\t"))
                    while(not self.board.check_piece(piece)):
                        piece=int(input("illegal selction\nselect piece:\t"))
                    self.selection=piece
    
    def select_square(self):
                    square=int(input("select square:\t"))
                    while(not self.board.check_square(square)):
                        square=int(input("illegal selction\nselect square:\t"))
                    self.board.place(self.selection, square)

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

a={0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11,12:12,13:13,14:14,15:15}

a={0:,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11,12:12,13:13,14:14,15:15}
a={0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11,12:12,13:13,14:14,15:15}
a={0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11,12:12,13:13,14:14,15:15}
a={0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11,12:12,13:13,14:14,15:15}







game = Game()
game.play()



