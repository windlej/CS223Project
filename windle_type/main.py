import tkinter as tk
import time
import threading
import random

class TypeSpeedGUI: # using a class lets me organize better
    
    def __init__(self):
        self.root = tk.Tk() # initial setup
        self.root.title("Jeremiah's Typing Test")
        self.root.geometry("1200x800")
        
        self.texts = open("texts.txt", "r").read().split("\n")
        
        self.frame = tk.Frame(self.root)
        
        self.sample_label = tk.Label(self.frame, text=random.choice(self.texts), font=("Helvetica", 18))    # label for sentence
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
        
        self.input_entry = tk.Entry(self.frame, width=40, font=("Helvetica", 24))   # entry field for typing
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyRelease>", self.start)                           # makes sure that the timer wont start till after the first key is released
        
        self.speed_label = tk.Label(self.frame, text="Speed: \n0.0 CPS\n0.0 CPM\n0.0 WPS\n 0.0 WPM", font=("Helvetica", 18))    # displays the starting metrics
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)
        
        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset, bg="Red", font=("Helvetica", 24))   # reset button
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
        
        self.frame.pack(expand=True)    # lets the window scale
        
        self.counter = 0
        self.running = False
        
        self.root.mainloop()
        
    def start(self, event):
        if not self.running:
            if not event.keycode in [16, 17, 18]:   # wont start if shift, alt, crtl are pressed
                self.running = True
                t = threading.Thread(target=self.time_thread)   #threading helps
                t.start()
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")   # makes text red if wrong letter
        else:
            self.input_entry.config(fg="black") # makes text black if right letter 
        if self.input_entry.get() == self.sample_label.cget('text'):    # -1 excludes last character due to weird bug
            self.running = False
            self.input_entry.config(fg="green") # finished text is green
    
    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1 # the smaller the interval the more points of data
            cps = len(self.input_entry.get()) / self.counter 
            cpm = cps * 60
            wps = len(self.input_entry.get().split(" ")) / self.counter
            wpm = wps * 60
            self.speed_label.config(text=f"Speed: \n{cps:.2f} CPS\n{cpm:.2f} CPM\n {wps:.2f} WPS\n {wpm:.2f} WPM")
    
    def reset(self):    # self explanatory
        self.running = False
        self.counter = 0
        self.speed_label.config(text="Speed: \n0.0 CPS\n0.0 CPM\n0.0 WPS\n 0.0 WPM")    # resets data
        self.sample_label.config(text=random.choice(self.texts))
        self.input_entry.delete(0, tk.END)
    
TypeSpeedGUI()  # runs the class