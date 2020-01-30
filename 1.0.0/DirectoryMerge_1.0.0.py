"""
    You can use DirectoryMerge to merge two directories without making any duplicate directories.
    You can also choose to replace duplicate files by the newer version.
    I would be most grateful for any feedback, you can send it on rainbowhogstudios@gmail.com.

    Copyright © 2020  Matyas Vasek

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from shutil import copytree, copyfile
from os import walk, remove, path
from tkinter import *


def list_dir(dir):
    for (dirpath, dirnames, filenames) in walk(dir):
        dirlist = [dirnames] + [filenames]
        break
    return dirlist, dirpath


def copy_missing_files(dir1, dir2, replace_old):
    #try:
    nextdirlist = []
    dirlist1, path1 = list_dir(dir1)
    dirlist2, path2 = list_dir(dir2)
    # print("Searching: "+path1,"\n","         ", path2)
    for i in dirlist1[1]:
        if i not in dirlist2[1]:
            # print("Copying missing file: " + i)
            copyfile(path1 + '\\' + i, path2 + '\\' + i)
        elif replace_old == 1:
            age1 = path.getmtime(path1 + '\\' + i)
            age2 = path.getmtime(path2 + '\\' + i)
            if age2 < age1:
                # print("Replacing file: " + i)
                remove(path2 + '\\' + i)
                copyfile(path1 + '\\' + i, path2 + '\\' + i)

    for i in dirlist1[0]:
        if i in dirlist2[0]:
            nextdirlist.append(i)
        else:
            # T1.insert(INSERT, "Copying missing directory: " + i)
            copytree(path1 + '\\' + i, path2 + '\\' + i)
    for i in nextdirlist:
        copy_missing_files(dir1 + "\\" + i, dir2 + "\\" + i, replace_old)
    T1.insert(END, "Merging complete!")
    #except:
        #T1.insert(END, "Invalid address")


if __name__ == "__main__":
    root = Tk(className=" DirectoryMerge")
    L0 = Label(root, bg="teal", fg="lavender", text="Welcome to DirectoryMerge!")
    L1 = Label(root, bg="teal", fg="lavender", text="Please do not use this script on whole drives it could result in unpleasant errors.")
    L2 = Label(root, bg="teal", fg="lavender", text=r"Format example: C:\example\dir1\dir2")
    L3 = Label(root, bg="teal", fg="lavender", text="Path to the origin directory:")
    L4 = Label(root, bg="teal", fg="lavender", text="Path to the destination directory:")
    LC1 = Label(root, bg="teal", fg="lavender", text="Replace old files")
    version = Label(root, bg="teal", text="version 1.0.0", fg="lightgray")
    dir1 = Entry(root)
    dir2 = Entry(root)
    replace_old = IntVar()
    C1 = Checkbutton(root,bg="teal", fg="black", variable=replace_old, onvalue=1, offvalue=0)
    T1 = Text(root)
    B1 = Button(root, text="START", bg="lavender", fg="teal", command=lambda : copy_missing_files(dir1.get(), dir2.get(), replace_old.get()))
    root.configure(background="teal")
    L0.grid(columnspan=2, row=0, pady=5)
    L1.grid(columnspan=2, row=1)
    L2.grid(columnspan=2, row=2)
    L3.grid(row=3)
    dir1.grid(column=1, row=3, sticky=W)
    L4.grid(row=4)
    dir2.grid(column=1, row=4, sticky=W)
    C1.grid(column=1, row=5, sticky=W)
    LC1.grid(row=5, sticky=E)
    B1.grid(columnspan=2, row=6, pady=10)
    version.grid(column=1, sticky=E)
    root.mainloop()
