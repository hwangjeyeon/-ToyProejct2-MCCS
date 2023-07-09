import GUI
import Info


def RBChk1(event):
    if Info.Alpha2 == 0 and Info.Alpha3 == 0:
        Info.Alpha2 = 1
        GUI.radiobutton1.select()
        GUI.radiobutton1.grid(row=0, column=0, padx=0, pady=20, sticky="e")
        #print("1: " + str(Info.Alpha2))
    else:
        Info.Alpha2 = 0
        GUI.radiobutton1.deselect()
        GUI.radiobutton1.grid(row=0, column=0, padx=0, pady=20, sticky="e")
        #print("1: " + str(Info.Alpha2))


def RBChk2(event):
    if Info.Alpha3 == 0 and Info.Alpha2 ==0:
        Info.Alpha3 = 1
        GUI.radiobutton2.select()
        GUI.radiobutton2.grid(row=0, column=2, padx=0, pady=20, sticky="w")
        #print("2: " + str(Info.Alpha3))
    else:
        Info.Alpha3 = 0
        GUI.radiobutton2.deselect()
        GUI.radiobutton2.grid(row=0, column=2, padx=0, pady=20, sticky="w")
        #print("2: " + str(Info.Alpha3))

def GetText1(event):
    Info.CountryName_S = GUI.textbox1.get("1.0", "end-1c")
    Info.CountryName_L = Info.CountryName_S.split()
    #print(Info.CountryCode_L)
def GetText2(event):
    Info.CountryCode_S = GUI.textbox2.get("1.0", "end-1c")
    Info.CountryCode_L = Info.CountryCode_S.split()
    #print(Info.CountryName_L)