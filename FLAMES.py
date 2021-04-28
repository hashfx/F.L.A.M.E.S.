from tkinter import *


def remove_match_char(list1, list2):
    for i in range(len(list1)):

        for j in range(len(list2)):

            # if common character is found then remove that character and return list of concatenated list with True Flag

            if list1[i] == list2[j]:
                c = list1[i]


                list1.remove(c)

                list2.remove(c)


                list3 = list1 + ["*"] + list2


                return [list3, True]


    list3 = list1 + ["*"] + list2

    return [list3, False]


# function for telling the relationship status

def tell_status():

    p1 = Player1_field.get()


    p1 = p1.lower()


    p1.replace(" ", "")


    p1_list = list(p1)


    p2 = Player2_field.get()

    p2 = p2.lower()

    p2.replace(" ", "")

    p2_list = list(p2)


    proceed = True


    while proceed:

        ret_list = remove_match_char(p1_list, p2_list)


        con_list = ret_list[0]


        proceed = ret_list[1]


        star_index = con_list.index("*")


        p1_list = con_list[: star_index]


        p2_list = con_list[star_index + 1:]


    count = len(p1_list) + len(p2_list)


    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]


    while len(result) > 1:


        split_index = (count % len(result) - 1)


        if split_index >= 0:

            # list slicing

            right = result[split_index + 1:]

            left = result[: split_index]

            # list concatenation

            result = right + left


        else:

            result = result[: len(result) - 1]

    Status_field.insert(10, result[0])



def clear_all():
    Player1_field.delete(0, END)

    Player2_field.delete(0, END)

    Status_field.delete(0, END)

    # set focus on the Player1_field entry box

    Player1_field.focus_set()


# Driver code

if __name__ == "__main__":
    # Create a GUI window

    root = Tk()


    root.geometry("500x250") # 350 X 125
    root.iconphoto(True, PhotoImage(file="icon.png"))
    root.resizable(0,0)

    # background image
    root.config(bg="red")
    bg = PhotoImage(file='bg.png')
    label1 = Label(root, image=bg)
    label1.place(x=1, y=0)

    root.title("F.L.A.M.E.S.")


    label1 = Label(root, text="Partner1 Name: ",

                   fg='white', bg='red', font="TimesNewRoman 14 bold", relief="sunken")


    label2 = Label(root, text="Partner2 Name: ",

                   fg='white', bg='red', font="TimesNewRoman 14 bold", relief="sunken")


    label3 = Label(root, text="Relationship: ",

                   fg='white', bg='#4f0000', font="TimesNewRoman 14 bold", relief="sunken")

    label1.grid(row=1, column=0, sticky="E", pady=10, padx=5)

    label2.grid(row=2, column=0, sticky="E", pady=10, padx=5)

    label3.grid(row=4, column=0, sticky="E", pady=10)


    Player1_field = Entry(root, font="TimesNewRoman 12 bold italic", justify='center', bg="#bdbdff", relief="sunken", highlightthickness=2)

    Player2_field = Entry(root, font="TimesNewRoman 12 bold italic", justify='center', bg="#eebdff", relief="sunken", highlightthickness=2)
    displaytext = StringVar()
    Status_field = Entry(root, font="TimesNewRoman 12 bold italic", justify='center', bg="#bdeeff", relief="sunken", highlightthickness=2)


    Player1_field.grid(row=1, column=1, ipadx="50")
    Player1_field.config(highlightbackground="red", highlightcolor="green")

    Player2_field.grid(row=2, column=1, ipadx="50")
    Player2_field.config(highlightbackground="red", highlightcolor="green")

    Status_field.grid(row=4, column=1, ipadx="50")
    Status_field.config(highlightbackground="green", highlightcolor="red")



    button1 = Button(root, text="Submit", bg="royal blue",

                     fg="white", font='TimesNewRoman 16 bold', command=tell_status)


    button2 = Button(root, text="Clear", bg="red",

                     fg="white", font='TimesNewRoman 16 bold', command=clear_all)


    button1.grid(row=3, column=1)

    button2.grid(row=5, column=1)

    # Start the GUI

    root.mainloop()