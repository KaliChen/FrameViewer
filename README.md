# FrameViewer
顯示視訊串流基本要素為使用cv2.VideoCapture()打開視訊源，然後在視訊源打開的狀況下以frame讀出並用cv2.imshow()一張張的播放出來，以下為例，

    def init_notebookpage_3(self):
        self.notebookpage_3_tab = tk.Frame(self.notebook2 )
        self.notebook2.add(self.notebookpage_3_tab, text="notebookpage_3")

在面板上我做一個tk.Button按鍵，title為'StreamOpenCV'，command設為self.StreamOpenCV，按下就可執行功能。

        StreamOpenCVbutton = tk.Button(self.notebookpage_3_tab,
                                       font=('Courier', 7),
                                       text = "StreamOpenCV",
                                       command = self.StreamOpenCV)
        StreamOpenCVbutton.pack(side = tk.TOP, expand=tk.YES, fill=tk.BOTH)
        
![https://ithelp.ithome.com.tw/upload/images/20200914/20119608X1Jel7pIeN.png](https://ithelp.ithome.com.tw/upload/images/20200914/20119608X1Jel7pIeN.png)

定義一個播放stream的函式StreamOpenCV，指定self.cap的視訊來源為cv2.VideoCapture(0)

    def StreamOpenCV(self, event = None):
        self.cap = cv2.VideoCapture(0)

當self.cap.isOpened()的前提下，以frame儲存self.cap.read()來的資料，cv2.imshow播放frame   

        while(self.cap.isOpened()):
             ret, frame = self.cap.read()
             cv2.imshow("StreamOpenCV", frame)

if c == 27: break表示等待按'Esc'跳出；

             c = cv2.waitKey(1)
             if c == 27: break
        self.cap.release()
        cv2.destroyAllWindows()
![https://ithelp.ithome.com.tw/upload/images/20200914/20119608GPzXGs2pqv.png](https://ithelp.ithome.com.tw/upload/images/20200914/20119608GPzXGs2pqv.png)

在使用tkinter介面播放video時，如果只用cv2.imshow()，呼叫出來的視訊視窗是浮在原本主控GUI上的，顯得點不夠美觀簡潔，於是我又找到另一種播放影像的方法，利用label元件來播放視訊，因為labe元件是定義在主GUI原件上的，只要控制label原件上的轉換就好了

要另外引入pillow的元件: 

    from PIL import Image, ImageTk

這邊是介面Layout:

    def init_notebookpage_3(self):
        self.notebookpage_3_tab = tk.Frame(self.notebook2 )
        self.notebook2.add(self.notebookpage_3_tab, text="notebookpage_3")
        StreamOpenCVbutton = tk.Button(self.notebookpage_3_tab ,                                                                
                                       font=('Courier', 7),
                                       text = "StreamOpenCV",
                                       command = self.StreamOpenCV)
        StreamOpenCVbutton.pack(side = tk.TOP, expand=tk.YES, fill=tk.BOTH)
        
        Showframebutton = tk.Button(self.notebookpage_3_tab , font=('Courier', 7),
                                    text = "ShowFrame",command = self.show_frame)
        Showframebutton.pack(side = tk.TOP, expand=tk.YES, fill=tk.BOTH)
        self.stream = tk.Label(self.notebookpage_3_tab, width=100, height=100)
        self.stream.pack(side=tk.LEFT, expand=tk.NO, fill = tk.BOTH)

我定義一個show_frame函式

    def show_frame(self, event = None):
        self.cap = cv2.VideoCapture(0)
        _, frame = self.cap.read()
        frame = cv2.resize(frame,(100,100))
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        self.stream.imgtk = imgtk
        self.stream.configure(image=imgtk)
        self.stream.after(15, self.show_frame)
        
![https://ithelp.ithome.com.tw/upload/images/20200914/20119608QCb02bDW8H.png](https://ithelp.ithome.com.tw/upload/images/20200914/20119608QCb02bDW8H.png)

這邊是一個視訊撥放器範例
![https://ithelp.ithome.com.tw/upload/images/20200925/20119608qXZpXyDDrn.jpg](https://ithelp.ithome.com.tw/upload/images/20200925/20119608qXZpXyDDrn.jpg)
  
在這邊我先簡單定義一個視訊撥放面板，

    def init_frameviewer(self):

定義常和寬

        self.LABEL_WIDTH = 540
        self.LABEL_HEIGHT = 330

影片來源控制面板

        self.StreamCtrlPanel = tk.LabelFrame(self.parent ,
                                             text="Stream Control Panel",
                                             font=('Courier', 9))
        self.StreamCtrlPanel.pack(side=tk.TOP, expand=tk.NO, fill = tk.X)
 
 選擇local camera的單選紐
 
        self.selStr = tk.StringVar()
        fromlocalCam = tk.Radiobutton(self.StreamCtrlPanel, 
                                      text = "Local Camera",
                                      font=('Courier', 9), 
                                      variable = self.selStr, 
                                      value = "From Local Camera",
                                      command = self.init_VideoCapture)
        fromlocalCam.pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)
 
輸入其他裝置來源網址的變數
 
        self.DEV_VIDEO_NAME= tk.StringVar()
        self.DEV_VIDEO_NAME.set("視訊網址")
        
選擇其他裝置視訊來源的單選紐
        
        fromdevCam = tk.Radiobutton(self.StreamCtrlPanel,
                                    text = "Device Camera",
                                    font=('Courier', 9), 
                                    variable = self.selStr,
                                    value = "From Device Camera", 
                                    command = self.init_VideoCapture)
        fromdevCam.pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)
        
輸入其他裝置來源的輸入方塊        
        
        self.DeviceVideoPath= tk.Entry(self.StreamCtrlPanel , 
                                       textvariable=self.DEV_VIDEO_NAME, 
                                       width = 10)
        self.DeviceVideoPath.pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)        
        
選擇local端的視訊影片       
        
        fromlocalVideofile = tk.Radiobutton(self.StreamCtrlPanel, 
                                            text = "Local Video File",
                                            font=('Courier', 9), 
                                            variable = self.selStr,
                                            value = "From Local Video File", 
                                            command = self.load_video)
        fromlocalVideofile.pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)

