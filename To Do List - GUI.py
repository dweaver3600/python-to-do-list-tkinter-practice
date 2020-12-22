from tkinter import *

root = Tk()
var = StringVar()

root.title('To Do List')
root.minsize(width=600, height=300)

# Try this to update label text in the future easily
# label = Label(root, textvariable=var)
# var.set("Hello")
# label.pack()

global to_list_text
global to_list_labels
to_list_text = []
to_list_labels = []


def label_on_hover_leave(event):
    value = event.widget
    value.config(fg='black')


def label_on_hover_enter(event):
    value = event.widget
    value.config(fg='grey')


def on_press_enter_to_list(event):
    add_to_list_function()


def click_destroy(event):
    value = event.widget['text'].strip('-<> ')
    print(value)

    widgets = root.grid_slaves()

    # remove from root or to list labels
    widgets[to_list_text.index(value)].destroy()

    # delete from to list text
    to_list_text.pop(to_list_text.index(value))


def enable_disable(event):
    if Entry_To_Add.get() is '':
        Button_To_Add.config(state='disable')
    else:
        Button_To_Add.config(state='normal')


def add_to_list_function():
    to_add = Entry_To_Add.get()

    if to_add is '':
        return

    mark = False

    if to_add in to_list_text:
        mark = True

    else:
        to_list_text.append(to_add)

        temp_lab = Label(text=to_add)
        temp_lab.bind('<Button-1>', click_destroy)
        temp_lab.bind('<Enter>', label_on_hover_enter)
        temp_lab.bind('<Leave>', label_on_hover_leave)
        temp_lab.grid(row=len(to_list_labels) + 1, column=1, sticky=W)

        to_list_labels.append(temp_lab)

    widgets = root.grid_slaves()

    for x in range(len(to_list_text)):
        if x == to_list_text.index(to_add) and mark:
            widgets[x].config(text='- - > ' + to_list_text[x] + ' < - -')
            mark = False
            continue

        else:
            widgets[x].config(text=to_list_text[x])

    Entry_To_Add.delete(0, END)


Label(root, text="Add To List Label: ").grid(row=0, column=0)

Entry_To_Add = Entry(border=2)
Entry_To_Add.bind('<Return>', on_press_enter_to_list)
Entry_To_Add.bind('<KeyRelease>', enable_disable)
Entry_To_Add.grid(row=0, column=1)

Entry_Store = Entry(border=2)
Entry_Store.insert(0, 'default text')
Entry_Store.grid(row=0, column=2)

Button_To_Add = Button(text='Enter', padx=25, border=2, command=add_to_list_function, state='disabled')
Button_To_Add.grid(row=0, column=3)


root.mainloop()
