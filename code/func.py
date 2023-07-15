import tkinter.messagebox
import GUI
import Info
import APIfunc

# 왼쪽 라디오 버튼 누를때 호출되는 함수
def RBChk1(event):
    if Info.Alpha2 == 0 and Info.Alpha3 == 0:
        Info.Alpha2 = 1
        GUI.radiobutton1.select()
        GUI.radiobutton1.grid(row=0, column=0, padx=0, pady=20, sticky="e")
    else:
        Info.Alpha2 = 0
        GUI.radiobutton1.deselect()
        GUI.radiobutton1.grid(row=0, column=0, padx=0, pady=20, sticky="e")

# 오른쪽 라디오 버튼 누를때 호출되는 함수 -> ver1.0 미지원
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

# 변환 버튼 눌렀을 때 옆 텍스트 상자로 변환해서 넣어주는 함수
def GetText1(event):
    # 작성한 값을 가져와서 변수에 저장
    Info.CountryName_S = GUI.textbox1.get("1.0", "end-1c")
    Info.CountryName_L = Info.CountryName_S.split("\n")
    Info.CountryCode_S = ""

    #값을 가져오기 위한 과정
    for name in Info.CountryName_L:
        # 먼저 메모리 저장소를 확인
        for key in Info.MemoryRepository.keys():
            # 값이 있으면 메모리 저장소로부터 가져옴
            if key == name:
                Info.CountryCode_S += Info.MemoryRepository[key]
                Info.Key_chk = 1
                break
            # 값이 없으면 Get 요청으로 값을 가져옴
        if Info.Key_chk != 1:
            Info.MemoryRepository[name] = str(APIfunc.getApi_1(name))
            Info.CountryCode_S += Info.MemoryRepository[name]
        else:
            Info.Key_chk = 0
        Info.CountryCode_S += "\n"
    # 옆 텍스트 상자로 값을 넣어주고 GUI 배치
    Info.CountryCode_S = Info.CountryCode_S[:-1]
    GUI.textbox2.delete("1.0", "end-1c")
    GUI.textbox2.insert("0.0", Info.CountryCode_S)
    GUI.textbox2.grid(row=2, column=2, padx=0, pady=0)


# 변환 버튼 눌렀을 때 옆 텍스트 상자로 변환해서 넣어주는 함수
def GetText2(event):
    # 작성한 값을 가져와서 변수에 저장
    Info.CountryCode_S = GUI.textbox2.get("1.0", "end-1c")
    Info.CountryCode_L = Info.CountryCode_S.split("\n")
    Info.CountryName_S = ""

    # 값을 가져오기 위한 과정
    for name in Info.CountryCode_L:
        #ISO Alpha3 변환을 요청할 때, 알림창 띄어주는 함수
        if len(name) == 3:
            tkinter.messagebox.showinfo(title="ver1.0", message="현재 버전에서 지원하지 않습니다")
            break
        # 먼저 메모리 저장소를 확인
        for key in Info.MemoryRepository.keys():
            # 값이 있으면 메모리 저장소로부터 가져옴
            if key == name:
                Info.CountryName_S += Info.MemoryRepository[key]
                Info.Key_chk = 1
                break
            # 값이 없으면 Get 요청으로 값을 가져옴
        if Info.Key_chk != 1:
            Info.MemoryRepository[name] = str(APIfunc.getApi_2(name))
            Info.CountryName_S += Info.MemoryRepository[name]
        else:
            Info.Key_chk = 0
        Info.CountryName_S += "\n"

    # 옆 텍스트 상자로 값을 넣어주고 GUI 배치
    Info.CountryName_S = Info.CountryName_S[:-1]
    GUI.textbox1.delete("1.0", "end-1c")
    GUI.textbox1.insert("0.0", Info.CountryName_S)
    GUI.textbox1.grid(row=2, column=0, padx=0, pady=0)

