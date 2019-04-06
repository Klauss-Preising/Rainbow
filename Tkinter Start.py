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
        self.colors = ["red", "orange red", "orange", "yellow",
                       "green yellow", "lawn green", "green", "spring green",
                       "light sea green", "dodger blue", "blue", "SlateBlue1",
                       "purple", "medium orchid", "violet red", "red"]

        # Starting
        self.settings()
        self.frames()
        self.asking()

        self.canvas = tk.Canvas(self.square_frame, width=640, height=640)
        self.canvas.pack()
        self.squares()
        # Main loop
        self.add_main_loop()

    def add_main_loop(self):
        self.master.mainloop()

    def settings(self):
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()

        x = (ws // 2) - (800 // 2)
        y = (hs // 2) - (800 // 2)
        self.master.geometry("1000x800+" + str(x) + "+" + str(y))
        self.master.resizable(0, 0)
        self.master.config(bg="#afafaf")

    def frames(self):
        self.square_frame = tk.Frame(self.master, width=640, height=640, bg="white")
        self.square_frame.pack(padx=50, pady=30)

        self.bot_frame = tk.Frame(self.master, width=1200, height=100, bg="#afafaf")
        self.bot_frame.pack()

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
    def submit_action(self):
        try:
            self.canvas.delete(tk.ALL)
            self.value = int(self.key.get().strip(), base=16)
            self.title.config(text=hex(self.value))
            self.squares()
            self.clear_action()
        except Exception:
            self.value = self.default_value
            self.title.config(text=hex(self.value))
            self.squares()
            self.clear_action()

    def clear_action(self):
        self.key.delete(0, tk.END)

    def random_action(self):
        self.value = int(rd.randint(0, self.BIGGEST+1))
        self.title.config(text=hex(self.value))
        self.squares()

    def squares(self):
        for i in range(0, 8):
            for j in range(0, 8):
                self.canvas.create_rectangle(i*80, j*80, i*80+80, j*80+80, fill=self.colors[self.value % 16])
                self.value //= 16


if __name__ == '__main__':
    root = Instance(tk.Tk())
