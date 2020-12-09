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


class Visualization:
    ''' Initial class that act as master of App'''

    def __init__(self, master):

        #This is for all Window Position

        global w,h,ws,hs,x,y

        w = 1000
        h = 650
        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen
        x = (ws/4) - (w/4)
        y = (hs/4) - (h/4)
        
        self.master = master

        master.title("HEU Technologies - Data Visualization")
        def onclick():
            root.quit()
            self.master.withdraw()
        self.master.protocol("WM_DELETE_WINDOW", onclick)

        self.canvas = Canvas(self.master, width=1000, height=650)
        self.canvas.pack()

        self.image = ImageTk.PhotoImage(Image.open("Images/Background.png"))
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)

        self.image1 = ImageTk.PhotoImage(Image.open("Images/logo.png"))
        self.canvas.create_image(500, 650, anchor=S, image=self.image1)

        self.canvas1 = Canvas(self.master, width=750, height=75)
        self.canvas1.place(x=150, y=20)

        self.i = self.canvas1.create_text(375, 38, fill="white",
                                          font=("Times New Roman 20 bold", 48),
                                          text="DATA VISUALIZATION")

        self.r = self.canvas1.create_rectangle(self.canvas.bbox(ALL),
                                               fill="#6C9CEE")
        self.canvas1.tag_lower(self.r, self.i)

        self.button1 = Button(self.master, text="Click to Continue",
                              foreground="white", command=self.clicktocontinue,
                              anchor=CENTER)

        self.button1.configure(width=30, activebackground="#7077E9",
                               bg='#574BD1', relief=FLAT)
        self.button1_window = self.canvas.create_window(400, 350, anchor=W,
                                                        window=self.button1)
        font1 = font.Font(family='Times New Roman', size=20, weight='normal')
        self.button1['font'] = font1
        self.button1.config(width=15, height=1)

        self.secondWin = Toplevel()

        self.secondWin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas2 = Canvas(self.secondWin, width=1000, height=650)
        self.canvas2.pack()

        self.image2 = ImageTk.PhotoImage(Image.open("Images/Background.png"))
        self.canvas2.create_image(0, 0, anchor=NW, image=self.image2)

        self.canvas2.create_text(100, 75, fill="black",
                                 font=("Times New Roman 20 bold", 32),
                                 text="About:")

        para = ("\n"
                "Understand different types of data visualization techniques used in\n"
                "Artificial Intelligence")

        para1 = ("\n"
                 "* Scatter Plot\n"
                 "* Line Plot\n"
                 "* Bar Plot\n"
                 "* Pie Plot\n"
                 "* Histogram\n"
                 "* Signal Plotting")

        self.canvas2.create_text(450, 150, fill="black", font=("Times", 18),
                                 text=para)
        self.canvas2.create_text(450, 250, fill="black",
                                 font=("Times bold", 26),
                                 text="Types of Plots")
        self.canvas2.create_text(200, 350, fill="black", font=("Times", 18),
                                 text=para1)

        self.button2 = Button(self.secondWin, text="Click for Help",
                              command=self.clickforhelp, anchor=CENTER)
        self.button2.configure(width=10, activebackground="#33B5E5",
                               bg='#578EE8', relief=FLAT)
        self.button2_window = self.canvas2.create_window(100, 500, anchor=NW,
                                                         window=self.button2)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button2['font'] = font1
        self.button2.config(width=12, height=2)

        self.button3 = Button(self.secondWin, text="HOME", command=self.home,
                              anchor=CENTER)
        self.button3.configure(width=10, activebackground="#33B5E5",
                               bg='#578EE8', relief=FLAT)
        self.button3_window = self.canvas2.create_window(400, 500, anchor=NW,
                                                         window=self.button3)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button3['font'] = font1
        self.button3.config(width=12, height=2)

        self.button4 = Button(self.secondWin, text="Click to Begin",
                              command=self.clicktobegin, anchor=CENTER)
        self.button4.configure(width=10, activebackground="#33B5E5",
                               bg='#578EE8', relief=FLAT)
        self.button4_window = self.canvas2.create_window(700, 500, anchor=NW,
                                                         window=self.button4)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button4['font'] = font1
        self.button4.config(width=12, height=2)

        self.secondWin.protocol("WM_DELETE_WINDOW", root.destroy)

        self.secondWin.withdraw()

        self.ThirdWin = Toplevel()

        self.ThirdWin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas3 = Canvas(self.ThirdWin, width=1000, height=650)
        self.canvas3.pack()

        self.image11 = ImageTk.PhotoImage(Image.open("Images/Background.png"))
        self.canvas3.create_image(0, 0, anchor=NW, image=self.image11)

        self.canvas4 = Canvas(self.ThirdWin, width=500, height=65)
        self.canvas4.place(x=250, y=50)

        self.i = self.canvas4.create_text(250, 35, fill="black",
                                          font=("Times New Roman 20", 32),
                                          text="HELP")
        self.r = self.canvas4.create_rectangle(self.canvas.bbox(ALL),
                                               fill="#6DB4EA")
        self.canvas4.tag_lower(self.r, self.i)

        self.button5 = Button(self.ThirdWin, foreground="white", text="HOME",
                              command=self.thirdwinhome,
                              anchor=CENTER)
        self.button5.configure(width=10, activebackground="#33B5E5",
                               bg='#2C56BC', relief=FLAT)
        self.button5_window = self.canvas3.create_window(60, 40, anchor=NW,
                                                         window=self.button5)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button5['font'] = font1
        self.button5.config(width=10, height=1)

        self.button6 = Button(self.ThirdWin, foreground="white", text="BACK",
                              command=self.back, anchor=CENTER)
        self.button6.configure(width=10, activebackground="#33B5E5",
                               bg='#2C56BC', relief=FLAT)
        self.button6_window = self.canvas3.create_window(800, 40, anchor=NW,
                                                         window=self.button6)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button6['font'] = font1
        self.button6.config(width=10, height=1)

        self.canvas3.create_rectangle(900, 625, 110, 150, outline="#6DB4EA",
                                      width=8)

        self.image4 = ImageTk.PhotoImage(Image.open("Images/visual.png"))
        self.canvas3.create_image(300, 200, anchor=NW, image=self.image4)

        self.ThirdWin.protocol("WM_DELETE_WINDOW", root.destroy)

        self.ThirdWin.withdraw()

        self.forthwin = Toplevel()

        self.forthwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas4 = Canvas(self.forthwin, width=1000, height=650)
        self.canvas4.pack()

        self.image3 = ImageTk.PhotoImage(Image.open("Images/Background.png"))
        self.canvas4.create_image(0, 0, anchor=NW, image=self.image3)

        self.canvas5 = Canvas(self.forthwin, width=500, height=65)
        self.canvas5.place(x=250, y=50)

        self.i = self.canvas5.create_text(250, 35, fill="black",
                                          font=("Times New Roman 20", 32),
                                          text="PLOTS")
        self.r = self.canvas5.create_rectangle(self.canvas.bbox(ALL),
                                               fill="#6DB4EA")
        self.canvas5.tag_lower(self.r, self.i)

        self.button5 = Button(self.forthwin, foreground="white", text="HOME",
                              command=self.forthwinhome,
                              anchor=CENTER)
        self.button5.configure(width=10, activebackground="#33B5E5",
                               bg='#2C56BC', relief=FLAT)
        self.button5_window = self.canvas4.create_window(60, 40, anchor=NW,
                                                         window=self.button5)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button5['font'] = font1
        self.button5.config(width=10, height=1)

        self.button6 = Button(self.forthwin, foreground="white", text="BACK",
                              command=self.forthwinback, anchor=CENTER)
        self.button6.configure(width=10, activebackground="#33B5E5",
                               bg='#2C56BC', relief=FLAT)
        self.button6_window = self.canvas4.create_window(800, 40, anchor=NW,
                                                         window=self.button6)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button6['font'] = font1
        self.button5.config(width=10, height=1)

        self.photo = ImageTk.PhotoImage(Image.open("Images/scatter.png"))
        self.scatter = Button(self.forthwin, height=210, width=165,
                              text="Scatter Plot", compound="top", bg="#69A7FF",
                              font=('Times New Roman', 18), foreground='white',
                              image=self.photo, command=self.scatter)
        self.scatter.place(x=150, y=175)

        self.photo1 = ImageTk.PhotoImage(Image.open("Images/line.png"))
        self.line = Button(self.forthwin, height=210, width=165,
                           text="Line Plot", compound="top", bg="#69A7FF",
                           font=('Times New Roman', 18), foreground='white',
                           image=self.photo1, command=self.line)
        self.line.place(x=400, y=175)

        self.photo2 = ImageTk.PhotoImage(Image.open("Images/bar.png"))
        self.bar = Button(self.forthwin, height=210, width=165, text="Bar Plot",
                          compound="top", bg="#69A7FF",
                          font=('Times New Roman', 18), foreground='white',
                          image=self.photo2, command=self.bar)
        self.bar.place(x=650, y=175)

        self.photo3 = ImageTk.PhotoImage(Image.open("Images/pie.png"))
        self.pie = Button(self.forthwin, height=210, width=165, text="Pie Plot",
                          compound="top", bg="#69A7FF",
                          font=('Times New Roman', 18), foreground='white',
                          image=self.photo3, command=self.pie)
        self.pie.place(x=150, y=400)

        self.photo4 = ImageTk.PhotoImage(Image.open("Images/hist.png"))
        self.hist = Button(self.forthwin, height=210, width=165,
                           text="Histogram", compound="top", bg="#69A7FF",
                           font=('Times New Roman', 18), foreground='white',
                           image=self.photo4, command=self.hist)
        self.hist.place(x=400, y=400)

        self.photo5 = ImageTk.PhotoImage(Image.open("Images/signal.png"))
        self.signal = Button(self.forthwin, height=210, width=165,
                             text="Signal Plot", compound="top", bg="#69A7FF",
                             font=('Times New Roman', 18), foreground='white',
                             image=self.photo5, command=self.signal)
        self.signal.place(x=650, y=400)

        self.canvas4.create_rectangle(900, 625, 110, 150, outline="#6DB4EA",
                                      width=8)

        self.forthwin.protocol("WM_DELETE_WINDOW", root.destroy)

        self.forthwin.withdraw()

        self.linewin = Toplevel()

        self.linewin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas6 = Canvas(self.linewin, width=1000, height=650)
        self.canvas6.pack()

        self.canvas7 = Canvas(self.linewin, width=500, height=65)
        self.canvas7.place(x=250, y=25)

        self.image5 = ImageTk.PhotoImage(Image.open("Images/Background.png"))
        self.canvas6.create_image(0, 0, anchor=NW, image=self.image5)

        self.i = self.canvas7.create_text(250, 35, fill="black",
                                          font=("Times 20 italic bold", 32),
                                          text="LINE PLOT")
        self.r = self.canvas7.create_rectangle(self.canvas.bbox(ALL),
                                               fill="#6DB4EA")
        self.canvas7.tag_lower(self.r, self.i)

        self.button7 = Button(self.linewin, text="HOME", foreground="white",
                              command=self.linehome,
                              anchor=CENTER)
        self.button7.configure(width=10, activebackground="#33B5E5",
                               bg='#2C56BC', relief=FLAT)
        self.button7_window = self.canvas6.create_window(60, 20, anchor=NW,
                                                         window=self.button7)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button7['font'] = font1
        self.button7.config(width=10, height=1)

        self.button8 = Button(self.linewin, text="BACK", foreground="white",
                              command=self.lineback,
                              anchor=CENTER)
        self.button8.configure(width=10, activebackground="#33B5E5",
                               bg='#2C56BC', relief=FLAT)
        self.button8_window = self.canvas6.create_window(800, 20, anchor=NW,
                                                         window=self.button8)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button8['font'] = font1
        self.button8.config(width=10, height=1)

        self.canvas6.create_rectangle(80, 100, 925, 625, outline="#6DB4EA",
                                      width=8)

        self.canvas8 = Canvas(self.linewin, bg="#B5B2B0", width=250, height=500)
        self.canvas8.place(x=88, y=108)

        self.canvas9 = Canvas(self.linewin, bg="#B5B2B0", width=550, height=500)
        self.canvas9.place(x=355, y=108)

        self.canvas37 = Canvas(self.canvas8, bg="#5E5E5E",
                               highlightbackground="#5E5E5E", width=210,
                               height=350)
        self.canvas37.place(x=15, y=60)

        self.canvas37.create_text(50, 25, fill="black", font=("Times", 18),
                                  text="X")
        self.canvas37.create_text(160, 25, fill="black", font=("Times", 18),
                                  text="Y")
        self.canvas37.create_line(0, 45, 220, 45, fill="black")
        self.canvas37.create_line(105, 0, 105, 400, fill="black")

        self.i = self.canvas8.create_text(125, 25, fill="black",
                                          font=("Times 20 "),
                                          text=" PARAMETERS ")
        self.r = self.canvas8.create_rectangle(self.canvas8.bbox(self.i),
                                               fill="#6DB4EA",
                                               outline="#6DB4EA")
        self.canvas8.tag_lower(self.r, self.i)

        self.entryx1 = Entry(self.canvas37, width=10)
        self.entryx1.place(x=20, y=50)
        self.entryx2 = Entry(self.canvas37, width=10)
        self.entryx2.place(x=20, y=75)
        self.entryx3 = Entry(self.canvas37, width=10)
        self.entryx3.place(x=20, y=100)
        self.entryx4 = Entry(self.canvas37, width=10)
        self.entryx4.place(x=20, y=125)
        self.entryx5 = Entry(self.canvas37, width=10)
        self.entryx5.place(x=20, y=150)
        self.entryx6 = Entry(self.canvas37, width=10)
        self.entryx6.place(x=20, y=175)
        self.entryx7 = Entry(self.canvas37, width=10)
        self.entryx7.place(x=20, y=200)
        self.entryx8 = Entry(self.canvas37, width=10)
        self.entryx8.place(x=20, y=225)
        self.entryx9 = Entry(self.canvas37, width=10)
        self.entryx9.place(x=20, y=250)
        self.entryx10 = Entry(self.canvas37, width=10)
        self.entryx10.place(x=20, y=275)

        self.entryy1 = Entry(self.canvas37, width=10)
        self.entryy1.place(x=120, y=50)
        self.entryy2 = Entry(self.canvas37, width=10)
        self.entryy2.place(x=120, y=75)
        self.entryy3 = Entry(self.canvas37, width=10)
        self.entryy3.place(x=120, y=100)
        self.entryy4 = Entry(self.canvas37, width=10)
        self.entryy4.place(x=120, y=125)
        self.entryy5 = Entry(self.canvas37, width=10)
        self.entryy5.place(x=120, y=150)
        self.entryy6 = Entry(self.canvas37, width=10)
        self.entryy6.place(x=120, y=175)
        self.entryy7 = Entry(self.canvas37, width=10)
        self.entryy7.place(x=120, y=200)
        self.entryy8 = Entry(self.canvas37, width=10)
        self.entryy8.place(x=120, y=225)
        self.entryy9 = Entry(self.canvas37, width=10)
        self.entryy9.place(x=120, y=250)
        self.entryy10 = Entry(self.canvas37, width=10)
        self.entryy10.place(x=120, y=275)

        self.i = self.canvas9.create_text(275, 25, fill="black",
                                          font=("Times 20"),
                                          text="  OUTPUT  ")
        self.r = self.canvas9.create_rectangle(self.canvas9.bbox(self.i),
                                               fill="#6DB4EA",
                                               outline="#6DB4EA")
        self.canvas9.tag_lower(self.r, self.i)

        

        self.button27 = Button(self.linewin, text="Get", command=self.getline,
                               anchor=CENTER)
        self.button27.configure(width=10, activebackground="#33B5E5",
                                bg='#69A7FF', relief=RAISED)
        self.button27_window = self.canvas8.create_window(20, 450, anchor=NW,
                                                          window=self.button27)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button27['font'] = font1
        self.button27.config(width=8, height=1)

        self.button28 = Button(self.linewin, text="Update",
                               command=self.updateline, anchor=CENTER)
        self.button28.configure(width=10, activebackground="#33B5E5",
                                bg='#69A7FF', relief=RAISED)
        self.button28_window = self.canvas8.create_window(130, 450, anchor=NW,
                                                          window=self.button28)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button28['font'] = font1
        self.button28.config(width=8, height=1)
        
        """Initial Graph"""
        self.fig, self.linegraph = plt.subplots(figsize=(5,4))
        self.linegraph.set_xlabel('X-Label')
        self.linegraph.set_ylabel('Y-Label')
        self.canvas9 = FigureCanvasTkAgg(self.fig, master=self.canvas9)
        self.canvas9.get_tk_widget().place(x=20, y=60)

        self.linewin.protocol("WM_DELETE_WINDOW", root.destroy)
        
        self.linewin.withdraw()

        self.barwin = Toplevel()

        self.barwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas10 = Canvas(self.barwin, width=1000, height=650)
        self.canvas10.pack()

        self.canvas11 = Canvas(self.barwin, width=500, height=65)
        self.canvas11.place(x=250, y=25)

        self.image6 = ImageTk.PhotoImage(Image.open("Images/Background.png"))
        self.canvas10.create_image(0, 0, anchor=NW, image=self.image6)

        self.i = self.canvas11.create_text(250, 35, fill="black",
                                           font=("Times 20 italic bold", 32),
                                           text="BAR PLOT")
        self.r = self.canvas11.create_rectangle(self.canvas.bbox(ALL),
                                                fill="#6DB4EA")
        self.canvas11.tag_lower(self.r, self.i)

        self.button10 = Button(self.barwin, text="HOME", foreground="white",
                               command=self.barhome,
                               anchor=CENTER)
        self.button10.configure(width=10, activebackground="#33B5E5",
                                bg='#2C56BC', relief=FLAT)
        self.button10_window = self.canvas10.create_window(60, 20, anchor=NW,
                                                           window=self.button10)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button10['font'] = font1
        self.button10.config(width=10, height=1)

        self.button11 = Button(self.barwin, text="BACK", foreground="white",
                               command=self.barback,
                               anchor=CENTER)
        self.button11.configure(width=10, activebackground="#33B5E5",
                                bg='#2C56BC', relief=FLAT)
        self.button11_window = self.canvas10.create_window(800, 20, anchor=NW,
                                                           window=self.button11)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button11['font'] = font1
        self.button11.config(width=10, height=1)

        self.canvas10.create_rectangle(80, 100, 925, 625, outline="#6DB4EA",
                                       width=8)

        self.canvas12 = Canvas(self.barwin, bg="#B5B2B0", width=250, height=500)
        self.canvas12.place(x=88, y=108)

        self.canvas13 = Canvas(self.barwin, bg="#B5B2B0", width=550, height=500)
        self.canvas13.place(x=355, y=108)

        self.canvas38 = Canvas(self.canvas12, bg="#5E5E5E",
                               highlightbackground="#5E5E5E", width=210,
                               height=350)
        self.canvas38.place(x=15, y=60)

        self.canvas38.create_text(50, 25, fill="black", font=("Times", 18),
                                  text="Names")
        self.canvas38.create_text(160, 25, fill="black", font=("Times", 18),
                                  text="Data")
        self.canvas38.create_line(105, 0, 105, 400, fill="black")
        
        self.canvas38.create_line(0, 45, 220, 45, fill="black")

        self.i = self.canvas12.create_text(125, 25, fill="black",
                                           font=("Times 20 "),
                                           text=" PARAMETERS ")
        self.r = self.canvas12.create_rectangle(self.canvas12.bbox(self.i),
                                                fill="#6DB4EA",
                                                outline="#6DB4EA")
        self.canvas12.tag_lower(self.r, self.i)

        self.entrybx1 = Entry(self.canvas38, width=10)
        self.entrybx1.place(x=20, y=50)
        self.entrybx2 = Entry(self.canvas38, width=10)
        self.entrybx2.place(x=20, y=75)
        self.entrybx3 = Entry(self.canvas38, width=10)
        self.entrybx3.place(x=20, y=100)
        self.entrybx4 = Entry(self.canvas38, width=10)
        self.entrybx4.place(x=20, y=125)
        self.entrybx5 = Entry(self.canvas38, width=10)
        self.entrybx5.place(x=20, y=150)
        self.entrybx6 = Entry(self.canvas38, width=10)
        self.entrybx6.place(x=20, y=175)
        self.entrybx7 = Entry(self.canvas38, width=10)
        self.entrybx7.place(x=20, y=200)
        self.entrybx8 = Entry(self.canvas38, width=10)
        self.entrybx8.place(x=20, y=225)
        self.entrybx9 = Entry(self.canvas38, width=10)
        self.entrybx9.place(x=20, y=250)
        self.entrybx10 = Entry(self.canvas38, width=10)
        self.entrybx10.place(x=20, y=275)

        self.entryby1 = Entry(self.canvas38, width=10)
        self.entryby1.place(x=120, y=50)
        self.entryby2 = Entry(self.canvas38, width=10)
        self.entryby2.place(x=120, y=75)
        self.entryby3 = Entry(self.canvas38, width=10)
        self.entryby3.place(x=120, y=100)
        self.entryby4 = Entry(self.canvas38, width=10)
        self.entryby4.place(x=120, y=125)
        self.entryby5 = Entry(self.canvas38, width=10)
        self.entryby5.place(x=120, y=150)
        self.entryby6 = Entry(self.canvas38, width=10)
        self.entryby6.place(x=120, y=175)
        self.entryby7 = Entry(self.canvas38, width=10)
        self.entryby7.place(x=120, y=200)
        self.entryby8 = Entry(self.canvas38, width=10)
        self.entryby8.place(x=120, y=225)
        self.entryby9 = Entry(self.canvas38, width=10)
        self.entryby9.place(x=120, y=250)
        self.entryby10 = Entry(self.canvas38, width=10)
        self.entryby10.place(x=120, y=275)

        self.i = self.canvas13.create_text(275, 25, fill="black",
                                           font=("Times 20"),
                                           text="  OUTPUT  ")
        self.r = self.canvas13.create_rectangle(self.canvas13.bbox(self.i),
                                                fill="#6DB4EA",
                                                outline="#6DB4EA")
        self.canvas13.tag_lower(self.r, self.i)

        

        self.button31 = Button(self.barwin, text="Get", foreground="black",
                               command=self.getbar,
                               anchor=CENTER)
        self.button31.configure(width=8, activebackground="#33B5E5",
                                bg='#69A7FF', relief=RAISED)
        self.button31_window = self.canvas12.create_window(20, 450, anchor=NW,
                                                           window=self.button31)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button31['font'] = font1
        self.button31.config(width=8, height=1)

        self.button32 = Button(self.barwin, text="Update", foreground="black",
                               command=self.updatebar,
                               anchor=CENTER)
        self.button32.configure(width=8, activebackground="#33B5E5",
                                bg='#69A7FF', relief=RAISED)
        self.button32_window = self.canvas12.create_window(130, 450, anchor=NW,
                                                           window=self.button32)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button32['font'] = font1
        self.button32.config(width=8, height=1)

        """Initial Graph"""
        self.fig, self.bargraph = plt.subplots(figsize=(5,4))
        self.canvas13 = FigureCanvasTkAgg(self.fig, master=self.canvas13)
        self.canvas13.get_tk_widget().place(x=20, y=60)

        self.barwin.protocol("WM_DELETE_WINDOW", root.destroy)

        self.barwin.withdraw()

        self.scatterwin = Toplevel()

        self.scatterwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas14 = Canvas(self.scatterwin, width=1000, height=650)
        self.canvas14.pack()

        self.canvas15 = Canvas(self.scatterwin, width=500, height=65)
        self.canvas15.place(x=250, y=25)

        self.image7 = ImageTk.PhotoImage(Image.open("Images/Background.png"))
        self.canvas14.create_image(0, 0, anchor=NW, image=self.image7)

        self.i = self.canvas15.create_text(250, 35, fill="black",
                                           font=("Times 20 italic bold", 32),
                                           text="SCATTER PLOT")
        self.r = self.canvas15.create_rectangle(self.canvas.bbox(ALL),
                                                fill="#6DB4EA")
        self.canvas15.tag_lower(self.r, self.i)

        self.button13 = Button(self.scatterwin, text="HOME", foreground="white",
                               command=self.scatterhome,
                               anchor=CENTER)
        self.button13.configure(width=10, activebackground="#33B5E5",
                                bg='#2C56BC', relief=FLAT)
        self.button13_window = self.canvas14.create_window(60, 20, anchor=NW,
                                                           window=self.button13)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button13['font'] = font1
        self.button13.config(width=10, height=1)

        self.button14 = Button(self.scatterwin, text="BACK", foreground="white",
                               command=self.scatterback,
                               anchor=CENTER)
        self.button14.configure(width=10, activebackground="#33B5E5",
                                bg='#2C56BC', relief=FLAT)
        self.button14_window = self.canvas14.create_window(800, 20, anchor=NW,
                                                           window=self.button14)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button14['font'] = font1
        self.button14.config(width=10, height=1)

        self.canvas14.create_rectangle(80, 100, 925, 625, outline="#6DB4EA",
                                       width=8)

        self.canvas16 = Canvas(self.scatterwin, bg="#B5B2B0", width=250,
                               height=500)
        self.canvas16.place(x=88, y=108)

        self.canvas17 = Canvas(self.scatterwin, bg="#B5B2B0", width=550,
                               height=500)
        self.canvas17.place(x=355, y=108)

        self.canvas39 = Canvas(self.canvas16, bg="#5E5E5E",
                               highlightbackground="#5E5E5E", width=210,
                               height=350)
        self.canvas39.place(x=15, y=60)

        self.canvas39.create_text(50, 25, fill="black", font=("Times", 18),
                                  text="X")
        self.canvas39.create_text(160, 25, fill="black", font=("Times", 18),
                                  text="Y")
        self.canvas39.create_line(0, 45, 220, 45, fill="black")
        self.canvas39.create_line(105, 0, 105, 400, fill="black")

        self.i = self.canvas16.create_text(125, 25, fill="black",
                                           font=("Times 20 "),
                                           text=" PARAMETERS ")
        self.r = self.canvas16.create_rectangle(self.canvas16.bbox(self.i),
                                                fill="#6DB4EA",
                                                outline="#6DB4EA")
        self.canvas16.tag_lower(self.r, self.i)

        self.entrysx1 = Entry(self.canvas39, width=10)
        self.entrysx1.place(x=20, y=50)
        self.entrysx2 = Entry(self.canvas39, width=10)
        self.entrysx2.place(x=20, y=75)
        self.entrysx3 = Entry(self.canvas39, width=10)
        self.entrysx3.place(x=20, y=100)
        self.entrysx4 = Entry(self.canvas39, width=10)
        self.entrysx4.place(x=20, y=125)
        self.entrysx5 = Entry(self.canvas39, width=10)
        self.entrysx5.place(x=20, y=150)
        self.entrysx6 = Entry(self.canvas39, width=10)
        self.entrysx6.place(x=20, y=175)
        self.entrysx7 = Entry(self.canvas39, width=10)
        self.entrysx7.place(x=20, y=200)
        self.entrysx8 = Entry(self.canvas39, width=10)
        self.entrysx8.place(x=20, y=225)
        self.entrysx9 = Entry(self.canvas39, width=10)
        self.entrysx9.place(x=20, y=250)
        self.entrysx10 = Entry(self.canvas39, width=10)
        self.entrysx10.place(x=20, y=275)

        self.entrysy1 = Entry(self.canvas39, width=10)
        self.entrysy1.place(x=120, y=50)
        self.entrysy2 = Entry(self.canvas39, width=10)
        self.entrysy2.place(x=120, y=75)
        self.entrysy3 = Entry(self.canvas39, width=10)
        self.entrysy3.place(x=120, y=100)
        self.entrysy4 = Entry(self.canvas39, width=10)
        self.entrysy4.place(x=120, y=125)
        self.entrysy5 = Entry(self.canvas39, width=10)
        self.entrysy5.place(x=120, y=150)
        self.entrysy6 = Entry(self.canvas39, width=10)
        self.entrysy6.place(x=120, y=175)
        self.entrysy7 = Entry(self.canvas39, width=10)
        self.entrysy7.place(x=120, y=200)
        self.entrysy8 = Entry(self.canvas39, width=10)
        self.entrysy8.place(x=120, y=225)
        self.entrysy9 = Entry(self.canvas39, width=10)
        self.entrysy9.place(x=120, y=250)
        self.entrysy10 = Entry(self.canvas39, width=10)
        self.entrysy10.place(x=120, y=275)

        self.i = self.canvas17.create_text(275, 25, fill="black",
                                           font=("Times 20"),
                                           text="  OUTPUT  ")
        self.r = self.canvas17.create_rectangle(self.canvas17.bbox(self.i),
                                                fill="#6DB4EA",
                                                outline="#6DB4EA")
        self.canvas17.tag_lower(self.r, self.i)

        

        self.button29 = Button(self.scatterwin, text="Get", foreground="black",
                               command=self.getscatter,
                               anchor=CENTER)
        self.button29.configure(width=8, activebackground="#33B5E5",
                                bg='#69A7FF', relief=RAISED)
        self.button29_window = self.canvas16.create_window(20, 450, anchor=NW,
                                                           window=self.button29)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button29['font'] = font1
        self.button29.config(width=8, height=1)

        self.button30 = Button(self.scatterwin, text="Update", foreground="black",
                               command=self.updatescatter,
                               anchor=CENTER)
        self.button30.configure(width=8, activebackground="#33B5E5",
                                bg='#69A7FF', relief=RAISED)
        self.button30_window = self.canvas16.create_window(130, 450, anchor=NW,
                                                           window=self.button30)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button30['font'] = font1
        self.button30.config(width=8, height=1)

        """Initial Graph"""
        self.fig, self.scattergraph = plt.subplots(figsize=(5,4))
        self.linegraph.set_xlabel('X-Label')
        self.linegraph.set_ylabel('Y-Label')
        self.canvas17 = FigureCanvasTkAgg(self.fig, master=self.canvas17)
        self.canvas17.get_tk_widget().place(x=20, y=60)

        self.scatterwin.protocol("WM_DELETE_WINDOW", root.destroy)

        self.scatterwin.withdraw()

        self.histwin = Toplevel()

        self.histwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas18 = Canvas(self.histwin, width=1000, height=650)
        self.canvas18.pack()

        self.canvas19 = Canvas(self.histwin, width=500, height=65)
        self.canvas19.place(x=250, y=25)

        self.image8 = ImageTk.PhotoImage(Image.open("Images/Background.png"))
        self.canvas18.create_image(0, 0, anchor=NW, image=self.image8)

        self.i = self.canvas19.create_text(250, 35, fill="black",
                                           font=("Times 20 italic bold", 32),
                                           text="HISTOGRAM")
        self.r = self.canvas19.create_rectangle(self.canvas.bbox(ALL),
                                                fill="#6DB4EA")
        self.canvas19.tag_lower(self.r, self.i)

        self.button16 = Button(self.histwin, text="HOME", foreground="white",
                               command=self.histhome,
                               anchor=CENTER)
        self.button16.configure(width=10, activebackground="#33B5E5",
                                bg='#2C56BC', relief=FLAT)
        self.button16_window = self.canvas18.create_window(60, 20, anchor=NW,
                                                           window=self.button16)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button16['font'] = font1
        self.button16.config(width=10, height=1)

        self.button17 = Button(self.histwin, text="BACK", foreground="white",
                               command=self.histback,
                               anchor=CENTER)
        self.button17.configure(width=10, activebackground="#33B5E5",
                                bg='#2C56BC', relief=FLAT)
        self.button17_window = self.canvas18.create_window(800, 20, anchor=NW,
                                                           window=self.button17)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button17['font'] = font1
        self.button17.config(width=10, height=1)

        self.canvas18.create_rectangle(80, 100, 925, 625, outline="#6DB4EA",
                                       width=8)

        self.canvas20 = Canvas(self.histwin, bg="#B5B2B0", width=250,
                               height=500)
        self.canvas20.place(x=88, y=108)

        self.canvas21 = Canvas(self.histwin, bg="#B5B2B0", width=550,
                               height=500)
        self.canvas21.place(x=355, y=108)

        self.canvas40 = Canvas(self.canvas20, bg="#5E5E5E",
                               highlightbackground="#5E5E5E", width=210,
                               height=350)
        self.canvas40.place(x=15, y=60)

        self.canvas40.create_text(100, 25, fill="black", font=("Times", 18),
                                  text="Data")
        self.canvas40.create_line(0, 45, 220, 45, fill="black")

        self.i = self.canvas20.create_text(125, 25, fill="black",
                                           font=("Times 20 "),
                                           text=" PARAMETERS ")
        self.r = self.canvas20.create_rectangle(self.canvas20.bbox(self.i),
                                                fill="#6DB4EA",
                                                outline="#6DB4EA")
        self.canvas20.tag_lower(self.r, self.i)

        self.entryhx1 = Entry(self.canvas40, width=10)
        self.entryhx1.place(x=65, y=50)
        self.entryhx2 = Entry(self.canvas40, width=10)
        self.entryhx2.place(x=65, y=75)
        self.entryhx3 = Entry(self.canvas40, width=10)
        self.entryhx3.place(x=65, y=100)
        self.entryhx4 = Entry(self.canvas40, width=10)
        self.entryhx4.place(x=65, y=125)
        self.entryhx5 = Entry(self.canvas40, width=10)
        self.entryhx5.place(x=65, y=150)
        self.entryhx6 = Entry(self.canvas40, width=10)
        self.entryhx6.place(x=65, y=175)
        self.entryhx7 = Entry(self.canvas40, width=10)
        self.entryhx7.place(x=65, y=200)
        self.entryhx8 = Entry(self.canvas40, width=10)
        self.entryhx8.place(x=65, y=225)
        self.entryhx9 = Entry(self.canvas40, width=10)
        self.entryhx9.place(x=65, y=250)
        self.entryhx10 = Entry(self.canvas40, width=10)
        self.entryhx10.place(x=65, y=275)


        self.i = self.canvas21.create_text(275, 25, fill="black",
                                           font=("Times 20"),
                                           text="  OUTPUT  ")
        self.r = self.canvas21.create_rectangle(self.canvas21.bbox(self.i),
                                                fill="#6DB4EA",
                                                outline="#6DB4EA")
        self.canvas21.tag_lower(self.r, self.i)

        

        self.button35 = Button(self.histwin, text="Get", command=self.gethist,
                               anchor=CENTER)
        self.button35.configure(width=10, activebackground="#33B5E5",
                                bg='#69A7FF', relief=RAISED)
        self.button35_window = self.canvas20.create_window(20, 450, anchor=NW,
                                                          window=self.button35)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button35['font'] = font1
        self.button35.config(width=8, height=1)

        self.button36 = Button(self.histwin, text="Update",
                               command=self.updatehist, anchor=CENTER)
        self.button36.configure(width=10, activebackground="#33B5E5",
                                bg='#69A7FF', relief=RAISED)
        self.button36_window = self.canvas20.create_window(130, 450, anchor=NW,
                                                          window=self.button36)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button36['font'] = font1
        self.button36.config(width=8, height=1)

        """Initial Graph"""
        self.fig, self.histgraph = plt.subplots(figsize=(5,4))
        self.canvas21 = FigureCanvasTkAgg(self.fig, master=self.canvas21)
        self.canvas21.get_tk_widget().place(x=20, y=60)

        self.histwin.protocol("WM_DELETE_WINDOW", root.destroy)

        self.histwin.withdraw()

        self.piewin = Toplevel()

        self.piewin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas22 = Canvas(self.piewin, width=1000, height=650)
        self.canvas22.pack()

        self.canvas23 = Canvas(self.piewin, width=500, height=65)
        self.canvas23.place(x=250, y=25)

        self.image9 = ImageTk.PhotoImage(Image.open("Images/Background.png"))
        self.canvas22.create_image(0, 0, anchor=NW, image=self.image9)

        self.i = self.canvas23.create_text(250, 35, fill="black",
                                           font=("Times 20 italic bold", 32),
                                           text="PIE PLOT")
        self.r = self.canvas23.create_rectangle(self.canvas.bbox(ALL),
                                                fill="#6DB4EA")
        self.canvas23.tag_lower(self.r, self.i)

        self.button19 = Button(self.piewin, text="HOME", foreground="white",
                               command=self.piehome,
                               anchor=CENTER)
        self.button19.configure(width=10, activebackground="#33B5E5",
                                bg='#2C56BC', relief=FLAT)
        self.button19_window = self.canvas22.create_window(60, 20, anchor=NW,
                                                           window=self.button19)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button19['font'] = font1
        self.button19.config(width=10, height=1)

        self.button20 = Button(self.piewin, text="BACK", foreground="white",
                               command=self.pieback,
                               anchor=CENTER)
        self.button20.configure(width=10, activebackground="#33B5E5",
                                bg='#2C56BC', relief=FLAT)
        self.button20_window = self.canvas22.create_window(800, 20, anchor=NW,
                                                           window=self.button20)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button20['font'] = font1
        self.button20.config(width=10, height=1)

        self.canvas22.create_rectangle(80, 100, 925, 625, outline="#6DB4EA",
                                       width=8)

        self.canvas24 = Canvas(self.piewin, bg="#B5B2B0", width=250, height=500)
        self.canvas24.place(x=88, y=108)

        self.canvas25 = Canvas(self.piewin, bg="#B5B2B0", width=550, height=500)
        self.canvas25.place(x=355, y=108)

        self.canvas41 = Canvas(self.canvas24, bg="#5E5E5E",
                               highlightbackground="#5E5E5E", width=210,
                               height=350)
        self.canvas41.place(x=15, y=60)

        self.canvas41.create_text(50, 25, fill="black", font=("Times", 18),
                                  text="Names")
        self.canvas41.create_text(160, 25, fill="black", font=("Times", 18),
                                  text="Data")
        self.canvas41.create_line(0, 45, 220, 45, fill="black")
        self.canvas41.create_line(105, 0, 105, 400, fill="black")

        self.i = self.canvas24.create_text(125, 25, fill="black",
                                           font=("Times 20 "),
                                           text=" PARAMETERS ")
        self.r = self.canvas24.create_rectangle(self.canvas24.bbox(self.i),
                                                fill="#6DB4EA",
                                                outline="#6DB4EA")
        self.canvas24.tag_lower(self.r, self.i)

        self.entrypx1 = Entry(self.canvas41, width=10)
        self.entrypx1.place(x=20, y=50)
        self.entrypx2 = Entry(self.canvas41, width=10)
        self.entrypx2.place(x=20, y=75)
        self.entrypx3 = Entry(self.canvas41, width=10)
        self.entrypx3.place(x=20, y=100)
        self.entrypx4 = Entry(self.canvas41, width=10)
        self.entrypx4.place(x=20, y=125)
        self.entrypx5 = Entry(self.canvas41, width=10)
        self.entrypx5.place(x=20, y=150)
        self.entrypx6 = Entry(self.canvas41, width=10)
        self.entrypx6.place(x=20, y=175)
        self.entrypx7 = Entry(self.canvas41, width=10)
        self.entrypx7.place(x=20, y=200)
        self.entrypx8 = Entry(self.canvas41, width=10)
        self.entrypx8.place(x=20, y=225)
        self.entrypx9 = Entry(self.canvas41, width=10)
        self.entrypx9.place(x=20, y=250)
        self.entrypx10 = Entry(self.canvas41, width=10)
        self.entrypx10.place(x=20, y=275)

        self.entrypy1 = Entry(self.canvas41, width=10)
        self.entrypy1.place(x=120, y=50)
        self.entrypy2 = Entry(self.canvas41, width=10)
        self.entrypy2.place(x=120, y=75)
        self.entrypy3 = Entry(self.canvas41, width=10)
        self.entrypy3.place(x=120, y=100)
        self.entrypy4 = Entry(self.canvas41, width=10)
        self.entrypy4.place(x=120, y=125)
        self.entrypy5 = Entry(self.canvas41, width=10)
        self.entrypy5.place(x=120, y=150)
        self.entrypy6 = Entry(self.canvas41, width=10)
        self.entrypy6.place(x=120, y=175)
        self.entrypy7 = Entry(self.canvas41, width=10)
        self.entrypy7.place(x=120, y=200)
        self.entrypy8 = Entry(self.canvas41, width=10)
        self.entrypy8.place(x=120, y=225)
        self.entrypy9 = Entry(self.canvas41, width=10)
        self.entrypy9.place(x=120, y=250)
        self.entrypy10 = Entry(self.canvas41, width=10)
        self.entrypy10.place(x=120, y=275)

        self.i = self.canvas25.create_text(275, 25, fill="black",
                                           font=("Times 20"),
                                           text="  OUTPUT  ")
        self.r = self.canvas25.create_rectangle(self.canvas25.bbox(self.i),
                                                fill="#6DB4EA",
                                                outline="#6DB4EA")
        self.canvas25.tag_lower(self.r, self.i)


        self.button33 = Button(self.piewin, text="Get", command=self.getpie,
                               anchor=CENTER)
        self.button33.configure(width=10, activebackground="#33B5E5",
                                bg='#69A7FF', relief=RAISED)
        self.button33_window = self.canvas24.create_window(20, 450, anchor=NW,
                                                          window=self.button33)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button33['font'] = font1
        self.button33.config(width=8, height=1)

        self.button34 = Button(self.piewin, text="Update",
                               command=self.updatepie, anchor=CENTER)
        self.button34.configure(width=10, activebackground="#33B5E5",
                                bg='#69A7FF', relief=RAISED)
        self.button34_window = self.canvas24.create_window(130, 450, anchor=NW,
                                                          window=self.button34)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button34['font'] = font1
        self.button34.config(width=8, height=1)

        """Initial Graph"""
        self.fig, self.piegraph = plt.subplots(figsize=(5,4))
        self.piegraph.get_xaxis().set_visible(False)
        self.piegraph.get_yaxis().set_visible(False)
        self.canvas25 = FigureCanvasTkAgg(self.fig, master=self.canvas25)
        self.canvas25.get_tk_widget().place(x=20, y=60)

        self.piewin.protocol("WM_DELETE_WINDOW", root.destroy)
        
        self.piewin.withdraw()

        self.signalwin = Toplevel()

        self.signalwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas26 = Canvas(self.signalwin, width=1000, height=650)
        self.canvas26.pack()

        self.canvas27 = Canvas(self.signalwin, width=500, height=65)
        self.canvas27.place(x=250, y=25)

        self.image10 = ImageTk.PhotoImage(Image.open("Images/Background.png"))
        self.canvas26.create_image(0, 0, anchor=NW, image=self.image10)

        self.i = self.canvas27.create_text(250, 35, fill="black",
                                           font=("Times 20 italic bold", 32),
                                           text="SIGNAL PLOT")
        self.r = self.canvas27.create_rectangle(self.canvas.bbox(ALL),
                                                fill="#6DB4EA")
        self.canvas27.tag_lower(self.r, self.i)

        self.button22 = Button(self.signalwin, text="HOME", foreground="white",
                               command=self.signalhome,
                               anchor=CENTER)
        self.button22.configure(width=10, activebackground="#33B5E5",
                                bg='#2C56BC', relief=FLAT)
        self.button22_window = self.canvas26.create_window(60, 20, anchor=NW,
                                                           window=self.button22)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button22['font'] = font1
        self.button22.config(width=10, height=1)

        self.button23 = Button(self.signalwin, text="BACK", foreground="white",
                               command=self.signalback,
                               anchor=CENTER)
        self.button23.configure(width=10, activebackground="#33B5E5",
                                bg='#2C56BC', relief=FLAT)
        self.button23_window = self.canvas26.create_window(800, 20, anchor=NW,
                                                           window=self.button23)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button23['font'] = font1
        self.button23.config(width=10, height=1)

        self.canvas26.create_rectangle(80, 100, 925, 625, outline="#6DB4EA",
                                       width=8)

        self.canvas28 = Canvas(self.signalwin, bg="#B5B2B0", width=250,
                               height=500)
        self.canvas28.place(x=88, y=108)

        self.canvas29 = Canvas(self.signalwin, bg="#B5B2B0", width=550,
                               height=500)
        self.canvas29.place(x=355, y=108)

        self.canvas42 = Canvas(self.canvas28, bg="#5E5E5E",
                               highlightbackground="#5E5E5E", width=210,
                               height=350)
        self.canvas42.place(x=15, y=60)

        self.canvas42.create_text(100, 25, fill="black", font=("Times", 18),
                                  text="Frequency")
        
        self.canvas42.create_line(0, 45, 220, 45, fill="black")
        

        self.i = self.canvas28.create_text(125, 25, fill="black",
                                           font=("Times 20 "),
                                           text=" PARAMETERS ")
        self.r = self.canvas28.create_rectangle(self.canvas28.bbox(self.i),
                                                fill="#6DB4EA",
                                                outline="#6DB4EA")
        self.canvas28.tag_lower(self.r, self.i)

        self.entrysix1 = Entry(self.canvas42, width=10)
        self.entrysix1.place(x=90, y=50)

        self.entrysix2 = Entry(self.canvas42, width=10)
        self.entrysix2.place(x=90, y=130)

        self.canvas42.create_text(50, 60, fill="black", font=("Times", 18),
                                  text="Sine")
        self.canvas42.create_text(50, 140, fill="black", font=("Times", 18),
                                  text="Cosine")
        
        self.canvas42.create_line(0, 45, 220, 45, fill="black")
        

        self.i = self.canvas29.create_text(275, 25, fill="black",
                                           font=("Times 20"),
                                           text="  OUTPUT  ")
        self.r = self.canvas29.create_rectangle(self.canvas29.bbox(self.i),
                                                fill="#6DB4EA",
                                                outline="#6DB4EA")
        self.canvas29.tag_lower(self.r, self.i)

        

        self.button37 = Button(self.signalwin, text="Get", command=self.getsine,
                               anchor=CENTER)
        self.button37.configure(width=5, activebackground="#33B5E5",
                                bg='#69A7FF', relief=RAISED)
        self.button37_window = self.canvas42.create_window(10, 80, anchor=NW,
                                                          window=self.button37)
        font1 = font.Font(family='Times New Roman', size=12, weight='normal')
        self.button37['font'] = font1
        self.button37.config(width=5, height=1)

        self.button39 = Button(self.signalwin, text="Get", command=self.getcos,
                               anchor=CENTER)
        self.button39.configure(width=5, activebackground="#33B5E5",
                                bg='#69A7FF', relief=RAISED)
        self.button39_window = self.canvas42.create_window(10, 170, anchor=NW,
                                                          window=self.button39)
        font1 = font.Font(family='Times New Roman', size=12, weight='normal')
        self.button39['font'] = font1
        self.button39.config(width=5, height=1)

        """Initial Graph"""
        self.fig, self.signalgraph = plt.subplots(figsize=(5,4))
        self.signalgraph.set_xlabel('X-Label')
        self.signalgraph.set_ylabel('Y-Label')
        self.canvas29 = FigureCanvasTkAgg(self.fig, master=self.canvas29)
        self.canvas29.get_tk_widget().place(x=20, y=60)

        self.signalwin.protocol("WM_DELETE_WINDOW", root.destroy)
        
        self.signalwin.withdraw()

    def clicktocontinue(self):
        """This  get you to About window"""
        def onclick():
            root.quit()
            self.secondWin.withdraw()
        self.secondWin.protocol("WM_DELETE_WINDOW", onclick)
        self.secondWin.resizable(width=False, height=False)
        self.master.withdraw()
        self.secondWin.deiconify()

    def clickforhelp(self):
        """This  get you to Help Window"""
        def onclick():
            root.quit()
            self.ThirdWin.withdraw()
        self.ThirdWin.protocol("WM_DELETE_WINDOW", onclick)
        self.ThirdWin.resizable(width = False, height = False)
        self.secondWin.withdraw()
        self.ThirdWin.deiconify()

    def home(self):
        """This get you to Home page"""
        self.secondWin.withdraw()
        self.master.deiconify()

    def clicktobegin(self):
        """This get you to All Plots page"""
        def onclick():
            root.quit()
            self.forthwin.withdraw()
        self.forthwin.protocol("WM_DELETE_WINDOW", onclick)
        self.forthwin.resizable(width = False, height = False)
        self.secondWin.withdraw()
        self.forthwin.deiconify()

    def thirdwinhome(self):
        """This get you to Home page"""
        def onclick():
            root.quit()
            self.master.withdraw()
        self.master.protocol("WM_DELETE_WINDOW", onclick)
        self.ThirdWin.withdraw()
        self.master.deiconify()

    def back(self):
        """This get you to About page"""
        self.ThirdWin.withdraw()
        self.secondWin.deiconify()

    def forthwinhome(self):
        """This get you to Home page"""
        self.forthwin.withdraw()
        self.master.deiconify()

    def forthwinback(self):
        """This get you to All Plots page"""
        self.forthwin.withdraw()
        self.secondWin.deiconify()

    def linehome(self):
        """This get you to Home page"""
        self.linewin.withdraw()
        self.master.deiconify()

    def lineback(self):
        """This get you to All Plots page"""
        self.linewin.withdraw()
        self.forthwin.deiconify()

    def barhome(self):
        """This get you to Home page"""
        self.barwin.withdraw()
        self.master.deiconify()

    def barback(self):
        """This get you to All Plots page"""
        self.barwin.withdraw()
        self.forthwin.deiconify()

    def scatterhome(self):
        """This get you to Home page"""
        self.scatterwin.withdraw()
        self.master.deiconify()

    def scatterback(self):
        """This get you to All Plots page"""
        self.scatterwin.withdraw()
        self.forthwin.deiconify()

    def histhome(self):
        """This get you to Home page"""
        self.histwin.withdraw()
        self.master.deiconify()

    def histback(self):
        """This get you to All Plots page"""
        self.histwin.withdraw()
        self.forthwin.deiconify()

    def piehome(self):
        """This get you to Home page"""
        self.piewin.withdraw()
        self.master.deiconify()

    def pieback(self):
        """This get you to All Plots page"""
        self.piewin.withdraw()
        self.forthwin.deiconify()

    def signalhome(self):
        """This get you to Home page"""
        self.signalwin.withdraw()
        self.master.deiconify()

    def signalback(self):
        """This get you to All Plots page"""
        self.signalwin.withdraw()
        self.forthwin.deiconify()

    #Scatter Plot

    def scatter(self):
        def onclick():
            root.quit()
            self.scatterwin.withdraw()
        self.scatterwin.protocol("WM_DELETE_WINDOW", onclick)
        self.sx1 = self.entrysx1.delete(first=0,last='end')
        self.sx2 = self.entrysx2.delete(first=0,last='end')
        self.sx3 = self.entrysx3.delete(first=0,last='end')
        self.sx4 = self.entrysx4.delete(first=0,last='end')
        self.sx5 = self.entrysx5.delete(first=0,last='end')
        self.sx6 = self.entrysx6.delete(first=0,last='end')
        self.sx7 = self.entrysx7.delete(first=0,last='end')
        self.sx8 = self.entrysx8.delete(first=0,last='end')
        self.sx9 = self.entrysx9.delete(first=0,last='end')
        self.sx10 = self.entrysx10.delete(first=0,last='end')
        self.sy1 = self.entrysy1.delete(first=0,last='end')
        self.sy2 = self.entrysy2.delete(first=0,last='end')
        self.sy3 = self.entrysy3.delete(first=0,last='end')
        self.sy4 = self.entrysy4.delete(first=0,last='end')
        self.sy5 = self.entrysy5.delete(first=0,last='end')
        self.sy6 = self.entrysy6.delete(first=0,last='end')
        self.sy7 = self.entrysy7.delete(first=0,last='end')
        self.sy8 = self.entrysy8.delete(first=0,last='end')
        self.sy9 = self.entrysy9.delete(first=0,last='end')
        self.sy10 = self.entrysy10.delete(first=0,last='end')
        self.scatterwin.resizable(width = False, height = False)
        self.scattergraph.cla()
        self.scattergraph.clear()
        self.canvas17.draw()
        
        self.forthwin.withdraw()
        self.scatterwin.deiconify()
        self.button29.config(state="normal")
        self.button30.config(state="disabled")

    def getscatter(self):
        def onclick():
            root.quit()
            self.scatterwin.withdraw()
        self.scatterwin.protocol("WM_DELETE_WINDOW", onclick)
        
        self.sx1 = self.entrysx1.get()
        self.sx2 = self.entrysx2.get()
        self.sx3 = self.entrysx3.get()
        self.sx4 = self.entrysx4.get()
        self.sx5 = self.entrysx5.get()
        self.sx6 = self.entrysx6.get()
        self.sx7 = self.entrysx7.get()
        self.sx8 = self.entrysx8.get()
        self.sx9 = self.entrysx9.get()
        self.sx10 = self.entrysx10.get()
        self.sy1 = self.entrysy1.get()
        self.sy2 = self.entrysy2.get()
        self.sy3 = self.entrysy3.get()
        self.sy4 = self.entrysy4.get()
        self.sy5 = self.entrysy5.get()
        self.sy6 = self.entrysy6.get()
        self.sy7 = self.entrysy7.get()
        self.sy8 = self.entrysy8.get()
        self.sy9 = self.entrysy9.get()
        self.sy10 = self.entrysy10.get()
        list = []
        list1 = []
        list = [self.sx1, self.sx2, self.sx3, self.sx4, self.sx5, self.sx6, self.sx7,
                self.sx8, self.sx9, self.sx10]
        list1 = [self.sy1, self.sy2, self.sy3, self.sy4, self.sy5, self.sy6, self.sy7,
                 self.sy8, self.sy9, self.sy10]
        print(list)
        print(list1)

        rlist = [i for i in list if i]
        rlist1 = [i for i in list1 if i]
        print(rlist)
        print(rlist1)
        try:
            flist = [float(i) for i in rlist]
            flist1 = [float(i) for i in rlist1]

            x = np.array(flist)
            y = np.array(flist1)
            """Updating the graph of canvas9 instead of creating graph here"""
            self.scattergraph.grid()
            self.scattergraph.scatter(x,y, color='red', alpha=0.5)
            self.scattergraph.set_xlabel('X-Label')
            self.scattergraph.set_ylabel('Y-Label')
            self.canvas17.draw()
            self.button29.config(state="disabled")
            self.button30.config(state="normal")
        except ValueError:
            tkinter.messagebox.showinfo("Invalid Parameter",
                                        "Please enter Integer or Float value. For Example - 2.5 or 2")
    def updatescatter(self):
        def onclick():
            root.quit()
            self.scatterwin.withdraw()
        self.scatterwin.protocol("WM_DELETE_WINDOW", onclick)
        self.sx1 = self.entrysx1.get()
        self.sx2 = self.entrysx2.get()
        self.sx3 = self.entrysx3.get()
        self.sx4 = self.entrysx4.get()
        self.sx5 = self.entrysx5.get()
        self.sx6 = self.entrysx6.get()
        self.sx7 = self.entrysx7.get()
        self.sx8 = self.entrysx8.get()
        self.sx9 = self.entrysx9.get()
        self.sx10 = self.entrysx10.get()
        self.sy1 = self.entrysy1.get()
        self.sy2 = self.entrysy2.get()
        self.sy3 = self.entrysy3.get()
        self.sy4 = self.entrysy4.get()
        self.sy5 = self.entrysy5.get()
        self.sy6 = self.entrysy6.get()
        self.sy7 = self.entrysy7.get()
        self.sy8 = self.entrysy8.get()
        self.sy9 = self.entrysy9.get()
        self.sy10 = self.entrysy10.get()
        list = []
        list1 = []
        list = [self.sx1, self.sx2, self.sx3, self.sx4, self.sx5, self.sx6, self.sx7,
                self.sx8, self.sx9, self.sx10]
        list1 = [self.sy1, self.sy2, self.sy3, self.sy4, self.sy5, self.sy6, self.sy7,
                 self.sy8, self.sy9, self.sy10]
        print(list)
        print(list1)

        rlist = [i for i in list if i]
        rlist1 = [i for i in list1 if i]
        print(rlist)
        print(rlist1)
        try:
            flist = [float(i) for i in rlist]
            flist1 = [float(i) for i in rlist1]
            self.scattergraph.cla()

            x = np.array(flist)
            y = np.array(flist1)
            self.scattergraph.grid()
            self.scattergraph.scatter(x,y, color='red', alpha=0.5)
            self.scattergraph.set_xlabel('X-Label')
            self.scattergraph.set_ylabel('Y-Label')
            self.canvas17.draw()
        except ValueError:
            tkinter.messagebox.showinfo("Invalid Parameter",
                                        "Please enter Integer or Float value. For Example - 2.5 or 2")

    #Line Plot

    def line(self):
        def onclick():
            root.quit()
            self.linewin.withdraw()
        self.linewin.protocol("WM_DELETE_WINDOW", onclick)
        """Deleting the existing entries, clearing the graph and updating the state of GET button"""
        self.x1 = self.entryx1.delete(first=0,last='end')
        self.x2 = self.entryx2.delete(first=0,last='end')
        self.x3 = self.entryx3.delete(first=0,last='end')
        self.x4 = self.entryx4.delete(first=0,last='end')
        self.x5 = self.entryx5.delete(first=0,last='end')
        self.x6 = self.entryx6.delete(first=0,last='end')
        self.x7 = self.entryx7.delete(first=0,last='end')
        self.x8 = self.entryx8.delete(first=0,last='end')
        self.x9 = self.entryx9.delete(first=0,last='end')
        self.x10 = self.entryx10.delete(first=0,last='end')
        self.y1 = self.entryy1.delete(first=0,last='end')
        self.y2 = self.entryy2.delete(first=0,last='end')
        self.y3 = self.entryy3.delete(first=0,last='end')
        self.y4 = self.entryy4.delete(first=0,last='end')
        self.y5 = self.entryy5.delete(first=0,last='end')
        self.y6 = self.entryy6.delete(first=0,last='end')
        self.y7 = self.entryy7.delete(first=0,last='end')
        self.y8 = self.entryy8.delete(first=0,last='end')
        self.y9 = self.entryy9.delete(first=0,last='end')
        self.y10 = self.entryy10.delete(first=0,last='end')
        self.linewin.resizable(width = False, height = False)
        self.linegraph.cla()
        self.linegraph.clear()
        self.canvas9.draw()
        self.forthwin.withdraw()
        self.linewin.deiconify()
        self.button27.config(state="normal")
        self.button28.config(state="disabled")

    def getline(self):
        print("Done")
        def onclick():
            root.quit()
            self.linewin.withdraw()
        self.linewin.protocol("WM_DELETE_WINDOW", onclick)
        global flist, flist1, rlist, rlist1
        self.x1 = self.entryx1.get()
        self.x2 = self.entryx2.get()
        self.x3 = self.entryx3.get()
        self.x4 = self.entryx4.get()
        self.x5 = self.entryx5.get()
        self.x6 = self.entryx6.get()
        self.x7 = self.entryx7.get()
        self.x8 = self.entryx8.get()
        self.x9 = self.entryx9.get()
        self.x10 = self.entryx10.get()
        self.y1 = self.entryy1.get()
        self.y2 = self.entryy2.get()
        self.y3 = self.entryy3.get()
        self.y4 = self.entryy4.get()
        self.y5 = self.entryy5.get()
        self.y6 = self.entryy6.get()
        self.y7 = self.entryy7.get()
        self.y8 = self.entryy8.get()
        self.y9 = self.entryy9.get()
        self.y10 = self.entryy10.get()
        list = []
        list1 = []
        list = [self.x1, self.x2, self.x3, self.x4, self.x5, self.x6, self.x7,
                self.x8, self.x9, self.x10]
        list1 = [self.y1, self.y2, self.y3, self.y4, self.y5, self.y6, self.y7,
                 self.y8, self.y9, self.y10]
        print(list)
        print(list1)

        rlist = [i for i in list if i]
        rlist1 = [i for i in list1 if i]
        print(rlist)
        print(rlist1)
        try:
            flist = [float(i) for i in rlist]
            flist1 = [float(i) for i in rlist1]
            """Updating the graph of canvas9 instead of creating graph here"""
            self.linegraph.grid()
            self.linegraph.plot(flist, flist1, color="green", marker=".")
            self.linegraph.set_xlabel('X-Label')
            self.linegraph.set_ylabel('Y-Label')
            self.canvas9.draw()
            self.button27.config(state="disabled")
            self.button28.config(state="normal")

        except ValueError:
            tkinter.messagebox.showinfo("Invalid Parameter",
                                        "Please enter Integer or Float value. For Example - 2.5 or 2")

    def updateline(self):
        def onclick():
            root.quit()
            self.linewin.withdraw()
        self.linewin.protocol("WM_DELETE_WINDOW", onclick)
        self.x1 = self.entryx1.get()
        self.x2 = self.entryx2.get()
        self.x3 = self.entryx3.get()
        self.x4 = self.entryx4.get()
        self.x5 = self.entryx5.get()
        self.x6 = self.entryx6.get()
        self.x7 = self.entryx7.get()
        self.x8 = self.entryx8.get()
        self.x9 = self.entryx9.get()
        self.x10 = self.entryx10.get()
        self.y1 = self.entryy1.get()
        self.y2 = self.entryy2.get()
        self.y3 = self.entryy3.get()
        self.y4 = self.entryy4.get()
        self.y5 = self.entryy5.get()
        self.y6 = self.entryy6.get()
        self.y7 = self.entryy7.get()
        self.y8 = self.entryy8.get()
        self.y9 = self.entryy9.get()
        self.y10 = self.entryy10.get()
        list = []
        list1 = []
        list = [self.x1, self.x2, self.x3, self.x4, self.x5, self.x6, self.x7,
                self.x8, self.x9, self.x10]
        list1 = [self.y1, self.y2, self.y3, self.y4, self.y5, self.y6, self.y7,
                 self.y8, self.y9, self.y10]

        self.linegraph.cla()
        rlist = [i for i in list if i]
        rlist1 = [i for i in list1 if i]
        print(rlist)
        print(rlist1)
        try:
            flist = [float(i) for i in rlist]
            flist1 = [float(i) for i in rlist1]
            self.linegraph.plot(flist, flist1, color="green", marker=".")
            self.linegraph.set_xlabel('X-Label')
            self.linegraph.set_ylabel('Y-Label')
            self.linegraph.grid()
            self.canvas9.draw()
        except ValueError:
            tkinter.messagebox.showinfo("Invalid Parameter",
                                        "Please enter Integer or Float value. For Example - 2.5 or 2")

    #Bar Plot

    def bar(self):
        def onclick():
            root.quit()
            self.barwin.withdraw()
        self.barwin.protocol("WM_DELETE_WINDOW", onclick)
        self.bx1 = self.entrybx1.delete(first=0,last='end')
        self.bx2 = self.entrybx2.delete(first=0,last='end')
        self.bx3 = self.entrybx3.delete(first=0,last='end')
        self.bx4 = self.entrybx4.delete(first=0,last='end')
        self.bx5 = self.entrybx5.delete(first=0,last='end')
        self.bx6 = self.entrybx6.delete(first=0,last='end')
        self.bx7 = self.entrybx7.delete(first=0,last='end')
        self.bx8 = self.entrybx8.delete(first=0,last='end')
        self.bx9 = self.entrybx9.delete(first=0,last='end')
        self.bx10 = self.entrybx10.delete(first=0,last='end')
        self.by1 = self.entryby1.delete(first=0,last='end')
        self.by2 = self.entryby2.delete(first=0,last='end')
        self.by3 = self.entryby3.delete(first=0,last='end')
        self.by4 = self.entryby4.delete(first=0,last='end')
        self.by5 = self.entryby5.delete(first=0,last='end')
        self.by6 = self.entryby6.delete(first=0,last='end')
        self.by7 = self.entryby7.delete(first=0,last='end')
        self.by8 = self.entryby8.delete(first=0,last='end')
        self.by9 = self.entryby9.delete(first=0,last='end')
        self.by10 = self.entryby10.delete(first=0,last='end')
        self.bargraph.get_xaxis().set_visible(False)
        self.bargraph.get_yaxis().set_visible(False)
        self.barwin.resizable(width = False, height = False)
        self.bargraph.cla()
        self.bargraph.clear()
        self.canvas13.draw()
        self.forthwin.withdraw()
        self.barwin.deiconify()
        self.button31.config(state="normal")
        self.button32.config(state="disabled")

    def getbar(self):
        def onclick():
            root.quit()
            self.barwin.withdraw()
        self.barwin.protocol("WM_DELETE_WINDOW", onclick)
        self.bx1 = self.entrybx1.get()
        self.bx2 = self.entrybx2.get()
        self.bx3 = self.entrybx3.get()
        self.bx4 = self.entrybx4.get()
        self.bx5 = self.entrybx5.get()
        self.bx6 = self.entrybx6.get()
        self.bx7 = self.entrybx7.get()
        self.bx8 = self.entrybx8.get()
        self.bx9 = self.entrybx9.get()
        self.bx10 = self.entrybx10.get()

        self.by1 = self.entryby1.get()
        self.by2 = self.entryby2.get()
        self.by3 = self.entryby3.get()
        self.by4 = self.entryby4.get()
        self.by5 = self.entryby5.get()
        self.by6 = self.entryby6.get()
        self.by7 = self.entryby7.get()
        self.by8 = self.entryby8.get()
        self.by9 = self.entryby9.get()
        self.by10 = self.entryby10.get()

        list = [self.bx1, self.bx2, self.bx3, self.bx4, self.bx5, self.bx6, self.bx7,
                self.bx8, self.bx9, self.bx10]
        print(list)
        list1 = [self.by1, self.by2, self.by3, self.by4, self.by5, self.by6, self.by7,
                self.by8, self.by9, self.by10]

        rlist = [i for i in list if i]
        print(rlist)
        rlist1 = [i for i in list1 if i]
        try:
            flist = [float(i) for i in rlist1]

            y = np.arange(len(rlist))
            print(y)
            width =0.2

            self.bargraph.get_xaxis().set_visible(True)
            self.bargraph.get_yaxis().set_visible(True)

            self.bargraph.bar(y,flist,align='center')
            self.bargraph.set_xticks(y)
            self.bargraph.set_xticklabels(rlist)
            self.bargraph.set_ylabel('Y-Label')
            self.canvas13.draw()
            self.button31.config(state="disabled")
            self.button32.config(state="normal")
        except ValueError:
            tkinter.messagebox.showinfo("Invalid Parameter",
                                        "Please enter Integer or Float value. For Example - 2.5 or 2")
    def updatebar(self):
        def onclick():
            root.quit()
            self.barwin.withdraw()
        self.barwin.protocol("WM_DELETE_WINDOW", onclick)
        self.bx1 = self.entrybx1.get()
        self.bx2 = self.entrybx2.get()
        self.bx3 = self.entrybx3.get()
        self.bx4 = self.entrybx4.get()
        self.bx5 = self.entrybx5.get()
        self.bx6 = self.entrybx6.get()
        self.bx7 = self.entrybx7.get()
        self.bx8 = self.entrybx8.get()
        self.bx9 = self.entrybx9.get()
        self.bx10 = self.entrybx10.get()
        
        self.by1 = self.entryby1.get()
        self.by2 = self.entryby2.get()
        self.by3 = self.entryby3.get()
        self.by4 = self.entryby4.get()
        self.by5 = self.entryby5.get()
        self.by6 = self.entryby6.get()
        self.by7 = self.entryby7.get()
        self.by8 = self.entryby8.get()
        self.by9 = self.entryby9.get()
        self.by10 = self.entryby10.get()
        
        self.bargraph.cla()

        list = [self.bx1, self.bx2, self.bx3, self.bx4, self.bx5, self.bx6, self.bx7,
                self.bx8, self.bx9, self.bx10]
        list1 = [self.by1, self.by2, self.by3, self.by4, self.by5, self.by6, self.by7,
                self.by8, self.by9, self.by10]

        rlist = [i for i in list if i]
        print(rlist)
        rlist1 = [i for i in list1 if i]
        try:
            flist = [float(i) for i in rlist1]

            y = np.arange(len(rlist))
            print(y)
            width =0.2

            self.bargraph.get_xaxis().set_visible(True)
            self.bargraph.get_yaxis().set_visible(True)

            self.bargraph.bar(y,flist,align='center')
            self.bargraph.set_xticks(y)
            self.bargraph.set_xticklabels(rlist)
            self.bargraph.set_ylabel('Y-Label')
            self.canvas13.draw()
        except ValueError:
            tkinter.messagebox.showinfo("Invalid Parameter",
                                        "Please enter Integer or Float value. For Example - 2.5 or 2")

    #Pie Plot

    def pie(self):
        def onclick():
            root.quit()
            self.piewin.withdraw()
        self.piewin.protocol("WM_DELETE_WINDOW", onclick)
        self.px1 = self.entrypx1.delete(first=0,last='end')
        self.px2 = self.entrypx2.delete(first=0,last='end')
        self.px3 = self.entrypx3.delete(first=0,last='end')
        self.px4 = self.entrypx4.delete(first=0,last='end')
        self.px5 = self.entrypx5.delete(first=0,last='end')
        self.px6 = self.entrypx6.delete(first=0,last='end')
        self.px7 = self.entrypx7.delete(first=0,last='end')
        self.px8 = self.entrypx8.delete(first=0,last='end')
        self.px9 = self.entrypx9.delete(first=0,last='end')
        self.px10 = self.entrypx10.delete(first=0,last='end')
        self.py1 = self.entrypy1.delete(first=0,last='end')
        self.py2 = self.entrypy2.delete(first=0,last='end')
        self.py3 = self.entrypy3.delete(first=0,last='end')
        self.py4 = self.entrypy4.delete(first=0,last='end')
        self.py5 = self.entrypy5.delete(first=0,last='end')
        self.py6 = self.entrypy6.delete(first=0,last='end')
        self.py7 = self.entrypy7.delete(first=0,last='end')
        self.py8 = self.entrypy8.delete(first=0,last='end')
        self.py9 = self.entrypy9.delete(first=0,last='end')
        self.py10 = self.entrypy10.delete(first=0,last='end')
        self.piewin.resizable(width = False, height = False)
        self.piegraph.cla()
        self.piegraph.clear()
        self.canvas25.draw()
        self.forthwin.withdraw()
        self.piewin.deiconify()
        self.button33.config(state="normal")
        self.button34.config(state="disabled")

    def getpie(self):
        def onclick():
            root.quit()
            self.piewin.withdraw()
        self.piewin.protocol("WM_DELETE_WINDOW", onclick)
        self.px1 = self.entrypx1.get()
        self.px2 = self.entrypx2.get()
        self.px3 = self.entrypx3.get()
        self.px4 = self.entrypx4.get()
        self.px5 = self.entrypx5.get()
        self.px6 = self.entrypx6.get()
        self.px7 = self.entrypx7.get()
        self.px8 = self.entrypx8.get()
        self.px9 = self.entrypx9.get()
        self.px10 = self.entrypx10.get()
        self.py1 = self.entrypy1.get()
        self.py2 = self.entrypy2.get()
        self.py3 = self.entrypy3.get()
        self.py4 = self.entrypy4.get()
        self.py5 = self.entrypy5.get()
        self.py6 = self.entrypy6.get()
        self.py7 = self.entrypy7.get()
        self.py8 = self.entrypy8.get()
        self.py9 = self.entrypy9.get()
        self.py10 = self.entrypy10.get()

        list = [self.px1, self.px2, self.px3, self.px4, self.px5, self.px6, self.px7,
                self.px8, self.px9, self.px10]
        list1 = [self.py1, self.py2, self.py3, self.py4, self.py5, self.py6, self.py7,
                 self.py8, self.py9, self.py10]
        rlist = [i for i in list if i]
        rlist1 = [i for i in list1 if i]
        print(rlist)
        print(rlist1)
        try:
            flist = [float(i) for i in rlist1]
            colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'green', 'red',
                      'blue', 'grey', 'black', 'white']
            self.piegraph.grid()
            self.piegraph.pie(flist, labels=rlist, colors=colors[:len(flist)+1],startangle=140)
            self.canvas25.draw()
            self.button33.config(state="disabled")
            self.button34.config(state="normal")
        except ValueError:
            tkinter.messagebox.showinfo("Invalid Parameter",
                                        "Please enter Integer or Float value. For Example - 2.5 or 2")
    def updatepie(self):
        def onclick():
            root.quit()
            self.piewin.withdraw()
        self.piewin.protocol("WM_DELETE_WINDOW", onclick)
        self.px1 = self.entrypx1.get()
        self.px2 = self.entrypx2.get()
        self.px3 = self.entrypx3.get()
        self.px4 = self.entrypx4.get()
        self.px5 = self.entrypx5.get()
        self.px6 = self.entrypx6.get()
        self.px7 = self.entrypx7.get()
        self.px8 = self.entrypx8.get()
        self.px9 = self.entrypx9.get()
        self.px10 = self.entrypx10.get()
        self.py1 = self.entrypy1.get()
        self.py2 = self.entrypy2.get()
        self.py3 = self.entrypy3.get()
        self.py4 = self.entrypy4.get()
        self.py5 = self.entrypy5.get()
        self.py6 = self.entrypy6.get()
        self.py7 = self.entrypy7.get()
        self.py8 = self.entrypy8.get()
        self.py9 = self.entrypy9.get()
        self.py10 = self.entrypy10.get()
        list = []
        list1 = []
        list = [self.px1, self.px2, self.px3, self.px4, self.px5, self.px6, self.px7,
                self.px8, self.px9, self.px10]
        list1 = [self.py1, self.py2, self.py3, self.py4, self.py5, self.py6, self.py7,
                 self.py8, self.py9, self.py10]

        self.piegraph.cla()
        rlist = [i for i in list if i]
        rlist1 = [i for i in list1 if i]
        print(rlist)
        print(rlist1)
        try:
            flist = [float(i) for i in rlist1]
            colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'green', 'red',
                      'blue', 'grey', 'black', 'white']
            self.piegraph.grid()
            self.piegraph.pie(flist, labels=rlist, colors=colors[:len(flist)+1],startangle=140)
            self.canvas25.draw()
        except ValueError:
            tkinter.messagebox.showinfo("Invalid Parameter",
                                        "Please enter Integer or Float value. For Example - 2.5 or 2")

    #Histogram Plot

    def hist(self):
        def onclick():
            root.quit()
            self.histwin.withdraw()
        self.histwin.protocol("WM_DELETE_WINDOW", onclick)
        self.hx1 = self.entryhx1.delete(first=0,last='end')
        self.hx2 = self.entryhx2.delete(first=0,last='end')
        self.hx3 = self.entryhx3.delete(first=0,last='end')
        self.hx4 = self.entryhx4.delete(first=0,last='end')
        self.hx5 = self.entryhx5.delete(first=0,last='end')
        self.hx6 = self.entryhx6.delete(first=0,last='end')
        self.hx7 = self.entryhx7.delete(first=0,last='end')
        self.hx8 = self.entryhx8.delete(first=0,last='end')
        self.hx9 = self.entryhx9.delete(first=0,last='end')
        self.hx10 = self.entryhx10.delete(first=0,last='end')
        self.histwin.resizable(width = False, height = False)
        self.histgraph.cla()
        self.histgraph.clear()
        self.canvas21.draw()
        self.forthwin.withdraw()
        self.histwin.deiconify()
        self.button35.config(state="normal")
        self.button36.config(state="disabled")

    def gethist(self):
        def onclick():
            root.quit()
            self.histwin.withdraw()
        self.histwin.protocol("WM_DELETE_WINDOW", onclick)
        self.hx1 = self.entryhx1.get()
        self.hx2 = self.entryhx2.get()
        self.hx3 = self.entryhx3.get()
        self.hx4 = self.entryhx4.get()
        self.hx5 = self.entryhx5.get()
        self.hx6 = self.entryhx6.get()
        self.hx7 = self.entryhx7.get()
        self.hx8 = self.entryhx8.get()
        self.hx9 = self.entryhx9.get()
        self.hx10 = self.entryhx10.get()
        
        list = []
        list1 = []
        list = [self.hx1, self.hx2, self.hx3, self.hx4, self.hx5, self.hx6, self.hx7,
                self.hx8, self.hx9, self.hx10]
        try:
            print(list)
            rlist = [i for i in list if i]
            print(rlist)
            
            b = max(rlist,key=rlist.count)
            bin = rlist.count(b)
            if bin == 1:
                bin = int(max(rlist))
                
            try:
                flist = [float(i) for i in rlist]
                
            except ValueError:
                tkinter.messagebox.showinfo("Invalid Parameter",
                                            "Please enter Integer or Float value. For Example - 2.5 or 2")
            
            self.histgraph.hist(flist, bin,rwidth=0.95)
            self.histgraph.set_xlabel('X-Label')
            self.histgraph.set_ylabel('Y-Label')
            self.histgraph.set_yticks(range(bin+1))
            self.canvas21.draw()
            self.button35.config(state="disabled")
            self.button36.config(state="normal")
        except ValueError:
            tkinter.messagebox.showinfo("Invalid Parameter",
                                        "Bins must be positive and an Integer value")
    def updatehist(self):
        def onclick():
            root.quit()
            self.histwin.withdraw()
        self.histwin.protocol("WM_DELETE_WINDOW", onclick)
        self.hx1 = self.entryhx1.get()
        self.hx2 = self.entryhx2.get()
        self.hx3 = self.entryhx3.get()
        self.hx4 = self.entryhx4.get()
        self.hx5 = self.entryhx5.get()
        self.hx6 = self.entryhx6.get()
        self.hx7 = self.entryhx7.get()
        self.hx8 = self.entryhx8.get()
        self.hx9 = self.entryhx9.get()
        self.hx10 = self.entryhx10.get()
        
        
        list = []
        list1 = []
        list = [self.hx1, self.hx2, self.hx3, self.hx4, self.hx5, self.hx6, self.hx7,
                self.hx8, self.hx9, self.hx10]
        try:
            bin = max(list,key=list.count)
            print(bin)
            print(list)
            
            self.histgraph.cla()

            rlist = [i for i in list if i]
            print(rlist)
            b = max(rlist,key=rlist.count)
            bin = rlist.count(b)
            if bin == 1:
                bin = int(max(rlist))
            try:
                flist = [float(i) for i in rlist]
            except ValueError:
                tkinter.messagebox.showinfo("Invalid Parameter",
                                            "Please enter Integer or Float value. For Example - 2.5 or 2")
            
            self.histgraph.hist(flist,bin,rwidth=0.95)
            self.histgraph.set_xlabel('X-Label')
            self.histgraph.set_ylabel('Y-Label')
            self.histgraph.set_yticks(range(bin+1))
            self.canvas21.draw()
        except ValueError:
            tkinter.messagebox.showinfo("Invalid Parameter",
                                        "Bins must be positive and an Integer value")

    #Signal Plot

    def signal(self):
        def onclick():
            root.quit()
            self.signalwin.withdraw()
        self.signalwin.protocol("WM_DELETE_WINDOW", onclick)
        self.six1 = self.entrysix1.delete(first=0,last='end')
        self.six2 = self.entrysix2.delete(first=0,last='end')
        self.signalwin.resizable(width = False, height = False)
        self.signalgraph.cla()
        self.signalgraph.clear()
        self.canvas29.draw()
        self.forthwin.withdraw()
        self.signalwin.deiconify()
        self.button37.config(state="normal")
        self.button39.config(state="normal")

    #Sine Function

    def getsine(self):
        def onclick():
            root.quit()
            self.signalwin.withdraw()
        self.signalwin.protocol("WM_DELETE_WINDOW", onclick)
        self.six1 = self.entrysix1.get()
        self.signalgraph.cla()
        list = []
        try:
            list = float(self.six1)

            time = np.arange(0,list,0.1)
            print(time)
            amp = np.sin(time)
            self.signalgraph.plot(time, amp, color="green")
            self.signalgraph.set_xlabel('X-Label')
            self.signalgraph.set_ylabel('Y-Label')
            self.signalgraph.grid()
            self.canvas29.draw()
        except ValueError:
                tkinter.messagebox.showinfo("Invalid Parameter",
                                            "Please enter Integer or Float value. For Example - 2.5 or 2")

    #Cosine Function
    
    def getcos(self):
        def onclick():
            root.quit()
            self.signalwin.withdraw()
        self.signalwin.protocol("WM_DELETE_WINDOW", onclick)
        self.six2 = self.entrysix2.get()

        self.signalgraph.cla()
        
        list = []
        try:
            list = float(self.six2)
            time = np.arange(0,list,0.1)
            print(time)
            amp = np.cos(time)
            self.signalgraph.plot(time, amp, color="green")
            self.signalgraph.set_xlabel('X-Label')
            self.signalgraph.set_ylabel('Y-Label')
            self.signalgraph.grid()
            self.canvas29.draw()
        except ValueError:
                tkinter.messagebox.showinfo("Invalid Parameter",
                                            "Please enter Integer or Float value. For Example - 2.5 or 2")

if __name__ == "__main__":
    root = Tk()
    myApp = Visualization(root)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(width=False, height=False)
    root.mainloop()
