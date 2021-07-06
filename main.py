import pandas as pd
from tkinter import *
from tkinter import filedialog


def openpad():
    pad = filedialog.askopenfile(title="Select file!")
    return pad


def seperator():
    sep = seperator.get()
    print(sep)


def savefile():
    locatie = filedialog.askdirectory(title="Save File!")
    toon_locatie = Label(assolister, text="Your file can be found here: " + locatie, bg="#59bfff")
    toon_locatie.grid(column=0, row=3, columnspan=4)
    return locatie


def start():

    df = pd.read_csv(openpad())

    a = df.values.tolist()
    print(a)

    b = str(a)

    c = b.replace("[['", "")
    d = c.replace("']]", "")
    e = d.replace("'],", seperator.get())
    f = e.replace(" ['", seperator.get())
    g = f.split(seperator.get())

    h = []
    for x in g:
        if x != "":
            h.append(x)

    df = pd.DataFrame(h, columns=["Associatie"])
    da = df.drop_duplicates(subset="Associatie", keep='first')
    print(da)

    da.to_excel(savefile()+r"\Associaties.xlsx")


assolister = Tk()
assolister.title("assolister")
assolister.iconbitmap(r"C:\Users\Verkesfl\Documents\Documenten\ICON\icon.ico")
assolister.configure(bg="#59bfff")
assolister.geometry("300x200")

buttonstart = Button(assolister, text="Get the associations!", padx=50, pady=10, borderwidth=10, bg="#fe37af",
                     command=start)
buttonstart.grid(row=2, column=0, columnspan=4)

buttonseperator = Button(assolister, text="Ok!", padx=50, pady=10, borderwidth=10, bg="#fe37af", command=seperator)
buttonseperator.grid(row=1, column=3, columnspan=2)

seper = Label(assolister, text="Please provide occurence seperator and press OK!", bg="#59bfff",
              font='Helvetica 7 bold')
seper.grid(row=0, column=0, columnspan=4)

seperator = Entry(assolister, borderwidth=10, width=1)
seperator.grid(row=1, column=2)


assolister.mainloop()
