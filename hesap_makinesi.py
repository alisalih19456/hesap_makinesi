import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("hesap makinesi-ali salih")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_824=tk.Button(root)
        GButton_824["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_824["font"] = ft
        GButton_824["fg"] = "#000000"
        GButton_824["justify"] = "center"
        GButton_824["text"] = "Button"
        GButton_824.place(x=370,y=280,width=70,height=25)
        GButton_824["command"] = self.GButton_824_command

        GButton_313=tk.Button(root)
        GButton_313["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_313["font"] = ft
        GButton_313["fg"] = "#000000"
        GButton_313["justify"] = "center"
        GButton_313["text"] = "Button"
        GButton_313.place(x=160,y=280,width=70,height=25)
        GButton_313["command"] = self.GButton_313_command

        GButton_734=tk.Button(root)
        GButton_734["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_734["font"] = ft
        GButton_734["fg"] = "#000000"
        GButton_734["justify"] = "center"
        GButton_734["text"] = "Button"
        GButton_734.place(x=230,y=280,width=70,height=25)
        GButton_734["command"] = self.GButton_734_command

        GButton_310=tk.Button(root)
        GButton_310["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_310["font"] = ft
        GButton_310["fg"] = "#000000"
        GButton_310["justify"] = "center"
        GButton_310["text"] = "Button"
        GButton_310.place(x=300,y=280,width=70,height=25)
        GButton_310["command"] = self.GButton_310_command

        GLabel_410=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_410["font"] = ft
        GLabel_410["fg"] = "#333333"
        GLabel_410["justify"] = "center"
        GLabel_410["text"] = "rakam1"
        GLabel_410.place(x=130,y=130,width=70,height=25)

        GLabel_51=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_51["font"] = ft
        GLabel_51["fg"] = "#333333"
        GLabel_51["justify"] = "center"
        GLabel_51["text"] = "rakam2"
        GLabel_51.place(x=200,y=130,width=70,height=25)

        GLabel_338=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_338["font"] = ft
        GLabel_338["fg"] = "#333333"
        GLabel_338["justify"] = "center"
        GLabel_338["text"] = "rakam3"
        GLabel_338.place(x=270,y=130,width=70,height=25)

        GLineEdit_306=tk.Entry(root)
        GLineEdit_306["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_306["font"] = ft
        GLineEdit_306["fg"] = "#333333"
        GLineEdit_306["justify"] = "center"
        GLineEdit_306["text"] = "Entry"
        GLineEdit_306.place(x=130,y=180,width=70,height=25)

        GLineEdit_618=tk.Entry(root)
        GLineEdit_618["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_618["font"] = ft
        GLineEdit_618["fg"] = "#333333"
        GLineEdit_618["justify"] = "center"
        GLineEdit_618["text"] = "Entry"
        GLineEdit_618.place(x=200,y=180,width=70,height=25)

        GLineEdit_818=tk.Entry(root)
        GLineEdit_818["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_818["font"] = ft
        GLineEdit_818["fg"] = "#333333"
        GLineEdit_818["justify"] = "center"
        GLineEdit_818["text"] = "Entry"
        GLineEdit_818.place(x=270,y=180,width=70,height=25)

    def GButton_824_command(self):
        print("buton 4'e basıldi")


    def GButton_313_command(self):
        print("buton 1'e basıldi")


    def GButton_734_command(self):
        print("buton 2'e basıldi")


    def GButton_310_command(self):
        print("buton 3'e basıldi")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
# Buraya ekleme oldu
textBoxYazilanlar1 = tk.StringVar()
textBoxYazilanlar2 = tk.StringVar()
textBoxYazilanlar3 = tk.StringVar()