from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.canvas = Canvas(self, height=400, width=500)
        self.canvas.grid()
        self.canvas.create_line(100,100, 120, 80)


        self.canvas.bind("<Button-1>", self.begin)
        self.canvas.bind("<Button1-Motion>", self.draw)

        self.oldx, self.oldy = 0,0

    def begin(self, event):
        self.oldx, self.oldy = event.x, event.y

    def draw(self, event):
        newx, newy = event.x, event.y

        self.canvas.create_line(self.oldx, self.oldy, newx, newy)

        self.oldx, self.oldy = newx, newy

# main
root = Tk()
root.title("Draw With Your Mouse!")
root.geometry("500x400")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