輸入local端影片變數

        self.LOCAL_VIDEO_NAME = tk.StringVar()
        
輸入local端影片來源輸入方塊
        
        self.LocalVideoPath= tk.Entry(self.StreamCtrlPanel , 
                                      textvariable=self.LOCAL_VIDEO_NAME, 
                                      width = 10)
        self.LocalVideoPath.pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)
        
影片操作面板

        self.VideoCtrlPanel = tk.LabelFrame(self.parent  , 
                                            text="VideoControl Panel",
                                            font=('Courier', 9))
        self.VideoCtrlPanel.pack(side=tk.TOP, expand=tk.NO, fill = tk.X)

播放鍵

        showframebutton = tk.Button(self.VideoCtrlPanel, 
                                    text = "PLAY",
                                    font=('Courier', 9), 
                                    command = self.show_frame)
        showframebutton.pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)
        
停止鍵
        
        capreleabutton = tk.Button(self.VideoCtrlPanel, 
                                   text ="STOP",
                                   font=('Courier', 9),
                                   command = self.cap_release)
        capreleabutton.pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)

把影片分割成一張張frame的功能鍵

        split_framebutton = tk.Button(self.VideoCtrlPanel, 
                                      text ="Split",
                                      font=('Courier', 9), 
                                      command = self.split_frame)
        split_framebutton.pack(side=tk.LEFT, expand=tk.NO, fill = tk.X)

承載撥放影片的frame版面

        self.streamplay_tab = tk.Frame(self.parent)
        self.streamplay_tab.pack(side = tk.LEFT, expand=tk.YES, fill=tk.BOTH)

