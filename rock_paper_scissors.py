from tkinter import *

class RockPaperScissors:
    def __init__(self, parent, switch_frame) -> None:
        super().__init__()
        self.parent = parent
        self.switch_frame = switch_frame
        self.frame = Frame(self.parent)
        self.p1_score: int = 0
        self.p2_score: int = 0
        self.p1_choice: str = ""
        self.p2_choice: str = ""
        self.turns: int = 0

        # Text widgets
        text_label = Label(self.frame, text="Rock, Paper & Scissors", font=("Calibri", 20))
        text_label.grid(pady=30, row=0, column=0, sticky="ne")
        self.score_label = Label(self.frame, text=f"SCORE:0-0", font=15)
        self.score_label.grid(row=1, column=0, sticky="w")

        # Game buttons
        self.rock_button = Button(self.frame, font=("Calibri", 15), text="ROCK",
                                command=lambda: self.element_selection("ROCK"))
        self.rock_button.grid(row=2, column=1, pady=30, sticky="sw")
        self.paper_button = Button(self.frame, font=("Calibri", 15), text="PAPER",
                                command=lambda: self.element_selection("PAPER"))
        self.paper_button.grid(row=2, column=2, pady=30, sticky="sw")
        self.scissors_button = Button(self.frame, font=("Calibri", 15), text="SCISSORS",
                                    command=lambda: self.element_selection("SCISSORS"))
        self.scissors_button.grid(row=2, column=3, pady=30, sticky="sw")

        self.back_button = Button(self.frame, font=("Calibri", 15), text="Back to Menu",
                                command=self.back_to_menu)
        self.back_button.grid(row=5, column=0, pady=30, sticky="sw")

    # Game logic
    def element_selection(self, choice: str) -> None:
        self.turns += 1
        if self.turns == 1:
            self.p1_choice = choice
        else:
            self.p2_choice = choice
            self.game_manage()

    def game_manage(self) -> None:
        if self.turns == 2:
            if self.p1_choice == self.p2_choice:
                self.result_message_box("DRAW")
            elif (self.p1_choice == "ROCK" and self.p2_choice == "SCISSORS") or \
                (self.p1_choice == "PAPER" and self.p2_choice == "ROCK") or \
                (self.p1_choice == "SCISSORS" and self.p2_choice == "PAPER"):
                self.p1_score += 1
                self.result_message_box("Player 1 WINS")
            else:
                self.p2_score += 1
                self.result_message_box("Player 2 WINS")
            self.score_label.config(text="SCORE:" + str(self.p1_score) + "-" + str(self.p2_score))
            self.turns = 0  # Reset turns after a round

    def back_to_menu(self) -> None:
        self.switch_frame("main_menu")
        self.score_restart()
        if hasattr(self, 'dialog'):
            self.dialog.destroy()

    def score_restart(self) -> None:
        self.p1_score = 0
        self.p2_score = 0
        self.score_label.config(text="SCORE:0-0")

    def restart(self) -> None:
        self.turns = 0
        self.p1_choice = ""
        self.p2_choice = ""
        if hasattr(self, 'dialog'):
            self.dialog.destroy()

    # Custom message box
    def result_message_box(self, result_text: str):
        self.dialog = Toplevel()
        self.dialog.title("Result")
        label = Label(self.dialog, text=result_text)
        label.pack()

        restart_button = Button(self.dialog, text="PLAY AGAIN?", command=self.restart)
        restart_button.pack()

        main_menu_button = Button(self.dialog, text="MAIN MENU", command=self.back_to_menu)
        main_menu_button.pack()