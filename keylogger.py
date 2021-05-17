from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.text = Text(root, width = 50, height = 12)
        self.text.grid()

        self.text.bind('<KeyPress>', self.record)

    def record(self, event):
        print('char = ' + event.keysym)

# main
root = Tk()
root.title("Keylogger")
root.geometry("400x200")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
