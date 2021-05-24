#!/usr/bin/python3.7

class Board:
    
    def __init__(self):
        self.board=[None]*16
        self.paths=[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[0,4,8,12],[1,5,9,13],[2,6,10,14],[3,7,11,15],[0,5,10,15],[3,6,9,12]]
        self.map = {(1,0):"hollow",(1,1):"solid",(2,0):"short",(2,1):"tall",(4,0):"square",(4,1):"round",(8,0):"dark",(8,1):"light"}
        
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
                    print("the pieces are:", [a,b,c,d])
                    print("the squares are:", path)
                    attribute=self.map[(x,aa)]
                    print("the attribute is:", attribute)
        return flag





    def toPiece(self, x):
        if(x<0 or x>15):
            raise Exception("x is not a valid integer")
        
        
board = Board()
board.place(0,0)
board.place(1,1)
board.place(2,2)
board.place(11,3)
print(board.check())



