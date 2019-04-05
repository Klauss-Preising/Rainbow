import tkinter as tk


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
        self.value = 0

        # Starting
        self.settings()
        self.frames()
        self.asking()

        # Main loop
        self.add_main_loop()

    def add_main_loop(self):
        self.master.mainloop()

    def settings(self):
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()

        x = (ws // 2) - (1200 // 2)
        y = (hs // 2) - (800 // 2)
        self.master.geometry("1200x800+" + str(x) + "+" + str(y))
        self.master.config(bg="#afafaf")

    def frames(self):
        self.square_frame = tk.Frame(self.master, width=1000, height=600, bg="white")
        self.square_frame.pack(padx=50, pady=30)

        self.bot_frame = tk.Frame(self.master, width=1200, height=100, bg="#afafaf")
        self.bot_frame.pack()

    def asking(self):
        self.key = tk.Entry(self.bot_frame, width=60)
        self.key.grid(row=1, column=1, columnspan=10)
        self.keyLabel = tk.Label(self.bot_frame, text="Key", bg="#afafaf", justify=tk.RIGHT)
        self.keyLabel.grid(row=1, column=0)

        self.submit = tk.Button(self.bot_frame, text="Submit", command=self.submit, bg="grey")
        self.submit.grid(row=2, column=4, pady=10)

        self.clear = tk.Button(self.bot_frame, text="Clear", command=self.clear, bg="grey")
        self.clear.grid(row=2, column=5, pady=10)

    # actions

    def submit(self):
        self.value = self.key.get().strip()

        self.clear()

    def clear(self):
        self.key.delete(0, tk.END)
        self.value = 0

    def squares(self):
        pass


if __name__ == '__main__':
    root = Instance(tk.Tk())
