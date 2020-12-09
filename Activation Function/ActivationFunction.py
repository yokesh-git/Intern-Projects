from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
import math
import matplotlib.pyplot as plt
plt.matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import tkinter.messagebox


class Activation:
    ''' Initial class that act as master of App'''

    def __init__(self, master):

        '''This is the function that automaically executes when the object of Activation class is created'''

        #This is for all Window Position

        global w,h,ws,hs,x,y

        w = 1000
        h = 650
        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen
        x = (ws/4) - (w/4)
        y = (hs/4) - (h/4)

        self.master = master
        self.function_generator = Activation_functions()
        master.title("HEU Technologies - Activation Function")

        def onclick():
            root.quit()
            self.master.withdraw()

        self.master.protocol("WM_DELETE_WINDOW", onclick)

        self.canvas = Canvas(self.master, width=1000, height=650)
        self.canvas.pack()

        self.image = ImageTk.PhotoImage(Image.open("Images/bg.png"))
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)

        self.image14 = ImageTk.PhotoImage(Image.open("Images/logo.png"))
        self.canvas.create_image(485, 650, anchor=S, image=self.image14)

        self.canvas19 = Canvas(self.master, width=500, height=75)
        self.canvas19.place(x=250, y=20)

        self.i = self.canvas19.create_text(250, 35, fill="white", font=("Times New Roman 20 italic bold", 32),
                                           text="Activation Functions")

        self.r = self.canvas19.create_rectangle(self.canvas.bbox(ALL), fill="#555BA7")
        self.canvas19.tag_lower(self.r, self.i)

        self.button1 = Button(self.master, text="Click To Start", foreground="white", command=self.clicktostart,
                              anchor=CENTER)

        self.button1.configure(width=30, activebackground="#33B5E5", bg='#575757', relief=FLAT)
        self.button1_window = self.canvas.create_window(350, 350, anchor=W, window=self.button1)
        font1 = font.Font(family='Times New Roman', size=20, weight='normal')
        self.button1['font'] = font1
        self.button1.config(width=20, height=2)

        self.secondWin = Toplevel()
        
        self.secondWin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas2 = Canvas(self.secondWin, width=1000, height=650)
        self.canvas2.pack()

        self.image1 = ImageTk.PhotoImage(Image.open("Images/bg.png"))
        self.canvas2.create_image(0, 0, anchor=NW, image=self.image1)

        self.canvas2.create_text(100, 75, fill="black", font=("Times New Roman 20 bold", 32),
                                 text="About:")

        para = """
         Activation function decides,  whether  a  neuron  should   be
activated or not by calculating weighted sum and further adding bias
with it. The purpose of the activation function is to introduce non-linearity
into the output of a neuron.

Understand different types of activation functions which are used in
neural network"""

        self.canvas2.create_text(475, 300, fill="black", font=("Times New Roman 20 italic", 18),
                                 text=para)

        self.button1 = Button(self.secondWin, text="Click for Help", command=self.clickforhelp, anchor=CENTER)
        self.button1.configure(width=10, activebackground="#33B5E5", bg='#558DEA', relief=FLAT)
        self.button1_window = self.canvas2.create_window(100, 500, anchor=NW, window=self.button1)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button1['font'] = font1
        self.button1.config(width=12, height=2)

        self.button2 = Button(self.secondWin, text="HOME", command=self.home, anchor=CENTER)
        self.button2.configure(width=10, activebackground="#33B5E5", bg='#558DEA', relief=FLAT)
        self.button2_window = self.canvas2.create_window(400, 500, anchor=NW, window=self.button2)

        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button2['font'] = font1
        self.button2.config(width=12, height=2)

        self.button3 = Button(self.secondWin, text="Click to Begin", command=self.clicktobegin, anchor=CENTER)
        self.button3.configure(width=10, activebackground="#33B5E5", bg='#558DEA', relief=FLAT)
        self.button3_window = self.canvas2.create_window(700, 500, anchor=NW, window=self.button3)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button3['font'] = font1
        self.button3.config(width=12, height=2)

        self.secondWin.protocol("WM_DELETE_WINDOW", root.destroy)

        self.secondWin.withdraw()

        self.ThirdWin = Toplevel()
        
        self.ThirdWin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas3 = Canvas(self.ThirdWin, width=1000, height=650)
        self.canvas3.pack()

        self.image2 = ImageTk.PhotoImage(Image.open("Images/bg.png"))
        self.canvas3.create_image(0, 0, anchor=NW, image=self.image2)

        self.canvas20 = Canvas(self.ThirdWin, width=500, height=65)
        self.canvas20.place(x=250, y=50)

        self.i = self.canvas20.create_text(250, 35, fill="black", font=("Times New Roman 20", 32),
                                           text="Activation Functions")
        self.r = self.canvas20.create_rectangle(self.canvas.bbox(ALL), fill="#6DB4EC")
        self.canvas20.tag_lower(self.r, self.i)

        self.button4 = Button(self.ThirdWin, foreground="white", text="HOME", command=self.thirdwinhome,
                              anchor=CENTER)
        self.button4.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button4_window = self.canvas3.create_window(60, 40, anchor=NW, window=self.button4)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button4['font'] = font1
        self.button4.config(width=10, height=1)

        self.button5 = Button(self.ThirdWin, foreground="white", text="BACK", command=self.back, anchor=CENTER)
        self.button5.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button5_window = self.canvas3.create_window(800, 40, anchor=NW, window=self.button5)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button5['font'] = font1
        self.button5.config(width=10, height=1)

        self.photo = ImageTk.PhotoImage(Image.open("Images/sigmoid.png"))
        self.sigmoid = Button(self.ThirdWin, height=210, width=165, text="Sigmoid", compound="top", bg="#6DB4EC",
                              font=('Times New Roman', 18), foreground='white', image=self.photo, command=self.sigmoid)
        self.sigmoid.place(x=150, y=175)

        self.photo1 = ImageTk.PhotoImage(Image.open("Images/tanh.png"))
        self.tanh = Button(self.ThirdWin, height=210, width=165, text="TanH", compound="top", bg="#6DB4EC",
                           font=('Times New Roman', 18), foreground='white', image=self.photo1, command=self.tanh)
        self.tanh.place(x=400, y=175)

        self.photo2 = ImageTk.PhotoImage(Image.open("Images/relu.png"))
        self.relu = Button(self.ThirdWin, height=210, width=165, text="ReLU", compound="top", bg="#6DB4EC",
                           font=('Times New Roman', 18), foreground='white', image=self.photo2, command=self.relu)
        self.relu.place(x=650, y=175)

        self.photo3 = ImageTk.PhotoImage(Image.open("Images/leaky_relu.png"))
        self.leakyrelu = Button(self.ThirdWin, height=210, width=165, text="Leaky ReLU", compound="top", bg="#6DB4EC",
                                font=('Times New Roman', 18), foreground='white', image=self.photo3,
                                command=self.leakyrelu)
        self.leakyrelu.place(x=200, y=400)

        self.photo4 = ImageTk.PhotoImage(Image.open("Images/softmax.png"))
        self.softmax = Button(self.ThirdWin, height=210, width=165, text="Softmax", compound="top", bg="#6DB4EC",
                              font=('Times New Roman', 18), foreground='white', image=self.photo4, command=self.softmax)
        self.softmax.place(x=600, y=400)

        self.canvas3.create_rectangle(900, 625, 110, 150, outline="#6DB4EC", width=5)

        self.ThirdWin.protocol("WM_DELETE_WINDOW", root.destroy)

        self.ThirdWin.withdraw()

        self.softmaxwin = Toplevel()
        
        self.softmaxwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas4 = Canvas(self.softmaxwin, width=1000, height=650)
        self.canvas4.pack()

        self.canvas21 = Canvas(self.softmaxwin, width=500, height=65)
        self.canvas21.place(x=250, y=25)

        self.image4 = ImageTk.PhotoImage(Image.open("Images/bg.png"))
        self.canvas4.create_image(0, 0, anchor=NW, image=self.image4)

        self.i = self.canvas21.create_text(250, 35, fill="black", font=("Times 20 italic bold", 32),
                                           text="SOFTMAX")
        self.r = self.canvas21.create_rectangle(self.canvas.bbox(ALL), fill="#6DB4EC")
        self.canvas21.tag_lower(self.r, self.i)

        self.button6 = Button(self.softmaxwin, text="HOME", foreground="white", command=self.softmaxhome,
                              anchor=CENTER)
        self.button6.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button6_window = self.canvas4.create_window(60, 20, anchor=NW, window=self.button6)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button6['font'] = font1
        self.button6.config(width=10, height=1)

        self.button7 = Button(self.softmaxwin, text="BACK", foreground="white", command=self.softmaxback,
                              anchor=CENTER)
        self.button7.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button7_window = self.canvas4.create_window(800, 20, anchor=NW, window=self.button7)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button7['font'] = font1
        self.button7.config(width=10, height=1)

        self.canvas4.create_rectangle(900, 625, 110, 100, outline="#6DB4EC", width=8)

        self.canvas5 = Canvas(self.softmaxwin, bg="#B5B2B0", width=250, height=500)
        self.canvas5.place(x=125, y=105)

        self.canvas6 = Canvas(self.softmaxwin, bg="#B5B2B0", width=450, height=500)
        self.canvas6.place(x=425, y=105)

        self.i = self.canvas5.create_text(125, 25, fill="black", font=("Times 20 "),
                                          text=" PARAMETERS ")
        self.r = self.canvas5.create_rectangle(self.canvas5.bbox(self.i), fill="#6DB4EC", outline="#6DB4EC")
        self.canvas5.tag_lower(self.r, self.i)

        self.image5 = ImageTk.PhotoImage(Image.open("Images/softmaxformula.png"))
        self.canvas5.create_image(5, 50, anchor=NW, image=self.image5)

        self.i = self.canvas5.create_text(125, 215, fill="black", font=("Times 20"),
                                          text="  Input Value  ")
        self.r = self.canvas5.create_rectangle(self.canvas5.bbox(self.i), fill="#6DB4EC", outline="#6DB4EC")
        self.canvas5.tag_lower(self.r, self.i)

        self.tb3 = Text(self.canvas5, height=3, width=26)
        self.tb3.place(x=20, y=250)
        self.tb3.bind("<Return>", self.updatesoftmax)

        self.button8 = Button(self.softmaxwin, text="Get", command=self.getsoftmax, anchor=CENTER)
        self.button8.configure(width=5, activebackground="#33B5E5", bg='#6DB4EC', relief=RAISED)
        self.button8_window = self.canvas5.create_window(25, 315, anchor=NW, window=self.button8)
        font1 = font.Font(family='Times New Roman', size=12, weight='normal')
        self.button8['font'] = font1
        self.button8.config(width=5, height=1)

        self.button21 = Button(self.softmaxwin, text="Update", command=self.updatesoftmax, anchor=CENTER)
        self.button21.configure(width=5, activebackground="#33B5E5", bg='#6DB4EC', relief=RAISED)
        self.button21_window = self.canvas5.create_window(100, 315, anchor=NW, window=self.button21)
        font1 = font.Font(family='Times New Roman', size=12, weight='normal')
        self.button21['font'] = font1
        self.button21.config(width=5, height=1)

        self.i = self.canvas5.create_text(125, 375, fill="black", font=("Times 20"),
                                          text="  Output Value  ")
        self.r = self.canvas5.create_rectangle(self.canvas5.bbox(self.i), fill="#6DB4EC", outline="#6DB4EC")
        self.canvas5.tag_lower(self.r, self.i)

        self.tb4 = Text(self.canvas5, height=3, width=26)
        self.tb4.place(x=20, y=410)

        self.i = self.canvas6.create_text(225, 25, fill="black", font=("Times 20"),
                                          text="  GRAPH  ")
        self.r = self.canvas6.create_rectangle(self.canvas6.bbox(self.i), fill="#6DB4EC", outline="#6DB4EC")
        self.canvas6.tag_lower(self.r, self.i)

        self.fig, self.ax4 = plt.subplots(figsize=(4, 4))
        self.ax4.spines['left'].set_position('center')
        self.ax4.spines['bottom'].set_position('center')
        self.ax4.spines['right'].set_color('none')
        self.ax4.spines['top'].set_color('none')
        self.ax4.xaxis.set_ticks_position('bottom')
        self.ax4.yaxis.set_ticks_position('left')

        self.canvas6 = FigureCanvasTkAgg(self.fig, master=self.canvas6)
        self.canvas6.get_tk_widget().place(x=25, y=50)

        self.softmaxwin.protocol("WM_DELETE_WINDOW", root.destroy)

        self.softmaxwin.withdraw()

        self.tanhwindow = Toplevel()
        
        self.tanhwindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas7 = Canvas(self.tanhwindow, width=1000, height=650)
        self.canvas7.pack()

        self.canvas22 = Canvas(self.tanhwindow, width=500, height=65)
        self.canvas22.place(x=250, y=25)

        self.image6 = ImageTk.PhotoImage(Image.open("Images/bg.png"))
        self.canvas7.create_image(0, 0, anchor=NW, image=self.image6)

        self.i = self.canvas22.create_text(250, 35, fill="black", font=("Times 20 italic bold", 32),
                                           text="TANH")
        self.r = self.canvas22.create_rectangle(self.canvas.bbox(ALL), fill="#6DB4EC")
        self.canvas22.tag_lower(self.r, self.i)

        self.button9 = Button(self.tanhwindow, text="HOME", foreground="white", command=self.tanhwinhome,
                              anchor=CENTER)
        self.button9.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button9_window = self.canvas7.create_window(60, 20, anchor=NW, window=self.button9)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button9['font'] = font1
        self.button9.config(width=10, height=1)

        self.button10 = Button(self.tanhwindow, text="BACK", foreground="white", command=self.tanhwinback,
                               anchor=CENTER)
        self.button10.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button10_window = self.canvas7.create_window(800, 20, anchor=NW, window=self.button10)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button10['font'] = font1
        self.button10.config(width=10, height=1)

        self.canvas7.create_rectangle(900, 625, 110, 100, outline="#6DB4EC", width=8)

        self.canvas8 = Canvas(self.tanhwindow, bg="#B5B2B0", width=250, height=500)
        self.canvas8.place(x=125, y=105)

        self.canvas9 = Canvas(self.tanhwindow, width=450, bg="#B5B2B0", height=500)
        self.canvas9.place(x=425, y=105)

        self.i = self.canvas8.create_text(125, 25, fill="black", font=("Times 20"),
                                          text=" PARAMETERS ")
        self.r = self.canvas8.create_rectangle(self.canvas8.bbox(self.i), fill="#6DB4EC", outline="#6DB4EC")
        self.canvas8.tag_lower(self.r, self.i)

        self.image7 = ImageTk.PhotoImage(Image.open("Images/tanhformula.png"))
        self.canvas8.create_image(5, 50, anchor=NW, image=self.image7)

        self.i = self.canvas8.create_text(125, 225, fill="black", font=("Times 20"),
                                          text="  Input Value  ")
        self.r = self.canvas8.create_rectangle(self.canvas8.bbox(self.i), fill="#6DB4EC", outline="#6DB4EC")
        self.canvas8.tag_lower(self.r, self.i)

        self.tb5 = Text(self.canvas8, height=3, width=26)
        self.tb5.place(x=20, y=250)
        self.tb5.bind("<Return>", self.updatetanh)

        self.i = self.canvas8.create_text(125, 375, fill="black", font=("Times 20"),
                                          text="  Output Value  ")
        self.r = self.canvas8.create_rectangle(self.canvas8.bbox(self.i), fill="#6DB4EC", outline="#6DB4EC")
        self.canvas8.tag_lower(self.r, self.i)

        self.tb6 = Text(self.canvas8, height=3, width=26)
        self.tb6.place(x=20, y=410)

        self.i = self.canvas9.create_text(225, 25, fill="black", font=("Times 20"),
                                          text="  GRAPH  ")
        self.r = self.canvas9.create_rectangle(self.canvas9.bbox(self.i), fill="#6DB4EC", outline="#6DB4EC")
        self.canvas9.tag_lower(self.r, self.i)

        self.button11 = Button(self.tanhwindow, text="Get", command=self.gettanh, anchor=CENTER)
        self.button11.configure(width=5, activebackground="#33B5E5", bg='#6DB4EC', relief=RAISED)
        self.button11_window = self.canvas8.create_window(25, 315, anchor=NW, window=self.button11)
        font1 = font.Font(family='Times New Roman', size=12, weight='normal')
        self.button11['font'] = font1
        self.button11.config(width=5, height=1)

        self.button22 = Button(self.tanhwindow, text="Update", command=self.updatetanh, anchor=CENTER)
        self.button22.configure(width=5, activebackground="#33B5E5", bg='#6DB4EC', relief=RAISED)
        self.button22_window = self.canvas8.create_window(100, 315, anchor=NW, window=self.button22)
        font1 = font.Font(family='Times New Roman', size=12, weight='normal')
        self.button22['font'] = font1
        self.button22.config(width=5, height=1)

        self.fig, self.ax1 = plt.subplots(figsize=(4, 4))
        self.ax1.spines['left'].set_position('center')
        self.ax1.spines['bottom'].set_position('center')
        self.ax1.spines['right'].set_color('none')
        self.ax1.spines['top'].set_color('none')
        self.ax1.xaxis.set_ticks_position('bottom')
        self.ax1.yaxis.set_ticks_position('left')

        self.canvas9 = FigureCanvasTkAgg(self.fig, self.canvas9)
        self.canvas9.get_tk_widget().place(x=25, y=50)

        self.tanhwindow.protocol("WM_DELETE_WINDOW", root.destroy)

        self.tanhwindow.withdraw()

        self.reluwindow = Toplevel()
        
        self.reluwindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas10 = Canvas(self.reluwindow, width=1000, height=650)
        self.canvas10.pack()

        self.canvas23 = Canvas(self.reluwindow, width=500, height=65)
        self.canvas23.place(x=250, y=25)

        self.image8 = ImageTk.PhotoImage(Image.open("Images/bg.png"))
        self.canvas10.create_image(0, 0, anchor=NW, image=self.image8)

        self.i = self.canvas23.create_text(250, 35, fill="black", font=("Times 20 italic bold", 32),
                                           text="RELU")
        self.r = self.canvas23.create_rectangle(self.canvas.bbox(ALL), fill="#6DB4EC")
        self.canvas23.tag_lower(self.r, self.i)

        self.button12 = Button(self.reluwindow, text="HOME", foreground="white", command=self.reluwinhome,
                               anchor=CENTER)
        self.button12.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button12_window = self.canvas10.create_window(60, 20, anchor=NW, window=self.button12)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button12['font'] = font1
        self.button12.config(width=10, height=1)

        self.button13 = Button(self.reluwindow, text="BACK", foreground="white", command=self.reluwinback,
                               anchor=CENTER)
        self.button13.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button13_window = self.canvas10.create_window(800, 20, anchor=NW, window=self.button13)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button13['font'] = font1
        self.button13.config(width=10, height=1)

        self.canvas10.create_rectangle(900, 625, 110, 100, outline="#6DB4EC", width=8)

        self.canvas11 = Canvas(self.reluwindow, bg="#B5B2B0", width=250, height=500)
        self.canvas11.place(x=125, y=105)

        self.canvas12 = Canvas(self.reluwindow, bg="#B5B2B0", width=450, height=500)
        self.canvas12.place(x=425, y=105)

        self.i = self.canvas11.create_text(125, 25, fill="black", font=("Times 20"),
                                           text=" PARAMETERS ")
        self.r = self.canvas11.create_rectangle(self.canvas11.bbox(self.i), fill="#6DB4EC", outline="#6DB4EC")
        self.canvas11.tag_lower(self.r, self.i)

        self.image9 = ImageTk.PhotoImage(Image.open("Images/reluformula.png"))
        self.canvas11.create_image(5, 50, anchor=NW, image=self.image9)

        self.i = self.canvas11.create_text(125, 225, fill="black", font=("Times 20"),
                                           text="  Input Value  ")
        self.r = self.canvas11.create_rectangle(self.canvas11.bbox(self.i), fill="#6DB4EC", outline="#6DB4EC")
        self.canvas11.tag_lower(self.r, self.i)

        self.tb1 = Text(self.canvas11, height=3, width=26)
        self.tb1.place(x=20, y=250)
        self.tb1.bind("<Return>", self.updaterelu)

        self.i = self.canvas11.create_text(125, 375, fill="black", font=("Times 20"),
                                           text="  Output Value  ")
        self.r = self.canvas11.create_rectangle(self.canvas11.bbox(self.i), fill="#6DB4EC", outline="#6DB4EC")
        self.canvas11.tag_lower(self.r, self.i)

        self.tb2 = Text(self.canvas11, height=3, width=26)
        self.tb2.place(x=20, y=410)

        self.i = self.canvas12.create_text(225, 25, fill="black", font=("Times 20"),
                                           text="  GRAPH  ")
        self.r = self.canvas12.create_rectangle(self.canvas12.bbox(self.i), fill="#6DB4EC", outline="#6DB4EC")
        self.canvas12.tag_lower(self.r, self.i)

        self.button14 = Button(self.reluwindow, text="Get", command=self.getrelu, anchor=CENTER)
        self.button14.configure(width=5, activebackground="#33B5E5", bg='#6DB4EC', relief=RAISED)
        self.button14_window = self.canvas11.create_window(25, 315, anchor=NW, window=self.button14)
        font1 = font.Font(family='Times New Roman', size=12, weight='normal')
        self.button14['font'] = font1
        self.button14.config(width=5, height=1)

        self.button23 = Button(self.reluwindow, text="Update", command=self.updaterelu, anchor=CENTER)
        self.button23.configure(width=5, activebackground="#33B5E5", bg='#6DB4EC', relief=RAISED)
        self.button23_window = self.canvas11.create_window(100, 315, anchor=NW, window=self.button23)
        font1 = font.Font(family='Times New Roman', size=12, weight='normal')
        self.button23['font'] = font1
        self.button23.config(width=5, height=1)

        self.fig, self.ax2 = plt.subplots(figsize=(4, 4))
        self.ax2.spines['left'].set_position('center')
        self.ax2.spines['bottom'].set_position('center')
        self.ax2.spines['right'].set_color('none')
        self.ax2.spines['top'].set_color('none')
        self.ax2.xaxis.set_ticks_position('bottom')
        self.ax2.yaxis.set_ticks_position('left')

        self.canvas12 = FigureCanvasTkAgg(self.fig, self.canvas12)
        self.canvas12.get_tk_widget().place(x=25, y=50)

        self.reluwindow.protocol("WM_DELETE_WINDOW", root.destroy)

        self.reluwindow.withdraw()

        self.sigmoidwin = Toplevel()
        
        self.sigmoidwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas13 = Canvas(self.sigmoidwin, width=1000, height=650)
        self.canvas13.pack()

        self.canvas24 = Canvas(self.sigmoidwin, width=500, height=65)
        self.canvas24.place(x=250, y=25)

        self.image10 = ImageTk.PhotoImage(Image.open("Images/bg.png"))
        self.canvas13.create_image(0, 0, anchor=NW, image=self.image10)

        self.i = self.canvas24.create_text(250, 35, fill="black", font=("Times 20 italic bold", 32),
                                           text="SIGMOID")
        self.r = self.canvas24.create_rectangle(self.canvas.bbox(ALL), fill="#6DB4EC")
        self.canvas24.tag_lower(self.r, self.i)

        self.button15 = Button(self.sigmoidwin, text="HOME", foreground="white", command=self.sigmoidwinhome,
                               anchor=CENTER)
        self.button15.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button15_window = self.canvas13.create_window(60, 20, anchor=NW, window=self.button15)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button15['font'] = font1
        self.button15.config(width=10, height=1)

        self.button16 = Button(self.sigmoidwin, text="BACK", foreground="white", command=self.sigmoidwinback,
                               anchor=CENTER)
        self.button16.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button16_window = self.canvas13.create_window(800, 20, anchor=NW, window=self.button16)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button16['font'] = font1
        self.button16.config(width=10, height=1)

        self.canvas13.create_rectangle(900, 625, 110, 100, outline="#6DB4EC", width=8)

        self.canvas14 = Canvas(self.sigmoidwin, bg="#B5B2B0", width=250, height=500)
        self.canvas14.place(x=125, y=105)

        self.canvas15 = Canvas(self.sigmoidwin, bg="#B5B2B0", width=450, height=500)
        self.canvas15.place(x=425, y=105)

        self.i = self.canvas14.create_text(125, 25, fill="black", font=("Times 20"),
                                           text=" PARAMETERS ")
        self.r = self.canvas14.create_rectangle(self.canvas14.bbox(self.i), fill="#6DB4EC", outline="#6DB4EC")
        self.canvas14.tag_lower(self.r, self.i)

        self.image11 = ImageTk.PhotoImage(Image.open("Images/sigmoidformula.png"))
        self.canvas14.create_image(5, 50, anchor=NW, image=self.image11)

        self.i = self.canvas14.create_text(125, 225, fill="black", font=("Times 20"),
                                           text="  Input Value  ")
        self.r = self.canvas14.create_rectangle(self.canvas14.bbox(self.i), fill="#6DB4EC", outline="#6DB4EC")
        self.canvas14.tag_lower(self.r, self.i)

        self.tb7 = Text(self.canvas14, height=3, width=26)
        self.tb7.place(x=20, y=250)
        self.tb7.bind("<Return>", self.updatesigmoid)

        self.i = self.canvas14.create_text(125, 375, fill="black", font=("Times 20"),
                                           text="  Output Value  ")
        self.r = self.canvas14.create_rectangle(self.canvas14.bbox(self.i), fill="#6DB4EC", outline="#6DB4EC")
        self.canvas14.tag_lower(self.r, self.i)

        self.tb8 = Text(self.canvas14, height=3, width=26)
        self.tb8.place(x=20, y=410)

        self.i = self.canvas15.create_text(225, 25, fill="black", font=("Times  20"),
                                           text="  GRAPH  ")
        self.r = self.canvas15.create_rectangle(self.canvas15.bbox(self.i), fill="#6DB4EC", outline="#6DB4EC")
        self.canvas15.tag_lower(self.r, self.i)

        self.button17 = Button(self.sigmoidwin, text="Get", command=self.getsigmoid, anchor=CENTER)
        self.button17.configure(width=5, activebackground="#33B5E5", bg='#6DB4EC', relief=RAISED)
        self.button17_window = self.canvas14.create_window(25, 315, anchor=NW, window=self.button17)
        font1 = font.Font(family='Times New Roman', size=12, weight='normal')
        self.button17['font'] = font1
        self.button17.config(width=5, height=1)

        self.button24 = Button(self.sigmoidwin, text="Update", command=self.updatesigmoid, anchor=CENTER)
        self.button24.configure(width=5, activebackground="#33B5E5", bg='#6DB4EC', relief=RAISED)
        self.button24_window = self.canvas14.create_window(100, 315, anchor=NW, window=self.button24)
        font1 = font.Font(family='Times New Roman', size=12, weight='normal')
        self.button24['font'] = font1
        self.button24.config(width=5, height=1)

        self.fig, self.ax = plt.subplots(figsize=(4, 4))
        self.ax.spines['left'].set_position('center')
        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')
        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')

        self.canvas15 = FigureCanvasTkAgg(self.fig, self.canvas15)
        self.canvas15.get_tk_widget().place(x=25, y=50)

        self.sigmoidwin.protocol("WM_DELETE_WINDOW", root.destroy)

        self.sigmoidwin.withdraw()

        self.leakyreluwin = Toplevel()
        
        self.leakyreluwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas16 = Canvas(self.leakyreluwin, width=1000, height=650)
        self.canvas16.pack()

        self.canvas25 = Canvas(self.leakyreluwin, width=500, height=65)
        self.canvas25.place(x=250, y=25)

        self.image12 = ImageTk.PhotoImage(Image.open("Images/bg.png"))
        self.canvas16.create_image(0, 0, anchor=NW, image=self.image12)

        self.i = self.canvas25.create_text(250, 35, fill="black", font=("Times 20 italic bold", 32),
                                           text="Leaky RELU")
        self.r = self.canvas25.create_rectangle(self.canvas.bbox(ALL), fill="#6DB4EC")
        self.canvas25.tag_lower(self.r, self.i)

        self.button18 = Button(self.leakyreluwin, text="HOME", foreground="white", command=self.leakyreluhome,
                               anchor=CENTER)
        self.button18.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button18_window = self.canvas16.create_window(60, 20, anchor=NW, window=self.button18)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button18['font'] = font1
        self.button18.config(width=10, height=1)

        self.button19 = Button(self.leakyreluwin, text="BACK", foreground="white", command=self.leakyreluback,
                               anchor=CENTER)
        self.button19.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button19_window = self.canvas16.create_window(800, 20, anchor=NW, window=self.button19)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button19['font'] = font1
        self.button19.config(width=10, height=1)

        self.canvas16.create_rectangle(900, 625, 110, 100, outline="#6DB4EC", width=8)

        self.canvas17 = Canvas(self.leakyreluwin, bg="#B5B2B0", width=250, height=500)
        self.canvas17.place(x=125, y=105)

        self.canvas18 = Canvas(self.leakyreluwin, bg="#B5B2B0", width=450, height=500)
        self.canvas18.place(x=425, y=105)

        self.i = self.canvas17.create_text(125, 25, fill="black", font=("Times 20"),
                                           text=" PARAMETERS ")
        self.r = self.canvas17.create_rectangle(self.canvas17.bbox(self.i), fill="#6DB4EC", outline="#6DB4EC")
        self.canvas17.tag_lower(self.r, self.i)

        self.image13 = ImageTk.PhotoImage(Image.open("Images/leakyreluformula.png"))
        self.canvas17.create_image(5, 50, anchor=NW, image=self.image13)

        self.i = self.canvas17.create_text(125, 225, fill="black", font=("Times 20"),
                                           text="  Input Value  ")
        self.r = self.canvas17.create_rectangle(self.canvas17.bbox(self.i), fill="#6DB4EC", outline="#6DB4EC")
        self.canvas17.tag_lower(self.r, self.i)

        self.tb9 = Text(self.canvas17, height=3, width=26)
        self.tb9.place(x=20, y=250)
        self.tb9.bind("<Return>", self.updateleakyrelu)

        self.i = self.canvas17.create_text(125, 375, fill="black", font=("Times 20"),
                                           text="  Output Value  ")
        self.r = self.canvas17.create_rectangle(self.canvas17.bbox(self.i), fill="#6DB4EC", outline="#6DB4EC")
        self.canvas17.tag_lower(self.r, self.i)

        self.tb10 = Text(self.canvas17, height=3, width=26)
        self.tb10.place(x=20, y=410)

        self.i = self.canvas18.create_text(225, 25, fill="black", font=("Times 20"),
                                           text="  GRAPH  ")
        self.r = self.canvas18.create_rectangle(self.canvas18.bbox(self.i), fill="#6DB4EC", outline="#6DB4EC")
        self.canvas18.tag_lower(self.r, self.i)

        self.button20 = Button(self.leakyreluwin, text="Get", command=self.getleakyrelu, anchor=CENTER)
        self.button20.configure(width=5, activebackground="#33B5E5", bg='#6DB4EC', relief=RAISED)
        self.button20_window = self.canvas17.create_window(25, 315, anchor=NW, window=self.button20)
        font1 = font.Font(family='Times New Roman', size=12, weight='normal')
        self.button20['font'] = font1
        self.button20.config(width=5, height=1)

        self.button25 = Button(self.leakyreluwin, text="Update", command=self.updateleakyrelu, anchor=CENTER)
        self.button25.configure(width=5, activebackground="#33B5E5", bg='#6DB4EC', relief=RAISED)
        self.button25_window = self.canvas17.create_window(100, 315, anchor=NW, window=self.button25)
        font1 = font.Font(family='Times New Roman', size=12, weight='normal')
        self.button25['font'] = font1
        self.button25.config(width=5, height=1)

        self.fig, self.ax3 = plt.subplots(figsize=(4, 4))
        self.ax3.spines['left'].set_position('center')
        self.ax3.spines['bottom'].set_position('center')
        self.ax3.spines['right'].set_color('none')
        self.ax3.spines['top'].set_color('none')
        self.ax3.xaxis.set_ticks_position('bottom')
        self.ax3.yaxis.set_ticks_position('left')

        self.canvas18 = FigureCanvasTkAgg(self.fig, self.canvas18)
        self.canvas18.get_tk_widget().place(x=25, y=50)

        self.leakyreluwin.protocol("WM_DELETE_WINDOW", root.destroy)

        self.leakyreluwin.withdraw()

    def home(self):
        '''This is secondwindow home button. It calls master window'''
        self.secondWin.withdraw()
        self.master.deiconify()

    def thirdwinhome(self):
        '''It calls master window from thirdwindow'''

        def onclick():
            root.quit()
            self.master.withdraw()

        self.master.protocol("WM_DELETE_WINDOW", onclick)

        self.ThirdWin.withdraw()
        self.master.deiconify()

    def sigmoidwinhome(self):
        def onclick():
            root.quit()
            self.master.withdraw()

        self.master.protocol("WM_DELETE_WINDOW", onclick)

        '''It calls master window from sigmoind window'''
        self.sigmoidwin.withdraw()
        self.master.deiconify()

    def sigmoidwinback(self):
        def onclick():
            root.quit()
            self.ThirdWin.withdraw()

        self.ThirdWin.protocol("WM_DELETE_WINDOW", onclick)

        '''It calls third window from sigmoid window'''
        self.sigmoidwin.withdraw()
        self.ThirdWin.deiconify()

    def tanhwinhome(self):
        def onclick():
            root.quit()
            self.master.withdraw()

        self.master.protocol("WM_DELETE_WINDOW", onclick)

        '''It calls master window from tanh window'''
        self.tanhwindow.withdraw()
        self.master.deiconify()

    def tanhwinback(self):
        def onclick():
            root.quit()
            self.ThirdWin.withdraw()

        self.ThirdWin.protocol("WM_DELETE_WINDOW", onclick)

        '''It calls third window from tanh window'''
        self.tanhwindow.withdraw()
        self.ThirdWin.deiconify()

    def reluwinhome(self):
        def onclick():
            root.quit()
            self.master.withdraw()

        self.master.protocol("WM_DELETE_WINDOW", onclick)

        '''It calls master window from relu window'''
        self.reluwindow.withdraw()
        self.master.deiconify()

    def reluwinback(self):
        def onclick():
            root.quit()
            self.ThirdWin.withdraw()

        self.ThirdWin.protocol("WM_DELETE_WINDOW", onclick)

        '''It calls third window from relu window'''
        self.reluwindow.withdraw()
        self.ThirdWin.deiconify()

    def leakyreluhome(self):
        def onclick():
            root.quit()
            self.master.withdraw()

        self.master.protocol("WM_DELETE_WINDOW", onclick)

        '''It calls master window from leaky relu window'''
        self.leakyreluwin.withdraw()
        self.master.deiconify()

    def leakyreluback(self):
        def onclick():
            root.quit()
            self.ThirdWin.withdraw()

        self.ThirdWin.protocol("WM_DELETE_WINDOW", onclick)

        '''It calls third window from leaky relu window'''
        self.leakyreluwin.withdraw()
        self.ThirdWin.deiconify()

    def softmaxhome(self):
        def onclick():
            root.quit()
            self.master.withdraw()

        self.master.protocol("WM_DELETE_WINDOW", onclick)

        '''It calls master window from softmax window'''
        self.softmaxwin.withdraw()
        self.master.deiconify()

    def softmaxback(self):
        def onclick():
            root.quit()
            self.ThirdWin.withdraw()

        self.ThirdWin.protocol("WM_DELETE_WINDOW", onclick)

        '''It calls third window from softmax window'''
        self.softmaxwin.withdraw()
        self.ThirdWin.deiconify()

    def clicktostart(self):
        '''This is the start page button fuction. It takes to the Second page (About page) of the application'''

        def onclick():
            root.quit()
            self.secondWin.withdraw()

        self.secondWin.protocol("WM_DELETE_WINDOW", onclick)
        self.secondWin.resizable(width=False, height=False)
        self.master.withdraw()
        self.secondWin.deiconify()

    def clickforhelp(self):
        '''It shows message box what exactly the application does.'''
        tkinter.messagebox.showinfo("Info", "This is completely about Activation Functions! \
Press Button 'Click to Begin' to start")

    def clicktobegin(self):
        '''It takes you to the Third window where the all Activation Functions there.'''

        def onclick():
            root.quit()
            self.ThirdWin.withdraw()

        self.ThirdWin.protocol("WM_DELETE_WINDOW", onclick)
        self.ThirdWin.resizable(width=False, height=False)
        self.secondWin.withdraw()
        self.ThirdWin.deiconify()

    def back(self):
        '''This is third window back button function. It takes you to Second window.(About page)'''
        self.ThirdWin.withdraw()
        self.secondWin.deiconify()

    # Now the following functions are present in the Third window as image buttons.

    # Sigmoid Function

    def sigmoid(self):
        '''It takes you to sigmoid page'''

        def onclick():
            root.quit()
            self.sigmoidwin.withdraw()
        self.sigmoidwin.protocol("WM_DELETE_WINDOW", onclick)
        global ax
        self.input = np.linspace(-25,25,100)
        self.output = self.function_generator.sigmoid_input(self.input)
        self.tb7.delete('1.0', END)
        self.tb8.delete('1.0', END)

        self.ax.cla()
        self.ax.clear()
        self.ax.grid()
        self.ax.plot(self.input, self.output, color = "deepskyblue", linewidth=3, label="sigmoid")
        self.canvas15.draw()
        self.button17.config(state="normal")
        self.button24.config(state="disabled")
        self.sigmoidwin.resizable(width=False, height=False)
        self.ThirdWin.withdraw()
        self.sigmoidwin.deiconify()

    def getsigmoid(self):
        def onclick():
            root.quit()
            self.sigmoidwin.withdraw()

        self.sigmoidwin.protocol("WM_DELETE_WINDOW", onclick)

        '''This is the function for generating sigmoid graph'''

        global list, list1, z

        list = []
        list1 = []
        list = self.tb7.get("1.0", 'end-1c').split(',')
        try:
            list1 = [float(i) for i in list]

            
            list1.sort()
            if max(list1) > 25.0 or min(list1) < -25.0:
                raise AttributeError

            x = np.array(list1)
            z = self.function_generator.sigmoid_input(x)

            # Ploting Points
            
            self.ax.scatter(x, z, color="tomato", linewidth=5, label="sigmoid",marker = "o")
            self.ax.plot(self.input, self.output, color = "deepskyblue", linewidth=3, label="sigmoid")
            
            
            self.tb8.insert(END, z)

            # Placing the Graph in the canvas
            self.canvas15.draw()
            self.button17.config(state="disabled")
            self.button24.config(state="normal")
        except ValueError:
            tkinter.messagebox.showinfo("Invalid Parameter",
                                        "Please enter Integer or Float value. For Example - 2.5 or 2")
        except AttributeError:
            tkinter.messagebox.showinfo("Invalid Data",
                                        "Please enter value in the range of -25 to 25")
            

    def updatesigmoid(self, *args):
        def onclick():
            root.quit()
            self.sigmoidwin.withdraw()

        self.sigmoidwin.protocol("WM_DELETE_WINDOW", onclick)

        '''This is update function of sigmoid when user changes input'''

        list = self.tb7.get("1.0", 'end-1c').split(',')
        try:
            list1 = [float(i) for i in list]
            #print(list)
            list1.sort()
            if max(list1) > 25.0 or min(list1) < -25.0:
                raise AttributeError
            self.ax.cla()
            x = np.array(list1)
            z = self.function_generator.sigmoid_input(x)

            self.tb8.delete('1.0', END)
            self.tb8.insert(END, z)

            # Updating points
            self.ax.grid()
            self.ax.plot(self.input, self.output, color = "deepskyblue", linewidth=3, label="sigmoid")
            self.ax.scatter(x, z, color="tomato", linewidth=5, label="sigmoid")
            # Update Graph in the Canvas
            self.canvas15.draw()
        except ValueError:
            tkinter.messagebox.showinfo("Invalid Parameter",
                                        "Please enter Integer or Float value. For Example - 2.5 or 2")
        except AttributeError:
            tkinter.messagebox.showinfo("Invalid Data",
                                        "Please enter value in the range of -25 to 25")

    # Tanh Function

    def tanh(self):
        '''It takes you to tanh page'''

        def onclick():
            root.quit()
            self.tanhwindow.withdraw()

        self.tanhwindow.protocol("WM_DELETE_WINDOW", onclick)
        global ax1

        plot_input = np.linspace(-25,25,100)
        plot_output = self.function_generator.tanh(plot_input)

        self.tb5.delete('1.0', END)
        self.tb6.delete('1.0', END)

        self.ax1.cla()
        self.ax1.clear()
        self.ax1.grid()
        self.ax1.plot(plot_input,plot_output,color = "deepskyblue", linewidth=3)
        self.canvas9.draw()
        self.button11.config(state="normal")
        self.button22.config(state="disabled")
        self.tanhwindow.resizable(width=False, height=False)
        self.ThirdWin.withdraw()
        self.tanhwindow.deiconify()

    def gettanh(self):
        def onclick():
            root.quit()
            self.tanhwindow.withdraw()

        self.tanhwindow.protocol("WM_DELETE_WINDOW", onclick)

        '''This is the function for generating Tanh graph'''

        global list, list1, z
        list = []
        list1 = []
        list = self.tb5.get("1.0", 'end-1c').split(',')
        try:
            list1 = [float(i) for i in list]
            list1.sort()
            if max(list1) > 25.0 or min(list1) < -25.0:
                raise AttributeError

            plot_input = np.linspace(-25,25,100)
            #print(plot_input)
            plot_output = self.function_generator.tanh(plot_input)
            #print(plot_output)
            x = np.array(list1)
            z = self.function_generator.tanh(x)

            self.tb6.insert(END, z)

            # Ploting Points
            
            self.ax1.plot(plot_input,plot_output,color = "deepskyblue", linewidth=3)
            self.ax1.scatter(x, z, color="tomato", linewidth=5, label="tanh")
            # Placing graph in the canvas

            self.canvas9.draw()
            self.button11.config(state="disabled")
            self.button22.config(state="normal")
        except ValueError:
            tkinter.messagebox.showinfo("Invalid Parameter",
                                        "Please enter Integer or Float value. For Example - 2.5 or 2")
        except AttributeError:
            tkinter.messagebox.showinfo("Invalid Data",
                                        "Please enter value in the range of -25 to 25")

    def updatetanh(self, *args):
        def onclick():
            root.quit()
            self.tanhwindow.withdraw()

        self.tanhwindow.protocol("WM_DELETE_WINDOW", onclick)

        '''This is update function of Tanh when user changes input'''

        list = self.tb5.get("1.0", 'end-1c').split(',')
        try:
            list1 = [float(i) for i in list]
            #print(list)
            list1.sort()
            if max(list1) > 25.0 or min(list1) < -25.0:
                raise AttributeError
            self.ax1.cla()

            x = np.array(list1)
            z = self.function_generator.tanh(x)

            self.tb6.delete('1.0', END)
            self.tb6.insert(END, z)
            plot_input = np.linspace(-25,25,100)
            plot_output = self.function_generator.tanh(plot_input)
            # Ploting Points
            self.ax1.grid()
            self.ax1.plot(plot_input,plot_output,color = "deepskyblue", linewidth=3)
            self.ax1.scatter(x, z, color="tomato", linewidth=5, label="tanh")
            # Update plots in canvas
            self.canvas9.draw()
        except ValueError:
            tkinter.messagebox.showinfo("Invalid Parameter",
                                        "Please enter Integer or Float value. For Example - 2.5 or 2")
        except AttributeError:
            tkinter.messagebox.showinfo("Invalid Data",
                                        "Please enter value in the range of -25 to 25")

    # Relu Function

    def relu(self):
        '''It takes you to relu page'''

        def onclick():
            root.quit()
            self.reluwindow.withdraw()

        self.reluwindow.protocol("WM_DELETE_WINDOW", onclick)
        global ax2

        self.tb1.delete('1.0', END)
        self.tb2.delete('1.0', END)

        self.ax2.cla()
        self.ax2.clear()
        self.ax2.grid()
        plot_input = np.linspace(-25,25,100)
        plot_output = self.function_generator.relu(plot_input)
        # Ploting Points
        self.ax2.plot(plot_input,plot_output,color = "deepskyblue", linewidth=3)
        self.canvas12.draw()
        self.button14.config(state="normal")
        self.button23.config(state="disabled")
        self.reluwindow.resizable(width=False, height=False)
        self.ThirdWin.withdraw()
        self.reluwindow.deiconify()

    def getrelu(self):

        def onclick():
            root.quit()
            self.reluwindow.withdraw()

        self.reluwindow.protocol("WM_DELETE_WINDOW", onclick)

        '''This is the function for generating relu graph'''
        global list, list1, z, input, output
        list = []
        list1 = []
        list = self.tb1.get("1.0", 'end-1c').split(',')
        try:
            list1 = [float(i) for i in list]
            list1.sort()
            if max(list1) > 25.0 or min(list1) < -25.0:
                raise AttributeError

            def relu(x):  # Relu Formula
                return np.maximum(0.0, x)

            input = np.array(list1)
            output = relu(input)

            self.tb2.insert(END, output)

            # Ploting Points
            plot_input = np.linspace(-25,25,100)
            plot_output = self.function_generator.relu(plot_input)
            # Ploting Points
            
            self.ax2.plot(plot_input,plot_output,color = "deepskyblue", linewidth=3)
            self.ax2.scatter(input,output, color="tomato", linewidth=5, label="relu")
            # Placing Graph in the canvas

            self.canvas12.draw()
            self.button14.config(state="disabled")
            self.button23.config(state="normal")
        except ValueError:
            tkinter.messagebox.showinfo("Invalid Parameter",
                                        "Please enter Integer or Float value. For Example - 2.5 or 2")
        except AttributeError:
            tkinter.messagebox.showinfo("Invalid Data",
                                        "Please enter value in the range of -25 to 25")

    def updaterelu(self, *args):
        def onclick():
            root.quit()
            self.reluwindow.withdraw()

        self.reluwindow.protocol("WM_DELETE_WINDOW", onclick)

        '''This is update function of relu when user changes input'''

        list = self.tb1.get("1.0", 'end-1c').split(',')
        try:
            list1 = [float(i) for i in list]
            #print(list)
            list1.sort()
            if max(list1) > 25.0 or min(list1) < -25.0:
                raise AttributeError
            self.ax2.cla()

            def relu(x):  # Relu Formula
                return np.maximum(0.0, x)

            input = np.array(list1)
            output = relu(input)

            self.tb2.delete('1.0', END)
            self.tb2.insert(END, output)

            # Ploting points
            plot_input = np.linspace(-25,25,100)
            plot_output = self.function_generator.relu(plot_input)
            # Ploting Points
            self.ax2.grid()
            self.ax2.plot(plot_input,plot_output,color = "deepskyblue", linewidth=3)
            self.ax2.scatter(input, output, color="tomato", linewidth=5, label="relu")
            # Update points in the canvas
            self.canvas12.draw()
        except ValueError:
            tkinter.messagebox.showinfo("Invalid Parameter",
                                        "Please enter Integer or Float value. For Example - 2.5 or 2")
        except AttributeError:
            tkinter.messagebox.showinfo("Invalid Data",
                                        "Please enter value in the range of -25 to 25")

    # LeakyRelu Function

    def leakyrelu(self):
        '''It takes you to leaky relu page'''

        def onclick():
            root.quit()
            self.leakyreluwin.withdraw()

        self.leakyreluwin.protocol("WM_DELETE_WINDOW", onclick)
        global ax3

        self.tb9.delete('1.0', END)
        self.tb10.delete('1.0', END)

        self.ax3.cla()
        self.ax3.clear()
        self.ax3.grid()
        plot_input = np.linspace(-25,25,100)
        plot_output = self.function_generator.leaky_relu(plot_input)
        # Ploting Points
        self.ax3.plot(plot_input,plot_output,color = "deepskyblue", linewidth=3)
        self.canvas18.draw()
        self.button20.config(state="normal")
        self.button25.config(state="disabled")
        self.leakyreluwin.resizable(width=False, height=False)
        self.ThirdWin.withdraw()
        self.leakyreluwin.deiconify()

    def getleakyrelu(self):
        def onclick():
            root.quit()
            self.leakyreluwin.withdraw()

        self.leakyreluwin.protocol("WM_DELETE_WINDOW", onclick)

        '''This is the function for generating Leaky Relu graph'''
        global list, list1, z, input, output

        list = []
        list1 = []
        list = self.tb9.get("1.0", 'end-1c').split(',')
        try:
            list1 = [float(i) for i in list]
            list1.sort()
            if max(list1) > 25.0 or min(list1) < -25.0:
                raise AttributeError

            def leakyrelu(x):  # Leaky Relu Formula
                return np.maximum(0.1*x, x)

            input = [x for x in list1]
            output = [leakyrelu(x) for x in input]

            self.tb10.insert(END, output)

            # ploting points
            plot_input = np.linspace(-25,25,100)
            plot_output = self.function_generator.leaky_relu(plot_input)
            # Ploting Points
            
            self.ax3.plot(plot_input,plot_output,color = "deepskyblue", linewidth=3)
            self.ax3.scatter(input,output, color="tomato", linewidth=5, label="leakyrelu")

            # Placing Graph in the Canvas
            self.canvas18.draw()
            self.button20.config(state="disabled")
            self.button25.config(state="normal")
        except ValueError:
            tkinter.messagebox.showinfo("Invalid Parameter",
                                        "Please enter Integer or Float value. For Example - 2.5 or 2")
        except AttributeError:
            tkinter.messagebox.showinfo("Invalid Data",
                                        "Please enter value in the range of -25 to 25")

    def updateleakyrelu(self, *args):
        def onclick():
            root.quit()
            self.leakyreluwin.withdraw()

        self.leakyreluwin.protocol("WM_DELETE_WINDOW", onclick)

        '''This is update function of Leaky Relu when user changes input'''
        list = self.tb9.get("1.0", 'end-1c').split(',')
        try:
            list1 = [float(i) for i in list]
            #print(list)
            list1.sort()
            if max(list1) > 25.0 or min(list1) < -25.0:
                raise AttributeError
            self.ax3.cla()

            def leakyrelu(x):  # Relu Formula
                return np.maximum(0.1*x, x)

            input = [x for x in list1]
            output = [leakyrelu(x) for x in input]

            self.tb10.delete('1.0', END)
            self.tb10.insert(END, output)

            # Updating Points
            plot_input = np.linspace(-25,25,100)
            plot_output = self.function_generator.leaky_relu(plot_input)
            # Ploting Points
            self.ax3.grid()
            self.ax3.plot(plot_input,plot_output,color = "deepskyblue", linewidth=3)
            self.ax3.scatter(input, output, color="tomato", linewidth=5, label="leakyrelu")

            # Update Graph in Canvas
            self.canvas18.draw()
        except ValueError:
            tkinter.messagebox.showinfo("Invalid Parameter",
                                        "Please enter Integer or Float value. For Example - 2.5 or 2")
        except AttributeError:
            tkinter.messagebox.showinfo("Invalid Data",
                                        "Please enter value in the range of -25 to 25")

    # Softmax Function

    def softmax(self):
        '''It takes you to softmax page'''

        def onclick():
            root.quit()
            self.softmaxwin.withdraw()

        self.softmaxwin.protocol("WM_DELETE_WINDOW", onclick)
        global ax4

        self.tb3.delete('1.0', END)
        self.tb4.delete('1.0', END)

        self.ax4.cla()
        self.ax4.clear()
        self.ax4.grid()
        plot_input = np.linspace(-25,25,10)
        plot_output = self.function_generator.softmax(plot_input)
        # Ploting Points
        self.ax4.plot(plot_input,plot_output,color = "deepskyblue", linewidth=3)
        self.canvas6.draw()
        self.button8.config(state="normal")
        self.button21.config(state="disabled")
        self.softmaxwin.resizable(width=False, height=False)
        self.ThirdWin.withdraw()
        self.softmaxwin.deiconify()

    def getsoftmax(self):
        def onclick():
            root.quit()
            self.softmaxwin.withdraw()

        self.softmaxwin.protocol("WM_DELETE_WINDOW", onclick)
        '''This the function for generating Softmax graph'''

        global list, list1, z
        list = []
        list1 = []
        list = self.tb3.get("1.0", 'end-1c').split(',')
        try:
            list1 = [float(i) for i in list]
            list1.sort()
            if max(list1) > 25.0 or min(list1) < -25.0:
                raise AttributeError
            self.ax4.cla()
            self.ax4.clear()
            self.ax4.grid()

            plot_input = np.linspace(-25,25,10)
            #print(plot_input)
            plot_output = self.function_generator.softmax(plot_input)
            #print(plot_output)

            # Ploting Functions
            x = np.array(list1)
            z = self.function_generator.softmax(x)

            self.tb4.insert(END, z)

            # Ploting Points
            
            self.ax4.plot(plot_input,plot_output,color = "deepskyblue", linewidth=3)
            self.ax4.scatter(x, z, color="tomato", linewidth=5, label="softmax")
            # Placing in Canvas
            self.canvas6.draw()

            self.button8.config(state="disabled")
            self.button21.config(state="normal")
        except ValueError:
            tkinter.messagebox.showinfo("Invalid Parameter",
                                        "Please enter Integer or Float value. For Example - 2.5 or 2")
        except AttributeError:
            tkinter.messagebox.showinfo("Invalid Data",
                                        "Please enter value in the range of -25 to 25")

    def updatesoftmax(self, *args):
        def onclick():
            root.quit()
            self.softmaxwin.withdraw()

        self.softmaxwin.protocol("WM_DELETE_WINDOW", onclick)
        '''This is update function of Softmax when user changes input'''

        list = self.tb3.get("1.0", 'end-1c').split(',')
        try:
            list1 = [float(i) for i in list]
            list1.sort()
            if max(list1) > 25.0 or min(list1) < -25.0:
                raise AttributeError

            #print(list)
            self.ax4.cla()

            x = np.array(list1)
            z = self.function_generator.softmax(x)

            self.tb4.delete('1.0', END)
            self.tb4.insert(END, z)

            # Ploting Functions
            plot_input = np.linspace(-25,25,10)
            #print(plot_input)
            plot_output = self.function_generator.softmax(plot_input)
            #print(plot_output)
            # Ploting Points
            self.ax4.grid()
            self.ax4.plot(plot_input,plot_output,color = "deepskyblue", linewidth=3)
            self.ax4.scatter(x, z, color="tomato", linewidth=5, label="softmax")
            # Display the Updated graph in Canvas
            self.canvas6.draw()
        except ValueError:
            tkinter.messagebox.showinfo("Invalid Parameter",
                                        "Please enter Integer or Float value. For Example - 2.5 or 2")
        except AttributeError:
            tkinter.messagebox.showinfo("Invalid Data",
                                        "Please enter value in the range of -25 to 25")


class Activation_functions:

    def sigmoid_input(self,input_point):
        output =  1 / (1 + np.exp(-input_point))
        return output

    def tanh(self,input):
        output = (np.exp(input) - np.exp(-input)) / (np.exp(input) + np.exp(-input))
        return output

    def relu(self,input):
        return np.maximum(0.0, input)

    def leaky_relu(self, input):
        return np.maximum(0.1*input,input)

    def softmax(self, input):
        output = np.exp(input) / float(sum(np.exp(input)))
        return output

if __name__ == "__main__":
    root = Tk()
    myApp = Activation(root)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(width=False, height=False)
    root.mainloop()
