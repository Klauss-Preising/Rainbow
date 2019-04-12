import tkinter as tk
import random as rd


class Instance:
    def __init__(self, master):
        # Variables
        self.master = master
        self.square_frame = None
        self.bot_frame = None
        self.key = None
        self.keyLabel = None
        self.submit = None
        self.clear = None
        self.random_button = None
        self.title = ""
        self.BIGGEST = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        self.default_value = 0xfedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210

        self.value = self.default_value
        self.values = []

        self.colors = ['#FF0000', '#FF4900', '#FF9700', '#FFF700',
                       '#AEFF00', '#3EFF00', '#00FF32', '#00FF97',
                       '#00F7FF', '#00AEFF', '#0046FF', '#2A00FF',
                       '#8B00FF', '#CD00FF', '#FF00E4', '#FF0061']


        # Starting
        self.settings()
        self.frames()
        self.asking()

        self.canvas = tk.Canvas(self.square_frame, width=640, height=640)
        self.canvas.pack()
        self.squares()
        # Main loop
        self.add_main_loop()

    # settings

    # starts
    def add_main_loop(self):
        self.master.mainloop()

    # master setting
    def settings(self):
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()

        x = (ws // 2) - (1000 // 2)
        y = (hs // 2) - (800 // 2)
        self.master.geometry("1000x800+" + str(x) + "+" + str(y))
        self.master.resizable(0, 0)
        self.master.config(bg="#afafaf")

    # setting the frames
    def frames(self):
        self.square_frame = tk.Frame(self.master, width=640, height=640, bg="white")
        self.square_frame.pack(padx=50, pady=30)

        self.bot_frame = tk.Frame(self.master, width=1200, height=100, bg="#afafaf")
        self.bot_frame.pack()

    # sets all the labels, entry, and buttons
    def asking(self):

        self.title = tk.Label(self.bot_frame, text=hex(self.default_value), bg="#afafaf")
        self.title.grid(row=0, column=0,columnspan=11)

        self.key = tk.Entry(self.bot_frame, width=60)
        self.key.grid(row=1, column=1, columnspan=10)
        self.keyLabel = tk.Label(self.bot_frame, text="Key", bg="#afafaf", justify=tk.RIGHT)
        self.keyLabel.grid(row=1, column=0)

        self.submit = tk.Button(self.bot_frame, text="Submit", command=self.submit_action, bg="grey")
        self.submit.grid(row=2, column=4, pady=10)

        self.clear = tk.Button(self.bot_frame, text="Clear", command=self.clear_action, bg="grey")
        self.clear.grid(row=2, column=5, pady=10)

        self.random_button = tk.Button(self.bot_frame, text="Random", command=self.random_action, bg="grey")
        self.random_button.grid(row=2, column=6, pady=10)

    # actions

    # takes the value and tries to make a pattern out of it
    def submit_action(self):
        self.canvas.delete(tk.ALL)
        try:
            self.value = int(self.key.get().strip(), base=16)
            self.title.config(text=hex(self.value))
            self.squares()
            self.clear_action()
        except Exception:
            self.value = self.default_value
            self.title.config(text=hex(self.value))
            self.squares()
            self.clear_action()

    # deletes the text in the Entry
    def clear_action(self):
        self.key.delete(0, tk.END)

    # randomizes the pattern
    def random_action(self):
        self.canvas.delete(tk.ALL)
        self.value = int(rd.randint(0, self.BIGGEST+1))
        self.title.config(text=hex(self.value))
        self.squares()

    # sets all the squares
    def squares(self):
        temp = self.value
        self.values.append(self.value)
        for i in range(8):
            for j in range(8):
                self.canvas.create_rectangle(j*80, i*80, j*80+80, i*80+80, fill=self.colors[temp % 16])
                temp //= 16

    def __str__(self):
        return str([hex(i) for i in self.values])


if __name__ == '__main__':
    root = Instance(tk.Tk())
    print(root)
