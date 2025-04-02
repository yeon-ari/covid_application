from tkinter import * #tkinter 모듈 재사용 선언
from tkinter import ttk #ttk 모듈 사용 선언
import tkinter.messagebox #tkinter.messagebox 모듈 사용 선언

window1 = Tk() #새로운 윈도우 창 개설
window1.title('코로나19 종합앱') #윈도우 창의 이름 설정
window1.geometry('360x300') #윈도우 창의 크기 설정
window1.resizable(width=FALSE, height=FALSE) #설정한 크기가 바뀌지 않도록 고정

#라벨로 앱 안내 문구 설정(해당 윈도우 창, 문구)하고 화면에 출력 입력
label_start=tkinter.Label(window1, text='[코로나19 종합 앱]\n 원하시는 항목을 클릭하세요.') 
label_start.pack()

def selfcheck(): #코로나19 자가진단 체크리스트 함수 설정

    window=Tk() #새로운 윈도우 창 개설
    window.title("코로나19 자가진단서") #윈도우 창의 이름 설정
    
    def clickMe(): #결과 확인 버튼 함수 설정

        check_num = cVar1.get()+cVar2.get()+cVar3.get()+cVar4.get()+cVar5.get()+cVar6.get() #체크리스트에 체크한 개수 취합

        if check_num == 0: #체크한 개수가 0개일 때, 해당 문구 출력
            str="정상입니다.\n코로나 예방에 주의를 기울이세요."
        elif check_num<=3 and check_num>=1: #체크한 개수가 1개이상 3개 이하일 때, 해당 문구 출력
            str="주의 단계입니다.\n자가 격리를 시작하시고 추후 몸 상태를 지켜보세요."
        else: #체크한 개수가 4개 이상일 때, 해당 문구 출력
            str="위험 단계입니다.\n 당장 가까운 선별진료소를 방문하세요."

        tkinter.messagebox.showinfo("자가진단 결과", str) #위 함수가 실행될 때 뜨는 문구를 메세지박스로 설정

    #체크버튼과 연결해서 사용할 변수 생성(int변수로 생성)
    cVar1=IntVar(window) 
    cVar2=IntVar(window)
    cVar3=IntVar(window)
    cVar4=IntVar(window)
    cVar5=IntVar(window)
    cVar6=IntVar(window)

    #자가진단 문구가 입력된 체크버튼 위젯 설정(해당 윈도우 창, 너비, 문구, 변수, 위치)
    c1=Checkbutton(window,width=30, text="37.5도 이상의 발열 증상이 있나요?", variable=cVar1).grid(row=1, sticky=W) 
    c2=Checkbutton(window,width=30,text="후각 또는 미각에 이상 증상이 있나요?", variable=cVar2).grid(row=2, sticky=W)
    c3=Checkbutton(window,width=30,text="마른 기침이 1시간 이상으로 지속되나요?", variable=cVar3).grid(row=3, sticky=W)
    c4=Checkbutton(window,width=30,text="최근 15일 이내 해외에서 입국하셨나요?", variable=cVar4).grid(row=4, sticky=W)
    c5=Checkbutton(window,width=30,text="대량 집회, 클럽, PC방, 코인노래방 등의\n장소를 방문한 적이 있나요?", variable=cVar5).grid(row=5, sticky=W)
    c6=Checkbutton(window,width=30,text="가족이나 지인 중 확진자가 있습니까?", variable=cVar6).grid(row=6, sticky=W)

    #체크버튼이 선택되지 않은 상태인 초기값 0으로 설정해 체크여부가 2개(체크,미체크)이도록 설정
    cVar1.set(0)
    cVar2.set(0)
    cVar3.set(0)
    cVar4.set(0)
    cVar5.set(0)
    cVar6.set(0)

    action=ttk.Button(window,text="결과 확인", command=clickMe).grid(row=7) #결과확인버튼 위젯 설정(해당 윈도우 창, 문구, 실행할 명령, 위치)

    window.mainloop() #등록한 코로나19 자가진단 체크리스트 윈도우 창 실행

