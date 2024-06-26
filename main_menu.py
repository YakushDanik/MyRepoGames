from tkinter import *

from rock_papper_scissors import RockPaperScissors
from tic_tac_toe import TicTacToe

class MainMenu:
    def __init__(self, window) -> None:
        self.window = window
        self.window.title("Games")
        self.window.geometry('500x500')
        self.window.resizable(False, False)
        self.frame = Frame(self.window)
        self.frame.grid(row=0, column=0, sticky="nsew")


        self.frames = {}
        self.frames["tic_tac"] = TicTacToe(self.window, self.switch_frame)
        self.frames["rock_paper_scissors"] = RockPaperScissors(self.window, self.switch_frame)
        
        for frame in self.frames.values():
            frame.frame.grid(row=0, column=0, sticky="nsew")

        self.frame.tkraise()

        #creating text:
        main_menu = Label(self.frame, text="MAIN MENU", justify="right")
        main_menu.config(font=("Calibri", 30))
        main_menu.grid(pady=50, row=0, column=2)

        #creating buttons
        tic_tac_button = Button(self.frame, font=("Calibri", 20), text = "Tic Tac Toe",
                                command=lambda: self.switch_frame("tic_tac"))
        tic_tac_button.grid(pady=10, row=1, column=1, sticky="w")

        rps_button = Button(self.frame, font=("Calibri", 20), text = "Rock, Paper & Scissors",
                                command=lambda: self.switch_frame("rock_paper_scissors"))
        rps_button.grid(pady=10, row=2, column=1, sticky="w")

        quit_button = Button(self.frame, font=("Calibri", 20), text="Quit",
                                command = self.window.destroy)
        quit_button.grid(pady=10, row=3, column=1, sticky="w")

    def switch_frame(self, frame_name) -> None:
        if(frame_name == "main_menu"):
            self.frame.tkraise()
        else:
            frame = self.frames[frame_name]
            frame.frame.tkraise() 


