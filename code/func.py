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
    if Info.Alpha3 == 0 and Info.Alpha2 ==0:
        Info.Alpha3 = 1
        GUI.radiobutton2.select()
        GUI.radiobutton2.grid(row=0, column=2, padx=0, pady=20, sticky="w")
    else:
        Info.Alpha3 = 0
        GUI.radiobutton2.deselect()
        GUI.radiobutton2.grid(row=0, column=2, padx=0, pady=20, sticky="w")

def GetText1(event):
    Info.CountryName_S = GUI.textbox1.get("1.0", "end-1c")
    Info.CountryName_L = Info.CountryName_S.split("\n")
    Info.CountryCode_S = ""
    for cc in Info.CountryName_L:
        Info.CountryCode_S += str(APIfunc.getApi_1(cc))
        Info.CountryCode_S += "\n"
    Info.CountryCode_S = Info.CountryCode_S[:-1]
    GUI.textbox2.delete("1.0", "end-1c")
    GUI.textbox2.insert("0.0", Info.CountryCode_S)
    GUI.textbox2.grid(row=2, column=2, padx=0, pady=0)

def GetText2(event):
    Info.CountryCode_S = GUI.textbox2.get("1.0", "end-1c")
    Info.CountryCode_L = Info.CountryCode_S.split("\n")
    Info.CountryName_S = ""
    for cc in Info.CountryCode_L:
        Info.CountryName_S += str(APIfunc.getApi_2(cc))
        Info.CountryName_S += "\n"
    Info.CountryName_S = Info.CountryName_S[:-1]
    GUI.textbox1.delete("1.0", "end-1c")
    GUI.textbox1.insert("0.0", Info.CountryName_S)
    GUI.textbox1.grid(row=2, column=0, padx=0, pady=0)

