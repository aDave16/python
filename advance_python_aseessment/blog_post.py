import tkinter as tk
from tkinter import messagebox
import os#import to work with files and directories

#stores username
class User:
    def __init__(self, name):
        self.name = name

#stores post details and saves to file
class Post:
    def __init__(self, user, title, content):
        self.user = user
        self.title = title
        self.content = content

    def save(self):
        filename = f"{self.user.name}_{self.title}.txt"#filename is created using username and title e.g. "Ami_MyFirstPost.txt"
        with open(filename, "w") as f:#open file in write mode
            f.write(self.content)#write content to file

# ---------------------------
# match-case controller
# ---------------------------
def handle_action(action):
    match action:

        case "save":
            save_post()

        case "view":
            view_post()

        case "create":
            name_entry.delete(0, tk.END)
            title_entry.delete(0, tk.END)
            text_box.delete("1.0", tk.END)


def save_post():
    name = name_entry.get()
    title = title_entry.get()
    content = text_box.get("1.0", tk.END).strip()#get content from line 1 ,0 character text box and remove leading/trailing whitespace

    if name == "" or title == "" or content == "":
        messagebox.showwarning("Error", "Fill all fields")
        return

    user = User(name)#user is object use to create User class name
    post = Post(user, title, content)

    try:
        post.save()#save method is called to save the post to a file
        messagebox.showinfo("Success", "Saved!")
        load_posts()#new posts are loaded to listbox after saving a new post
    except:
        messagebox.showerror("Error", "Could not save")

def load_posts():
    listbox.delete(0, tk.END)#clear all old list
    for file in os.listdir():#list all files in current directory
        if file.endswith(".txt"):
            listbox.insert(tk.END, file)#insert file that ends with .txt to listbox

def view_post():
    try:
        file = listbox.get(listbox.curselection())#get the selected file from listbox 
        with open(file, "r") as f:
            data = f.read()
        text_box.delete("1.0", tk.END)#clear old text
        text_box.insert(tk.END, data)#add new text
    except:
        messagebox.showwarning("Error", "Select a file")


root = tk.Tk()
root.title("MiniBlog")

tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Title").grid(row=1, column=0, padx=10, pady=5)
title_entry = tk.Entry(root)
title_entry.grid(row=1, column=1)

tk.Label(root, text="Content").grid(row=2, column=0, padx=10, pady=5)
text_box = tk.Text(root, height=5, width=40)
text_box.grid(row=2, column=1, columnspan=2)

tk.Button(root, text="Create", command=lambda: handle_action("create")).grid(row=3, column=0, pady=10)
tk.Button(root, text="Save", command=lambda: handle_action("save")).grid(row=3, column=1)
tk.Button(root, text="View", command=lambda: handle_action("view")).grid(row=3, column=2)

listbox = tk.Listbox(root, width=40)
listbox.grid(row=4, column=0, columnspan=3)

load_posts()#initially load all posts to listbox when application starts

root.mainloop()