#Step 1: Import Libraries
import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfilename


#Step 4:Making use of those button
def save_file():
    file_location = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text files","*.txt"),  ("All files", "*.*")]
    )

    if not file_location:
        return
    
    with open(file_location, "w") as file_output:
        text  = text_edit.get(1.0, tk.END)
        file_output.write(text)
    root.title(f"My Own NotePad - {file_location}")

def open_file():
    file_locaion = askopenfilename(
        filetypes=[("Text files","*.txt"),("All files","*.*")]
    )

    if not file_locaion:
        return
    
    text_edit.delete(1.0, tk.END)
    with open(file_locaion, "r") as file_input:
        text = file_input.read()
        text_edit.insert(tk.END, text)
    root.title(f"My Own NotePad - {file_locaion}")



#Step 2:Create a Base for the NotePad
root = tk.Tk()
root.title("Untitled-NotePad")
root.geometry("644x444")

text_edit = tk.Text(root)           #Whatever text is  written will be writtn in my tkinter window
text_edit.grid(row=0,column=1, sticky="nsew")



#Step 3:Add Save and Open Buttons
frame_button = tk.Frame(root, relief=tk.RAISED, bd=3)           #Setting Button Border
frame_button.grid(row=0,column=0, sticky="ns")

button_open = tk.Button(frame_button, text="Open", command=open_file)
button_open.grid(row=0, column=0, padx=5, pady=5)

button_save = tk.Button(frame_button, text="Save As", command=save_file)
button_save.grid(row=1, column=0, padx=5, pady=5)


root.mainloop()
