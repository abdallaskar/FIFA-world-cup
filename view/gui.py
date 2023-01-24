
from tkinter import *
from tkinter.scrolledtext import ScrolledText


class Gui:
    def create_start_main_window(self):
        self.main_window = Tk()
        self.main_window.title("World CUP ")
        self.main_window.geometry("1900x750")


    def creat_league_lable(self):
        outputLabel1 = Label(font=('vendor', 20, 'bold'), fg='blue')
        outputLabel1.place(x=600, y=20)
        outputLabel1.configure(
            text='Egyptian league')
        outputLabel = Label(font=('vendor', 15, 'bold'), fg='black')
        outputLabel.place(x=320, y=70)
        outputLabel.configure(text='league :            Teams                                                    PTS  WIN  LOS  DIF')

    def creat_cup_lable(self):
        outputLabel1 = Label(font=('vendor', 20, 'bold'), fg='blue')
        outputLabel1.place(x=600, y=20)
        outputLabel1.configure(
            text='Egyptian Cup       ')
        outputLabel = Label(font=('vendor', 15, 'bold'), fg='black')
        outputLabel.place(x=320, y=70)
        outputLabel.configure(text='                                                                                                                        ')

    def creat_world_cup_lable(self):
        outputLabel1 = Label(font=('vendor', 20, 'bold'), fg='blue')
        outputLabel1.place(x=600, y=20)
        outputLabel1.configure(
            text='World Cup         ')
        outputLabel = Label(font=('vendor', 15, 'bold'), fg='black')
        outputLabel.place(x=320, y=70)
        outputLabel.configure(text='                                                                                                                        ')

    # create button and active it
    def create_league_button(self,league_controller):

        league_button = Button(self.main_window, text=" League ", command=league_controller,
                               font=('vendor', 18, 'bold'), height=1,width=13)
        league_button.place(x=50, y=100)


    def create_cup_button(self, cup_controller):
        # create button and active it
        cup_button = Button(self.main_window, text="   CUP   ", command=cup_controller,
                               font=('vendor', 18, 'bold'), height=1,width=13)
        cup_button.place(x=50, y=200)

    def create_world_cup_button(self, world_controller):
        # create button and active it
        world_button = Button(self.main_window, text=" World CUP ", command=world_controller,
                            font=('vendor', 18, 'bold'), height=1, width=13)
        world_button.place(x=50, y=300)



    def create_output_box(self):
        self.output_box = ScrolledText(font=('Verdana', 16), height=27, width=92)
        self.output_box.place(x=320, y=100)

    def print_in_ouput_box(self,output_string):
        #output_box.delete(1.0, END)
        self.output_box.insert(END,output_string)


    def delet_output_box(self):
        self.output_box.delete(1.0, END)





    def create_main_window(self):
        self.main_window.mainloop()
