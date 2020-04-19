from tkinter import * 
import random
import itertools
import collections
import time

class Node:

    def __init__(self, puzzle, parent=None, action=None):
        self.puzzle = puzzle
        self.parent = parent
        self.action = action

    @property
    def state(self):
        return str(self)

    @property 
    def path(self):
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)

    @property
    def solved(self):
        return self.puzzle.solved

    @property
    def actions(self):
        return self.puzzle.actions

    def __str__(self):
        return str(self.puzzle)

class Solver:

    def __init__(self, start):
        self.start = start

    def solve(self):
        print("Recherche de solution")
        global j
        queue = collections.deque([Node(self.start)])
        seen  = set()
        seen.add(queue[0].state)
        while queue:
            node = queue.pop()
            if node.solved:
            	z= list(node.path)
            	self.aff5(z)
            	print("solution trouvée en", len(z) , " coups")
            	break
            for move, action in node.actions:
                child = Node(move(), node, action)             
                if child.state not in seen:
                    queue.appendleft(child)
                    seen.add(child.state)

    def solve_Long(self):
        global j
        print("Recherche de solution 2")
        queue = collections.deque([Node(self.start)])
        seen  = set()
        seen.add(queue[0].state)
        while queue:
            node = queue.pop()
            if node.solved:
            	z= list(node.path)
            	self.aff5(z)
            	print("solution trouvée en", len(z) , " coups")
            	break
            for move, action in node.actions:
                child = Node(move(), node, action)
                if child.state not in seen:
                    queue.append(child)
                    seen.add(child.state)
        
    def aff5(self , p , i=1):
    	node = p[0]
    	p=p[1:]
    	x=node.puzzle.convL()
    	print("coup",i," : ",x)
    	node.puzzle.afficher2(x)
    	if p:
            fenetre.after(1500, self.aff5, p, i+1)
    	else :
        	print("fin")


class Puzzle:

    def __init__(self, board):
        self.width = len(board[0]) 
        self.board = board

    @property
    def solved(self):

        tab = []
        sol = True
        for i in range (self.width):
	        tab.extend(self.board[i]);

        for j in range (len(tab)-2):
        	if (tab[j]!=(tab[j+1]-1)):
        		sol = False;
        if tab[-1] != 0 :
        	sol = False;
        return sol

    @property 
    def actions(self):
        def create_move(at, to):
            return lambda: self.move(at, to)

        moves = []
        for i, j in itertools.product(range(self.width),
                                      range(self.width)):
            direcs = {'R':(i, j-1),
                      'L':(i, j+1),
                      'D':(i-1, j),
                      'U':(i+1, j)}

            for action, (r, c) in direcs.items():
                if r >= 0 and c >= 0 and r < self.width and c < self.width and \
                   self.board[r][c] == 0:
                    move = create_move((i,j), (r,c)), action
                    moves.append(move)
        return moves

    def shuffle(self):
        puzzle = self
        for k in range(1000):
            puzzle = random.choice(puzzle.actions)[0]()
        x=puzzle.convL()
        print(x)
        self.afficher2(x)
        self = puzzle
        puzzl.board = self.board
        return puzzle

    def copy(self):
        board = []
        for row in self.board:
            board.append([x for x in row])
        return Puzzle(board)

    def move(self, at, to):
        copy = self.copy()
        i, j = at
        r, c = to
        copy.board[i][j], copy.board[r][c] = copy.board[r][c], copy.board[i][j]
        return copy

    def afficher2 (self,liste1  ):
        "afficher les images sur le canvas"
        for k in range(len(liste1)) :
            eff =can.create_image((30+ 150*(k % self.width)), 30+(150*( k // self.width)), anchor=NW, image=Lph[0])
            aff =can.create_image((30+ 150*(k % self.width)), 30+(150*( k // self.width)), anchor=NW ,image = Lph[liste1[k]])

    def pprint(self):
        for row in self.board:
            print(row)
        print()

    def convL(self):
    	L=[]
    	for row in self.board:
    		L.extend(row)
    	return L 

    def __str__(self):
        return ''.join(map(str, self))

    def __iter__(self):
        for row in self.board:
            yield from row





global puzzl , t ,j
j=0
fenetre = Tk()

print("Donner la taille de votre puzzle : \n 3 --> 3*3 \n 4 --> 4*4")
t=int(input())
time.sleep(2)

if(t==3):
	board = [[1,2,3],[4,5,6],[7,8,0]]
else :
	board = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]

puzzl = Puzzle(board)
s = Solver(puzzl)
fenetre['bg']='white'
fenetre.title (' Taquin resolution IA')
can=Canvas( width=180*t,height=180*t,bg='white')
can.pack( side =TOP, padx =20, pady =20)

def melanger(puz):
	puz = puz.shuffle()

global photo1, photo2 , photo3 , photo4 , photo5 , photo6 , photo7 , photo8 , photo9 , photo10 , photo11 , photo12 , photo13 , photo14 , photo15 , photo0
photo3 = PhotoImage(file="3.png")
photo2 = PhotoImage(file="2.png")
photo1 = PhotoImage(file="1.png")
photo4 = PhotoImage(file="4.png")
photo5 = PhotoImage(file="5.png")
photo6 = PhotoImage(file="6.png")
photo7 = PhotoImage(file="7.png")
photo8 = PhotoImage(file="8.png")
photo9 = PhotoImage(file="9.png")
photo10 = PhotoImage(file="10.png")
photo11 = PhotoImage(file="11.png")
photo12 = PhotoImage(file="12.png")
photo13 = PhotoImage(file="13.png")
photo14 = PhotoImage(file="14.png")
photo15 = PhotoImage(file="15.png")
photo0 = PhotoImage(file="16.png")
global Lph , LAff
if ( t==3 ):
	Lph = list([photo0 ,photo1, photo2 , photo3 , photo4 , photo5 , photo6 , photo7 , photo8  ])
else :
	Lph = list([photo0 ,photo1, photo2 , photo3 , photo4 , photo5 , photo6 , photo7 , photo8 , photo9 ,photo10 , photo11,photo12 , photo13,photo14 , photo15 ])

LAff = list([0,1,2,3,4,5,6,7,8])
LAff=[]
for row in board:
    LAff.extend(row)

menubar = Menu(fenetre)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="melanger", command=puzzl.shuffle)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="melanger", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Recherche en longeur", command=s.solve)
menu2.add_command(label="Recherche en largeur", command=s.solve_Long)
menu2.add_command(label="A *", command=s.solve)
menubar.add_cascade(label="Résoudre", menu=menu2)
fenetre.config(menu=menubar)

Button(text='MEL',command=puzzl.shuffle).pack(side=LEFT)
Button(text='RESO1',command=s.solve).pack(side=LEFT)
Button(text='RESO2',command=s.solve_Long).pack(side=LEFT)

bouton1 = Radiobutton(fenetre, text="3*3", variable=t, value=3)
bouton2 = Radiobutton(fenetre, text="4*4", variable=t, value=4)
bouton1.pack()
bouton2.pack()




for k in range(len(Lph)) :
    eff = can.create_image((30+ 150*(k % t)), 30+(150*( k // t)), anchor=NW, image=Lph[0])
    aff = can.create_image((30+ 150*(k % t)), 30+(150*( k // t)), anchor=NW ,image = Lph[LAff[k]])

can.pack()

fenetre.mainloop()