定義self.stream為承載影片的載體，使用物件label

        self.stream = tk.Label(self.streamplay_tab, 
                               width=self.LABEL_WIDTH, 
                               height=self.LABEL_HEIGHT)
        self.stream.pack(side=tk.LEFT, expand=tk.NO, fill = tk.BOTH)
       
撥放影片
 
     def show_frame(self, event = None):
        _, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        frame = cv2.resize(frame,(self.LABEL_WIDTH,self.LABEL_HEIGHT))
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        self.stream.imgtk = imgtk
        self.stream.configure(image=imgtk)
        self.stream.after(15, self.show_frame)

停止視訊
        
    def cap_release(self, event = None):
        self.cap.release()
        self.stream.configure(image=圖片檔路徑)

切分視訊成為frame

    def split_frame(self, event = None):
        if self.selStr.get() =="From Local Camera":
            self.cap = cv2.VideoCapture(0)
        elif self.selStr.get() =="From Local Video File":
            self.cap = cv2.VideoCapture(self.localvideoname)
        #調整預設影像大小，預設值很大，很吃效能 
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.LABEL_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.LABEL_HEIGHT)

        if not os.path.exists(os.getcwd()+"/split_frame"):
            os.mkdir("split_frame")
        while(self.cap.isOpened()): #當攝影機打開時，對每個frame進行偵測    
            T = int(100*time.time())
            #讀出frame資訊
            ret, frame = self.cap.read()
            #輸出到畫面
            cv2.imshow("Split frame", frame)
            cv2.imwrite('split_frame/'+str(T)+'.jpg', frame)
            #如果按下ESC键，就退出
            if cv2.waitKey(1) == 27: break
        #釋放記憶體
        self.cap.release()
        #關閉所有視窗
        cv2.destroyAllWindows() 

選擇視訊來源

    def init_VideoCapture(self, event = None):
        if self.selStr.get() =="From Local Camera":
            self.cap = cv2.VideoCapture(0)

        elif self.selStr.get() =="From Local Video File":
            self.cap = cv2.VideoCapture(self.localvideoname)
       
        elif self.selStr.get() =="From Device Camera":
            self.cap = cv2.VideoCapture(self.DEV_VIDEO_NAME.get())
 
以下是選取視訊來源程序上的差異:

