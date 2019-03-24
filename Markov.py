import tkinter
import tkFileDialog
import Mark2

text = "Three blind mice dodge dark fools. These fools let mice leave.  When all is done, darkness covers foolish mice."

def maketext():
    return


def generate():
    global show
    global save
    show1 = show.get()
    save1 = save.get()
    if not (show1 or save1):
        message ["text"] = "Please select an output method."
        return
    if save1:
        loc = location.get()
        if len(loc) == 0:
            message["text"] = "Please enter a valid location."
            return
        if len (loc) <5 :
            loc = loc+".txt"
        else:
            if loc[len(loc)-4:len(loc)] != '.txt':
                loc = loc+".txt"
    if Lb.size() == 0:
        message["text"] = "please add source files."
        return
    text = ""
    for f in Lb.get(0, 'end'):
        text = text+"\n"+load(f)
        print(text)
    markov = Mark2.markov(text, int( length.get()), int(order.get())+1)
    if show1:
        message["text"] = markov
    if save1:
        f = open(loc, 'w')
        f.write(markov)



def load(f):
    fi = open(f, "r")
    return(fi.read())


main=tkinter.Tk(className='Name Maker')
leftFrame = tkinter.Frame(main)
leftFrame.pack(side='left')
m = tkinter.Frame(leftFrame)
m.pack()
nameFrame = tkinter.Frame(leftFrame)
nameFrame.pack()

fileFrame = tkinter.Frame(main)
fileFrame.pack(side = 'right')

Lb = tkinter.Listbox(fileFrame, width = 60, height = 20)
Lb.pack() 

add = tkinter.Button(fileFrame, text = "Add", command = lambda Lb = Lb: Lb.insert('end', tkFileDialog.askopenfilename(title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))))
add.pack(side = 'left')

rem = tkinter.Button(fileFrame, text = "Remove", command = lambda Lb = Lb: Lb.delete('anchor'))
rem.pack()

show = tkinter.IntVar()
save = tkinter.IntVar()
tkinter.Checkbutton(m, text='Display in Window', variable = show).grid(column = 0, row = 1, sticky = 'w')
tkinter.Checkbutton(m, text='Save as File:', variable = save).grid(row = 2, column = 0, sticky = 'w')
location = tkinter.Entry(m)
location.grid(row = 2, column = 1)

orderlabel = tkinter.Label(m, text='Order')
orderlabel.grid(row=4, column = 0)
 
order = tkinter.Entry(m)
order.grid(row = 4, column = 1)

lengthlabel = tkinter.Label(m, text='Length')
lengthlabel.grid(row=3, column = 0)

length = tkinter.Entry(m)
length.grid(row =3, column = 1)

run = tkinter.Button(nameFrame, command = generate, text='Run')
run.pack()


message = tkinter.Message(nameFrame, bg = 'white')
message.pack()



m.mainloop()
