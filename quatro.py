from bitarray import *
from bitarray.util import *
import base64

class Node:
    def __init__(self, board, exploration_code, output_class):
        self.board=board
        self.exploration_code=exploration_code
        self.output_class = output_class

    def encode(self):
        ret = bitarray()
        ret.extend(self.board)
        ret.extend(self.exploration_code)
        ret.extend(self.output_class)
        return ret

def encode_number(x):
    ret=bitarray()
    ret.encode({None:bitarray("00000"),
        0:bitarray("10000"),1:bitarray("10001"),2:bitarray("10010"),3:bitarray("10011"),
        4:bitarray("10100"),5:bitarray("10101"),6:bitarray("10110"),7:bitarray("10111"),
        8:bitarray("11000"),9:bitarray("11001"),10:bitarray("11010"),11:bitarray("11011"),
        12:bitarray("11100"),13:bitarray("11101"),14:bitarray("11110"),15:bitarray("11111")},[x])
    return ret


def decode_number(x):
    return x.decode({None:bitarray("00000"),
        0:bitarray("10000"),1:bitarray("10001"),2:bitarray("10010"),3:bitarray("10011"),
        4:bitarray("10100"),5:bitarray("10101"),6:bitarray("10110"),7:bitarray("10111"),
        8:bitarray("11000"),9:bitarray("11001"),10:bitarray("11010"),11:bitarray("11011"),
        12:bitarray("11100"),13:bitarray("11101"),14:bitarray("11110"),15:bitarray("11111")})[0]

def encode_other(x):
    ret=bitarray()
    ret.encode({0:bitarray("00"),1:bitarray("01"),2:bitarray("10"),3:bitarray("11")},[x])
    return ret

def decode_other(x):
    return x.decode({0:bitarray("00"),1:bitarray("01"),2:bitarray("10"),3:bitarray("11")},[0])

#def write_file(x, path):
#    f = open(path, "wb")
#    x.tofile(f)
#    f.close()

#def read_file(path):
#    f = open(path, "rb")
#    ret = bitarray()
#    ret.fromfile(f)
#    f.close()
#    return ret

def filename_encode(x):
    urlbytes = base64.urlsafe_b64encode(x)
    urlstring = str(urlbytes, "utf-8")
    return urlstring

