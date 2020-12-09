from tkinter import *
from PIL import ImageTk, Image
from tkinter import font,filedialog
import tkinter.messagebox
import io
import os
import ghostscript #It is an API to save canvas contents as image.
                   #You need to install in your System. I provided the link in document to download.

coordinates = [] #For Triangle Function
class Geometric_Shapes:
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


        #Initial declarations for Triangle function

        self.verts = []
        self.vert_ids = []


        self.master = master
        self.function_generator = Shapes()
        master.title("HEU Technologies - Geometric Shape Prediction")

        def onclick():
            root.quit()
            self.master.withdraw()

        self.master.protocol("WM_DELETE_WINDOW", onclick)

        self.canvas = Canvas(self.master, width=1000, height=650)
        self.canvas.pack()

        self.image = ImageTk.PhotoImage(Image.open("Images/bg.png"))
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)

        self.image1 = ImageTk.PhotoImage(Image.open("Images/logo.png"))
        self.canvas.create_image(485, 650, anchor=S, image=self.image1)

        self.canvas1 = Canvas(self.master, width=500, height=75)
        self.canvas1.place(x=250, y=20)

        self.i = self.canvas1.create_text(250, 35, fill="white", font=("Times New Roman 20 italic bold", 28),
                                           text="Geometric Shape Prediction")

        self.r = self.canvas1.create_rectangle(self.canvas.bbox(ALL), fill="#555BA7")
        self.canvas1.tag_lower(self.r, self.i)

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

        self.image2 = ImageTk.PhotoImage(Image.open("Images/bg.png"))
        self.canvas2.create_image(0, 0, anchor=NW, image=self.image2)

        self.canvas2.create_text(100, 75, fill="black", font=("Times New Roman 20 bold", 32),
                                 text="About:")

        para = """
    Learn how to build your Geometric shape prediction
    model by creating the data, training the model and
    testing your model results

    Understand the steps involved in AI Project
        * Create your own database
        * Train AI Model
        * Predict with new drawn data"""

        self.canvas2.create_text(400, 275, fill="black", font=("Times New Roman", 22),
                                 text=para)

        self.button2 = Button(self.secondWin, text="Click for Help", command=self.clickforhelp, anchor=CENTER)
        self.button2.configure(width=10, activebackground="#33B5E5", bg='#558DEA', relief=FLAT)
        self.button2_window = self.canvas2.create_window(100, 500, anchor=NW, window=self.button2)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button2['font'] = font1
        self.button2.config(width=12, height=2)

        self.button3 = Button(self.secondWin, text="HOME", command=self.home, anchor=CENTER)
        self.button3.configure(width=10, activebackground="#33B5E5", bg='#558DEA', relief=FLAT)
        self.button3_window = self.canvas2.create_window(400, 500, anchor=NW, window=self.button3)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button3['font'] = font1
        self.button3.config(width=12, height=2)

        self.button4 = Button(self.secondWin, text="Click to Begin", command=self.clicktobegin, anchor=CENTER)
        self.button4.configure(width=10, activebackground="#33B5E5", bg='#558DEA', relief=FLAT)
        self.button4_window = self.canvas2.create_window(700, 500, anchor=NW, window=self.button4)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button4['font'] = font1
        self.button4.config(width=12, height=2)

        self.secondWin.protocol("WM_DELETE_WINDOW", root.destroy)

        self.secondWin.withdraw()

        self.ThirdWin = Toplevel()

        self.ThirdWin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas3 = Canvas(self.ThirdWin, width=1000, height=650)
        self.canvas3.pack()

        self.image3 = ImageTk.PhotoImage(Image.open("Images/bg.png"))
        self.canvas3.create_image(0, 0, anchor=NW, image=self.image3)

        self.button5 = Button(self.ThirdWin, foreground="white", text="HOME", command=self.thirdwinhome,
                              anchor=CENTER)
        self.button5.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button5_window = self.canvas3.create_window(60, 20, anchor=NW, window=self.button5)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button5['font'] = font1
        self.button5.config(width=10, height=1)

        self.button6 = Button(self.ThirdWin, foreground="white", text="EXIT", command=self.exit, anchor=CENTER)
        self.button6.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button6_window = self.canvas3.create_window(800, 20, anchor=NW, window=self.button6)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button6['font'] = font1
        self.button6.config(width=10, height=1)

        self.canvas4 = Canvas(self.ThirdWin,bg="#8DC1E8", width=900, height=500)
        self.canvas4.place(x=50,y=75)

        self.i = self.canvas4.create_text(450, 50, fill="white", font=("Times 20"),
                                           text=" Geometric Shape Prediction ")
        self.r = self.canvas4.create_rectangle(self.canvas4.bbox(self.i),fill="#2C56BC",outline="#2C56BC")
        self.canvas4.tag_lower(self.r, self.i)

        self.button7 = Button(self.ThirdWin, foreground="white", text="Create your own \n Database",
                              command=self.createdatabase, anchor=CENTER)
        self.button7.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button7_window = self.canvas4.create_window(100, 150, anchor=NW, window=self.button7)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button7['font'] = font1
        self.button7.config(width=15, height=10)

        self.canvas4.create_line(280, 270, 350, 270, fill="#2C56BC",arrow='last',width=12)

        self.button8 = Button(self.ThirdWin, foreground="white", text="Train AI Model \n and \n Save Database",
                              command=self.trainmodel, anchor=CENTER)
        self.button8.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button8_window = self.canvas4.create_window(350, 150, anchor=NW, window=self.button8)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button8['font'] = font1
        self.button8.config(width=15, height=10)

        self.canvas4.create_line(530, 270, 600, 270, fill="#2C56BC",arrow='last',width=12)

        self.button9 = Button(self.ThirdWin, foreground="white", text="Local Database \n and \n Test our Model",
                              command=self.testmodel, anchor=CENTER)
        self.button9.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button9_window = self.canvas4.create_window(600, 150, anchor=NW, window=self.button9)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button9['font'] = font1
        self.button9.config(width=15, height=10)

        self.button10 = Button(self.ThirdWin, foreground="white", text="BACK", command=self.back, anchor=CENTER)
        self.button10.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button10_window = self.canvas3.create_window(450, 600, anchor=NW, window=self.button10)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button10['font'] = font1
        self.button10.config(width=10, height=1)

        self.ThirdWin.protocol("WM_DELETE_WINDOW", root.destroy)

        self.ThirdWin.withdraw()

        self.Databasewin = Toplevel()

        self.Databasewin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas5 = Canvas(self.Databasewin, width=1000, height=650)
        self.canvas5.pack()

        self.image4 = ImageTk.PhotoImage(Image.open("Images/bg.png"))
        self.canvas5.create_image(0, 0, anchor=NW, image=self.image4)

        self.button11 = Button(self.Databasewin, foreground="white", text="HOME", command=self.dbwinhome,
                              anchor=CENTER)
        self.button11.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button11_window = self.canvas5.create_window(60, 20, anchor=NW, window=self.button11)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button11['font'] = font1
        self.button11.config(width=10, height=1)

        self.button12 = Button(self.Databasewin, foreground="white", text="EXIT", command=self.exit, anchor=CENTER)
        self.button12.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button12_window = self.canvas5.create_window(800, 20, anchor=NW, window=self.button12)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button12['font'] = font1
        self.button12.config(width=10, height=1)

        self.canvas6 = Canvas(self.Databasewin,bg="#8DC1E8", width=900, height=500)
        self.canvas6.place(x=50,y=75)

        self.i = self.canvas6.create_text(450, 40, fill="white", font=("Times 20"),
                                           text="  Database Creation  ")
        self.r = self.canvas6.create_rectangle(self.canvas6.bbox(self.i),fill="#2C56BC",outline="#2C56BC")
        self.canvas6.tag_lower(self.r, self.i)

        self.i = self.canvas6.create_text(200, 100, fill="white", font=("Times 20"),
                                           text="  Shapes  ")
        self.r = self.canvas6.create_rectangle(self.canvas6.bbox(self.i),fill="#2C56BC",outline="#2C56BC")
        self.canvas6.tag_lower(self.r, self.i)

        self.button13 = Button(self.Databasewin, foreground="black", text="CIRCLE", command=self.circle, anchor=CENTER)
        self.button13.configure(width=10, activebackground="#33B5E5", bg='white', relief=FLAT)
        self.button13_window = self.canvas6.create_window(130, 160, anchor=NW, window=self.button13)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button13['font'] = font1
        self.button13.config(width=10, height=1)

        self.button14 = Button(self.Databasewin, foreground="black", text="TRIANGLE", command=self.triangle,
                               anchor=CENTER)
        self.button14.configure(width=10, activebackground="#33B5E5", bg='white', relief=FLAT)
        self.button14_window = self.canvas6.create_window(130, 260, anchor=NW, window=self.button14)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button14['font'] = font1
        self.button14.config(width=10, height=1)

        self.button15 = Button(self.Databasewin, foreground="black", text="RECTANGLE", command=self.rectangle,
                               anchor=CENTER)
        self.button15.configure(width=10, activebackground="#33B5E5", bg='white', relief=FLAT)
        self.button15_window = self.canvas6.create_window(130, 360, anchor=NW, window=self.button15)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button15['font'] = font1
        self.button15.config(width=10, height=1)

        self.canvas7 = Canvas(self.Databasewin,bg="white", width=400, height=350)
        self.canvas7.place(x=400,y=150)

        self.button16 = Button(self.Databasewin, foreground="black", text="Click to save", command=self.clicktosave,
                               anchor=CENTER)
        self.button16.configure(width=10, activebackground="#33B5E5", bg='white', relief=FLAT)
        self.button16_window = self.canvas6.create_window(400, 450, anchor=NW, window=self.button16)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button16['font'] = font1
        self.button16.config(width=10, height=1)

        self.button27 = Button(self.Databasewin, foreground="black", text="Choose Folders", command=self.choosefolder,
                               anchor=CENTER)
        self.button27.configure(width=10, activebackground="#33B5E5", bg='white', relief=FLAT)
        self.button27_window = self.canvas6.create_window(550, 450, anchor=NW, window=self.button27)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button27['font'] = font1
        self.button27.config(width=12, height=1)

        self.button17 = Button(self.Databasewin, foreground="white", text="BACK", command=self.dbwinback, anchor=CENTER)
        self.button17.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button17_window = self.canvas5.create_window(450, 600, anchor=NW, window=self.button17)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button17['font'] = font1
        self.button17.config(width=10, height=1)

        self.Databasewin.protocol("WM_DELETE_WINDOW", root.destroy)

        self.Databasewin.withdraw()

        self.Trainwin = Toplevel()

        self.Trainwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas8 = Canvas(self.Trainwin, width=1000, height=650)
        self.canvas8.pack()

        self.image5 = ImageTk.PhotoImage(Image.open("Images/bg.png"))
        self.canvas8.create_image(0, 0, anchor=NW, image=self.image5)

        self.button18 = Button(self.Trainwin, foreground="white", text="HOME", command=self.trainwinhome,
                              anchor=CENTER)
        self.button18.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button18_window = self.canvas8.create_window(60, 20, anchor=NW, window=self.button18)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button18['font'] = font1
        self.button18.config(width=10, height=1)

        self.button19 = Button(self.Trainwin, foreground="white", text="EXIT", command=self.exit, anchor=CENTER)
        self.button19.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button19_window = self.canvas8.create_window(800, 20, anchor=NW, window=self.button19)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button19['font'] = font1
        self.button19.config(width=10, height=1)

        self.canvas9 = Canvas(self.Trainwin,bg="#8DC1E8", width=900, height=500)
        self.canvas9.place(x=50,y=75)

        self.i = self.canvas9.create_text(450, 40, fill="white", font=("Times 20"),
                                           text="  TRAIN AND SAVE MODEL  ")
        self.r = self.canvas9.create_rectangle(self.canvas9.bbox(self.i),fill="#2C56BC",outline="#2C56BC")
        self.canvas9.tag_lower(self.r, self.i)

        self.canvas10 = Canvas(self.Trainwin,bg="white", width=180, height=225)
        self.canvas10.place(x=100,y=200)

        self.canvas10.create_text(100,100,fill="black",font="Times 16 bold",
                        text="         Upload \nDatabase images")

        self.button22 = Button(self.Trainwin, foreground="black", text="Click Here", command=self.uploadfolder,
                               anchor=CENTER)
        self.button22.configure(width=10, activebackground="#33B5E5", bg='#8DC1E8', relief=FLAT)
        self.button22_window = self.canvas10.create_window(20, 170, anchor=NW, window=self.button22)
        font1 = font.Font(family='Times New Roman', size=14, weight='normal')
        self.button22['font'] = font1
        self.button22.config(width=12, height=1)

        self.canvas9.create_line(250, 230, 300, 230, fill="white",arrow='last',width=12)

        self.button20 = Button(self.Trainwin, foreground="black", text="Train \n AI Model", command=self.trainaimodel,
                               anchor=CENTER)
        self.button20.configure(width=10, activebackground="#33B5E5", bg='white', relief=FLAT)
        self.button20_window = self.canvas9.create_window(325, 125, anchor=NW, window=self.button20)
        font1 = font.Font(family='Times New Roman', size=16, weight='bold')
        self.button20['font'] = font1
        self.button20.config(width=15, height=9)

        self.canvas9.create_line(530, 230, 580, 230, fill="white",arrow='last',width=12)

        self.button21 = Button(self.Trainwin, foreground="black", text="Save Model \n and \n Database",
                               command=self.savemodel, anchor=CENTER)
        self.button21.configure(width=10, activebackground="#33B5E5", bg='white', relief=FLAT)
        self.button21_window = self.canvas9.create_window(620, 125, anchor=NW, window=self.button21)
        font1 = font.Font(family='Times New Roman', size=16, weight='bold')
        self.button21['font'] = font1
        self.button21.config(width=15, height=9)

        self.button23 = Button(self.Trainwin, foreground="white", text="BACK", command=self.trainwinback, anchor=CENTER)
        self.button23.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button23_window = self.canvas8.create_window(450, 600, anchor=NW, window=self.button23)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button23['font'] = font1
        self.button23.config(width=10, height=1)

        self.Trainwin.protocol("WM_DELETE_WINDOW", root.destroy)

        self.Trainwin.withdraw()

        self.Testwin = Toplevel()

        self.Testwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas11 = Canvas(self.Testwin, width=1000, height=650)
        self.canvas11.pack()

        self.image6 = ImageTk.PhotoImage(Image.open("Images/bg.png"))
        self.canvas11.create_image(0, 0, anchor=NW, image=self.image6)

        self.button24 = Button(self.Testwin, foreground="white", text="HOME", command=self.testwinhome,
                              anchor=CENTER)
        self.button24.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button24_window = self.canvas11.create_window(60, 20, anchor=NW, window=self.button24)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button24['font'] = font1
        self.button24.config(width=10, height=1)

        self.button25 = Button(self.Testwin, foreground="white", text="EXIT", command=self.exit, anchor=CENTER)
        self.button25.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button25_window = self.canvas11.create_window(800, 20, anchor=NW, window=self.button25)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button25['font'] = font1
        self.button25.config(width=10, height=1)

        self.canvas12 = Canvas(self.Testwin,bg="#8DC1E8", width=900, height=500)
        self.canvas12.place(x=50,y=75)

        self.i = self.canvas12.create_text(450, 40, fill="white", font=("Times 20"),
                                           text="  Testing AI Model  ")
        self.r = self.canvas12.create_rectangle(self.canvas12.bbox(self.i),fill="#2C56BC",outline="#2C56BC")
        self.canvas12.tag_lower(self.r, self.i)

        self.canvas13 = Canvas(self.canvas12,bg="white", width=275, height=300)
        self.canvas13.place(x=50,y=125)

        self.i = self.canvas13.create_text(125, 40, fill="black", font=("Times 20"),
                                           text="  DRAW  ")
        self.r = self.canvas13.create_rectangle(self.canvas13.bbox(self.i),fill="#2C56BC",outline="#2C56BC")
        self.canvas13.tag_lower(self.r, self.i)

        #Binding Canvas to make sketch

        def draw(event):
            x1,y1 = (event.x-1),(event.y-1)
            x2,y2 = (event.x+1),(event.y+1)
            self.canvas13.create_oval(x1,y1,x2,y2,outline='black')

        self.canvas13.bind('<B1-Motion>',draw)

        self.canvas12.create_line(350, 230, 380, 230, fill="#2C56BC",arrow='last',width=12)

        self.button26 = Button(self.Testwin, foreground="black", text="GEOMETRIC SHAPE \n PREDICTION \n MODEL",
                               command=self.geometricshapeprediction, anchor=CENTER)
        self.button26.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button26_window = self.canvas12.create_window(390, 180, anchor=NW, window=self.button26)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button26['font'] = font1
        self.button26.config(width=15, height=5)

        self.canvas12.create_line(600, 230, 630, 230, fill="#2C56BC",arrow='last',width=12)

        self.canvas14 = Canvas(self.canvas12,bg="white", width=200, height=300)
        self.canvas14.place(x=650,y=125)

        self.i = self.canvas14.create_text(100, 40, fill="black", font=("Times 20"),
                                           text="  Result  ")
        self.r = self.canvas14.create_rectangle(self.canvas14.bbox(self.i),fill="#2C56BC",outline="#2C56BC")
        self.canvas14.tag_lower(self.r, self.i)

        self.button23 = Button(self.Testwin, foreground="white", text="BACK", command=self.testwinback, anchor=CENTER)
        self.button23.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button23_window = self.canvas11.create_window(450, 600, anchor=NW, window=self.button23)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button23['font'] = font1
        self.button23.config(width=10, height=1)

        self.Testwin.protocol("WM_DELETE_WINDOW", root.destroy)

        self.Testwin.withdraw()
        
    def home(self):
        '''It get you to Home Page'''
        
        self.secondWin.withdraw()
        self.master.deiconify()

    def back(self):
        '''It get you to SecondWin from ThirdWin'''
        
        self.ThirdWin.withdraw()
        self.secondWin.deiconify()

    def clicktostart(self):
        '''It get you to Second Page'''
        
        def onclick():
            root.quit()
            self.secondWin.withdraw()

        self.secondWin.protocol("WM_DELETE_WINDOW", onclick)
        self.secondWin.resizable(width=False, height=False)
        self.master.withdraw()
        self.secondWin.deiconify()
        
    def clickforhelp(self):
        '''It shows message box what exactly the application does.'''
        tkinter.messagebox.showinfo("Info", "")
        
    def clicktobegin(self):
        '''It get you to Third Window where you can select Various options'''
        
        def onclick():
            root.quit()
            self.ThirdWin.withdraw()
        self.ThirdWin.protocol("WM_DELETE_WINDOW", onclick)
        self.ThirdWin.resizable(width=False, height=False)
        self.secondWin.withdraw()
        self.ThirdWin.deiconify()

    def thirdwinhome(self):
        '''It get you to Home Page from Third Page'''
        
        def onclick():
            root.quit()
            self.master.withdraw()
        self.master.protocol("WM_DELETE_WINDOW", onclick)
        self.ThirdWin.withdraw()
        self.master.deiconify()

    def dbwinhome(self):
        '''It get you to Home Page from DatabaseWin page'''
        
        def onclick():
            root.quit()
            self.master.withdraw()
        self.master.protocol("WM_DELETE_WINDOW", onclick)
        self.Databasewin.withdraw()
        self.master.deiconify()


    def dbwinback(self):
        '''It get you to Third Window from DatabaseWin'''
        
        def onclick():
            root.quit()
            self.master.withdraw()
        self.master.protocol("WM_DELETE_WINDOW", onclick)
        self.Databasewin.withdraw()
        self.ThirdWin.deiconify()

    def trainwinhome(self):
        '''It get you to Home Page from TrainWin'''

        def onclick():
            root.quit()
            self.master.withdraw()
        self.master.protocol("WM_DELETE_WINDOW", onclick)
        self.Trainwin.withdraw()
        self.master.deiconify()

    def trainwinback(self):
        '''It get you to DatabaseWin from TrainWin'''
        
        def onclick():
            root.quit()
            self.master.withdraw()
        self.master.protocol("WM_DELETE_WINDOW", onclick)
        self.Trainwin.withdraw()
        self.Databasewin.deiconify()

    def testwinhome(self):
        '''It get you to Home Page from TestWin Page'''
        
        def onclick():
            root.quit()
            self.master.withdraw()
        self.master.protocol("WM_DELETE_WINDOW", onclick)
        self.Testwin.withdraw()
        self.master.deiconify()

    def testwinback(self):
        '''It get you to TrainWin from TestWin'''
        
        def onclick():
            root.quit()
            self.master.withdraw()
        self.master.protocol("WM_DELETE_WINDOW", onclick)
        self.Testwin.withdraw()
        self.Trainwin.deiconify()

    def exit(self):
        '''It Terminates the Application from Anywhere'''
        
        self.ThirdWin.withdraw()
        self.Databasewin.withdraw()
        self.Trainwin.withdraw()
        self.Testwin.withdraw()
        sys.exit(myApp)

    def createdatabase(self):
        '''It is the window where you can create your images and save in the desired folders'''
        
        self.ThirdWin.withdraw()
        self.Databasewin.deiconify()
        
        self.button13.config(state="disabled")
        self.button14.config(state="disabled")
        self.button15.config(state="disabled")
        self.button16.config(state="disabled")

        self.infowin = Toplevel()
        self.infowin.title("Info")
        w = 260
        h = 150
        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen
        x = (ws/2.5) - (w/2.5)
        y = (hs/2.5) - (h/2.5)
        Message(self.infowin, text ="Choose Three foldres ony-by-one.\nThe first folder is for Circle.\nThe\Second folder is for Triangle\nThe Third folder is for Rectangle.",
                padx = 20,pady = 20).pack()
        self.infowin.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.infowin.resizable(width=False, height=False)
        self.infowin.after(3000,self.infowin.destroy)

    def choosefolder(self):
        '''It is the function to choose three folder of Circle, Triangle and Rectangle respectively'''

        global dirs

        i = 0
        dirs = []

        while i < 3:
            dirname = filedialog.askdirectory()
            dirs.append(dirname)
            i+=1
        self.button13.config(state="normal")
        self.button14.config(state="normal")
        self.button15.config(state="normal")
        self.button16.config(state="normal")
        self.button27.config(state="disabled")
        
        print(dirs)
        print(dirs[0])

    def clicktosave(self):
        '''This is the function to save the Image to selected folders'''

        global count

        #Circle Folder

        if count == 1:

            print(count)
            
            i = 1
            while os.path.exists(dirs[0]+"/circle%s.png" % i):
                i+=1
            file = "circle%s"%i

            ps = self.canvas7.postscript(colormode='color')
            img = Image.open(io.BytesIO(ps.encode('utf-8')))
            path = tkinter.filedialog.asksaveasfilename(defaultextension = '.png',
                                                        initialdir=dirs[0],
                                                        initialfile = file)        
            img.save(path)

        #Triangle Folder

        if count == 2:

            print(count)

            i = 1
            while os.path.exists(dirs[1]+"/triangle%s.png" % i):
                i+=1
            file = "triangle%s"%i
                
            ps = self.canvas7.postscript(colormode='color')
            img = Image.open(io.BytesIO(ps.encode('utf-8')))
            path = tkinter.filedialog.asksaveasfilename(defaultextension = '.png',
                                                        initialdir=dirs[1],
                                                        initialfile = file)        
            img.save(path)

        #Rectangle Folder

        if count == 3:

            print(count)

            i = 1
            while os.path.exists(dirs[2]+"/rectangle%s.png" % i):
                i+=1
            file = "rectangle%s"%i
                
            ps = self.canvas7.postscript(colormode='color')
            img = Image.open(io.BytesIO(ps.encode('utf-8')))
            path = tkinter.filedialog.asksaveasfilename(defaultextension = '.png',
                                                        initialdir=dirs[2],
                                                        initialfile = file)        
            img.save(path)
            
        self.button13.config(state="normal")
        self.button14.config(state="normal")
        self.button15.config(state="normal")

        self.canvas7.delete("all")
        
    def trainmodel(self):
        '''It get you to Train Model Window'''
        
        self.ThirdWin.withdraw()
        self.Trainwin.deiconify()

    def trainaimodel(self):
        print("Train Model")

    def uploadfolder(self):
        '''It is for choose folder for training model'''
        
        directory = filedialog.askdirectory()
        print(directory)

    def savemodel(self):
        print("Save Model in Database")
        
    def testmodel(self):
        '''It get you to Testing Window'''
        
        self.ThirdWin.withdraw()
        self.Testwin.deiconify()

    #Circle Function

    def circle(self):
        print("Circle")

        #Popup Message

        self.infowin = Toplevel()
        self.infowin.title("Info")
        w = 260
        h = 100
        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen
        x = (ws/2.5) - (w/2.5)
        y = (hs/2.5) - (h/2.5)
        Message(self.infowin, text ="Click and drag on the Drawing area to make Circle",
                padx = 20,pady = 20).pack()
        self.infowin.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.infowin.resizable(width=False, height=False)
        self.infowin.after(3000,self.infowin.destroy)
        

        self.colorwin = Toplevel()
        self.colorwin.title("Choose Color")
        w = 260
        h = 100
        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen
        x = (ws/2.5) - (w/2.5)
        y = (hs/2.5) - (h/2.5)
        self.colorwin.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.colorwin.resizable(width=False, height=False)
        BlueButton = Button(self.colorwin,text="Blue",bg="Blue",fg="white",width=5,command=self.blue)
        BlueButton.place(x=20,y=40)
        RedButton = Button(self.colorwin,text="Red",bg="Red",fg="white",width=5,command=self.red)
        RedButton.place(x=100,y=40)
        BlackButton = Button(self.colorwin,text="Black",bg="Black",fg="white",width=5,command=self.black)
        BlackButton.place(x=180,y=40)
        
        global count

        count = 1

        self.x = self.y = 0

        self.canvas7.bind("<ButtonPress-1>", self.on_button_press_c)
        self.canvas7.bind("<B1-Motion>", self.on_move_press_c)
        self.canvas7.bind("<ButtonRelease-1>", self.on_button_release_c)

        self.circle = None

        self.start_x = None
        self.start_y = None

        self.button13.config(state="disabled")
        self.button14.config(state="disabled")
        self.button15.config(state="disabled")

    def on_button_press_c(self, event):
        # save mouse drag start position
        self.start_x = self.canvas7.canvasx(event.x)
        self.start_y = self.canvas7.canvasy(event.y)

        # create circle if not yet exist
        if not self.circle:
            self.circle = self.canvas7.create_oval(self.x, self.y, 1, 1,fill = color)

    def on_move_press_c(self, event):
        curX = self.canvas7.canvasx(event.x)
        curY = self.canvas7.canvasy(event.y)

        w, h = self.canvas7.winfo_width(), self.canvas7.winfo_height()

        # expand circle as you drag the mouse
        self.canvas7.coords(self.circle, self.start_x, self.start_y, curX, curY)    

    def on_button_release_c(self, event):
        pass

    #Triangle Function

    def triangle(self):
        print("Triangle")

        #Popup Message

        self.infowin = Toplevel()
        self.infowin.title("Info")
        w = 260
        h = 100
        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen
        x = (ws/2.5) - (w/2.5)
        y = (hs/2.5) - (h/2.5)
        Message(self.infowin, text ="Randomly Click 3 times on the draw area that will make triangle",
                padx = 20,pady = 20).pack()
        self.infowin.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.infowin.resizable(width=False, height=False)
        self.infowin.after(3000,self.infowin.destroy)

        self.colorwin = Toplevel()
        self.colorwin.title("Choose Color")
        w = 260
        h = 100
        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen
        x = (ws/2.5) - (w/2.5)
        y = (hs/2.5) - (h/2.5)
        self.colorwin.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.colorwin.resizable(width=False, height=False)
        BlueButton = Button(self.colorwin,text="Blue",bg="Blue",fg="white",width=5,command=self.blue)
        BlueButton.place(x=20,y=40)
        RedButton = Button(self.colorwin,text="Red",bg="Red",fg="white",width=5,command=self.red)
        RedButton.place(x=100,y=40)
        BlackButton = Button(self.colorwin,text="Black",bg="Black",fg="white",width=5,command=self.black)
        BlackButton.place(x=180,y=40)

        self.canvas7.bind("<Button-1>", self.make_point)


        global count

        count = 2

        self.button13.config(state="disabled")
        self.button14.config(state="disabled")
        self.button15.config(state="disabled")
    
    def make_point(self, e):
            
        self.verts += [[e.x, e.y]]
        size = 3
        self.vert_ids.append(self.canvas7.create_oval(e.x-size,e.y-size,e.x+size,e.y+size,fill="blue"))
        print(self.vert_ids)
        print(self.verts)
        self.make_shape(color)

    def make_shape(self, color):
        if len(self.vert_ids) == 3:
            s = self.function_generator.tri(self.verts.copy(), color,self.canvas7)
            self.canvas7.unbind("<Button-1>")
            self.vert_ids.clear()
            self.verts.clear()
    
    #Rectangle Function

    def rectangle(self):
        print("Rectangle")

        #Popup Message

        self.infowin = Toplevel()
        self.infowin.title("Info")
        w = 260
        h = 100
        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen
        x = (ws/2.5) - (w/2.5)
        y = (hs/2.5) - (h/2.5)
        Message(self.infowin, text ="Click and drag on the Drawing area to make Rectangle",
                padx = 20,pady = 20).pack()
        self.infowin.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.infowin.resizable(width=False, height=False)
        self.infowin.after(3000,self.infowin.destroy)

        self.colorwin = Toplevel()
        self.colorwin.title("Choose Color")
        w = 260
        h = 100
        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen
        x = (ws/2.5) - (w/2.5)
        y = (hs/2.5) - (h/2.5)
        self.colorwin.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.colorwin.resizable(width=False, height=False)
        BlueButton = Button(self.colorwin,text="Blue",bg="Blue",fg="white",width=5,command=self.blue)
        BlueButton.place(x=20,y=40)
        RedButton = Button(self.colorwin,text="Red",bg="Red",fg="white",width=5,command=self.red)
        RedButton.place(x=100,y=40)
        BlackButton = Button(self.colorwin,text="Black",bg="Black",fg="white",width=5,command=self.black)
        BlackButton.place(x=180,y=40)

        global count

        count = 3

        self.x = self.y = 0

        self.canvas7.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas7.bind("<B1-Motion>", self.on_move_press)
        self.canvas7.bind("<ButtonRelease-1>", self.on_button_release)

        self.rect = None

        self.start_x = None
        self.start_y = None

        self.button13.config(state="disabled")
        self.button14.config(state="disabled")
        self.button15.config(state="disabled")

    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = self.canvas7.canvasx(event.x)
        self.start_y = self.canvas7.canvasy(event.y)

        # create rectangle if not yet exist
        if not self.rect:
            self.rect = self.canvas7.create_rectangle(self.x, self.y, 1, 1,fill=color)

    def on_move_press(self, event):
        curX = self.canvas7.canvasx(event.x)
        curY = self.canvas7.canvasy(event.y)

        w, h = self.canvas7.winfo_width(), self.canvas7.winfo_height()

        # expand rectangle as you drag the mouse
        self.canvas7.coords(self.rect, self.start_x, self.start_y, curX, curY)

    def on_button_release(self, event):
        pass

    #Color Selection Functions

    def blue(self):
        print("Blue")
        global color
        color = "blue"
        self.colorwin.withdraw()
    def red(self):
        global color
        color = "red"
        self.colorwin.withdraw()
    def black(self):
        global color
        color = "black"
        self.colorwin.withdraw()

    def geometricshapeprediction(self):
        print("Predict Button in Testing Window")

class Shapes:

    '''This is the Class for Triangle Function'''
    
    def tri(self, points, color,canvas):
        
        self.points = points
        self.color = color
        self.canvas7 = canvas
        self.id = self.canvas7.create_polygon(points, fill=color)
        
if __name__ == "__main__":
    root = Tk()
    myApp = Geometric_Shapes(root)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(width=False, height=False)
    root.mainloop()
