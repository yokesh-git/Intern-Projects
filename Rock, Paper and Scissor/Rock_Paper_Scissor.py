from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
import tkinter.messagebox
import sys
from random import randint
import tkinter.messagebox

class Rock_Paper_Scissor:
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
        master.title("HEU Technologies - Rock Paper and Scissor")

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

        self.i = self.canvas1.create_text(250, 35, fill="white", font=("Times New Roman 20 italic bold", 32),
                                           text="Rock, Paper and Scissor")

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
    Learn how to build your own Rock, Paper, Scissor
    game by creating the knowledge base and traning
    the model.

    Understand the steps involved in AI Project
        * Create your own Knowledge-base
        * Play with the computer
        * Change data in Knowledge-base and confuse
          the computer"""

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

        self.canvas4 = Canvas(self.ThirdWin,bg="#8DC1E8", width=900, height=500)
        self.canvas4.place(x=50,y=75)

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

        self.canvas5 = Canvas(self.ThirdWin,bg="#8DC1E8", width=900, height=500)
        self.canvas5.place(x=50,y=75)

        self.i = self.canvas5.create_text(275, 90, fill="white", font=("Times 20"),
                                           text=" Knowledge-base ")
        self.r = self.canvas5.create_rectangle(self.canvas5.bbox(self.i),fill="#2C56BC",outline="#2C56BC")
        self.canvas5.tag_lower(self.r, self.i)

        self.photo = ImageTk.PhotoImage(Image.open("Images/gear-icon.png"))
        self.knowledgebase = Button(self.canvas5, height=210, width=200, compound="top",
                              font=('Times New Roman', 18), foreground='white', image=self.photo, command=self.knowledgebase)
        self.knowledgebase.place(x=175, y=150)

        self.i = self.canvas5.create_text(625, 90, fill="white", font=("Times 20"),
                                           text=" Play with AI ")
        self.r = self.canvas5.create_rectangle(self.canvas5.bbox(self.i),fill="#2C56BC",outline="#2C56BC")
        self.canvas5.tag_lower(self.r, self.i)

        self.photo1 = ImageTk.PhotoImage(Image.open("Images/base_image.png"))
        self.playwithai = Button(self.canvas5, height=210, width=200, compound="top", bg="white",
                              font=('Times New Roman', 18), foreground='white', image=self.photo1, command=self.playwithai)
        self.playwithai.place(x=525, y=150)

        self.button7 = Button(self.ThirdWin, foreground="white", text="BACK", command=self.back, anchor=CENTER)
        self.button7.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button7_window = self.canvas3.create_window(450, 600, anchor=NW, window=self.button7)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button7['font'] = font1
        self.button7.config(width=10, height=1)

        self.ThirdWin.withdraw()

        self.knowledgebasewin = Toplevel()

        self.knowledgebasewin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas4 = Canvas(self.knowledgebasewin, width=1000, height=650)
        self.canvas4.pack()

        self.image4 = ImageTk.PhotoImage(Image.open("Images/bg.png"))
        self.canvas4.create_image(0, 0, anchor=NW, image=self.image4)

        self.button8 = Button(self.knowledgebasewin, foreground="white", text="HOME", command=self.knowledgebasewinhome,
                              anchor=CENTER)
        self.button8.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button8_window = self.canvas4.create_window(60, 20, anchor=NW, window=self.button8)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button8['font'] = font1
        self.button8.config(width=10, height=1)

        self.button9 = Button(self.knowledgebasewin, foreground="white", text="EXIT", command=self.exit, anchor=CENTER)
        self.button9.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button9_window = self.canvas4.create_window(800, 20, anchor=NW, window=self.button9)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button9['font'] = font1
        self.button9.config(width=10, height=1)

        self.canvas6 = Canvas(self.knowledgebasewin,bg="#8DC1E8", width=900, height=500)
        self.canvas6.place(x=50,y=75)

        self.i = self.canvas6.create_text(450, 40, fill="white", font=("Times 20"),
                                           text=" Knowledge-base ")
        self.r = self.canvas6.create_rectangle(self.canvas6.bbox(self.i),fill="#2C56BC",outline="#2C56BC")
        self.canvas6.tag_lower(self.r, self.i)

        self.i = self.canvas6.create_text(750, 40, fill="black", font=("Times 15"),
                                           text=" 1 - YOU WIN \t\t\n 0 - YOU LOSS \t\t\n -1 - TIE \t\t")
        self.r = self.canvas6.create_rectangle(self.canvas6.bbox(self.i),fill="white",outline="white")
        self.canvas6.tag_lower(self.r, self.i)

        self.i = self.canvas6.create_text(120, 110, fill="white", font=("Times 20"),
                                           text=" Combinations with \n%s Rock"%(' '*11))
        self.r = self.canvas6.create_rectangle(self.canvas6.bbox(self.i),fill="#2C56BC",outline="#2C56BC")
        self.canvas6.tag_lower(self.r, self.i)

        self.i = self.canvas6.create_text(450, 110, fill="white", font=("Times 20"),
                                           text=" Combinations with \n%s Paper"%(' '*11))
        self.r = self.canvas6.create_rectangle(self.canvas6.bbox(self.i),fill="#2C56BC",outline="#2C56BC")
        self.canvas6.tag_lower(self.r, self.i)

        self.i = self.canvas6.create_text(780, 110, fill="white", font=("Times 20"),
                                           text=" Combinations with \n%s Scissor"%(' '*11))
        self.r = self.canvas6.create_rectangle(self.canvas6.bbox(self.i),fill="#2C56BC",outline="#2C56BC")
        self.canvas6.tag_lower(self.r, self.i)

        #Coimbinations with Rock

        self.canvas7 = Canvas(self.canvas6,bg="white", width=210, height=310)
        self.canvas7.place(x=15,y=150)

        self.i = self.canvas7.create_text(30, 15, fill="white", font=("Times 16"),
                                           text="   AI   ")
        self.r = self.canvas7.create_rectangle(self.canvas7.bbox(self.i),fill="black",outline="black")
        self.canvas7.tag_lower(self.r, self.i)

        self.i = self.canvas7.create_text(102, 15, fill="white", font=("Times 16"),
                                           text="   YOU   ")
        self.r = self.canvas7.create_rectangle(self.canvas7.bbox(self.i),fill="black",outline="black")
        self.canvas7.tag_lower(self.r, self.i)

        self.i = self.canvas7.create_text(180, 15, fill="white", font=("Times 16"),
                                           text="   1/0   ")
        self.r = self.canvas7.create_rectangle(self.canvas7.bbox(self.i),fill="black",outline="black")
        self.canvas7.tag_lower(self.r, self.i)

        self.image5 = ImageTk.PhotoImage(Image.open("Images/Rock.png"))
        self.canvas7.create_image(5, 80, anchor=NW, image=self.image5)

        self.image8 = ImageTk.PhotoImage(Image.open("Images/scissor.png"))
        self.canvas7.create_image(80, 80, anchor=NW, image=self.image8)


        self.entry1 = Entry(self.canvas7,bg ="#8DC1E8",width=6)
        self.entry1.place(x=160,y=95)
        
        
        self.image6 = ImageTk.PhotoImage(Image.open("Images/Rock.png"))
        self.canvas7.create_image(5, 160, anchor=NW, image=self.image6)

        self.image9 = ImageTk.PhotoImage(Image.open("Images/paper.png"))
        self.canvas7.create_image(80, 160, anchor=NW, image=self.image9)

        self.entry2 = Entry(self.canvas7,bg ="#8DC1E8",width=6)
        self.entry2.place(x=160,y=175)
        
        self.image7 = ImageTk.PhotoImage(Image.open("Images/Rock.png"))
        self.canvas7.create_image(5, 240, anchor=NW, image=self.image7)

        self.image10 = ImageTk.PhotoImage(Image.open("Images/Rock.png"))
        self.canvas7.create_image(80, 240, anchor=NW, image=self.image10)

        self.entry3 = Entry(self.canvas7,bg ="#8DC1E8",width=6)
        self.entry3.place(x=160,y=255)
        

        #Coimbinations with Paper

        self.canvas8 = Canvas(self.canvas6,bg="white", width=210, height=310)
        self.canvas8.place(x=345,y=150)

        self.i = self.canvas8.create_text(30, 15, fill="white", font=("Times 16"),
                                           text="   AI   ")
        self.r = self.canvas8.create_rectangle(self.canvas8.bbox(self.i),fill="black",outline="black")
        self.canvas8.tag_lower(self.r, self.i)

        self.i = self.canvas8.create_text(102, 15, fill="white", font=("Times 16"),
                                           text="   YOU   ")
        self.r = self.canvas8.create_rectangle(self.canvas8.bbox(self.i),fill="black",outline="black")
        self.canvas8.tag_lower(self.r, self.i)

        self.i = self.canvas8.create_text(180, 15, fill="white", font=("Times 16"),
                                           text="   1/0   ")
        self.r = self.canvas8.create_rectangle(self.canvas8.bbox(self.i),fill="black",outline="black")
        self.canvas8.tag_lower(self.r, self.i)

        self.image11 = ImageTk.PhotoImage(Image.open("Images/paper.png"))
        self.canvas8.create_image(5, 80, anchor=NW, image=self.image11)

        self.image14 = ImageTk.PhotoImage(Image.open("Images/scissor.png"))
        self.canvas8.create_image(80, 80, anchor=NW, image=self.image14)

        self.entry4 = Entry(self.canvas8,bg ="#8DC1E8",width=6)
        self.entry4.place(x=160,y=95)
        

        self.image12 = ImageTk.PhotoImage(Image.open("Images/paper.png"))
        self.canvas8.create_image(5, 160, anchor=NW, image=self.image12)

        self.image15 = ImageTk.PhotoImage(Image.open("Images/paper.png"))
        self.canvas8.create_image(80, 160, anchor=NW, image=self.image15)

        self.entry5 = Entry(self.canvas8,bg ="#8DC1E8",width=6)
        self.entry5.place(x=160,y=175)
        

        self.image13 = ImageTk.PhotoImage(Image.open("Images/paper.png"))
        self.canvas8.create_image(5, 240, anchor=NW, image=self.image13)

        self.image16 = ImageTk.PhotoImage(Image.open("Images/Rock.png"))
        self.canvas8.create_image(80, 240, anchor=NW, image=self.image16)

        self.entry6 = Entry(self.canvas8,bg ="#8DC1E8",width=6)
        self.entry6.place(x=160,y=255)
        

        #Coimbinations with Scissor

        self.canvas9 = Canvas(self.canvas6,bg="white", width=210, height=310)
        self.canvas9.place(x=675,y=150)

        self.i = self.canvas9.create_text(30, 15, fill="white", font=("Times 16"),
                                           text="   AI   ")
        self.r = self.canvas9.create_rectangle(self.canvas9.bbox(self.i),fill="black",outline="black")
        self.canvas9.tag_lower(self.r, self.i)

        self.i = self.canvas9.create_text(102, 15, fill="white", font=("Times 16"),
                                           text="   YOU   ")
        self.r = self.canvas9.create_rectangle(self.canvas9.bbox(self.i),fill="black",outline="black")
        self.canvas9.tag_lower(self.r, self.i)

        self.i = self.canvas9.create_text(180, 15, fill="white", font=("Times 16"),
                                           text="   1/0   ")
        self.r = self.canvas9.create_rectangle(self.canvas9.bbox(self.i),fill="black",outline="black")
        self.canvas9.tag_lower(self.r, self.i)

        self.image17 = ImageTk.PhotoImage(Image.open("Images/scissor.png"))
        self.canvas9.create_image(5, 80, anchor=NW, image=self.image17)

        self.image20 = ImageTk.PhotoImage(Image.open("Images/scissor.png"))
        self.canvas9.create_image(80, 80, anchor=NW, image=self.image20)

        self.entry7 = Entry(self.canvas9,bg ="#8DC1E8",width=6)
        self.entry7.place(x=160,y=95)
        

        self.image18 = ImageTk.PhotoImage(Image.open("Images/scissor.png"))
        self.canvas9.create_image(5, 160, anchor=NW, image=self.image18)

        self.image21 = ImageTk.PhotoImage(Image.open("Images/paper.png"))
        self.canvas9.create_image(80, 160, anchor=NW, image=self.image21)

        self.entry8 = Entry(self.canvas9,bg ="#8DC1E8",width=6)
        self.entry8.place(x=160,y=175)
        

        self.image19 = ImageTk.PhotoImage(Image.open("Images/scissor.png"))
        self.canvas9.create_image(5, 240, anchor=NW, image=self.image19)

        self.image22 = ImageTk.PhotoImage(Image.open("Images/Rock.png"))
        self.canvas9.create_image(80, 240, anchor=NW, image=self.image22)

        self.entry9 = Entry(self.canvas9,bg ="#8DC1E8",width=6)
        self.entry9.place(x=160,y=255)
        

        self.button10 = Button(self.knowledgebasewin, foreground="white", text="BACK", command=self.knowledgebasewinback,
                               anchor=CENTER)
        self.button10.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button10_window = self.canvas4.create_window(450, 600, anchor=NW, window=self.button10)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button10['font'] = font1
        self.button10.config(width=10, height=1)

        self.setbutton = Button(self.knowledgebasewin, foreground="white", text="Set", command=self.set,
                               anchor=CENTER)
        self.setbutton.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.setbutton_window = self.canvas6.create_window(410, 470, anchor=NW, window=self.setbutton)
        font1 = font.Font(family='Times New Roman', size=10, weight='normal')
        self.setbutton['font'] = font1
        self.setbutton.config(width=10, height=1)

        self.knowledgebasewin.withdraw()

        self.playwithaiwin = Toplevel()

        self.playwithaiwin.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.canvas10 = Canvas(self.playwithaiwin, width=1000, height=650)
        self.canvas10.pack()

        self.image23 = ImageTk.PhotoImage(Image.open("Images/bg.png"))
        self.canvas10.create_image(0, 0, anchor=NW, image=self.image23)

        self.button11 = Button(self.playwithaiwin, foreground="white", text="HOME", command=self.playwithaiwinhome,
                              anchor=CENTER)
        self.button11.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button11_window = self.canvas10.create_window(60, 20, anchor=NW, window=self.button11)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button11['font'] = font1
        self.button11.config(width=10, height=1)

        self.button12 = Button(self.playwithaiwin, foreground="white", text="EXIT", command=self.exit, anchor=CENTER)
        self.button12.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button12_window = self.canvas10.create_window(800, 20, anchor=NW, window=self.button12)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button12['font'] = font1
        self.button12.config(width=10, height=1)

        self.i = self.canvas10.create_text(500, 50, fill="black", font=("Times 16 bold"),
                                           text=" PLAY AGAINST AI ")
        self.r = self.canvas10.create_rectangle(self.canvas10.bbox(self.i),fill="#8DC1E8",outline="#8DC1E8")
        self.canvas10.tag_lower(self.r, self.i)

        self.canvas11 = Canvas(self.playwithaiwin,bg="#8DC1E8", width=900, height=500)
        self.canvas11.place(x=50,y=75)

        self.canvas12 = Canvas(self.playwithaiwin,bg="white", width=300, height=300)
        self.canvas12.place(x=150,y=150)

        self.i = self.canvas12.create_text(150, 20, fill="black", font=("Times 16 bold"),
                                           text="%sAI%s"%(' '*15,' '*15))
        self.r = self.canvas12.create_rectangle(self.canvas12.bbox(self.i),fill="#8DC1E8",outline="#8DC1E8")
        self.canvas12.tag_lower(self.r, self.i)

        self.canvas13 = Canvas(self.playwithaiwin,bg="white", width=300, height=300)
        self.canvas13.place(x=550,y=150)

        self.i = self.canvas13.create_text(150, 20, fill="black", font=("Times 16 bold"),
                                           text="%sYOU%s"%(' '*15,' '*15))
        self.r = self.canvas13.create_rectangle(self.canvas13.bbox(self.i),fill="#8DC1E8",outline="#8DC1E8")
        self.canvas13.tag_lower(self.r, self.i)

        self.button13 = Button(self.playwithaiwin, foreground="black", text="CLICK TO PLAY", command=self.clicktoplay,
                               anchor=CENTER)
        self.button13.configure(width=10, activebackground="#33B5E5", bg='white', relief=FLAT)
        self.button13_window = self.canvas11.create_window(350, 400, anchor=NW, window=self.button13)
        font1 = font.Font(family='Times New Roman Bold', size=16, weight='normal')
        self.button13['font'] = font1
        self.button13.config(width=15, height=1)

        self.button14 = Button(self.playwithaiwin, foreground="white", text="BACK", command=self.playwithaiwinback,
                               anchor=CENTER)
        self.button14.configure(width=10, activebackground="#33B5E5", bg='#2C56BC', relief=FLAT)
        self.button14_window = self.canvas10.create_window(450, 600, anchor=NW, window=self.button14)
        font1 = font.Font(family='Times New Roman', size=16, weight='normal')
        self.button14['font'] = font1
        self.button14.config(width=10, height=1)

        global panel

        self.image24 = ImageTk.PhotoImage(Image.open("Images/rock-paper-scissors.png"))
        #self.canvas12.create_image(15, 70, anchor=NW,image=self.image24)
        panel = Label(self.canvas12, image=self.image24)
        panel.place(x=10,y=50)

        
        self.photo2 = ImageTk.PhotoImage(Image.open("Images/paper.png"))
        self.paper = Button(self.canvas13, height=60, width=60, compound="top",bg = "white",
                            foreground='white', image=self.photo2, command=self.paper)
        self.paper.configure(relief=FLAT)
        self.paper.place(x=40, y=60)

        self.photo3 = ImageTk.PhotoImage(Image.open("Images/scissor.png"))
        self.scissor = Button(self.canvas13, height=60, width=60, compound="top",bg = "white",
                            foreground='white', image=self.photo3, command=self.scissor)
        self.scissor.configure(relief=FLAT)
        self.scissor.place(x=200, y=60)

        self.photo4 = ImageTk.PhotoImage(Image.open("Images/Rock.png"))
        self.rock = Button(self.canvas13, height=60, width=60, compound="top",bg = "white",
                            foreground='white', image=self.photo4, command=self.rock)
        self.rock.configure(relief=FLAT)
        self.rock.place(x=120, y=180)

        self.playwithaiwin.withdraw()

        

    def clicktostart(self):
        def onclick():
            root.quit()
            self.secondWin.withdraw()

        self.secondWin.protocol("WM_DELETE_WINDOW", onclick)
        self.secondWin.resizable(width=False, height=False)
        self.master.withdraw()
        self.secondWin.deiconify()

    def clickforhelp(self):
        '''It shows message box what exactly the application does.'''
        tkinter.messagebox.showinfo("Info", "Welcome to Rock, Paper and Scissor!\nYou can set rules of the game as \
per you need.\nPress Button 'Click to Begin' to start")

    def home(self):
        self.secondWin.withdraw()
        self.master.deiconify()
    def back(self):
        self.ThirdWin.withdraw()
        self.secondWin.deiconify()
    def knowledgebasewinback(self):
        self.knowledgebasewin.withdraw()
        self.ThirdWin.deiconify()
    def playwithaiwinback(self):
        self.playwithaiwin.withdraw()
        self.ThirdWin.deiconify()
    def exit(self):
        self.ThirdWin.withdraw()
        self.knowledgebasewin.withdraw()
        self.playwithaiwin.withdraw()
        sys.exit(myApp)
    def clicktobegin(self):
        def onclick():
            root.quit()
            self.ThirdWin.withdraw()
        self.ThirdWin.protocol("WM_DELETE_WINDOW", onclick)
        self.ThirdWin.resizable(width=False, height=False)
        self.secondWin.withdraw()
        self.ThirdWin.deiconify()

    def thirdwinhome(self):
        def onclick():
            root.quit()
            self.master.withdraw()
        self.master.protocol("WM_DELETE_WINDOW", onclick)
        self.ThirdWin.withdraw()
        self.master.deiconify()
    def knowledgebasewinhome(self):
        def onclick():
            root.quit()
            self.master.withdraw()
        self.master.protocol("WM_DELETE_WINDOW", onclick)
        self.knowledgebasewin.withdraw()
        self.master.deiconify()

    def playwithaiwinhome(self):
        def onclick():
            root.quit()
            self.master.withdraw()
        self.master.protocol("WM_DELETE_WINDOW", onclick)
        self.playwithaiwin.withdraw()
        self.master.deiconify()
        
    def knowledgebase(self):
        print("Done")
        def onclick():
            root.quit()
            self.knowledgebasewin.withdraw()
        self.knowledgebasewin.protocol("WM_DELETE_WINDOW", onclick)

        self.helpwin = Toplevel()
        self.helpwin.title("Rules")
        w = 260
        h = 100
        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen
        x = (ws/2.5) - (w/2.5)
        y = (hs/2.5) - (h/2.5)
        self.helpwin.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.helpwin.resizable(width=False, height=False)
        Message(self.helpwin, text = "Rules:\n1) You have to fix the value before going to play\n2) The values must be 0,1 or -1\n3) Based on the entered value the results will display",
                padx = 20,pady = 20).pack()
        self.helpwin.after(5000,self.helpwin.destroy)
        self.knowledgebasewin.resizable(width=False, height=False)
        self.ThirdWin.withdraw()
        self.knowledgebasewin.deiconify()
        
    def playwithai(self):
        print("Done!")
        def onclick():
            root.quit()
            self.playwithaiwin.withdraw()
        self.playwithaiwin.protocol("WM_DELETE_WINDOW", onclick)
        self.playwithaiwin.resizable(width=False, height=False)
        self.paper.config(state="disabled")
        self.scissor.config(state="disabled")
        self.rock.config(state="disabled")
        self.ThirdWin.withdraw()
        self.playwithaiwin.deiconify()
        
    def clicktoplay(self):
        print("Done!!")

        self.default = ImageTk.PhotoImage(Image.open('Images/rock-paper-scissors.png'))
        panel.configure(image = self.default)
        panel.image = self.default
        panel.place(x=10,y=50)
        
        global val1,val2,val3,val4,val4,val5,val6,val7,val8,val9,count
        count = 0
        try:
            val1 = int(self.entry1.get())
            val2 = int(self.entry2.get())
            val3 = int(self.entry3.get())
            val4 = int(self.entry4.get())
            val5 = int(self.entry5.get())
            val6 = int(self.entry6.get())
            val7 = int(self.entry7.get())
            val8 = int(self.entry8.get())
            val9 = int(self.entry9.get())
            count = 0
            
        except ValueError:
            tkinter.messagebox.showinfo("Error","Please Enter Values in Knowledge-base section.")
            self.playwithaiwin.withdraw()
            self.knowledgebasewin.deiconify()
            count += 1
            
        self.paper.config(state="normal")
        self.scissor.config(state="normal")
        self.rock.config(state="normal")
        if count == 0:
            self.msgwin = Toplevel()
            self.msgwin.title("Info")
            w = 260
            h = 100
            ws = root.winfo_screenwidth() # width of the screen
            hs = root.winfo_screenheight() # height of the screen
            x = (ws/2.5) - (w/2.5)
            y = (hs/2.5) - (h/2.5)
            self.msgwin.geometry('%dx%d+%d+%d' % (w, h, x, y))
            self.msgwin.resizable(width=False, height=False)
            '''Message(self.msgwin, text = "AI chosen one! It your turn!!\nAfter 3 seconds you are allowed to pick your choice",
                    padx = 20,pady = 20).pack()'''
            self.label = Label(self.msgwin,text = "",width = 10)
            self.label.config(font=("Courier", 44))
            self.label.pack()
            global remaining
            self.remaining = 0
            self.countdown(3)
            #self.msgwin.after(3000,self.msgwin.destroy)

            
        #self.msgwin.withdraw()
        global ai,user,ai_choice
        ai = randint(1,3)
        if ai == 1:
            ai_choice = "Paper"
        elif ai == 2:
            ai_choice = "Sciccor"
        else:
            ai_choice = "Rock"
        paper = 0
        scissor = 0
        rock = 0
        self.button13.config(state="disabled")

    def countdown(self,remaining = None):
            if remaining is not None:
                self.remaining = remaining
            if self.remaining <= 0:
                self.msgwin.destroy()
            else:
                self.label.configure(text="%d" %self.remaining)
                self.remaining = self.remaining - 1
                self.msgwin.after(1000,self.countdown)
    def set(self):
        
        def onclick():
            root.quit()
            self.playwithaiwin.withdraw()
        self.playwithaiwin.protocol("WM_DELETE_WINDOW", onclick)
        try:
            val1 = int(self.entry1.get())
            val2 = int(self.entry2.get())
            val3 = int(self.entry3.get())
            val4 = int(self.entry4.get())
            val5 = int(self.entry5.get())
            val6 = int(self.entry6.get())
            val7 = int(self.entry7.get())
            val8 = int(self.entry8.get())
            val9 = int(self.entry9.get())
            self.button13.config(state="normal")
            list = [val1,val2,val3,val4,val5,val6,val7,val8,val9]
            print(list)
            for i in range(len(list)):
                if list[i]>1 or list[i]<-1:
                    raise AttributeError
        except ValueError:
            tkinter.messagebox.showinfo("Error","Please Enter Only 1 , 0 0r -1 and don't leave as empty")
        except AttributeError:
            tkinter.messagebox.showinfo("Error","Please Enter Only 1 , 0 0r -1 and don't leave as empty")
        self.knowledgebasewin.withdraw()
        self.playwithaiwin.deiconify()
        self.paper.config(state="disabled")
        self.scissor.config(state="disabled")
        self.rock.config(state="disabled")
    def paper(self):
        print("Paper")
        user = 1
        self.paper.config(state="disabled")
        self.scissor.config(state="disabled")
        self.rock.config(state="disabled")
        self.game(user)
        self.button13.config(state="normal")
    def scissor(self):
        print("Scissor")
        user = 2
        self.paper.config(state="disabled")
        self.scissor.config(state="disabled")
        self.rock.config(state="disabled")
        self.game(user)
        self.button13.config(state="normal")
    def rock(self):
        print("Rock")
        user = 3
        self.paper.config(state="disabled")
        self.scissor.config(state="disabled")
        self.rock.config(state="disabled")
        self.game(user)
        self.button13.config(state="normal")
    def game(self,user):

        global a,b
        a = "Result"
        b = "You Win" + "\nAI Picked" + " " + ai_choice
        c = "You Lose" + "\nAI Picked" + " " + ai_choice
        
        #Paper Column
        
        if ai is 1:

            self.img2 = ImageTk.PhotoImage(Image.open('Images/aipaper.png'))
            panel.configure(image = self.img2)
            panel.image = self.img2
            panel.place(x=75,y=100)

            if ai == 1 and user == 1:
                if val5 == 1:
                    tkinter.messagebox.showinfo(a,b)
                elif val5 == 0:
                    tkinter.messagebox.showinfo(a,c)
                else:
                    tkinter.messagebox.showinfo("Result","Tie")
            if ai == 1 and user == 2:
                if val4 == 1:
                    tkinter.messagebox.showinfo(a,b)
                elif val4 == 0:
                    tkinter.messagebox.showinfo(a,c)
                else:
                    tkinter.messagebox.showinfo("Result","Tie")
            if ai == 1 and user == 3:
                if val6 == 1:
                    tkinter.messagebox.showinfo(a,b)
                elif val6 == 0:
                    tkinter.messagebox.showinfo(a,c)
                else:
                    tkinter.messagebox.showinfo("Result","Tie")

        #Scissor Column

        if ai is 2:

            self.img3 = ImageTk.PhotoImage(Image.open('Images/aiscissor.png'))
            panel.configure(image = self.img3)
            panel.image = self.img3
            panel.place(x=75,y=100)

            if ai == 2 and user == 1:
                if val8 == 1:
                    tkinter.messagebox.showinfo(a,b)
                elif val8 == 0:
                    tkinter.messagebox.showinfo(a,c)
                else:
                    tkinter.messagebox.showinfo("Result","Tie")
            if ai == 2 and user == 2:
                if val7 == 1:
                    tkinter.messagebox.showinfo(a,b)
                elif val7 == 0:
                    tkinter.messagebox.showinfo(a,c)
                else:
                    tkinter.messagebox.showinfo("Result","Tie")
            if ai == 2 and user == 3:
                if val9 == 1:
                    tkinter.messagebox.showinfo(a,b)
                elif val9 == 0:
                    tkinter.messagebox.showinfo(a,c)
                else:
                    tkinter.messagebox.showinfo("Result","Tie")

        #Rock Column

        if ai is 3:

            self.img4 = ImageTk.PhotoImage(Image.open('Images/airock.png'))
            panel.configure(image = self.img4)
            panel.image = self.img4
            panel.place(x=75,y=100)

            if ai == 3 and user == 1:
                if val2 == 1:
                    tkinter.messagebox.showinfo(a,b)
                elif val2 == 0:
                    tkinter.messagebox.showinfo(a,c)
                else:
                    tkinter.messagebox.showinfo("Result","Tie")
            if ai == 3 and user == 2:
                if val1 == 1:
                    tkinter.messagebox.showinfo(a,b)
                elif val1 == 0:
                    tkinter.messagebox.showinfo(a,c)
                else:
                    tkinter.messagebox.showinfo("Result","Tie")
            if ai == 3 and user == 3:
                if val3 == 1:
                    tkinter.messagebox.showinfo(a,b)
                elif val3 == 0:
                    tkinter.messagebox.showinfo(a,c)
                else:
                    tkinter.messagebox.showinfo("Result","Tie")
            

if __name__ == "__main__":
    root = Tk()
    myApp = Rock_Paper_Scissor(root)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(width=False, height=False)
    root.mainloop()