![https://ithelp.ithome.com.tw/upload/images/20200927/201196086vEvVAVDbC.jpg](https://ithelp.ithome.com.tw/upload/images/20200927/201196086vEvVAVDbC.jpg)

打開資料夾載入視訊檔

    def load_video(self, event = None):
        self.localvideoname =  filedialog.askopenfilename(
                                          initialdir = "/",
                                          title = "Select file",
                                          filetypes = (("mp4 files","*.mp4*"),
                                                       ("all files","*.*")))
        self.LOCAL_VIDEO_NAME.set(self.localvideoname)
        self.init_VideoCapture()

在製作視訊工具時，我想在畫面上打映出時間戳記，在show_frame()內部可以利用下面的程式碼...

        # timestamp
        Time = time.time()
        # datetime 物件
        local_time = time.ctime(Time)
        # write the time information on the frame
        cv2.putText(frame, str(local_time), (10, 10), 
                    1,
                    1, 
                    (255,255,255), 
                    1,
                    0)

![https://ithelp.ithome.com.tw/upload/images/20200926/201196086bURC64Ste.png](https://ithelp.ithome.com.tw/upload/images/20200926/201196086bURC64Ste.png)

![https://ithelp.ithome.com.tw/upload/images/20200926/20119608d8R7aP9PuY.jpg](https://ithelp.ithome.com.tw/upload/images/20200926/20119608d8R7aP9PuY.jpg)

    def init_FrameViewer(self):
        self.init_FrameViewer_tab = tk.Frame(self.notebook)
        self.init_FrameViewer_tab.pack(side = tk.LEFT, expand=tk.YES, fill=tk.BOTH)
        self.notebook.add(self.init_FrameViewer_tab, text="init_FrameViewer")
        self.FrameSwitch = tk.StringVar()

        fvfram1 = tk.Frame(self.init_FrameViewer_tab )
        fvfram1.grid(row =0, column = 0, sticky = tk.E+tk.W)
        self.fv1 = FV.FrameViewer(fvfram1)
        fvfram1_2 = tk.Frame(self.init_FrameViewer_tab )
        fvfram1_2.grid(row =1, column = 0, sticky = tk.E+tk.W)
        switch1 = tk.Radiobutton(fvfram1_2, 
                                 text = "Frame\n Switch 1",
                                 font=('Courier', 9),
                                 variable = self.FrameSwitch,
                                 value = "Frame Switch 1",
                                 command = self.frameswitch)
        switch1.pack(side=tk.RIGHT, expand=tk.NO, fill = tk.X)

        fvfram2 = tk.Frame(self.init_FrameViewer_tab )
        fvfram2.grid(row =2, column = 0, sticky = tk.E+tk.W)
        self.fv2 = FV.FrameViewer(fvfram2)
        fvfram2_2 = tk.Frame(self.init_FrameViewer_tab )
        fvfram2_2.grid(row =3, column = 0, sticky = tk.E+tk.W)
        switch2 = tk.Radiobutton(fvfram2_2,
                                 text = "Frame\n Switch 2",
                                 font=('Courier', 9), 
                                 variable = self.FrameSwitch, 
                                 value = "Frame Switch 2", 
                                 command = self.frameswitch)
        switch2.pack(side=tk.RIGHT, expand=tk.NO, fill = tk.X)

        fvfram3 = tk.Frame(self.init_FrameViewer_tab )
        fvfram3.grid(row =0, column = 1, sticky = tk.E+tk.W)
        self.fv3 = FV.FrameViewer(fvfram3)
        fvfram3_2 = tk.Frame(self.init_FrameViewer_tab )
        fvfram3_2.grid(row =1, column = 1, sticky = tk.E+tk.W)
        switch3 = tk.Radiobutton(fvfram3_2,
                                 text = "Frame\n Switch 3",
                                 font=('Courier', 9),
                                 variable = self.FrameSwitch,
                                 value = "Frame Switch 3",
                                 command = self.frameswitch)
        switch3.pack(side=tk.RIGHT, expand=tk.NO, fill = tk.X)
 
        fvfram4 = tk.Frame(self.init_FrameViewer_tab )
        fvfram4.grid(row =2, column = 1, sticky = tk.E+tk.W)
        self.fv4 = FV.FrameViewer(fvfram4)
        fvfram4_2 = tk.Frame(self.init_FrameViewer_tab )
        fvfram4_2.grid(row =3, column = 1, sticky = tk.E+tk.W)
        switch4 = tk.Radiobutton(fvfram4_2,
                                 text = "Frame\n Switch 4",
                                 font=('Courier', 9),
                                 variable = self.FrameSwitch,
                                 value = "Frame Switch 4",
                                 command = self.frameswitch)
        switch4.pack(side=tk.RIGHT, expand=tk.NO, fill = tk.X)

切換頻道用的switch
    
    def frameswitch(self):
        if self.FrameSwitch.get() =="Frame Switch 1": 
            StreamFile = self.fv1.cap#self.iv1.image_paths[self.iv1.image_idx]
        elif self.FrameSwitch.get() =="Frame Switch 2":
            StreamFile = self.fv2.cap#self.iv2.image_paths[self.iv2.image_idx]
        elif self.FrameSwitch.get() =="Frame Switch 3":
            StreamFile = self.fv3.cap#self.iv3.image_paths[self.iv3.image_idx]
        elif self.FrameSwitch.get() =="Frame Switch 4":
            StreamFile = self.fv4.cap#self.iv4.image_paths[self.iv4.image_idx]

