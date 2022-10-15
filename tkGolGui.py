from tkinter import *
from gameOfLife import GameOfLife


SIM_PAUSED = 0
SIM_ACTIVE = 1
PAUSE_SIM = "Pause Sim"
START_SIM = "Start Sim"
SIM_DELAY = 500 # 0.5sec
GUI_DIMENSIONS = "800x600"


class Window(Frame):

    def __init__(self, main=None):
        Frame.__init__(self, main)
        self.main = main
        self.main.protocol("WM_DELETE_WINDOW", self.client_exit)
        self.__sim_state = SIM_PAUSED
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
        self.sim_button = Button(self, text=START_SIM, command=self.sim_start_stop)
        self.sim_button.pack()
        pass_time_button = Button(self, text="Pass Time", command=self.pass_time_garden)
        pass_time_button.pack()
        reset_button = Button(self, text="Reset Garden", command=self.reset_garden)
        reset_button.pack()

        # key bindings
        self.main.bind('<Return>', self.pass_time_garden)
        self.main.bind('<r>', self.reset_garden)
        self.main.bind('<q>', self.client_exit)

    def client_exit(self, event=None):
        print("Closing up.")
        exit()

    def schedule_simulate(self):
        self.pass_time_garden()
        self.__simulate = self.main.after(SIM_DELAY, self.schedule_simulate)

    def sim_start_stop(self):
        if (self.__sim_state is SIM_PAUSED):
            self.__sim_state = SIM_ACTIVE
            self.sim_button['text'] = PAUSE_SIM
            self.__simulate = self.main.after(0, self.schedule_simulate)
        else:
            self.__sim_state = SIM_PAUSED
            self.sim_button['text'] = START_SIM
            self.main.after_cancel(self.__simulate)

    def pass_time_garden(self, event=None):
        self.__garden.pass_time()
        self.__garden_label.config(text=self.__garden.get_garden_as_text())

    def reset_garden(self, event=None):
        self.__garden.reset_garden()
        self.__garden_label.config(text=self.__garden.get_garden_as_text())



def main():
    print("Hello World!")

    root = Tk()
    root.geometry(GUI_DIMENSIONS)
    app = Window(root)
    root.mainloop()



if __name__ == "__main__":
    main()
