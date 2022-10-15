from tkinter import *
from gameOfLife import GameOfLife



class Window(Frame):

    def __init__(self, main=None):
        Frame.__init__(self, main)
        self.main = main
        self.main.protocol("WM_DELETE_WINDOW", self.client_exit)
        self.init_window()

    def init_window(self):
        self.main.title("Conway's Game of Life")
        self.pack(fill=BOTH, expand=1)
        
        # menu
        menu = Menu(self.main)
        self.main.config(menu=menu)
        file = Menu(menu, tearoff=False)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file, underline=0)
        
        # create garden
        self.__garden = GameOfLife(10, 10)
        self.__garden_label = Label(self, text=self.__garden.get_garden_as_text(), font=("Helvetica",25))
        self.__garden_label.pack()

        # garden buttons
        pass_time_button = Button(self, text="Pass Time", command=self.pass_time_garden)
        pass_time_button.pack(side=LEFT)
        reset_button = Button(self, text="Reset Garden", command=self.reset_garden)
        reset_button.pack(side=LEFT)

        # key bindings
        self.main.bind('<Return>', self.pass_time_garden)
        self.main.bind('<r>', self.reset_garden)
        self.main.bind('<q>', self.client_exit)

    def client_exit(self, event=None):
        print("Closing up.")
        exit()

    def pass_time_garden(self, event=None):
        self.__garden.pass_time()
        self.__garden_label.config(text=self.__garden.get_garden_as_text())

    def reset_garden(self, event=None):
        self.__garden.reset_garden()
        self.__garden_label.config(text=self.__garden.get_garden_as_text())



def main():
    print("Hello World!")

    root = Tk()
    root.geometry("800x600")
    app = Window(root)
    root.mainloop()



if __name__ == "__main__":
    main()
