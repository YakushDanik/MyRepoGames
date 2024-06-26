from tkinter import *

class TicTacToe:

    def __init__(self, parent, switch_frame) -> None:
        super().__init__()
        self.parent = parent
        self.switch_frame = switch_frame
        self.frame = Frame(self.parent)
        self.turns:int = 1
        self.rows = [0, 0, 0]
        self.columns = [0, 0, 0]
        self.diag1:int = 0
        self.diag2:int = 0
        self.o_score:int = 0
        self.x_score:int = 0

        #Text widgets
        text_label = Label(self.frame, text="Tic Tac Toe Game", font=("Calibri", 20))
        text_label.grid(pady=30, row=0, column = 0, sticky="ne")
        self.score_label = Label(self.frame, text=f"SCORE:0-0", font=15)
        self.score_label.grid(row=1, column=0, sticky="w")


        #Game buttons
        self.game_buttons = {}
        for i in range(0,3):
            for j in range(0,3):
                self.game_buttons[i, j] = Button(self.frame, height=5, width=10,
                                            command=lambda i=i, j=j: self.button_on_click(i,j))
                self.game_buttons[i, j].grid(row=i + 2, column=j + 2, sticky="nsew")

        self.back_button = Button(self.frame, font=("Calibri", 15), text="Back to Menu",
                            command=self.back_to_menu)
        self.back_button.grid(row=5, column=0, pady=30, sticky="sw")

    #Game logic
    def button_on_click(self, i:int, j:int) -> None:
        if not self.game_buttons[i,j]["text"]:
            self.game_buttons[i, j].config(text="O" if self.turns % 2 == 0 else "X")
            self.turns+=1
            self.game_manage(i, j)

    def game_manage(self, i:int, j:int) -> None:
        point = 1 if self.turns%2 == 1 else -1
        self.rows[i] += point
        self.columns[j] += point
        if i == j : self.diag1 += point
        if i+j == 2: self.diag2 += point
        
        if(abs(self.rows[i]) == 3 or abs(self.columns[j]) == 3 or abs(self.diag1) == 3 or abs(self.diag2) == 3):
            if(point == 1):
                self.result_message_box("O WINS")
                self.o_score+=1
            else:
                self.result_message_box("X WINS")
                self.x_score+=1
            self.score_label.config(text="SCORE:"+str(self.x_score)+"-"+str(self.o_score))
                
        if self.turns == 10: 
            self.result_message_box("DRAW")

    #Message box buttons_on_click 
    def restart(self) -> None:
        for button in self.game_buttons.values():
            button.config(text="")
        self.turns=1
        self.rows = [0, 0, 0]
        self.columns = [0, 0, 0]
        self.diag1 = 0
        self.diag2 = 0
        self.dialog.destroy()
    
    def back_to_menu(self) -> None:
        self.switch_frame("main_menu")
        self.score_restart()
        self.dialog.destroy()
        self.restart()

    def score_restart(self) -> None:
        self.o_score = 0
        self.x_score = 0
        self.score_label.config(text="SCORE:0-0")

    #Custom message box
    def result_message_box(self, result_text:str):
        self.dialog = Toplevel()
        self.dialog.title("Result")
        label = Label(self.dialog, text=result_text)
        label.pack()

        restart_button = Button(self.dialog, text="PLAY AGAIN?", command=self.restart)
        restart_button.pack()

        main_menu_button = Button(self.dialog, text="MAIN MENU", command=self.back_to_menu)
        main_menu_button.pack()