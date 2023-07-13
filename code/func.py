import time
import tkinter.messagebox

import GUI
import Info
import APIfunc


def RBChk1(event):
    if Info.Alpha2 == 0 and Info.Alpha3 == 0:
        Info.Alpha2 = 1
        GUI.radiobutton1.select()
        GUI.radiobutton1.grid(row=0, column=0, padx=0, pady=20, sticky="e")
    else:
        Info.Alpha2 = 0
        GUI.radiobutton1.deselect()
        GUI.radiobutton1.grid(row=0, column=0, padx=0, pady=20, sticky="e")


def RBChk2(event):
    GUI.radiobutton2.deselect()
    tkinter.messagebox.showinfo(title="ver 1.0", message="현재 버전에서 지원하지 않습니다.")
    if Info.Alpha3 == 0 and Info.Alpha2 ==0:

        '''Info.Alpha3 = 1
        GUI.radiobutton2.select()
        GUI.radiobutton2.grid(row=0, column=2, padx=0, pady=20, sticky="w")'''
    else:
        '''Info.Alpha3 = 0
        GUI.radiobutton2.deselect()
        GUI.radiobutton2.grid(row=0, column=2, padx=0, pady=20, sticky="w")'''

def GetText1(event):
    start = time.time()
    Info.CountryName_S = GUI.textbox1.get("1.0", "end-1c")
    Info.CountryName_L = Info.CountryName_S.split("\n")
    Info.CountryCode_S = ""



    for cc in Info.CountryName_L:
        for dd in Info.MemoryRepository.keys():
            if dd == cc:
                Info.CountryCode_S += Info.MemoryRepository[dd]
                Info.Key_chk = 1
                break
        if Info.Key_chk != 1:
            Info.MemoryRepository[cc] = str(APIfunc.getApi_1(cc))
            Info.CountryCode_S += Info.MemoryRepository[cc]
        else:
            Info.Key_chk = 0
        Info.CountryCode_S += "\n"
    Info.CountryCode_S = Info.CountryCode_S[:-1]
    GUI.textbox2.delete("1.0", "end-1c")
    GUI.textbox2.insert("0.0", Info.CountryCode_S)
    GUI.textbox2.grid(row=2, column=2, padx=0, pady=0)
    end = time.time()
    print(f"{end - start} sec")
def GetText2(event):
    start = time.time()
    Info.CountryCode_S = GUI.textbox2.get("1.0", "end-1c")
    Info.CountryCode_L = Info.CountryCode_S.split("\n")
    Info.CountryName_S = ""

    for cc in Info.CountryCode_L:
        if len(cc) == 3:
            tkinter.messagebox.showinfo(title="ver1.0", message="현재 버전에서 지원하지 않습니다")
            break
        for dd in Info.MemoryRepository.keys():
            if dd == cc:
                Info.CountryName_S += Info.MemoryRepository[dd]
                Info.Key_chk = 1
                break
        if Info.Key_chk != 1:
            Info.MemoryRepository[cc] = str(APIfunc.getApi_2(cc))
            Info.CountryName_S += Info.MemoryRepository[cc]
        else:
            Info.Key_chk = 0
        Info.CountryName_S += "\n"
    Info.CountryName_S = Info.CountryName_S[:-1]
    GUI.textbox1.delete("1.0", "end-1c")
    GUI.textbox1.insert("0.0", Info.CountryName_S)
    GUI.textbox1.grid(row=2, column=0, padx=0, pady=0)
    end = time.time()
    print(f"{end - start} sec")

