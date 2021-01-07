from tkinter import *
from tkinter.font import Font
import numpy as np


class DiceScreen(Tk):
    def __init__(self):
        super().__init__()
        self.bgcolor = '#4589cc'
        self.photo = PhotoImage(file="img/regular/roll.png")
        self.dice = StringVar()
        self.dice.set('regular')
        self.title("Dice Simulator")
        self.geometry("550x400")
        self.resizable(False, False)
        self.configure(background=self.bgcolor)
        self.iconphoto(False, self.photo)
        self.dice_state = 'roll'
        self.roll_count = 0
        self.tframe = Frame(self)
        self.tframe.pack(side=TOP)
        self.heading = Label(self.tframe, text='Dice Simulator by Ayush Solanki', font=Font(size=25), bg=self.bgcolor)
        self.heading.pack()

    def roll_dice(self):
        dice = self.dice.get()
        num = 'roll'
        if dice == 'regular':
            num = np.random.choice([1, 2, 3, 4, 5, 6],
                                   p=[0.25, 0.25, 0.25, 0.15, 0.05, 0.05])
        elif dice == 'silver':
            num = np.random.choice([1, 2, 3, 4, 5, 6],
                                   p=[0.1, 0.1, 0.15, 0.25, 0.25, 0.15])
        elif dice == 'gold':
            num = np.random.choice([1, 2, 3, 4, 5, 6],
                                   p=[0.10, 0.10, 0.10, 0.10, 0.30, 0.30])
        self.roll_count += 1
        self.lblCount.configure(text=f'Rolled {self.roll_count} times')
        image = PhotoImage(file=f"img/{dice}/{num}.png")
        self.imgCanvas.delete("all")
        self.imgCanvas.create_image(0, 0, anchor='nw', image=image)
        self.imgCanvas.image = image

    def imagebar(self):
        self.lframe = Frame(self)
        self.lframe.pack(side=LEFT, padx=50)
        self.lblCount = Label(self.lframe, text=f'Rolled {self.roll_count} times', font=Font(size=15))
        self.lblCount.pack()
        self.imgCanvas = Canvas(self.lframe, height=150, width=150, bg=self.bgcolor, highlightthickness=0)
        self.imgCanvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.imgCanvas.pack()
    
    def buttonbar(self):
        self.rframe = Frame(self, bg=self.bgcolor)
        self.rframe.pack(side=RIGHT, padx=100, pady=(50, 150))
        self.regRadioButton = Radiobutton(self.rframe, text='Regular', bg=self.bgcolor, font=Font(size=15),
                                          variable=self.dice, value='regular',
                                          command=self.selectradio).pack(side=TOP, anchor='w')
        self.silverRadioButton = Radiobutton(self.rframe, text='Silver', bg=self.bgcolor, font=Font(size=15),
                                             variable=self.dice, value='silver', tristatevalue=0,
                                             command=self.selectradio).pack(side=TOP, anchor='w')
        self.goldRadioButton = Radiobutton(self.rframe, text='Gold', bg=self.bgcolor, font=Font(size=15),
                                           variable=self.dice, value='gold', tristatevalue=0,
                                           command=self.selectradio).pack(side=TOP, anchor='w')
        Button(self.rframe, text='Roll', font=Font(size=15), command=self.roll_dice, padx=50).pack()
    
    def selectradio(self):
        self.imgCanvas.delete("all")
        dice = self.dice.get()
        image = PhotoImage(file=f"img/{dice}/roll.png")
        self.imgCanvas.create_image(0, 0, anchor='nw', image=image)
        self.imgCanvas.image = image
