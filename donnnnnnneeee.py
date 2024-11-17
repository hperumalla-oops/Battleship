import tkinter as tk
from tkinter import messagebox
import random
import numpy

# Global variables
main_list=[]
fart=[]
ship_sizes = [2,3,4]
n = 0
ug = []
game_started = False
your_score=0
comp_score=0
your_sea_buttons=0
comp_sea_buttons=0
tblol=0
cs_index=0

def main():
    global your_sea_buttons, comp_sea_buttons, tblol, root, cg, main_list, your_score, comp_score, game_started
    global cs_index


    root = tk.Tk()
    root.title("Battleship Grids")

    your_score = 0
    comp_score = 0
    game_started = False
    main_list = [] 

    grid_frame = tk.Frame(root)
    grid_frame.pack()

    your_sea_buttons = gridsssss(grid_frame, SeaButton, start_row=1, start_col=0, title="Your Sea", button_color="light blue", clickable=True)
    comp_sea_buttons = gridsssss(grid_frame, CompButton, start_row=1, start_col=10, title="Computer's Grid", clickable=False)

    info= "Battleship is a two player game in which player places their 'ships' on 8x8 grid or 'sea'. Each player takes turn guessing the position of the ship in their opponent's sea, by calling out its position, (2,2 etc) or in this case clicking a  button.\n\nIf you successfully manage to guess all the places where your opponent's ships are, you win the game.\n\nYou each have three ships- 2dot, 3 dot and 4 dot, where dots denotes the number of grid boxes the ship will occupy.\n\nThe game is set against the computer, which will begin first. Each time you guess correctly, you 'hit' a ship and each time you guess incorrectly, you 'miss' a ship.\n\n Good luck!!"
    messagebox.showinfo("Introduction", info)
    
    tblol_frame = tk.Frame(root)
    tblol_frame.pack(pady=10)
    tblol = tk.Text(tblol_frame, height=3, width=60, state="disabled", font=("Cambria", 11, "bold"))
    
    tblol.tag_configure("center", justify="center")
    tblol.pack()

    
    cg = comp_ship_place()
    colorcolor(cg)
    ship_placement(cs_index)

    display("Hello, Welcome to BattleShip!!")
    #display("Hello, Welcome to suck!!")


    root.mainloop()


def display(str):
    tblol.config(state="normal")  
    tblol.insert(tk.END, str, "center") 
    tblol.config(state="disabled") 
    tblol.see(tk.END)

class SeaButton:
    def __init__(self, master, row, column, initial_text=" ", color="light blue", clickable=True): ##is_computer=False):
        self.button = tk.Button(master, text=initial_text, width=4, height=2, bg=color, command=self.on_click)
        self.button.grid(row=row, column=column)
        self.row = row
        self.column = column
        self.clicked = False
        self.clickable = clickable
        

    def on_click(self):
        if not self.clickable:
            return
        global ug
        
        if len(ug) < n and not self.clicked:
                self.button.config(bg="green", text="V")
                ug.append((self.row, self.column))
                self.clicked = True
        
        if len(ug) == n:
                result = set_sea(ug)
                if result == 1:
                    messagebox.showerror("Error", "Please select consecutive buttons for your sea!")
                    #print(ug)
                    for (r, c) in ug:
                        your_sea_buttons[r-2][c-1].button.config(bg="light blue", text=" ")
                        your_sea_buttons[r-2][c-1].clicked = False

                    print(ug)
                    ug.clear()

                elif result == 0:
                    next_ship()

def next_ship():
    global cs_index,n,ug
    
    #messagebox.showinfo("Success", "Nicely done, chomu!")
    cs_index = cs_index+ 1

    if cs_index < len(ship_sizes):
        ship_placement(cs_index)
    else:
        start_game()

def ship_placement(lol):
    global n, ug
    n = ship_sizes[lol]
    ug = []
    messagebox.showinfo("Ship Placement", f"Please select {n} buttons to place your {n}-dot ship.")

