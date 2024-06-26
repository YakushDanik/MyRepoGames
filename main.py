import tkinter as tk

from main_menu import MainMenu


def main() -> None:
    root = tk.Tk()
    MainMenu(root)
    root.mainloop()

if __name__ == '__main__':
    main()
