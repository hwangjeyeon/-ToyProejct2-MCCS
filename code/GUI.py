import tkinter

import customtkinter

import func

window = customtkinter.CTk()
window.geometry("500x500")
window.title("Test")
window.resizable(False,False)
window.grid_columnconfigure((0,2),weight=1)
window.grid_rowconfigure((2,20),weight=1)
frame1 = customtkinter.CTkFrame(window, fg_color="transparent")

align_label1 = customtkinter.CTkLabel(window, text="", anchor="center")

radiobutton1 = customtkinter.CTkRadioButton(window, text="ISO alpha2")
radiobutton2 = customtkinter.CTkRadioButton(window, text="ISO alpha3")

text_label1 = customtkinter.CTkLabel(window, text="국가명")
text_label2 = customtkinter.CTkLabel(window, text="국가 코드")

textbox1 = customtkinter.CTkTextbox(window, width=170, height=300,border_width=2, border_color="black")
textbox2 = customtkinter.CTkTextbox(window, width=170, height=300,border_width=2, border_color="black")



button1 = customtkinter.CTkButton(frame1, text="변환", width=50)
button2 = customtkinter.CTkButton(frame1, text="변환", width=50)


canvas1 = tkinter.Canvas(frame1, width=50, height=20, bg="#ebebeb", bd=0, highlightthickness=0)
canvas2 = tkinter.Canvas(frame1, width=50, height=20, bg="#ebebeb", bd=0, highlightthickness=0)
canvas1.create_line(0, 10, 50, 10, arrow="last", width=2)
canvas2.create_line(50, 10, 0, 10, arrow="last", width=2)


align_label1.grid(row=0,column=1,padx=0,pady=20, sticky="e")
radiobutton1.grid(row=0,column=0,padx=0,pady=20, sticky="e")
radiobutton2.grid(row=0,column=2,padx=0,pady=20, sticky="w")
frame1.grid(row=2,column=1,padx=0,pady=0,sticky="ns")
text_label1.grid(row=1,column=0,padx=0,pady=40)
text_label2.grid(row=1,column=2,padx=0,pady=40)
textbox1.grid(row=2, column=0, padx=0, pady=0)
textbox2.grid(row=2, column=2, padx=0, pady=0)
button1.grid(row=0,column=0,padx=0,pady=30)
button2.grid(row=3,column=0,padx=0,pady=0)
canvas1.grid(row=1, column=0,padx=0,pady=15)
canvas2.grid(row=2, column=0,padx=0,pady=40)


radiobutton1.bind("<ButtonRelease-1>", func.RBChk1)
radiobutton2.bind("<ButtonRelease-1>", func.RBChk2)
button1.bind("<ButtonRelease-1>", func.GetText1)
button2.bind("<ButtonRelease-1>", func.GetText2)
