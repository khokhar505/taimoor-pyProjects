import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def hello ():  
    label1 = tk.Label(root, text= 'hello bhola record', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    
button1 = tk.Button(text='Click Me',command=hello, bg='blue',fg='orange')
canvas1.create_window(150, 150, window=button1)

root.mainloop()