class CompButton:
    def __init__(self, master, row, column, clickable=True):
        self.button = tk.Button(master, text=" ", width=4, height=2, bg="white", command=self.on_click)
        self.button.grid(row=row, column=column)
        self.row = row
        self.column = column
        self.clicked = False
        self.clickable = clickable

    def on_click(self):
        if not self.clickable:
            #self.clickable=False
            return
        
        
        
        # Mark the button as clicked
        self.clicked = True
         
            


def gridsssss(master,func, start_row, start_col, title, button_color="white", clickable=True):
    tk.Label(master, text=title, font=('Arial', 12, 'bold')).grid(row=start_row, column=start_col + 1, columnspan=8, pady=(0, 10))

    for i in range(8):
        tk.Label(master, text=str(i), font=('Arial', 10)).grid(row=start_row + i + 1, column=start_col)
        tk.Label(master, text=str(i), font=('Arial', 10)).grid(row=start_row, column=start_col + i + 1)

    buttons = []
    for row in range(8):
        button_row = []
        for col in range(8):
            button = func(master, row=start_row + row + 1, column=start_col + col + 1, clickable=clickable)
            button_row.append(button)
        buttons.append(button_row)
    
    
    return buttons



def set_sea(ug):
    for_rows = []
    for_cols = []


    for item in ug:
        for_rows.append(item[0])
        for_cols.append(item[1])

    #print("fart---")
    #print(for_rows,for_cols)

    if is_consecutive(for_rows)==0 and len(set(for_cols))==1:
       # print("ship is in the same coulmn")
        for (a,b) in ug:
           main_list.append((a-2,b-1))
        ug.clear()
        return 0
    
    elif is_consecutive(for_cols)==0 and len(set(for_rows))==1:
        #print("ship is in the same row")
        for (a,b) in ug:
           main_list.append((a-2,b-1))
             #main_list.append((a,b))
        ug.clear()
        return 0
    
    else:
        print("please enter the dots consecutively")
        return 1 ##error funking chomu dash gdha
    
def comp_ship_place():
    cg=[]
    d=random.randint(0,1)
    #print(d)

    ### for 3-dot ship
    if d==0:
        ##fix row
        x=random.randint(0,7)
        y=random.randint(0,5)
        cg=[(x,y),(x,y+1),(x,y+2)]
    else:
        ##fix column
        y=random.randint(0,7)
        x=random.randint(0,5)
        cg=[(x,y),(x+1,y),(x+2,y)]

### for 4 dot ship

    d=random.randint(0,1)
    if d==0:
        ##fix row
        x2=random.randint(0,7)
        while True:
            if x2==x:
                x2=random.randint(0,7)
            else:
                break
        
        y2=random.randint(0,3)
        cg=cg+[(x2,y2),(x2,y2+1),(x2,y2+2),(x2,y2+3)]
    else:
        ##fix column
        y2=random.randint(0,7)
        while True:
            if y2==y:
                y2=random.randint(0,7)
            else:
                break
        
        x2=random.randint(0,3)
        cg=cg+[(x2,y2),(x2+1,y2),(x2+2,y2),(x2+3,y2)]

    ### FOR 2 DOT SHIP
    d=random.randint(0,1)
    if d==0:
        ##fix row
        x3=random.randint(0,7)
        while True:
            if x3==x or x3==x:
                x3=random.randint(0,7)
            else:
                break
        
        y3=random.randint(0,6)
        cg=cg+[(x3,y3),(x3,y3+1)]
    else:
        ##fix column
        y3=random.randint(0,7)
        while True:
            if y3==y or y3==y2:
                y3=random.randint(0,7)
            else:
                break
        
        x3=random.randint(0,6)
        cg=cg+[(x3,y3),(x3+1,y3)]
        #cg=[(x, y), (x + 1, y), (x + 2, y)]
    
    #print(cg)
    if len(cg)!=len(set(cg)):
         return comp_ship_place()
    
    print(cg)
    return cg




def start_game():
    global game_started
    game_started = True
    
    messagebox.showinfo("Game Start", "And the game begins!")

    #disaling your buttons
    for row in your_sea_buttons:
        for ybtn in row:
            ybtn.clickable = False

    computer_turn()