def place():
    from tkinter import messagebox
    from PIL import Image  #pillow 모듈 재사용 선언(다른 사용자 컴퓨터에서 프로그램 실행 시 명령 프롬프트 창에서 pillow 모듈 설치 필요)
    import webbrowser  #webbroswer 모듈 재사용 선언     

    def openurl_gn01():  #강남구 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("http://health.gangnam.go.kr/main.do")  #해당 진료소 홈페이지로 이동
    def map_gn01():  #강남구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()  #새로운 윈도우 창 생성
        p_window.title('강남구보건소'); p_window.geometry('500x500')  #윈도우 창 제목 & 크기 지정
        msg = Label(p_window, text = '평일: 09:00~20:00,\n 주말: 09:00~19:00,\n 전화번호: 02-3423-5555\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)  #해당 진료소 운영시간 & 전화번호 정보 제공 위한 라벨 설정 후 msg 대입
        msg.pack()  #msg 화면에 출력 설정
        btn01 = Button(p_window,text = "강남구보건소 사이트로 이동", command = openurl_gn01)  #해당 진료소 홈페이지로 이동시켜 줄 버튼 생성
        btn01.pack()  #버튼 출력
        photo_gn01 = PhotoImage(file = "learning/강남구보건소.png", master = p_window)  #PhotoImage에 이미지(진료소 인근에 위치한 지하철역 포함 사진) 경로 설정하여 photo_지역이름 변수 대입
        photo_gn01_resize = photo_gn01.subsample(2, 2)  #캡처 사진 파일 크기 반으로 조정
        label01 = Label(p_window, image = photo_gn01_resize)  #label01 변수에 이미지 라벨 설정 후 대입
        label01.pack()  #label01 화면에 출력 설정
        p_window.mainloop()  #등록한 이벤트 실행

    def openurl_gn02(): 
        webbrowser.open("http://www.samsunghospital.com/home/main/index.do")
    def map_gn02():
        p_window = Tk()
        p_window.title('삼성서울병원'); p_window.geometry('800x800')
        msg = Label(p_window, text = '평일: 00:00~24:00,\n 주말: 00:00~24:00,\n 전화번호: 02-3410-0543\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "삼성서울병원 사이트로 이동", command = openurl_gn02)
        btn01.pack()
        photo_gn02 = PhotoImage(file = "learning/삼성서울병원.png", master = p_window)
        photo_gn02_resize = photo_gn02.subsample(2, 2)
        label01 = Label(p_window, image = photo_gn02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_gn03():
        webbrowser.open("https://gs.iseverance.com/")
    def map_gn03():
        p_window = Tk()
        p_window.title('강남세브란스병원'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 09:00~17:00,\n 토: 09:00~12:30, 일: 미운영,\n 전화번호: 02-1599-6114\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "강남세브란스병원 사이트로 이동", command = openurl_gn03)
        btn01.pack()
        photo_gn03 = PhotoImage(file = "learning/강남세브란스병원.png", master = p_window)
        photo_gn03_resize = photo_gn03.subsample(2, 2)
        label01 = Label(p_window, image = photo_gn03_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_gd01():  #강동구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("https://www.gangdong.go.kr/health/site/main/home")
    def map_gd01():  #강동구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('강동구보건소'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말: 09:00~17:00,\n 전화번호: 02-3425-6713\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "강동구보건소 사이트로 이동", command = openurl_gd01)
        btn01.pack()
        photo_gd01 = PhotoImage(file = "learning/강동구보건소.png", master = p_window)
        photo_gd01_resize = photo_gd01.subsample(2, 2)
        label01 = Label(p_window, image = photo_gd01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_gd02():
        webbrowser.open("https://seoul.bohun.or.kr/000main/index.php")
    def map_gd02():
        p_window = Tk()
        p_window.title('중앙보훈병원'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 09:00~17:30,\n 주말: 미운영,\n 전화번호: 02-2225-1114\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "중앙보훈병원 사이트로 이동", command = openurl_gd02)
        btn01.pack()
        photo_gd02 = PhotoImage(file = "learning/중앙보훈병원.png", master = p_window)
        photo_gd02_resize = photo_gd02.subsample(2, 2)
        label01 = Label(p_window, image = photo_gd02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_gd03():
        webbrowser.open("http://www.khnmc.or.kr/index.do")
    def map_gd03():
        p_window = Tk()
        p_window.title('강동경희대병원'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 09:00~17:30,\n 토: 09:00~12:00 일: 미운영,\n 전화번호: 02-440-7000\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "강동경희대병원 사이트로 이동", command = openurl_gd02)
        btn01.pack()
        photo_gd03 = PhotoImage(file = "learning/강동경희대병원.png", master = p_window)
        photo_gd03_resize = photo_gd03.subsample(2, 2)
        label01 = Label(p_window, image = photo_gd03_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_gd04():
        webbrowser.open("https://www.kdh.or.kr:446/index.asp")
    def map_gd04():
        p_window = Tk()
        p_window.title('강동성심병원'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 08:30~16:30,\n 토: 08:30~11:30 일: 미운영,\n 전화번호: 1588-4100\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "강동성심병원 사이트로 이동", command = openurl_gd04)
        btn01.pack()
        photo_gd04 = PhotoImage(file = "learning/강동성심병원.png", master = p_window)
        photo_gd04_resize = photo_gd04.subsample(2, 2)
        label01 = Label(p_window, image = photo_gd04_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_gb01():  #강북구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("http://ehealth.gangbuk.go.kr/site/kr/index.jsp")
    def map_gb01():  #강북구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('강북구보건소'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말: 09:00~18:00,\n 전화번호: 02-901-7704(6)\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "강북구보건소 사이트로 이동", command = openurl_gb01)
        btn01.pack()
        photo_gb01 = PhotoImage(file = "learning/강북구보건소.png", master = p_window)
        photo_gb01_resize = photo_gb01.subsample(2, 2)
        label01 = Label(p_window, image = photo_gb01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_gs01():  #강서구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("https://www.gangseo.seoul.kr/site/health/index.jsp")
    def map_gs01():  #강서구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('강서구보건소'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말: 09:00~18:00,\n 전화번호: 02-2600-5465\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "강서구보건소 사이트로 이동", command = openurl_gs01)
        btn01.pack()
        photo_gs01 = PhotoImage(file = "learning/강서구보건소.png", master = p_window)
        photo_gs01_resize = photo_gs01.subsample(2, 2)
        label01 = Label(p_window, image = photo_gs01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_gs02():
        webbrowser.open("https://seoul.eumc.ac.kr/main.do")
    def map_gs02():
        p_window = Tk()
        p_window.title('이화여자대학교 서울병원'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 09:30~12:00,\n 주말: 미운영,\n 전화번호: 1522-7000\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "이화여자대학교 서울병원 사이트로 이동", command = openurl_gs02)
        btn01.pack()
        photo_gs02 = PhotoImage(file = "learning/이화여자대학교 서울병원.png", master = p_window)
        photo_gs02_resize = photo_gs02.subsample(2, 2)
        label01 = Label(p_window, image = photo_gs02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_ga01():  #관악구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("http://www.gwanak.go.kr/site/health/main.do")
    def map_ga01():  #관악구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('관악구보건소'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 토: 09:00~18:00, 일: 09:00~13:00\n 전화번호: 02-879-7131\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "관악구보건소 사이트로 이동", command = openurl_ga01)
        btn01.pack()
        photo_ga01 = PhotoImage(file = "learning/관악구보건소.png", master = p_window)
        photo_ga01_resize = photo_ga01.subsample(2, 2)
        label01 = Label(p_window, image = photo_ga01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_ga02():
        webbrowser.open("http://www.newyjh.com/main/index.htm")
    def map_ga02():
        p_window = Tk()
        p_window.title('에이치플러스 양지병원'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 08:30~17:00,\n 토: 08:30~12:30, 일: 미운영\n 전화번호: 1877-8875\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "에이치플러스 양지병원 사이트로 이동", command = openurl_ga02)
        btn01.pack()
        photo_ga02 = PhotoImage(file = "learning/에이치플러스 양지병원.png", master = p_window)
        photo_ga02_resize = photo_gs01.subsample(2, 2)
        label01 = Label(p_window, image = photo_ga02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_gj01():  #광진구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("https://www.gwangjin.go.kr/health/main/main.do")
    def map_gj01():  #광진구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('광진구보건소'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말: 09:00~17:00\n 전화번호: 02-450-1937\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "광진구보건소 사이트로 이동", command = openurl_gj01)
        btn01.pack()
        photo_gj01 = PhotoImage(file = "learning/광진구보건소.png", master = p_window)
        photo_gj01_resize = photo_gj01.subsample(2, 2)
        label01 = Label(p_window, image = photo_gj01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_gj02():
        webbrowser.open("https://www.kuh.ac.kr/main.do")
    def map_gj02():
        p_window = Tk()
        p_window.title('건국대학교병원'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 토: 09:00~12:30, 일:미운영\n 전화번호: 02-1588-1533\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "건국대학교병원 사이트로 이동", command = openurl_gj02)
        btn01.pack()
        photo_gj02 = PhotoImage(file = "learning/건국대학교병원.png", master = p_window)
        photo_gj02_resize = photo_gj02.subsample(2, 2)
        label01 = Label(p_window, image = photo_gj02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_gr01():  #구로구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("https://www.guro.go.kr/health/index.do")
    def map_gr01():  #구로구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('구로구보건소'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말: 09:00~18:00\n 전화번호: 02-860-2012\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "구로구보건소 사이트로 이동", command = openurl_gr01)
        btn01.pack()
        photo_gr01 = PhotoImage(file = "learning/구로구보건소.png", master = p_window)
        photo_gr01_resize = photo_gr01.subsample(2, 2)
        label01 = Label(p_window, image = photo_gr01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_gr02():
        webbrowser.open("http://guro.kumc.or.kr/main/index.do")
    def map_gr02():
        p_window = Tk()
        p_window.title('고대구로병원'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~17:30,\n 주말: 미운영\n 전화번호: 02-2626-1554\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "고대구로병원 사이트로 이동", command = openurl_gr02)
        btn01.pack()
        photo_gr02 = PhotoImage(file = "learning/고대구로병원.png", master = p_window)
        photo_gr02_resize = photo_gr02.subsample(2, 2)
        label01 = Label(p_window, image = photo_gr02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_gr03():
        webbrowser.open("http://www.kurosungsim.co.kr/main/main.php")
    def map_gr03():
        p_window = Tk()
        p_window.title('구로성심병원'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~17:30,\n 토:09:00~12:30, 일: 미운영\n 전화번호: 02-2067-1500\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "구로성심병원 사이트로 이동", command = openurl_gr03)
        btn01.pack()
        photo_gr03 = PhotoImage(file = "learning/구로성심병원.png", master = p_window)
        photo_gr03_resize = photo_gr03.subsample(2, 2)
        label01 = Label(p_window, image = photo_gr03_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_gc01():  #구로구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("https://www.geumcheon.go.kr/health/index.do")
    def map_gc01():  #금천구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('금천구보건소'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말:09:00~16:00\n 전화번호: 02-2627-2717\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "금천구보건소 사이트로 이동", command = openurl_gc01)
        btn01.pack()
        photo_gc01 = PhotoImage(file = "learning/금천구보건소.png", master = p_window)
        photo_gc01_resize = photo_gc01.subsample(2, 2)
        label01 = Label(p_window, image = photo_gc01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_gc02():
        webbrowser.open("https://hmhp.co.kr:41329/new/main.php")
    def map_gc02():
        p_window = Tk()
        p_window.title('희명병원'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 00:00~24:00,\n 주말:00:00~24:00\n 전화번호: 02-2219-7231\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "희명병원 사이트로 이동", command = openurl_gc02)
        btn01.pack()
        photo_gc02 = PhotoImage(file = "learning/희명병원.png", master = p_window)
        photo_gc02_resize = photo_gc02.subsample(2, 2)
        label01 = Label(p_window, image = photo_gc02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_nw01():  #노원구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("https://www.nowon.kr/health/index.do")
    def map_nw01():   #노원구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('노원구보건소'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 토:09:00~18:00, 일: 09:00~13:00\n 전화번호: 02-2116-3000\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "노원구보건소 사이트로 이동", command = openurl_nw01)
        btn01.pack()
        photo_nw01 = PhotoImage(file = "learning/노원구보건소.png", master = p_window)
        photo_nw01_resize = photo_nw01.subsample(2, 2)
        label01 = Label(p_window, image = photo_nw01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_nw02():
        webbrowser.open("http://www.eulji.or.kr/index.jsp")
    def map_nw02():
        p_window = Tk()
        p_window.title('노원을지대학교병원'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 09:00~17:00,\n 주말: 미운영\n 전화번호: 02-970-8000\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "노원을지대학교병원 사이트로 이동", command = openurl_nw02)
        btn01.pack()
        photo_nw02 = PhotoImage(file = "learning/노원을지대학교병원.png", master = p_window)
        photo_nw02_resize = photo_nw02.subsample(2, 2)
        label01 = Label(p_window, image = photo_nw02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_nw03():
        webbrowser.open("http://www.paik.ac.kr/sanggye/")
    def map_nw03():
        p_window = Tk()
        p_window.title('상계백병원'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~16:00,\n 주말: 미운영\n 전화번호: 02-950-1114\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "상계백병원 사이트로 이동", command = openurl_nw03)
        btn01.pack()
        photo_nw03 = PhotoImage(file = "learning/상계백병원.png", master = p_window)
        photo_nw03_resize = photo_nw03.subsample(2, 2)
        label01 = Label(p_window, image = photo_nw03_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_db01():  #도봉구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("http://health.dobong.go.kr/")
    def map_db01():  #도봉구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('도봉구보건소'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말: 09:00~18:00\n 전화번호: 02-2091-4436\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "도봉구보건소 사이트로 이동", command = openurl_db01)
        btn01.pack()
        photo_db01 = PhotoImage(file = "learning/도봉구보건소.png", master = p_window)
        photo_db01_resize = photo_db01.subsample(2, 2)
        label01 = Label(p_window, image = photo_db01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_db02():
        webbrowser.open("https://www.hanilmed.net/portal/index.do;jsessionid=x9tSuJ6TYSRGVD1hfGlGUOlrSaBzRcGB1aWwa8wGdZLN4CN2V8TIUJfefCbEVzaB.hpwebr01_servlet_hompg")
    def map_db02():
        p_window = Tk()
        p_window.title('한일병원'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~17:30,\n 주말: 미운영\n 전화번호: 02-901-3479\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "한일병원 사이트로 이동", command = openurl_db02)
        btn01.pack()
        photo_db02 = PhotoImage(file = "learning/한일병원.png", master = p_window)
        photo_db02_resize = photo_db02.subsample(2, 2)
        label01 = Label(p_window, image = photo_db02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_ddm01():  #동대문구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("https://health.ddm.go.kr/")
    def map_ddm01():  #동대문구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('동대문구보건소'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말: 09:00~15:00\n 전화번호: 02-2127-4283\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "동대문구보건소 사이트로 이동", command = openurl_ddm01)
        btn01.pack()
        photo_ddm01 = PhotoImage(file = "learning/동대문구보건소.png", master = p_window)
        photo_ddm01_resize = photo_ddm01.subsample(2, 2)
        label01 = Label(p_window, image = photo_ddm01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_ddm02():
        webbrowser.open("https://health.ddm.go.kr/")
    def map_ddm02():
        p_window = Tk()
        p_window.title('삼육서울병원'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~16:30,\n 토: 미운영, 일: 09:00~16:30\n 전화번호: 1577-3675\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "삼육서울병원 사이트로 이동", command = openurl_ddm02)
        btn01.pack()
        photo_ddm02 = PhotoImage(file = "learning/삼육서울병원.png", master = p_window)
        photo_ddm02_resize = photo_ddm02.subsample(2, 2)
        label01 = Label(p_window, image = photo_ddm02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_ddm03():
        webbrowser.open("https://www.dbhosp.go.kr/")
    def map_ddm03():
        p_window = Tk()
        p_window.title('서울특별시 동부병원'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 09:00~22:00,\n 주말: 09:00~18:00\n 전화번호: 920-9340/9119\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "서울특별시 동부병원 사이트로 이동", command = openurl_ddm03)
        btn01.pack()
        photo_ddm03 = PhotoImage(file = "learning/서울특별시 동부병원.png", master = p_window)
        photo_ddm03_resize = photo_ddm03.subsample(2, 2)
        label01 = Label(p_window, image = photo_ddm03_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_ddm04():
        webbrowser.open("http://www.sshosp.co.kr/")
    def map_ddm04():
        p_window = Tk()
        p_window.title('서울성심병원'); p_window.geometry('700x700')
        msg = Label(p_window, text = '평일: 09:00~16:00,\n 주말: 미운영\n 전화번호: 966-1616\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "서울성심병원 사이트로 이동", command = openurl_ddm04)
        btn01.pack()
        photo_ddm04 = PhotoImage(file = "learning/서울성심병원.png", master = p_window)
        photo_ddm04_resize = photo_ddm04.subsample(2, 2)
        label01 = Label(p_window, image = photo_ddm04_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_ddm05():
        webbrowser.open("http://www.khmc.or.kr/index.php")
    def map_ddm05():
        p_window = Tk()
        p_window.title('경희의료원'); p_window.geometry('700x700')
        msg = Label(p_window, text = '평일: 08:30~17:00,\n 토: 08:30~12:00, 일: 미운영\n 전화번호: 958-8114\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "경희의료원 사이트로 이동", command = openurl_ddm05)
        btn01.pack()
        photo_ddm05 = PhotoImage(file = "learning/경희의료원.png", master = p_window)
        photo_ddm05_resize = photo_ddm05.subsample(2, 2)
        label01 = Label(p_window, image = photo_ddm05_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_dj01():  #동작구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("http://www.dongjak.go.kr/healthcare/main/main.do")
    def map_dj01():  #동작구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('동작구보건소'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말: 09:00~15:00\n 전화번호: 02-820-9465\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "동작구보건소 사이트로 이동", command = openurl_dj01)
        btn01.pack()
        photo_dj01 = PhotoImage(file = "learning/동작구보건소.png", master = p_window)
        photo_dj01_resize = photo_dj01.subsample(2, 2)
        label01 = Label(p_window, image = photo_dj01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_dj02():
        webbrowser.open("https://www.brmh.org/index.do")
    def map_dj02():
        p_window = Tk()
        p_window.title('서울특별시 보라매병원'); p_window.geometry('700x700')
        msg = Label(p_window, text = '평일: 09:00~17:30,\n 주말: 09:00~12:30\n 전화번호: 02-870-2114\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "서울특별시 보라매병원 사이트로 이동", command = openurl_dj02)
        btn01.pack()
        photo_dj02 = PhotoImage(file = "learning/서울특별시 보라매병원.png", master = p_window)
        photo_dj02_resize = photo_dj02.subsample(2, 2)
        label01 = Label(p_window, image = photo_dj02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_dj03():
        webbrowser.open("https://ch.caumc.or.kr/")
    def map_dj03():
        p_window = Tk()
        p_window.title('서울특별시 중앙대학교 병원'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 08:30~17:00,\n 토: 08:30~12:00, 일: 미운영\n 전화번호: 1800-1114\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "서울특별시 중앙대학교 병원 사이트로 이동", command = openurl_dj03)
        btn01.pack()
        photo_dj03 = PhotoImage(file = "learning/서울특별시 중앙대학교 병원.png", master = p_window)
        photo_dj03_resize = photo_dj03.subsample(2, 2)
        label01 = Label(p_window, image = photo_dj03_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_mp01():  #마포구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("https://www.mapo.go.kr/site/health/home")
    def map_mp01():  #마포구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('마포구보건소'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말: 09:00~13:00\n 전화번호: 02-3153-9037\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "마포구보건소 사이트로 이동", command = openurl_mp01)
        btn01.pack()
        photo_mp01 = PhotoImage(file = "learning/마포구보건소.png", master = p_window)
        photo_mp01_resize = photo_mp01.subsample(2, 2)
        label01 = Label(p_window, image = photo_mp01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_sdm01():  #서대문구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("http://www.sdm.go.kr/health/")
    def map_sdm01():  #서대문구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('서대문구보건소'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말: 09:00~13:00\n 전화번호: 02-330-1806\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "서대문구보건소 사이트로 이동", command = openurl_sdm01)
        btn01.pack()
        photo_sdm01 = PhotoImage(file = "learning/서대문구보건소.png", master = p_window)
        photo_sdm01_resize = photo_sdm01.subsample(2, 2)
        label01 = Label(p_window, image = photo_sdm01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_sdm02():
        webbrowser.open("https://sev.iseverance.com/index.asp")
    def map_sdm02():
        p_window = Tk()
        p_window.title('세브란스병원'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 08:00~15:30,\n 토: 09:00~12:00, 일: 미운영\n 전화번호: 1599-1004\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "세브란스병원 사이트로 이동", command = openurl_sdm02)
        btn01.pack()
        photo_sdm02 = PhotoImage(file = "learning/세브란스병원.png", master = p_window)
        photo_sdm02_resize = photo_sdm02.subsample(2, 2)
        label01 = Label(p_window, image = photo_sdm02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_j01():  #중구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("https://ch.caumc.or.kr/")
    def map_j01():  #중구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('서울중구보건소'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말: 09:00~16:00\n 전화번호: 1800-1114\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "서울중구보건소 사이트로 이동", command = openurl_j01)
        btn01.pack()
        photo_j01 = PhotoImage(file = "learning/서울중구보건소.png", master = p_window)
        photo_j01_resize = photo_j01.subsample(2, 2)
        label01 = Label(p_window, image = photo_j01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_j02():
        webbrowser.open("http://www.paik.ac.kr/seoul/main.asp")
    def map_j02():
        p_window = Tk()
        p_window.title('인제대학교 서울백병원'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 08:00~16:30,\n 토: 08:00~11:30, 일: 미운영\n 전화번호: 02-2270-0114\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "인제대학교 서울백병원 사이트로 이동", command = openurl_j02)
        btn01.pack()
        photo_j02 = PhotoImage(file = "learning/인제대학교 서울백병원.png", master = p_window)
        photo_j02_resize = photo_j02.subsample(2, 2)
        label01 = Label(p_window, image = photo_j02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_j03():
        webbrowser.open("https://www.nmc.or.kr/nmc/main/main.do")
    def map_j03():
        p_window = Tk()
        p_window.title('국립중앙의료원'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 08:30~17:30,\n 토: 08:30~12:30, 일: 미운영\n 전화번호: 02-2276-7114\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "국립중앙의료원 사이트로 이동", command = openurl_j03)
        btn01.pack()
        photo_j03 = PhotoImage(file = "learning/국립중앙의료원.png", master = p_window)
        photo_j03_resize = photo_j03.subsample(2, 2)
        label01 = Label(p_window, image = photo_j03_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_sc01():  #서초구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("https://www.seocho.go.kr/site/sh/main.do")
    def map_sc01():  #서초구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('서초구보건소'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~20:00,\n 주말:09:00~18:00\n 전화번호: 02-2155-8093\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "서초구보건소 사이트로 이동", command = openurl_sc01)
        btn01.pack()
        photo_sc01 = PhotoImage(file = "learning/서초구보건소.png", master = p_window)
        photo_sc01_resize = photo_sc01.subsample(2, 2)
        label01 = Label(p_window, image = photo_sc01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_sc02():
        webbrowser.open("https://www.cmcseoul.or.kr/page/main")
    def map_sc02():
        p_window = Tk()
        p_window.title('가톨릭대학교 서울성모병원'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 08:00~16:30,\n 토: 08:00~12:00, 일: 미운영\n 전화번호: 02-1588-1511\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "가톨릭대학교 서울성모병원 사이트로 이동", command = openurl_sc02)
        btn01.pack()
        photo_sc02 = PhotoImage(file = "learning/가톨릭대학교 서울성모병원.png", master = p_window)
        photo_sc02_resize = photo_sc02.subsample(2, 2)
        label01 = Label(p_window, image = photo_sc02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_sc03():
        webbrowser.open("https://childhosp.seoul.go.kr/")
    def map_sc03():
        p_window = Tk()
        p_window.title('서울특별시 어린이병원'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 10:00~15:00,\n 주말: 미운영\n 전화번호: 02-570-8000\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "서울특별시 어린이병원 사이트로 이동", command = openurl_sc03)
        btn01.pack()
        photo_sc03 = PhotoImage(file = "learning/서울특별시 어린이병원.png", master = p_window)
        photo_sc03_resize = photo_sc03.subsample(2, 2)
        label01 = Label(p_window, image = photo_sc03_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_sd01():  #성동구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("http://bogunso.sd.go.kr/bogunso.do")
    def map_sd01():  #성동구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('성동구보건소'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말:09:00~18:00\n 전화번호: 02-2286-7172\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "성동구보건소 사이트로 이동", command = openurl_sd01)
        btn01.pack()
        photo_sd01 = PhotoImage(file = "learning/성동구보건소.png", master = p_window)
        photo_sd01_resize = photo_sd01.subsample(2, 2)
        label01 = Label(p_window, image = photo_sd01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_sd02():
        webbrowser.open("https://www.hyumc.com/")
    def map_sd02():
        p_window = Tk()
        p_window.title('한양대학교병원'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~17:00,\n 토:09:00~12:00, 일: 미운영\n 전화번호: 02-2290-9880\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "한양대학교병원 사이트로 이동", command = openurl_sd02)
        btn01.pack()
        photo_sd02 = PhotoImage(file = "learning/한양대학교병원.png", master = p_window)
        photo_sd02_resize = photo_sd02.subsample(2, 2)
        label01 = Label(p_window, image = photo_sd02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_sd03():
        webbrowser.open("https://internationalclinic.modoo.at/")
    def map_sd03():
        p_window = Tk()
        p_window.title('성동군자의원'); p_window.geometry('700x700')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말: 미운영\n 전화번호: 02-499-7785\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "성동군자의원 사이트로 이동", command = openurl_sd03)
        btn01.pack()
        photo_sd03 = PhotoImage(file = "learning/성동군자의원.png", master = p_window)
        photo_sd03_resize = photo_sd03.subsample(2, 2)
        label01 = Label(p_window, image = photo_sd03_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_sb01():  #성북구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("http://www.sb.go.kr/bogunso/main.do")
    def map_sb01():  #성북구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('성북구보건소'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말:09:00~15:00\n 전화번호: 02-2241-5912\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "성북구보건소 사이트로 이동", command = openurl_sb01)
        btn01.pack()
        photo_sb01 = PhotoImage(file = "learning/성북구보건소.png", master = p_window)
        photo_sb01_resize = photo_sb01.subsample(2, 2)
        label01 = Label(p_window, image = photo_sb01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_sb02():
        webbrowser.open("http://anam.kumc.or.kr/main/index.do")
    def map_sb02():
        p_window = Tk()
        p_window.title('고려대학교의료원안암병원'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~16:00,\n 토:09:00~12:30, 일: 미운영\n 전화번호: 02-1577-0083\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "고려대학교의료원안암병원 사이트로 이동", command = openurl_sb02)
        btn01.pack()
        photo_sb02 = PhotoImage(file = "learning/고려대학교의료원안암병원.png", master = p_window)
        photo_sb02_resize = photo_sb02.subsample(2, 2)
        label01 = Label(p_window, image = photo_sb02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_sp01():  #송파구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("http://www.songpa.go.kr/403.html")
    def map_sp01():  #송파구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('송파구보건소'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말:09:00~16:00\n 전화번호: 02-2147-3479\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "송파구보건소 사이트로 이동", command = openurl_sp01)
        btn01.pack()
        photo_sp01 = PhotoImage(file = "learning/송파구보건소.png", master = p_window)
        photo_sp01_resize = photo_sp01.subsample(2, 2)
        label01 = Label(p_window, image = photo_sp01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_sp02():
        webbrowser.open("https://www.nph.go.kr/nph/main/main.do")
    def map_sp02():
        p_window = Tk()
        p_window.title('경찰병원'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 09:00~16:00,\n 주말:미운영\n 전화번호: 02-3400-1114\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "경찰병원 사이트로 이동", command = openurl_sp02)
        btn01.pack()
        photo_sp02 = PhotoImage(file = "learning/경찰병원.png", master = p_window)
        photo_sp02_resize = photo_sp02.subsample(2, 2)
        label01 = Label(p_window, image = photo_sp02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_yc01():  #양천구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("http://www.yangcheon.go.kr/health/health/main.do")
    def map_yc01():  #양천구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('양천구보건소'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말:09:00~18:00\n 전화번호: 02-2620-3856\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "양천구보건소 사이트로 이동", command = openurl_yc01)
        btn01.pack()
        photo_yc01 = PhotoImage(file = "learning/양천구보건소.png", master = p_window)
        photo_yc01_resize = photo_yc01.subsample(2, 2)
        label01 = Label(p_window, image = photo_yc01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_yc02():
        webbrowser.open("https://mokdong.eumc.ac.kr/main.do")
    def map_yc02():
        p_window = Tk()
        p_window.title('이화여자대학교의과대학부속목동병원'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~16:30,\n 주말: 미운영\n 전화번호: 02-1666-5000\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "이화여자대학교의과대학부속목동병원 사이트로 이동", command = openurl_yc02)
        btn01.pack()
        photo_yc02 = PhotoImage(file = "learning/이화여자대학교의과대학부속목동병원.png", master = p_window)
        photo_yc02_resize = photo_yc02.subsample(2, 2)
        label01 = Label(p_window, image = photo_yc02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_yc03():
        webbrowser.open("https://www.seoulsnh.or.kr/index.asp")
    def map_yc03():
        p_window = Tk()
        p_window.title('서울특별시 서남병원'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~21:00,\n 주말: 09:00~21:00\n 전화번호: 1566-6688\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "서울특별시 서남병원 사이트로 이동", command = openurl_yc03)
        btn01.pack()
        photo_yc03 = PhotoImage(file = "learning/서울특별시 서남병원.png", master = p_window)
        photo_yc03_resize = photo_yc03.subsample(2, 2)
        label01 = Label(p_window, image = photo_yc03_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_yc04():
        webbrowser.open("http://www.hih.or.kr/")
    def map_yc04():
        p_window = Tk()
        p_window.title('홍익병원'); p_window.geometry('700x700')
        msg = Label(p_window, text = '평일: 09:00~17:00,\n 토: 09:00~13:00, 일: 미운영\n 전화번호: 02-2693-5555\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "홍익병원 사이트로 이동", command = openurl_yc04)
        btn01.pack()
        photo_yc04 = PhotoImage(file = "learning/홍익병원.png", master = p_window)
        photo_yc04_resize = photo_yc04.subsample(2, 2)
        label01 = Label(p_window, image = photo_yc04_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_ydp01():  #영등포구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("https://www.ydp.go.kr/health/main.do")
    def map_ydp01():  #영등포구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('영등포구보건소'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말:09:00~18:00\n 전화번호: 02-2670-4953\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "영등포구보건소 사이트로 이동", command = openurl_ydp01)
        btn01.pack()
        photo_ydp01 = PhotoImage(file = "learning/영등포구보건소.png", master = p_window)
        photo_ydp01_resize = photo_ydp01.subsample(2, 2)
        label01 = Label(p_window, image = photo_ydp01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_ydp02():
        webbrowser.open("https://kangnam.hallym.or.kr/index.asp")
    def map_ydp02():
        p_window = Tk()
        p_window.title('한림대학교 강남성심병원'); p_window.geometry('1000x800')
        msg = Label(p_window, text = '평일: 08:30~16:30,\n 토:08:30~11:30, 일: 미운영\n 전화번호: 1577-5587\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "한림대학교 강남성심병원 사이트로 이동", command = openurl_ydp02)
        btn01.pack()
        photo_ydp02 = PhotoImage(file = "learning/한림대학교 강남성심병원.png", master = p_window)
        photo_ydp02_resize = photo_ydp02.subsample(2, 2)
        label01 = Label(p_window, image = photo_ydp02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_ydp03():
        webbrowser.open("http://www.sungae.co.kr/intro/index.do")
    def map_ydp03():
        p_window = Tk()
        p_window.title('의료법인 성애병원'); p_window.geometry('700x700')
        msg = Label(p_window, text = '평일: 09:00~17:00,\n 주말:미운영\n 전화번호: 02-840-7115\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "의료법인 성애병원 사이트로 이동", command = openurl_ydp03)
        btn01.pack()
        photo_ydp03 = PhotoImage(file = "learning/의료법인 성애병원.png", master = p_window)
        photo_ydp03_resize = photo_ydp03.subsample(2, 2)
        label01 = Label(p_window, image = photo_ydp03_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_ydp04():
        webbrowser.open("https://www.cmcsungmo.or.kr/page/main")
    def map_ydp04():
        p_window = Tk()
        p_window.title('가톨릭대학교 여의도성모병원'); p_window.geometry('700x700')
        msg = Label(p_window, text = '평일: 08:30~16:30,\n 주말:미운영\n 전화번호: 1661-7575\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "가톨릭대학교 여의도성모병원 사이트로 이동", command = openurl_ydp04)
        btn01.pack()
        photo_ydp04 = PhotoImage(file = "learning/가톨릭대학교 여의도성모병원.png", master = p_window)
        photo_ydp04_resize = photo_ydp04.subsample(2, 2)
        label01 = Label(p_window, image = photo_ydp04_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_ys01():  #용산구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("http://www.yongsan.go.kr/site/ha/index.jsp")
    def map_ys01():  #용산구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('용산구보건소'); p_window.geometry('700x700')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말:09:00~13:00\n 전화번호: 02-2199-6300\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "용산구보건소 사이트로 이동", command = openurl_ys01)
        btn01.pack()
        photo_ys01 = PhotoImage(file = "learning/용산구보건소.png", master = p_window)
        photo_ys01_resize = photo_ys01.subsample(2, 2)
        label01 = Label(p_window, image = photo_ys01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_ys02():
        webbrowser.open("https://www.schmc.ac.kr/seoul/index.do")
    def map_ys02():
        p_window = Tk()
        p_window.title('순천향대학교 서울병원'); p_window.geometry('900x600')
        msg = Label(p_window, text = '평일: 08:30~17:00,\n 토: 08:30~12:00, 일: 미운영\n 전화번호: 02-709-9114\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "순천향대학교 서울병원 사이트로 이동", command = openurl_ys02)
        btn01.pack()
        photo_ys02 = PhotoImage(file = "learning/순천향대학교 서울병원.png", master = p_window)
        photo_ys02_resize = photo_ys02.subsample(2, 2)
        label01 = Label(p_window, image = photo_ys02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_ep01():  #은평구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("https://health.ep.go.kr/CmsWeb/viewPage.req?idx=PG0000003588")
    def map_ep01():  #은평구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('은평구보건소'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~18:00\n, 주말:09:00~13:00\n 전화번호: 02-351-8114\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "은평구보건소 사이트로 이동", command = openurl_ep01)
        btn01.pack()
        photo_ep01 = PhotoImage(file = "learning/은평구보건소.png", master = p_window)
        photo_ep01_resize = photo_ep01.subsample(2, 2)
        label01 = Label(p_window, image = photo_ep01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_ep02():
        webbrowser.open("https://www.cmcep.or.kr/page/main")
    def map_ep02():
        p_window = Tk()
        p_window.title('은평성모병원'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 08:30~16:30\n, 주말:미운영\n 전화번호: 1811-7755\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "은평성모병원 사이트로 이동", command = openurl_ep02)
        btn01.pack()
        photo_ep02 = PhotoImage(file = "learning/은평성모병원.png", master = p_window)
        photo_ep02_resize = photo_ep02.subsample(2, 2)
        label01 = Label(p_window, image = photo_ep02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_ep03():
        webbrowser.open("https://sbhosp.seoul.go.kr/")
    def map_ep03():
        p_window = Tk()
        p_window.title('서울특별시 서북병원'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 09:00~18:00\n, 토:09:00~12:00, 일: 미운영\n 전화번호: 02-3156-3022\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "서울특별시 서북병원 사이트로 이동", command = openurl_ep03)
        btn01.pack()
        photo_ep03 = PhotoImage(file = "learning/서울특별시 서북병원.png", master = p_window)
        photo_ep03_resize = photo_ep03.subsample(2, 2)
        label01 = Label(p_window, image = photo_ep03_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_ep04():
        webbrowser.open("https://ephosp.seoul.go.kr/")
    def map_ep04():
        p_window = Tk()
        p_window.title('서울특별시 은평병원'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 10:00~17:00,\n 주말:미운영\n 전화번호: 02-300-8060\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "서울특별시 은평병원 사이트로 이동", command = openurl_ep04)
        btn01.pack()
        photo_ep04 = PhotoImage(file = "learning/서울특별시 은평병원.png", master = p_window)
        photo_ep04_resize = photo_ep04.subsample(2, 2)
        label01 = Label(p_window, image = photo_ep04_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_ep05():
        webbrowser.open("http://www.cgss.co.kr/")
    def map_ep05():
        p_window = Tk()
        p_window.title('청구성심병원'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 00:00~24:00,\n 주말:00:00~24:00\n 전화번호: 02-383-0129\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "청구성심병원 사이트로 이동", command = openurl_ep05)
        btn01.pack()
        photo_ep05 = PhotoImage(file = "learning/청구성심병원.png", master = p_window)
        photo_ep05_resize = photo_ep05.subsample(2, 2)
        label01 = Label(p_window, image = photo_ep05_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_jn01():  #종로구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("https://www.jongno.go.kr/healthMain.do")
    def map_jn01():  #종로구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('종로구보건소'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말:09:00~16:00\n 전화번호: 02-2148-3557\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "종로구보건소 사이트로 이동", command = openurl_jn01)
        btn01.pack()
        photo_jn01 = PhotoImage(file = "learning/종로구보건소.png", master = p_window)
        photo_jn01_resize = photo_jn01.subsample(2, 2)
        label01 = Label(p_window, image = photo_jn01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_jn02():
        webbrowser.open("https://www.kbsmc.co.kr/index.jsp")
    def map_jn02():
        p_window = Tk()
        p_window.title('강북삼성병원'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 07:00~17:30,\n 토: 07:30~12:00, 일: 미운영\n 전화번호: 02-2001-1896\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "강북삼성병원 사이트로 이동", command = openurl_jn02)
        btn01.pack()
        photo_jn02 = PhotoImage(file = "learning/강북삼성병원.png", master = p_window)
        photo_jn02_resize = photo_jn02.subsample(2, 2)
        label01 = Label(p_window, image = photo_jn02_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_jn03():
        webbrowser.open("https://www.kbsmc.co.kr/index.jsp")
    def map_jn03():
        p_window = Tk()
        p_window.title('서울적십자병원'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~17:00,\n 주말: 미운영\n 전화번호: 02-2002-8650\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "서울적십자병원 사이트로 이동", command = openurl_jn03)
        btn01.pack()
        photo_jn03 = PhotoImage(file = "learning/서울적십자병원.png", master = p_window)
        photo_jn03_resize = photo_jn03.subsample(2, 2)
        label01 = Label(p_window, image = photo_jn03_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_jr01():  #중랑구 진료소 홈페이지로 이동시키기 위한 함수 정의
        webbrowser.open("https://www.jungnang.go.kr/health/main.do")
    def map_jr01():  #중랑구 진료소에 대한 정보 제공을 위한 함수 정의
        p_window = Tk()
        p_window.title('중랑구보건소'); p_window.geometry('600x600')
        msg = Label(p_window, text = '평일: 09:00~18:00,\n 주말:09:00~15:00\n 전화번호: 02-2094-0800\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "중랑구보건소 사이트로 이동", command = openurl_jr01)
        btn01.pack()
        photo_jr01 = PhotoImage(file = "learning/중랑구보건소.png", master = p_window)
        photo_jr01_resize = photo_jr01.subsample(2, 2)
        label01 = Label(p_window, image = photo_jr01_resize)
        label01.pack()
        p_window.mainloop()

    def openurl_jr02():
        webbrowser.open("https://www.seoulmc.or.kr/site/kr/index.jsp")
    def map_jr02():
        p_window = Tk()
        p_window.title('서울의료원'); p_window.geometry('500x500')
        msg = Label(p_window, text = '평일: 09:00~22:00,\n 주말:09:00~22:00\n 전화번호: 02-2276-8333\n',\
            bg = 'white', fg = 'black', width=50, height=10, anchor = CENTER)
        msg.pack()
        btn01 = Button(p_window,text = "서울의료원 사이트로 이동", command = openurl_jr02)
        btn01.pack()
        photo_jr02 = PhotoImage(file = "learning/서울의료원.png", master = p_window)
        photo_jr02_resize = photo_jr02.subsample(2, 2)
        label01 = Label(p_window, image = photo_jr02_resize)
        label01.pack()
        p_window.mainloop()

    def destroy_last_button():  #사용자가 새로운 거주지를 입력했을 때 이전 거주지를 반영한 버튼을 없애고 새로운 거주지 정보를 반영하기 위한 함수 정의
        global button01; global button02; global button03; global button04; global button05  #button01~button05 전역변수 선언 
        button01.destroy()  #이전 button01 파괴
        button02.destroy()  #이전 button02 파괴
        button03.destroy()  #이전 button03 파괴
        button04.destroy()  #이전 button04 파괴
        button05.destroy()  #이전 button05 파괴
    
    def hospital():  #hospital 함수 정의
        address = e1.get() #입력창 안의 문자열 반환해서 address라는 변수에 저장
        global button01; global button02; global button03; global button04; global button05  #button01~button05 전역변수 선언    
        if "강남" in address:  #사용자가 입력한 주소에 '강남'이라는 단어가 포함되어 있을 경우
            destroy_last_button()  #이전에 입력한 정보를 반영한 버튼 파괴 함수 호출
            button01 = Button(window, text = '강남구보건소', command = map_gn01)  #강남구보건소 버튼 생성, 정보 관련 함수 호출
            button01.grid(row=2,column=1)  #버튼 위치 지정
            
            button02 = Button(window, text = '삼성서울병원', command = map_gn02)  #삼성서울병원 버튼 생성, 정보 관련 함수 호출
            button02.grid(row=2,column=2)  #버튼 위치 지정
            
            button03 = Button(window, text = '강남세브란스병원', command = map_gn03)  #강남세브란스병원 버튼 생성, 정보 관련 함수 호출
            button03.grid(row=2,column=3)  #버튼 위치 지정
            
        elif "강동" in address:  #사용자가 입력한 주소에 '강동'이라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '강동구보건소', command = map_gd01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '중앙보훈병원', command = map_gd02)
            button02.grid(row=2,column=2)
            
            button03 = Button(window, text = '강동경희대병원', command = map_gd03)
            button03.grid(row=2,column=3)      

            button04 = Button(window, text = '강동성심병원', command = map_gd04)
            button04.grid(row=2,column=4)
            

        elif "강북" in address:  #사용자가 입력한 주소에 '강북'이라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '강북구보건소', command = map_gb01)
            button01.grid(row=2,column=1)
            
        elif "강서" in address:  #사용자가 입력한 주소에 '강서'라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '강서구보건소', command = map_gs01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '이화여자대학교 서울병원', command = map_gs02)
            button02.grid(row=2,column=2)

        elif "관악" in address:  #사용자가 입력한 주소에 '관악'이라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '관악구보건소', command = map_ga01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '에이치플러스양지병원', command = map_gs02)
            button02.grid(row=2,column=2)
        
        elif "광진" in address:  #사용자가 입력한 주소에 '광진'이라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '광진구보건소', command = map_gj01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '건국대학교병원', command = map_gj02)
            button02.grid(row=2,column=2)

        elif "구로" in address:  #사용자가 입력한 주소에 '구로'라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '구로구보건소', command = map_gr01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '고대구로병원', command = map_gr02)
            button02.grid(row=2,column=2)
            
            button03 = Button(window, text = '구로성심병원', command = map_gr03)
            button03.grid(row=2,column=3)      

        elif "금천" in address:  #사용자가 입력한 주소에 '금천'이라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '금천구보건소', command = map_gc01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '희명병원', command = map_gc02)
            button02.grid(row=2,column=2)

        elif "노원" in address:  #사용자가 입력한 주소에 '노원'이라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '노원구보건소', command = map_nw01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '노원을지대학교병원', command = map_nw02)
            button02.grid(row=2,column=2)
            
            button03 = Button(window, text = '상계백병원', command = map_nw03)
            button03.grid(row=2,column=3)      

        elif "도봉" in address:  #사용자가 입력한 주소에 '도봉'이라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '도봉구보건소', command = map_db01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '한일병원', command = map_db02)
            button02.grid(row=2,column=2)
        
        elif "동대문" in address:  #사용자가 입력한 주소에 '동대문'이라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '동대문구보건소', command = map_ddm01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '삼육서울병원', command = map_ddm02)
            button02.grid(row=2,column=2)
            
            button03 = Button(window, text = '서울특별시 동부병원', command = map_ddm03)
            button03.grid(row=2,column=3)      

            button04 = Button(window, text = '서울성심병원', command = map_ddm04)
            button04.grid(row=2,column=4)

            button05 = Button(window, text = '경희의료원', command = map_ddm05)
            button05.grid(row=2,column=5)

        elif "동작" in address:  #사용자가 입력한 주소에 '동작'이라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '동작구보건소', command = map_dj01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '서울특별시 보라매병원', command = map_dj02)
            button02.grid(row=2,column=2)
            
            button03 = Button(window, text = '서울특별시 중앙대학교 병원', command = map_dj03)
            button03.grid(row=2,column=3)  

        elif "마포" in address:  #사용자가 입력한 주소에 '마포'라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '마포구보건소', command = map_mp01)
            button01.grid(row=2,column=1)

        elif "서대문" in address:  #사용자가 입력한 주소에 '서대문'이라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '서대문구보건소', command = map_sdm01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '세브란스병원', command = map_sdm02)
            button02.grid(row=2,column=2)
        
        elif "중구" in address:  #사용자가 입력한 주소에 '중구'라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '서울중구보건소', command = map_j01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '인제대학교 서울백병원', command = map_j02)
            button02.grid(row=2,column=2)
            
            button03 = Button(window, text = '국립중앙의료원', command = map_j03)
            button03.grid(row=2,column=3)

        elif "서초" in address:  #사용자가 입력한 주소에 '서초'라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '서초구보건소', command = map_sc01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '가톨릭대학교 서울성모병원', command = map_sc02)
            button02.grid(row=2,column=2)
            
            button03 = Button(window, text = '서울특별시 어린이병원', command = map_sc03)
            button03.grid(row=2,column=3)            

        elif "성동" in address:  #사용자가 입력한 주소에 '성동'이라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '성동구보건소', command = map_sd01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '한양대학교병원', command = map_sd02)
            button02.grid(row=2,column=2)
            
            button03 = Button(window, text = '성동군자의원', command = map_sd03)
            button03.grid(row=2,column=3)      

        elif "성북" in address:  #사용자가 입력한 주소에 '성북'이라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '성북구보건소', command = map_sb01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '고려대학교의료원안암병원', command = map_sb02)
            button02.grid(row=2,column=2)

        elif "송파" in address:  #사용자가 입력한 주소에 '송파'라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '송파구보건소', command = map_sp01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '경찰병원', command = map_sp02)
            button02.grid(row=2,column=2)

        elif "양천" in address:  #사용자가 입력한 주소에 '양천'이라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '양천구보건소', command = map_yc01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '이화여자대학교의과대학부속목동병원', command = map_yc02)
            button02.grid(row=2,column=2)
            
            button03 = Button(window, text = '서울특별시 서남병원', command = map_yc03)
            button03.grid(row=2,column=3)

            button04 = Button(window, text = '홍익병원', command = map_yc04)
            button04.grid(row=2,column=4)

        elif "영등포" in address:  #사용자가 입력한 주소에 '영등포'라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '영등포구보건소', command = map_ydp01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '한림대학교 강남성심병원', command = map_ydp02)
            button02.grid(row=2,column=2)
            
            button03 = Button(window, text = '의료법인 성애병원', command = map_ydp03)
            button03.grid(row=2,column=3)

            button04 = Button(window, text = '가톨릭대학교 여의도성모병원', command = map_ydp04)
            button04.grid(row=2,column=4)
                
        elif "용산" in address:  #사용자가 입력한 주소에 '용산'이라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '용산구보건소', command = map_ys01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '순천향대학교 서울병원', command = map_ys02)
            button02.grid(row=2,column=2)

        elif "은평" in address:  #사용자가 입력한 주소에 '은평'이라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '은평구보건소', command = map_ep01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '은평성모병원', command = map_ep02)
            button02.grid(row=2,column=2)
            
            button03 = Button(window, text = '서울특별시 서북병원', command = map_ep03)
            button03.grid(row=2,column=3)

            button04 = Button(window, text = '서울특별시 은평병원', command = map_ep04)
            button04.grid(row=2,column=4)

            button05 = Button(window, text = '청구성심병원', command = map_ep05)
            button05.grid(row=2,column=5)  

        elif "종로" in address:  #사용자가 입력한 주소에 '종로'라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '종로구보건소', command = map_jn01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '강북삼성병원', command = map_jn02)
            button02.grid(row=2,column=2)
            
            button03 = Button(window, text = '서울적십자병원', command = map_jn03)
            button03.grid(row=2,column=3)    

        elif "중랑" in address:  #사용자가 입력한 주소에 '중랑'이라는 단어가 포함되어 있을 경우
            destroy_last_button()
            button01 = Button(window, text = '중랑구보건소', command = map_jr01)
            button01.grid(row=2,column=1)
            
            button02 = Button(window, text = '서울의료원', command = map_jr02)
            button02.grid(row=2,column=2)
        

    window = Tk()  #새로운 윈도우 창 생성
    window.geometry("600x200")  #윈도우 창 크기 지정
    window.title("선별 진료소 추천")  #윈도우 창 제목

    living_place = Label(window, text="거주지", width=10).place(x=30,y=50)  #라벨 설정 후 living_place(거주지 입력받기 위해) 라는 변수에 대입
    e1= Entry(window, width =20)  #입력창 생성 후 e1이라는 변수에 저장
    e1.place(x=100,y=50)  #입력창 위치 지정
 
    global button01; global button02; global button03; global button04; global button05  #button01~button05 전역변수 선언
    button01=Button(window)
    button02=Button(window)
    button03=Button(window)
    button04=Button(window)
    button05=Button(window)

    input_button= Button(window, text = "입력",command=hospital)  #입력 버튼 생성, 사용자가 거주지 입력 후 버튼 누르면 hospital 함수로 이동
    input_button.place(x=50, y=100)  #입력 버튼 위치 지정
 
    

    window.mainloop()  #등록한 이벤트 실행



def common_id(): #코로나19 관련 상식 함수 설정
    window = Tk() #새로운 윈도우 창 개설
    window.title('코로나19 관련 상식') #윈도우 창의 이름 설정
    window.geometry('540x780') #윈도우 창의 크기 설정

    #라벨로 안내문구 설정(해당 윈도우 창, 문구)하고 출력 입력
    label=tkinter.Label(window, text='코로나19 관련 상식입니다.\n 해당 상식을 클릭하시면 추가 설명이 나옵니다.')
    label.pack()
    
    #관련 상식 1번~20번에 각각 해당하는 함수를 실행했을 때 뜨는 상식내용을 메세지박스로 설정
    def info1():
        tkinter.messagebox.showinfo('상세설명','who는 "건강식이 균에 대항하는 능력을 키우는 것은 사실"이라고 밝혔으나 마늘이 코로나19를 막아준다는 직접적인 증거는 없다. 오히려 과다복용은 위험할 수 있다.')
    def info2():
        tkinter.messagebox.showinfo('상세설명','기적의 미네랄은 지난해 미국 식품의 약국(FDA)으로부터 "마시면 건강에 위험이 된다"는 경고를 받은 물질이다. FDA는 "이 물질이 안전하거나, 치료에 도움이 된다는 어떠한 연구도 없다"고 설명했다.')   
    def info3():
        tkinter.messagebox.showinfo('상세설명','소독제에 쓰이는 알코올은 함량이 60~70% 이상 되어야 한다. 그러나 아무리 강한 술, 즉 보드카라고 하더라도 알코올 도수는 40도에 불과하다. 소주도 마찬가지다. 소주 제조용 알코올 원료(함량 90%)로는 소독제를 만들 수 있지만 16~18도의 소주로는 불가능하다. 오히려 첨가된 당분 때문에 소주가 묻는 손에서 세균이 번식할 수 있다.')
    def info4():
        tkinter.messagebox.showinfo('상세설명','이는 섬유에 붙어있는 바이러스를 씻어내는 행위로 예방에 효과적이다.')
    def info5():
        tkinter.messagebox.showinfo('상세설명','자외선은 피부자극을 유발할 수 있기 때문에 손이나 다른 피부소독을 위해 사용해서는 안된다. 물론 코로나 바이러스 살균도 불가능하다.')
    def info6():
        tkinter.messagebox.showinfo('상세설명','항생제는 오직 세균에만 작용하며 바이러스에 작용하지 않는다.')
    def info7():
        tkinter.messagebox.showinfo('상세설명','코로나19 유무를 떠나 마스크 착용은 호흡기 성장 관련 문제를 일으킬 수 있다.')
    def info8():
        tkinter.messagebox.showinfo('상세설명','잠복기는 [비말 등을 통해 바이러스가 몸속으로 침입해 가벼운 증상이 나타나는 단계]를 칭한다.')
    def info9():
        tkinter.messagebox.showinfo('상세설명','구강청결제는 입속의 미생물들을 죽이고 입냄새를 제거할 수는 있으나 바이러스를 섬멸할 정도의 힘을 가지고 있지는 않다.')
    def info10():
        tkinter.messagebox.showinfo('상세설명','WHO에 따르면, 목욕이나 샤워를 할 때 물 온도에 상관없이 체온은 36.5도~37도 사이에서 머무르며 뜨거운 물로 샤워나 목욕을 한다고 해서 코로나 바이러스를 차단할 수는 없다.')
    def info11():
        tkinter.messagebox.showinfo('상세설명','WHO는 “이제까지 모기에 의해 코로나19에 감염됐다는 정보나 증거나 단 한 건도 없다”며 “코로나19는 감염된 사람의 기침이나 재채기에서 나오는 비말 즉, 날아 흩어지거나 튀어 오르는 분비물 방울이나 침이나 코에서 나오는 분비물 방울을 통해 주로 전염되는 호흡기 바이러스”라고 밝혔다.')
    def info12():
        tkinter.messagebox.showinfo('상세설명','생리 식염수나 소금물 등으로 코를 씻으면 일반 감기에서 회복하는 데 도움을 줄 수는 있으나 코로나바이러스와는 관련이 없다.')
    def info13():
        tkinter.messagebox.showinfo('상세설명','코 지지대(철사심)가 위쪽, 주름 방향 아래인 면이 앞쪽, 끈 부착면이 앞쪽이다.')
    def info14():
        tkinter.messagebox.showinfo('상세설명','코로나19 바이러스가 몸 밖으로 나올 경우 평균 2-3시간의 생존율을 갖기 때문에 장기간 생존하는 것은 불가능하다.')
    def info15():
        tkinter.messagebox.showinfo('상세설명','모든 연령대의 사람들이 동일한 가능성으로 코로나19에 감염되고 있다.')
    def info16():
        tkinter.messagebox.showinfo('상세설명','식약처 인증 보건 마스크 중에서 [KF80]이상을 착용하는 것이 적절하며, [KF90] 이상은 우수하지만 숨이 차서 오래 착용하기 어렵기 때문에 이를 굳이 고집할 필요는 없다. 또, 필터가 따로 없는 일반 마스크를 착용해도 마스크를 착용하지 않는 것보다는 예방 효과가 훨씬 좋다.')
    def info17():
        tkinter.messagebox.showinfo('상세설명','바이러스를 함유한 상대방의 침이 눈에 튀어 점막에 접촉한다면 감염이 이뤄질 수 있다. 그러나 바이러스는 주로 호흡기 감염으로 전파되기 때문에 눈을 통한 감염 가능성은 상대적으로 낮다. 고로, 상대 침이 튀는 것을 막기 위해 안경을 쓰는 정도까지의 노력은 필요가 없다.')
    def info18():
        tkinter.messagebox.showinfo('상세설명','코로나19의 가장 흔한 임상적 특징은 발열로 많이 알려져 있다. 하지만 실제로 코로나19 초기 증상으로 발열이 나타난 경우는 3분의1에도 미치지 않는다. 이보다는 기침 증상이 40.8%로 가장 빈번하다.')
    def info19():
        tkinter.messagebox.showinfo('상세설명','적절하게 염소 소독이 된 풀장 물에서 바이러스는 사멸한다.')
    def info20():
        tkinter.messagebox.showinfo('상세설명','바이러스가 입을 통해 들어가는 것은 맞지만 호흡기를 통해 유입된다. 고로, 물을 마시는 것과 바이러스 제거는 관련이 없다.')

    #관련 상식 20개 각각에 해당하는 버튼 설정(해당 윈도우 창, 크기, 문구, 실행할 명령(위에서 설정한 해당하는 함수들), 버튼 실행 시 나타나는 색)
    button_ci1 = tkinter.Button(window, width=50,height=2, text='마늘 섭취는 코로나19를 막아주지 못한다.',command=info1,activebackground='orange') 
    button_ci2 = tkinter.Button(window, width=50,height=2,text='기적의 미네랄(miracle minerals)는 코로나 19 대응식품이 아니다.',command=info2,activebackground='orange')
    button_ci3 = tkinter.Button(window, width=50,height=2,text='보드카로 손소독제를 만드는 것은 불가능하다.',command=info3,activebackground='orange')
    button_ci4 = tkinter.Button(window, width=50,height=2,text='따뜻한 물수건등으로 침구류를 닦아주는 것은 코로나19 예방에 효과적이다.',command=info4,activebackground='orange')
    button_ci5 = tkinter.Button(window, width=50,height=2,text='자외선 램프는 코로나19를 죽일 수 없다.',command=info5,activebackground='orange')
    button_ci6 = tkinter.Button(window, width=50,height=2,text='항생제는 코로나 19를 예방하거나 치료하는데 효과적이 않다.',command=info6,activebackground='orange')
    button_ci7 = tkinter.Button(window, width=50,height=2,text='24개월 미만의 아기들은 마스크를 착용하지 않는 것이 좋다.',command=info7,activebackground='orange')
    button_ci8 = tkinter.Button(window, width=50,height=2,text='코로나 잠복기에는 가벼운 증상이 나타난다.',command=info8,activebackground='orange')
    button_ci9 = tkinter.Button(window, width=50,height=2,text='구강 청결제로 입안을 자주 헹구는 행이는 코로나19에 예방되지 않는다.',command=info9,activebackground='orange')
    button_ci10 = tkinter.Button(window, width=50,height=2,text='뜨거운 물로 샤워한다고 코로나19를 막을 수는 없다.',command=info10,activebackground='orange')
    button_ci11= tkinter.Button(window, width=50,height=2,text='모기에 물리는 것과 코로나 19 감염은 관련이 없다.',command=info11,activebackground='orange')
    button_ci12 = tkinter.Button(window, width=50,height=2,text='소금물로 코를 세척한다고 코로나바이러스를 막을 수 있는 것은 아니다.',command=info12,activebackground='orange')
    button_ci13 = tkinter.Button(window, width=50,height=2,text='올바른 마스크 착용법',command=info13,activebackground='orange')
    button_ci14 = tkinter.Button(window, width=50,height=2,text='해외 택배물은 코로나 바이러스 감염의 원인이 아니다.',command=info14,activebackground='orange')
    button_ci15 = tkinter.Button(window, width=50,height=2,text='노령자나 어린이들이 코로나19에 더 취약하다는 사실은 틀리다.',command=info15,activebackground='orange')
    button_ci16 = tkinter.Button(window, width=50,height=2,text='마스크는 KF90 이상만이 코로나 예방에 효과적인 것이 아니다.',command=info16,activebackground='orange')
    button_ci17 = tkinter.Button(window, width=50,height=2,text='코로나는 눈 점막을 통해서도 감염될 수 있다.',command=info17,activebackground='orange')
    button_ci18 = tkinter.Button(window, width=50,height=2,text='코로나 감염 후 증상은 발열보다 기침이 많다.',command=info18,activebackground='orange')
    button_ci19 = tkinter.Button(window, width=50,height=2,text='수영장에서는 코로나가 감염되지 않는다.',command=info19,activebackground='orange')
    button_ci20 = tkinter.Button(window, width=50,height=2,text='15분마다 물을 마신다고  코로나 19가 씻겨나가지는 않는다.',command=info20,activebackground='orange')

    #설정한 버튼들 화면에 출력 설정
    button_ci1.pack()
    button_ci2.pack()
    button_ci3.pack()
    button_ci4.pack()
    button_ci5.pack()
    button_ci6.pack()
    button_ci7.pack()
    button_ci8.pack()
    button_ci9.pack()
    button_ci10.pack()
    button_ci11.pack()
    button_ci12.pack()
    button_ci13.pack()
    button_ci14.pack()
    button_ci15.pack()
    button_ci16.pack()
    button_ci17.pack()
    button_ci18.pack()
    button_ci19.pack()
    button_ci20.pack()

    window.mainloop() #등록된 코로나19 관련 상식 윈도우 창 실행
my_score = 0

def real_quiz(): #코로나19 관련 상식 퀴즈 함수 설정
    from tkinter import messagebox # tkinter messagebox 모듈 사용 선언
    
    def destroy_menu(): #입력 버튼 파괴 함수 설정
        inputbutton01.destroy() #inputbutton01 파괴
    def destroy_last_button_q(): #버튼 파괴 함수 설정
        buttonA.destroy() #이전 버튼 A 파괴
        buttonB.destroy() #이전 버튼 B 파괴
        buttonC.destroy() #이전 버튼 C 파괴
        buttonD.destroy() #이전 버튼 D 파괴
        buttonE.destroy() #이전 버튼 E 파괴
        
    def clear(): #화면 지우기 함수 설정
        mylist= window.place_slaves() #place로 정의된 것들을 mylist로 입력
        for a in mylist:
            a.destroy() #mylist에 입력 된 것 파괴

    def quiz(): #퀴즈 시작 함수 설정
        destroy_last_button_q() #버튼 파괴 함수 실행
        destroy_menu() #입력 버튼 파괴 함수 실행
        clear() #화면 지우기 함수 실행
        buttonA= Button(window,text= '1번문제',width=20,command=quiz1) #1번문제로 이동시켜줄 버튼 출력
        buttonA.place(x=40,y=50) #버튼 위치 설정
    def quiz1(): #1번 문제 함수 설정
        destroy_last_button_q() #버튼 파괴 함수 실행
        destroy_menu() #입력 버튼 파괴 함수 실행
        clear() #화면 지우기 함수 실행
        labels=Label(window,text="1. 마늘 섭취는 코로나19를 막아준다.", width=70).place(x=1,y=100)#1번 문제 라벨로 출력 
        buttonA= Button(window, text= 'O',width=10,command= right1) # O버튼 출력 및 클릭시 right1 함수로 이동
        buttonA.place(x=150,y=150)
        buttonB= Button(window, text='X', width=10, command= wrong1) # X버튼 출력 및 클릭시 wrong1 함수로 이동
        buttonB.place(x=250,y=150)
    def right1(): # O를 선택했을 시 함수 설정
        destroy_last_button_q() #버튼 파괴 함수 실행
        destroy_menu() #입력 버튼 파괴 함수 실행
        clear() #화면 지우기 함수 실행
        labels=Label(window,text="틀렸습니다.",width=50).place(x=40,y=50) #정답이 아니기때문에 틀렸다고 Label을 통해 출력
        buttonA= Button(window, text='다음 문제로', width=30,command=quiz2) # 다음 문제로 버튼 출력 및 클릭시 2번 문제로 이동
        buttonA.place(x=150,y=150) #버튼 위치 설정
    def wrong1(): # X를 선택했을 시 함수 설정
        destroy_last_button_q() #버튼 파괴 함수 실행
        destroy_menu() #입력 버튼 파괴 함수 실행
        clear() #화면 지우기 함수 실행
        global my_score # my_score 전역변수 설정
        my_score+=1 #정답이기때문에 (기존 성적점수) +1 
        labels=Label(window,text="정답입니다.",width=50).place(x=40,y=50)#정답이라고 Label을 통해 출력
        buttonA= Button(window, text='다음 문제로', width=30,command=quiz2) # 다음 문제로 버튼 출력 및 클릭시 2번 문제로 이동
        buttonA.place(x=150,y=150) #버튼 위치 설정
        
    def quiz2(): #2번 문제함수 설정
        destroy_last_button_q()
        destroy_menu()
        clear()
        labels=Label(window,text="2. 보드카로 손소독제를 만들 수 있다.", width=70).place(x=1,y=100)
        buttonA= Button(window, text= 'O',width=10,command= right2)
        buttonA.place(x=150,y=150)
        buttonB= Button(window, text='X', width=10, command= wrong2)
        buttonB.place(x=250,y=150)
    def right2():
        destroy_last_button_q()
        destroy_menu()
        clear()
        labels=Label(window,text="틀렸습니다.",width=50).place(x=40,y=50)
        buttonA= Button(window, text='다음 문제로', width=30,command=quiz3)
        buttonA.place(x=150,y=150)
    def wrong2():
        destroy_last_button_q()
        destroy_menu()
        clear()
        global my_score
        my_score+=1
        labels=Label(window,text="정답입니다.",width=50).place(x=40,y=50)
        buttonA= Button(window, text='다음 문제로', width=30,command=quiz3)
        buttonA.place(x=150,y=150)
    def quiz3(): #3번 문제 함수 설정
        destroy_last_button_q()
        destroy_menu()
        clear()
        labels=Label(window,text="3.따뜻한 물수건으로 침구류를 닦는 것은 코로나19 예방에 효과적이다.", width=55).place(x=1,y=100)
        buttonA= Button(window, text= 'O',width=10,command= right3)
        buttonA.place(x=150,y=150)
        buttonB= Button(window, text='X', width=10, command= wrong3)
        buttonB.place(x=250,y=150)
    def right3():
        destroy_last_button_q()
        destroy_menu()
        clear()
        global my_score
        my_score+=1
        labels=Label(window,text="정답입니다.",width=50).place(x=40,y=50)
        buttonA= Button(window, text='다음 문제로', width=30,command=quiz4)
        buttonA.place(x=150,y=150)
    def wrong3():
        destroy_last_button_q()
        destroy_menu()
        clear()
        labels=Label(window,text="틀렸습니다.",width=50).place(x=40,y=50)
        buttonA= Button(window, text='다음 문제로', width=30,command=quiz4)
        buttonA.place(x=150,y=150)
    def quiz4(): #4번 문제 함수 설정
        destroy_last_button_q()
        destroy_menu()
        clear()
        labels=Label(window,text="4.자외선 램프는 코로나 19를 죽일 수 있다.", width=55).place(x=1,y=100)
        buttonA= Button(window, text= 'O',width=10,command= right4)
        buttonA.place(x=150,y=150)
        buttonB= Button(window, text='X', width=10, command= wrong4)
        buttonB.place(x=250,y=150)
    def right4(): 
        destroy_last_button_q()
        destroy_menu()
        clear()
        labels=Label(window,text="틀렸습니다.",width=50).place(x=40,y=50)
        buttonA= Button(window, text='다음 문제로', width=30,command=quiz5)
        buttonA.place(x=150,y=150)
    def wrong4():
        destroy_last_button_q()
        destroy_menu()
        clear()
        global my_score
        my_score+=1
        labels=Label(window,text="정답입니다.",width=50).place(x=40,y=50)
        buttonA= Button(window, text='다음 문제로', width=30,command=quiz5)
        buttonA.place(x=150,y=150)
    def quiz5(): #5번 문제 함수 설정
        destroy_last_button_q()
        destroy_menu()
        clear()
        labels=Label(window,text="5.24개월 미만의 아기들은 마스크를 착용하지 않는 것이 더 좋다", width=55).place(x=1,y=100)
        buttonA= Button(window, text= 'O',width=10,command= right5)
        buttonA.place(x=150,y=150)
        buttonB= Button(window, text='X', width=10, command= wrong5)
        buttonB.place(x=250,y=150)
    def right5():
        destroy_last_button_q()
        destroy_menu()
        clear()
        global my_score
        my_score+=1
        
        labels=Label(window,text="정답입니다.",width=50).place(x=40,y=50)
        buttonA= Button(window, text='다음 문제로', width=30,command=quiz6)
        buttonA.place(x=150,y=150)
    def wrong5():
        destroy_last_button_q()
        destroy_menu()
        clear()
        labels=Label(window,text="틀렸습니다.",width=50).place(x=40,y=50)
        buttonA= Button(window, text='다음 문제로', width=30,command=quiz6)
        buttonA.place(x=150,y=150)
    def quiz6(): #6번 문제 함수 설정
        destroy_last_button_q()
        destroy_menu()
        clear()
        labels=Label(window,text="6.항생제는 코로나 19를 예방하거나 치료하는데 효과적이다.", width=55).place(x=1,y=100)
        buttonA= Button(window, text= 'O',width=10,command= right6)
        buttonA.place(x=150,y=150)
        buttonB= Button(window, text='X', width=10, command= wrong6)
        buttonB.place(x=250,y=150)
    def right6():
        destroy_last_button_q()
        destroy_menu()
        clear()
        labels=Label(window,text="틀렸습니다.",width=50).place(x=40,y=50)
        buttonA= Button(window, text='다음 문제로', width=30,command=quiz7)
        buttonA.place(x=150,y=150)
    def wrong6():
        destroy_last_button_q()
        destroy_menu()
        clear()
        global my_score
        my_score+=1
        labels=Label(window,text="정답입니다.",width=50).place(x=40,y=50)
        buttonA= Button(window, text='다음 문제로', width=30,command=quiz7)
        buttonA.place(x=150,y=150)
    def quiz7(): #7번 문제 함수 설정
        destroy_last_button_q()
        destroy_menu()
        clear()
        labels=Label(window,text="7.코로나 잠복기에는 가벼운 증상이 나타난다", width=55).place(x=1,y=100)
        buttonA= Button(window, text= 'O',width=10,command= right7)
        buttonA.place(x=150,y=150)
        buttonB= Button(window, text='X', width=10, command= wrong7)
        buttonB.place(x=250,y=150)
    def right7():
        destroy_last_button_q()
        destroy_menu()
        clear()
        global my_score
        my_score+=1
        labels=Label(window,text="정답입니다.",width=50).place(x=40,y=50)
        buttonA= Button(window, text='퀴즈 종료', width=30,command=ending) # '퀴즈 종료' 버튼 출력 및 클릭시 결과창으로 연결
        buttonA.place(x=150,y=150)
    def wrong7():
        destroy_last_button_q()
        destroy_menu()
        clear()
        labels=Label(window,text="틀렸습니다.",width=50).place(x=40,y=50)
        buttonA= Button(window, text='퀴즈 종료', width=30,command=ending) # '퀴즈 종료' 버튼 출력 및 클릭시 결과창으로 연결
        buttonA.place(x=150,y=150)
    def ending(): #결과창 함수 설정
        destroy_last_button_q()
        destroy_menu()
        clear()
        name = Label(window,text="사용자의 이름을 입력하세요",width=50).place(x=40,y=50) #사용자 이름을 확인하기 위한 라벨 출력
        global e2 #전역변수 e2 설정
        e2 = Entry(window,width=20) #Entry e2 출력
        e2.place(x=150,y=70) #e2 위치 설정
        inputbutton01= Button(window, text = "결과확인", command=final_score) # 결과확인 버튼 출력 및 성적 함수로 연결
        inputbutton01.place(x=250, y=250)# 버튼 위치 설정
    def final_score(): #성적 함수
        global user_name #전역변수 user_name 설정
        user_name = e2.get() # user_name는 e2에서 얻은 것이라고 정의
        final_label=Label(window,text=("%s님의 점수는 %s점입니다." %(user_name, my_score)),width=30).place(x=100,y=150) #성적 최종 결과 출력
    window = Tk() #새로운 윈도우 창 개설
    window.geometry("400x300") # 윈도우 창 크기 설정
    window.title("코로나19 상식퀴즈") #윈도우 창 이름 설정

    labels= Label(window, text="**코로나19 상식 퀴즈입니다.**", width=50).place(x=40,y=70) # label을 통해 문구 출력


    inputbutton01= Button(window, text = "시작", command=quiz) #시작 버튼 출력 및 퀴즈 함수로 연결
    inputbutton01.place(x=350, y=250) #버튼 위치 설정
    buttonA= Button(window)
    buttonB= Button(window)
    buttonC= Button(window)
    buttonD= Button(window)
    buttonE= Button(window)
    labels= Label(window)
    window.mainloop()
  
    
    
#항목별 4개의 버튼 설정(해당 윈도우 창, 크기, 문구, 실행할 명령(해당하는 항목 함수), 버튼 실행 시 나타나는 색)
btn1 = Button(window1, width=40,height=3,text='자가 진단',command=selfcheck,activebackground='orange')
btn2 = Button(window1, width=40,height=3,text='선별 진료소 위치',command=place,activebackground='orange')
btn3 = Button(window1, width=40,height=3,text='코로나 관련 상식', command=common_id,activebackground='orange')
btn4 = Button(window1, width=40,height=3,text='코로나 관련 상식 퀴즈',command=real_quiz,activebackground='orange')



#설정한 항목별 버튼들 화면에 출력 설정
btn1.pack()

btn2.pack()

btn3.pack()

btn4.pack()

window1.mainloop() #코로나19 종합앱 윈도우 창 실행