def filename_decode(x):
    urlbytes = bytes(x, "utf-8")
    ret = base64.urlsafe_b64decode(urlbytes)
    return ret

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
        self.paths=((0,1,2,3),(4,5,6,7),(8,9,10,11),(12,13,14,15),(0,4,8,12),
                (1,5,9,13),(2,6,10,14),(3,7,11,15),(0,5,10,15),(3,6,9,12))
        # maps tuple of atrribute, value to pretty representation
        self.attribute_map = {(1,0):"hollow",(1,1):"solid",(2,0):"short",(2,1):"tall",
                (4,0):"square",(4,1):"round",(8,0):"dark",(8,1):"light"}
        # maps integer representation of piece to pretty representaion
        self.pretty_map = {None:"  ",0:" 0",1:" 1",2:" 2",3:" 3",4:" 4",5:" 5",6:" 6",7:" 7",
                8:" 8",9:" 9",10:"10",11:"11",12:"12",13:"13",14:"14",15:"15"}
        # all possible unique board permutations
        self.board_permutations=(
                {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11,12:12,13:13,14:14,15:15},
                {0:12,1:8,2:4,3:0,4:13,5:9,6:5,7:1,8:14,9:10,10:6,11:2,12:15,13:11,14:7,15:3},
                {0:15,1:14,2:13,3:12,4:11,5:10,6:9,7:8,8:7,9:6,10:5,11:4,12:3,13:2,14:1,15:0},
                {0:3,1:7,2:11,3:15,4:2,5:6,6:10,7:14,8:1,9:5,10:9,11:13,12:0,13:4,14:8,15:12},
                {0:12,1:13,2:14,3:15,4:8,5:9,6:10,7:11,8:4,9:5,10:6,11:7,12:0,13:1,14:2,15:3},
                {0:3,1:2,2:1,3:0,4:7,5:6,6:5,7:4,8:11,9:10,10:9,11:8,12:15,13:14,14:13,15:12},
                {0:15,1:11,2:7,3:3,4:14,5:10,6:6,7:2,8:13,9:9,10:5,11:1,12:12,13:8,14:4,15:0},
                {0:0,1:4,2:8,3:12,4:1,5:5,6:9,7:13,8:2,9:6,10:10,11:14,12:3,13:7,14:11,15:15})
        # all possible unique attribute possitions
        self.attribute_permutations=(
            (0,1,2,3),(0,1,3,2),(0,2,1,3),(0,2,3,1),(0,3,1,2),(0,3,2,1),(1,0,2,3),(1,0,3,2),
            (1,2,0,3),(1,2,3,0),(1,3,0,2),(1,3,2,0),(2,0,1,3),(2,0,3,1),(2,1,0,3),(2,1,3,0),
            (2,3,0,1),(2,3,1,0),(3,0,1,2),(3,0,2,1),(3,1,0,2),(3,1,2,0),(3,2,0,1),(3,2,1,0))

    def from_position(self, board, selection, white):
        self.board=board
        self.selection=selection
        self.white=white
    


    def from_bitarray(self, x):
        num=0
        for i in range(16):
            ii = 3+(5*i)
            y=decode_number(x[ii:ii+5])
            self.board[i]=y
            if(not y is None):
                num=num+1
        self.selection=decode_number(x[83:88])
        if(num%2==0):
            self.white=True
        else:
            self.white=False

    def to_bitarray(self):
        ret=bitarray("111")
        for i in range(16):
            ret.extend(encode_number(self.board[i]))
        ret.extend(encode_number(self.selection))
        return ret
        
    # place the selected piece, throws exception if invalid
    def place(self, square):
        if(self.check_square(square)):
            board=self.board.copy()
            board[square]=self.selection
            ret = Board()
            ret.from_position(board, None, self.white)
            return ret 
        else:
            raise Exception("illegal sqaure")

    # select a piece, change player's turn
    def select(self, piece):
        if(not self.selection is None):
            raise Exception("must place piece")
        if(self.check_piece(piece)):
            board=self.board.copy()
            ret = Board()
            ret.from_position(board, piece, not self.white)
            return ret 
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
        print("::"+self.pretty_map[self.selection])
        print("\u250c\u2500\u2500\u252c\u2500\u2500\u252c\u2500\u2500\u252c\u2500\u2500\u2510")
        print("\u2502"+self.pretty_map[self.board[12]]+"\u2502"+self.pretty_map[self.board[13]]+"\u2502"+self.pretty_map[self.board[14]]+"\u2502"+self.pretty_map[self.board[15]]+"\u2502")
        print("\u251c\u2500\u2500\u253c\u2500\u2500\u253c\u2500\u2500\u253c\u2500\u2500\u2524")
        print("\u2502"+self.pretty_map[self.board[8]]+"\u2502"+self.pretty_map[self.board[9]]+"\u2502"+self.pretty_map[self.board[10]]+"\u2502"+self.pretty_map[self.board[11]]+"\u2502")
        print("\u251c\u2500\u2500\u253c\u2500\u2500\u253c\u2500\u2500\u253c\u2500\u2500\u2524")
        print("\u2502"+self.pretty_map[self.board[4]]+"\u2502"+self.pretty_map[self.board[5]]+"\u2502"+self.pretty_map[self.board[6]]+"\u2502"+self.pretty_map[self.board[7]]+"\u2502")
        print("\u251c\u2500\u2500\u253c\u2500\u2500\u253c\u2500\u2500\u253c\u2500\u2500\u2524")
        print("\u2502"+self.pretty_map[self.board[0]]+"\u2502"+self.pretty_map[self.board[1]]+"\u2502"+self.pretty_map[self.board[2]]+"\u2502"+self.pretty_map[self.board[3]]+"\u2502")
        print("\u2514\u2500\u2500\u2534\u2500\u2500\u2534\u2500\u2500\u2534\u2500\u2500\u2518")


    # return true if two boards are equivalent
    def is_equivalent(self, other):
        for permutation in self.board_permutations:
            l1=[None]*16
            for i in range(16):
                l1[permutation[i]]=self.board[i]
            l2=[]
            l3=[]
            flag=False
            for i in range(16):
                if(l1[i] is None):
                    if(not other.board[i] is None):
                        flag=True
                        break
                else:
                    if(other.board[i] is None):
                        flag=True
                        break
                    else:
                       l2.append(l1[i])
                       l3.append(other.board[i])
            if(flag):
                continue
            if(not self.selection is None):
                l2.append(self.selection)
            if(not other.selection is None):
                l3.append(other.selection)
            for a in self.attribute_permutations:
                for b in range(16):
                    flag=True
                    for c in range(len(l2)):
                        number=l2[c]
                        number=number^b
                        zero=number&(pow(2,a[0]))>0
                        one=number&(pow(2,a[1]))>0
                        two=number&(pow(2,a[2]))>0
                        three=number&(pow(2,a[3]))>0
                        d=0
                        if(zero):
                            d+=1
                        if(one):
                            d+=2
                        if(two):
                            d+=4
                        if(three):
                            d+=8
                        number=d
                        if(not number==l3[c]):
                            flag=False
                            break
                    if(flag):
                        return True
        return False

    # return true if two boards are equivalent in their position
    # does not consider selections
    def is_equivalent_position(self, other):
        for permutation in self.board_permutations:
            l1=[None]*16
            for i in range(16):
                l1[permutation[i]]=self.board[i]
            flag=True
            for i in range(16):
                if(not l1[i]==other.board[i]):
                    flag=False
                    break
            if(flag):
                return True
        return False

    # return true if two boards are equivalent in their position
    # does consider selections
    def is_equivalent_attribute(self, other):
        l1=[]
        l2=[]
        if(not self.selection is None):
            l1.append(self.selection)
        if(not other.selection is None):
            l2.append(other.selection)
        for i in range(16):
            if(not self.board[i] is None):
                l1.append(self.board[i])
            if(not other.board[i] is None):
                l2.append(other.board[i])
        for a in self.attribute_permutations:
            for b in range(16):
                flag=True
                for c in range(len(l1)):
                    number=l1[c]
                    number=number^b
                    zero=number&(pow(2,a[0]))>0
                    one=number&(pow(2,a[1]))>0
                    two=number&(pow(2,a[2]))>0
                    three=number&(pow(2,a[3]))>0
                    d=0
                    if(zero):
                        d+=1
                    if(one):
                        d+=2
                    if(two):
                        d+=4
                    if(three):
                        d+=8
                    number=d
                    if(not number==l2[c]):
                        flag=False
                        break
                if(flag):
                    return True
        return False