def computer_turn():
    global comp_score, your_score,fart
    

    a=random.randint(0,7)
    b=random.randint(0,7)
    fart.append((a,b))

    print(fart)
    print(f"len(fart)={len(fart)}, len(set(fart))={len(set(fart))}")
    print(a,b)


    if len(fart)==len(set(fart)):

            your_sea_buttons[a][b].button.config(bg="purple", text="F")

            if (a, b) in main_list:
                your_sea_buttons[a][b].button.config(bg="red", text="X")
                #display(f"COMP'S HIT YOUR 2-DOT SHIP!!\n ")
                comp_score += 1

                """elif (a, b) in main_list[2:5]:
                your_sea_buttons[a][b].button.config(bg="red", text="X")
                display(f"COMP'S HIT YOUR 3-DOT SHIP!!\n ")
            comp_score += 1

            elif (a, b) in main_list[5:9]:
            your_sea_buttons[a][b].button.config(bg="red", text="X")
            display(f"COMP'S HIT YOUR 4-DOT SHIP!!\n ")
            comp_score += 1"""

            else:
                your_sea_buttons[a][b].button.config(bg="light yellow", text="O")
                display("COMP MISS\n")
                #display("YOUR TURN!!\n")
                #print("YOUR TURN!!\n")

            if comp_score == 9:
                your_sea_buttons[a][b].button.config(bg="red", text="X")
                messagebox.showinfo("FAILURE", "You lost!")
                root.destroy()
            elif your_score == 9:
                #your_sea_buttons[a][b].button.config(bg="red", text="X")
                messagebox.showinfo("SUCCESS", "You won!")
                root.destroy()

            if comp_score < 9:
                #print("comp_score:",comp_score)
                print(f"comp score: {comp_score}\nyour score: {your_score}\n")
                display(f"comp score: {comp_score}\nyour score: {your_score}\n")

                for row in comp_sea_buttons:
                    for cbtn in row:
                        cbtn.clickable = True
                        cbtn.button.config(command=lambda btn=cbtn: player_turn(btn))
                        #cbtn.clickable =False

    else:
        fart.remove((a,b))
        print("we are in else:",fart)
        computer_turn()


    


def player_turn(btn):
    global your_score

    x = btn.row - 2
    y = btn.column - 11


    if (x, y) in cg :
        comp_sea_buttons[x][y].button.config(bg="red", text="X")
        your_score += 1
        cg.remove((x,y))
        #comp_sea_buttons[x][y].clickable= False

        

    else:
        if not comp_sea_buttons[x][y].button.config(bg="red"):
            comp_sea_buttons[x][y].button.config(bg="light yellow", text="O")
            display("YOU MISS!!\n")
        #display("IT'S COMP'S TURN!!\n")

    if comp_score == 9:
        #your_sea_buttons[a][b].button.config(bg="red", text="X")
        messagebox.showinfo("FAILURE", "You lost!")
        root.destroy()

    elif your_score == 9:
        btn.button.config(bg="red", text="X")
        messagebox.showinfo("SUCCESS", "You won!")
        root.destroy()

    for row in comp_sea_buttons:
        for cbtn in row:
            cbtn.clickable = False

    if your_score < 9:
        computer_turn()



def colorcolor(cg):
    ##cg=[(0, 2), (0, 3), (0, 4), (6, 3), (6, 4), (6, 5), (6, 6), (4, 4), (5, 4)]
    for (r, c) in cg[0:3]:
        comp_sea_buttons[r][c].button.config(bg="yellow")
    for (r, c) in cg[3:7]:
        comp_sea_buttons[r][c].button.config(bg="pink")
    for (r, c) in cg[7:9]:
        comp_sea_buttons[r][c].button.config(bg="purple")

def is_consecutive(a):
    k=numpy.sort(a)
    for i in range(0,len(k)-1):
        if k[i+1] != k[i]+1:
            return 1
    else:
        return 0




if __name__ == "__main__":
    main()


        

#2. all the displays
#3. remove the highlight

#the number of ways to change everything.
#cool
