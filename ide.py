from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
root = Tk()

root.title('Custom IDE')

file_path = ''

def set_file_path(path):
    global file_path
    file_path = path 

# def run():
#     code = editor.get('1.0', END)
#     exec(code)

def run():
    if file_path == '':
        # save_dialog = Toplevel()
        # save_dialog.title('WARNING!')
        # text = Label(save_dialog, text='Save your code to execute it.')
        # text.pack()
        messagebox.showerror('Error!', 'Save your code to execute it.')
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr = subprocess.PIPE, shell=TRUE)
    output, error = process.communicate()
    code_output.delete('1.0', END)
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)

def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

def save():
    path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)

def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0',END)
        editor.insert('1.0',code)
        set_file_path(path)


menu_bar = Menu(root)

file = Menu(menu_bar, tearoff=0)
# file.add_command(label='Run', command = run)
file.add_command(label='Open', command = open_file)
file.add_command(label='Save', command = save)
file.add_command(label='Save As', command = save_as)
file.add_command(label='Exit', command = exit)
menu_bar.add_cascade(label='File', menu = file)
root.config(menu=menu_bar)

# run = Menu(menu_bar, tearoff=0)
# run.add_command(label='Run', command = run)
# menu_bar.add_cascade(label='Run', menu = run)
# root.config(menu=menu_bar)

menu_bar.add_command(label='Run', command = run)

editor = Text()
editor.pack()

code_output = Text(height=12)
code_output.pack()

root.mainloop()