def explore(iteration):
    white=True
    if(iteration%2==1):
        white=False
    
    # list of nodes currently in queue
    queue_prev=[]
    if(iteration is 0):
        # create start node
        board=Board()
        x=Node(board.to_bitarray(),encode_other(0),encode_other(0))
        queue_prev.append(x)
    else:
        # read queue of nodes from file
        queue_prev_path = "database/" + "{:02d}".format(iteration-1) + "_queue"
        queue_prev_file=open(queue_prev_path, "rb")
        while(True):
            x=queue_prev_file.read(12)
            if(x==b''):
                break
            y=bitarray()
            y.frombytes(x)
            z=Node(y[0:88],y[88:92],y[92:96])
            #yeah=Board()
            #yeah.from_bitarray(z.board)
            #yeah.print()
            queue_prev.append(z)
        queue_prev_file.close()

    
    # will contain all leaf nodes from each node on this depth
    queue_next=[]
    for node in queue_prev:
        # will contain all leaf nodes from the current node
        transitions=[]
        # step i: generate all placements, compare positions to remove duplicates
        current=Board()
        current.from_bitarray(node.board)
        moves=[]
        for i in range(16):
            if(current.check_square(i)):
                move=current.place(i)
                flag=True
                for other in moves:
                    if(move.is_equivalent_position(other)):
                        flag=False
                        break
                if(flag):
                    moves.append(move)
        # step ii: generate all selections, compare attributes to remove duplicates        
        for board in moves:
            moves_ii=[]
            for i in range(16):
                if(board.check_piece(i)):
                    move=board.select(i)
                    flag=True
                    for other in moves_ii:
                        if(move.is_equivalent_attribute(other)):
                            flag=False
                            break
                    if(flag):
                        moves_ii.append(move)
                        # determine wheter this leaf node is equivalent to another leaf node on the same depth 
                        x=Node(move.to_bitarray(),encode_other(0),encode_other(0))
                        equiv=None
                        for other in queue_next:
                            other_board = Board()
                            other_board.from_bitarray(other.board)
                            if(move.is_equivalent(other_board)):
                                equiv=other
                                break
                        if(equiv is None):
                            transitions.append(x)
                            queue_next.append(x)
                        else:
                            transitions.append(equiv)
        
        # write this node to file
        node_path="database/" + "{:02d}".format(iteration) + "/" + filename_encode(node.board.tobytes())
        node_file=open(node_path,"wb")
        node.encode().tofile(node_file)
        for transition in transitions:
            x=transition.encode()
            x.tofile(node_file)
        node_file.close()

    
    # write the queue of nodes to file
    queue_next_path = "database/" + "{:02d}".format(iteration) + "_queue"
    queue_next_file=open(queue_next_path,"wb")
    for node in queue_next:
        x = node.encode()
        x.tofile(queue_next_file)
    queue_next_file.close()

    print(len(queue_prev), "-->", len(queue_next))



#explore(0)
#explore(1)
explore(2)
