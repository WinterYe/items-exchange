from tkinter import*
import tkinter.messagebox
from tkinter.ttk import*
from tkinter.scrolledtext import ScrolledText
# 用字典存储usernames里面的信息，其中用户信息{用户名:[密码,地址,手机号,0/1]},管理员{用户名:[密码,地址,手机号,2]}
f = open('usernames.txt','r',encoding='utf-8')
fi = f.readlines()
dic={}
listindic=[]
for lst in fi:
    d = str(lst).strip('').split(",")
    listindic.append(d[1])
    listindic.append(d[2])
    listindic.append(d[3])
    listindic.append(d[4])
    dic[d[0]]=listindic
    listindic=[]
    
f.close()

class First:
    def __init__(self,master):
        # 定义储存entry中内容的变量
        self.name = StringVar(master,value='')
        self.pswd = StringVar(master,value='')
        # 设计窗口组件
        master.title('你帮我助')
        master['height'] = 300
        master['width'] = 600
        self.labelName = Label(master,text='用户名:',font=('华文新魏',14),justify=RIGHT,anchor='e',width=80)
        self.labelName.place(x=0,y=40,width=200,height=30)
        self.labelPswd = Label(master,text='密码:',font=('华文新魏',14),justify=RIGHT,anchor='e',width=80)
        self.labelPswd.place(x=0,y=70,width=200,height=30)

        self.entryName = Entry(master,width=80,textvariable=self.name)
        self.entryName.place(x=220,y=40,width=200,height=30)
        self.entryCode = Entry(master,show='*',width=80,textvariable=self.pswd)
        self.entryCode.place(x=220,y=70,width=200,height=30)

        self.buttonLogin = Button(master,text='登录',command=self.login)
        self.buttonLogin.place(x=270,y=135,width=80,height=30)

        self.buttonRegister = Button(master,text='注册',command=self.register)
        self.buttonRegister.place(x=170,y=135,width=80,height=30)

        self.buttonCancel = Button(master,text='取消',command=self.cancel)
        self.buttonCancel.place(x=370,y=135,width=80,height=30)

    # 设计登录函数，要有管理员2登录成功，普通用户1登录成功，普通用户信息待批准0，登录失败四个结果
    def login(self):
        self.name_1 = self.entryName.get()
        self.pswd_1 = self.entryCode.get()
        if self.name_1=='' or self.pswd_1=='':
            tkinter.messagebox.showwarning('提示','用户名或密码不得为空')
        if self.name_1 in dic and self.pswd_1 == dic[self.name_1][0] and dic[self.name_1][3]=='0\n':
            tkinter.messagebox.showwarning('提示','您的注册信息正在审核中')
        if self.name_1 in dic and self.pswd_1 == dic[self.name_1][0] and dic[self.name_1][3]=='1\n':
            app1 = General()
        if self.name_1 in dic and self.pswd_1 == dic[self.name_1][0] and dic[self.name_1][3]=='2\n':
            app2 = Administer()
        if self.name_1 !='' and self.pswd_1 !='' and (self.name_1 not in dic or self.pswd_1 != dic[self.name_1][0]):
            answer = tkinter.messagebox.askquestion('提示','用户名或密码错误，是否注册？')
            if answer=='yes':
                app3 = Register()
            else:
                self.cancel()
    def register(self):
        app3 = Register()
    
    def cancel(self):
        self.name.set('')
        self.pswd.set('')


class Register:
    def __init__(self):
        # 先将原有的登录窗口隐藏
        root.withdraw()
        # 程序类独立创建“注册”根窗口
        self.root_reg = Tk()
        self.root_reg.title('你帮我助-新用户注册')
        self.root_reg['height'] = 300
        self.root_reg['width'] = 600
        # 定义存储entry中内容的变量
        self.newname = StringVar(self.root_reg,value='')
        self.newpswd = StringVar(self.root_reg,value='')
        self.newaddress = StringVar(self.root_reg,value='')
        self.newtelenum = StringVar(self.root_reg,value='')
        # 设计窗口组件
        labelnewname = Label(self.root_reg,text='设置用户名:',font=('华文新魏',14),justify=RIGHT,anchor='e',width=80)
        labelnewname.place(x=40,y=40,width=200,height=30)
        labelnewpswd = Label(self.root_reg,text='设置新密码:',font=('华文新魏',14),justify=RIGHT,anchor='e',width=80)
        labelnewpswd.place(x=40,y=70,width=200,height=30)
        labelnewaddress = Label(self.root_reg,text='请输入您的地址:',font=('华文新魏',14),justify=RIGHT,anchor='e',width=80)
        labelnewaddress.place(x=40,y=100,width=200,height=30)
        labelnewtelenum = Label(self.root_reg,text='请输入您的电话号码:',font=('华文新魏',14),justify=RIGHT,anchor='e',width=80)
        labelnewtelenum.place(x=40,y=130,width=200,height=30)

        self.entrynewname = Entry(self.root_reg,width=80,textvariable=self.newname)
        self.entrynewname.place(x=260,y=40,width=200,height=30)
        self.entrynewpswd = Entry(self.root_reg,show='*',width=80,textvariable=self.newpswd)
        self.entrynewpswd.place(x=260,y=70,width=200,height=30)
        self.entrynewaddress = Entry(self.root_reg,width=80,textvariable=self.newaddress)
        self.entrynewaddress.place(x=260,y=100,width=200,height=30)
        self.entrynewtelenum = Entry(self.root_reg,width=80,textvariable=self.newtelenum)
        self.entrynewtelenum.place(x=260,y=130,width=200,height=30)

        btn1 = Button(self.root_reg,text='确定',command=self.writein)
        btn1.place(x=170,y=180,width=80,height=30)
        btn2 = Button(self.root_reg,text='清空',command=self.cancel)
        btn2.place(x=270,y=180,width=80,height=30)
        btn3 = Button(self.root_reg,text='返回',command=self.back)
        btn3.place(x=370,y=180,width=80,height=30)
        
        self.root_reg.mainloop()

    def writein(self):
        newname1 = self.entrynewname.get()
        newpswd1 = self.entrynewpswd.get()
        newaddress1 = self.entrynewaddress.get()
        newtelenum1 = self.entrynewtelenum.get()
        # 将注册信息写入usernames.txt并注明是待审核用户'0'
        if newname1 == '' or newpswd1 =='' or newaddress1 == '' or newtelenum1 == '':
            tkinter.messagebox.showwarning('提示','请检查您的信息是否填写完全')
        if newname1 in dic:
            tkinter.messagebox.showwarning('提示','用户已存在，请勿重复注册')
            self.cancel()
        if newname1 != '' and newpswd1 !='' and newaddress1 != '' and newtelenum1 != '' and newname1 not in dic:
            f1 = open('usernames.txt','a',encoding='utf-8')
            f1.write(newname1)
            f1.write(',')
            f1.write(newpswd1)
            f1.write(',')
            f1.write(newaddress1)
            f1.write(',')
            f1.write(newtelenum1)
            f1.write(',')
            f1.write('0')
            f1.write('\n')
            f1.close
            tkinter.messagebox.showwarning('提示','提交信息成功，请等待管理员审核')
            self.back()
    def cancel(self):
        self.newname.set('')
        self.newpswd.set('')
        self.newaddress.set('')
        self.newtelenum.set('')
    def back(self):
        self.root_reg.destroy()
        root.deiconify()

class Administer:
    def __init__(self):
        root.withdraw()
        # 进入管理员界面
        self.adm_root = Tk()
        self.adm_root.title('欢迎来到“你帮我助”平台--管理员')
        self.adm_root['height'] = 300
        self.adm_root['width'] = 600
        # 设置一个功能选择菜单
        self.admmenu = Menu(self.adm_root)
        self.adm_root.config(menu=self.admmenu)
        self.menu_type = Menu(self.admmenu)

        self.admmenu.add_cascade(label='选项', menu=self.menu_type)
        self.menu_type.add_command(label='设置新的物品类型', command=self.newtype)
        self.menu_type.add_command(label='修改物品类型', command=self.edittype)
        self.menu_type.add_separator()
        self.menu_type.add_command(label='退出',command=self.cancel)

        self.menu_ratify = Menu(self.admmenu)
        self.admmenu.add_cascade(label='审核', menu=self.menu_ratify)
        self.menu_ratify.add_command(label='审核新用户', command=self.newmember)
        # 设置一个frame，方便清除组件
        self.f = Frame(self.adm_root,width=600,height=300)
        self.f.pack()
        # 读取category文件中的物品类型并存在列表中
        f10 = open('category+attribute.txt','r',encoding='utf-8')
        fi10 = f10.readlines()
        self.typelstold = []
        for lst in fi10:
            d = str(lst).strip('').split(",")
            self.typelstold.append(d[0])   
        f10.close()
        self.adm_root.mainloop()
    # 添加新的类型
    def newtype(self):
        # 将之前的组件清除
        for widget in self.f.winfo_children():
            widget.destroy()
        # 创建新的组件
        newname_label = Label(self.f,text ='请输入新的物品类型：', font=('华文新魏',14),justify=LEFT,anchor='e',width=400)
        newname_label.place(x=0,y=50,width=230,height=30)
        self.newname1 = StringVar(self.adm_root,value='')
        newname_entry = Entry(self.f,width=80,textvariable=self.newname1)
        newname_entry.place(x=230,y=50,width=230,height=30)
        newtypebtn1 = Button(self.f,text ='确认',command=self.newtxt)
        newtypebtn1.place(x=480,y=50,width=80,height=30)
        newname_label2 = Label(self.f,text ='请定义新类型的属性，若有多个属性，用英文逗号分隔，填写完成请按创建按钮：', font=('华文新魏',14),justify=LEFT,anchor='e',width=450)
        newname_label2.place(x=50,y=90,width=520,height=30)
        self.newname2 = StringVar(self.adm_root,value='')
        newname_entry2 = Entry(self.f,width=80,textvariable=self.newname2)
        newname_entry2.place(x=80,y=120,width=450,height=30)
        newtypebtn2 = Button(self.f,text ='确认',command=self.newattribute)
        newtypebtn2.place(x=260,y=150,width=100,height=30)


    def newtxt(self):
        self.newname1str = self.newname1.get()
        if self.newname1str == '' : tkinter.messagebox.showinfo('提示','请填写类型！')
        if self.newname1str in self.typelstold: 
            tkinter.messagebox.showinfo('提示','类型已存在，请勿重复创建')
            self.newname1 = ''
        else:
            full_path = self.newname1str +'.txt'
            file = open(full_path,'w')
            file.close()
            self.newname1 = ''
            tkinter.messagebox.showinfo('提示','接下来请填写属性')
    def newattribute(self):
        newname2str = self.newname2.get()
        if newname2str == '': tkinter.messagebox.showinfo('提示','请填写属性！')
        else:
            f9 = open('category+attribute.txt','a',encoding='utf-8')
            f9.write(self.newname1str)
            f9.write(',')
            f9.write(newname2str)
            f9.write('\n')
            f9.close()
            tkinter.messagebox.showinfo('提示','物品类型创建成功！')
            self.newname2 = ''

    def edittype(self):
        # 将之前的组件清除
        for widget in self.f.winfo_children():
            widget.destroy()
        # 为了解决修改物品类型之后物品的私有属性的改变问题，需要先保存物品的公共属性，然后需要管理员重新填入私有属性，从原文档删除，加入新文档
        # 先输入本来的类型
        edit_label1 = Label(self.f,text = '请选择原本的属性：',font=('华文新魏',14),justify=LEFT,anchor='e',width=400)
        edit_label1.place(x=0,y=0,width=230,height=30)
        # 读取category文件中的物品类型并存在列表中
        f4 = open('category+attribute.txt','r',encoding='utf-8')
        fi4 = f4.readlines()
        self.typelst = []
        for lst in fi4:
            d = str(lst).strip('').split(",")
            self.typelst.append(d[0])   
        f4.close()
        # 创建用户选择组合框-选择类型
        self.var = StringVar(self.adm_root,value='')
        type_comb = Combobox(self.f,textvariable=self.var,values=self.typelst)
        type_comb.place(x=230,y=0,width=230,height=30)
        # 按钮1
        edittypebtn1 = Button(self.f,text ='确认',command=self.searchedit)
        edittypebtn1.place(x=480,y=0,width=100,height=30)
        

    def searchedit(self):
        # 先找到该物品，保存所有信息，重写该文档
        self.varstr = self.var.get()
        path = self.varstr + '.txt'
        f11 = open(path,'r',encoding='utf-8')
        fi11 = f11.readlines()
 
        listindic=[]
        for lst in fi11:
            d = str(lst).strip('').split("/")
            listindic.append(d[0])
            
        f11.close()
        # 创建组合框，方便选择物品
        edit_label2 = Label(self.f,text = '请选择物品名称：',font=('华文新魏',14),justify=LEFT,anchor='e',width=400)
        edit_label2.place(x=0,y=30,width=230,height=30)
        self.var2 = StringVar(self.adm_root,value='')
        type_comb2 = Combobox(self.f,textvariable=self.var2,values=listindic)
        type_comb2.place(x=230,y=30,width=230,height=30)

        # 按钮2
        editbtn2 = Button(self.f,text = '确认',command = self.prientry)
        editbtn2.place(x=480,y=30,width=100,height=30)

    def prientry(self):
        # 读取category文件中的物品私有类型个数
        f4 = open('category+attribute.txt','r',encoding='utf-8')
        fi4 = f4.readlines()
        typelst = []
        for lst in fi4:
            d = str(lst).strip('').split(",")
            if self.varstr in d:
                typelst.extend(d)   
        f4.close()
        typenum = len(typelst)-1
       
        self.var2str = self.var2.get()
        path2 = self.varstr + '.txt'
        f12 = open(path2,'r',encoding='utf-8')
        fi12 = f12.readlines()
        self.edit =[]
        # 先保存待改变物品的公有信息
        for lst in fi12:
            d = str(lst).split('/')
            if  d[0]== self.var2str:
                self.edit.append(d[0])
                self.edit.append(d[1])
                self.edit.append(d[2])
                self.edit.append(d[3])
                self.edit.append(d[4])
        f12.close()
       
        # 重新写入除这个物品之外的其他物品
        f13 = open(path2,'r',encoding='utf-8')
        fi13 = f13.readlines()
        totaldic = {}
        totallst =[]
        for lst in fi13:
            i = 0
            d = str(lst).split('/')
            if d[0] != self.var2str:
                while i <= 3 + typenum :
                    totallst.append(d[i+1])
                    i=i+1

                totaldic[d[0]] =  totallst
        f13.close()

        f14 = open(path2,'w',encoding='utf-8')
        for key in totaldic.keys():
            f14.write(key)
            f14.write('/')
            i = 0 
            while i < 3 + typenum:
                f14.write(totaldic[key][i])
                f14.write('/')
                i = i+1
            f14.write(totaldic[key][3+typenum])
        f14.close()

        # 处理待改变的物品
        # 选择需要改成的类型
        edit_label3 = Label(self.f,text = '请选择新的属性：',font=('华文新魏',14),justify=LEFT,anchor='e',width=400)
        edit_label3.place(x=0,y=60,width=230,height=30)

        # 创建用户选择组合框-选择类型
        self.var3 = StringVar(self.adm_root,value='')
        type_comb3 = Combobox(self.f,textvariable=self.var3,values=self.typelst)
        type_comb3.place(x=230,y=60,width=230,height=30)
        # 按钮3
        edittypebtn3 = Button(self.f,text ='确认',command=self.update)
        edittypebtn3.place(x=480,y=60,width=100,height=30)
        
    def update(self):
        # 确定新类型的私有属性
        self.var3str = self.var3.get()
        f14 = open('category+attribute.txt','r',encoding='utf-8')
        fi14 = f14.readlines()
        typelstnew = []
        for lst in fi14:
            d = str(lst).strip('').split(',')
            if d[0] == self.var3str:
                typelstnew.extend(d[1:])
        f14.close()
        i=0
        self.entry = []
        while i < len(typelstnew):
            prilabel = Label(self.f,text = typelstnew[i].strip('\n')+'：',font=('华文新魏',14),justify=LEFT,anchor='e',width=30)
            prilabel.place(x=130,y=60+30*(i+1),width=100,height=40)
            self.pri = StringVar(self.adm_root,value='')
            self.prientry = Entry(self.f,width=40,textvariable=self.pri)
            self.prientry.place(x=230,y=60+30*(i+1),width=200,height=30)
            i=i+1
            self.entry.append(self.pri)
        
        edittypebtn4 = Button(self.f,text ='确认',command=self.lastone)
        edittypebtn4.place(x=480,y=90,width=100,height=30)

    def lastone(self):
        # 将物品新的信息全部整合在self.edit列表里
        i =0
        while i< len(self.entry):
            self.edit.append(self.entry[i].get())
            i = i+1

        path3 = self.var3str + '.txt'
        f16 = open(path3,'a',encoding='utf-8')
        if '' in self.entry:
            tkinter.messagebox.showinfo('提示','请输入属性！')
        else:
            # 将列表写入文件
            t=0
            while t < 4 + len(self.entry)  :
                f16.write(self.edit[t])
                f16.write('/')
                t = t+1
            f16.write(self.edit[4+len(self.entry)])
            f16.write('\n')
            f16.close()

            # 写完提示
            tkinter.messagebox.showinfo('提示','物品类型更改成功！')



    # 退出系统
    def cancel(self):
        answer = tkinter.messagebox.askquestion('提示','是否退出程序？')
        if answer=='yes':
            self.adm_root.destroy()
        else:
            pass


    # 菜单栏中的审核新成员
    def newmember(self):
        # 先把frame中之前的组件清掉
        for widget in self.f.winfo_children():
            widget.destroy()
        newdic={}
        f = open('usernames.txt','r',encoding='utf-8')
        fi = f.readlines()
        listindic_1=[]
        for lst in fi:
            d = str(lst).strip('').split(",")
            if d[4] == '0\n':
                listindic_1.append(d[2])
                listindic_1.append(d[3])
                newdic[d[0]]=listindic_1
            listindic_1=[]
        f.close()
          
        newlst = newdic.items()
        self.Lstbox1 = Listbox(self.f)
        self.Lstbox1.place(width=300,height=300)
        for item in newlst:
            self.Lstbox1.insert(END, item)
        label1 = Label(self.f,text="请审核注册信息，\n(若同意通过请选中并按下方按钮)",font=('华文新魏',14),justify=LEFT,anchor='e',width=400)
        label1.place(x=350,y=10,width=215,height=50)
        self.btn1 = Button(self.f,text="通过",command = self.correct)
        self.btn1.place(x=410,y=100,width=80,height=30)
        if newdic == {}:
            tkinter.messagebox.showinfo('提示','暂无待审核用户')
            self.btn1['state'] = DISABLED  
        
    def correct(self):
        self.newone = self.Lstbox1.get(self.Lstbox1.curselection())
        newdic_1={}
        f2 = open('usernames.txt','r',encoding='utf-8')
        fi2 = f2.readlines()
        listindic_1=[]
        for lst in fi2:
            d = str(lst).strip('').split(",")
            for lst in fi:
                listindic_1.append(d[1])
                listindic_1.append(d[2])
                listindic_1.append(d[3])
                listindic_1.append(d[4])
                newdic_1[d[0]]=listindic_1
                listindic_1=[]
        print(newdic_1)
        f2.close()

        newdic_1[self.newone[0]][3] = '1\n'
        f3 = open('usernames.txt','w',encoding='utf-8')
        for key in newdic_1.keys():
            f3.write(key)
            f3.write(',')
            f3.write(newdic_1[key][0])
            f3.write(',')
            f3.write(newdic_1[key][1])
            f3.write(',')
            f3.write(newdic_1[key][2])
            f3.write(',')
            f3.write(newdic_1[key][3])
        f3.close()
        # 操作完成，跳出提示符
        tkinter.messagebox.showinfo('提示','操作成功！')
        # 删除已完成的项目
        self.Lstbox1.delete(self.Lstbox1.curselection())
        if self.Lstbox1.size() == 0:
            tkinter.messagebox.showinfo('提示','暂无待审核用户')
            self.btn1['state'] = DISABLED

       
class General:
    def __init__(self):
        # 将登录窗口destroy
        root.withdraw()
        # 进入普通正式用户使用界面
        self.general_root = Tk()
        self.general_root.title('欢迎来到“你帮我助”平台')
        self.general_root['height'] = 300
        self.general_root['width'] = 600
        # 添加菜单
        self.genmenu = Menu(self.general_root)
        self.general_root.config(menu=self.genmenu)
        self.menu_type = Menu(self.genmenu)

        self.genmenu.add_cascade(label='选项', menu=self.menu_type)
        self.menu_type.add_command(label='查找物品', command=self.search)
        self.menu_type.add_command(label='添加物品', command=self.add)
        self.menu_type.add_separator()
        self.menu_type.add_command(label='退出',command=self.cancel)

        # 设置一个frame，方便清除组件
        self.f2 = Frame(self.general_root,width=600,height=300)
        self.f2.pack()
        self.general_root.mainloop()

    
    # 定义查找函数
    def search(self):
        # 先将frame中之前的组件清除
        for widget in self.f2.winfo_children():
            widget.destroy()
        # 建立新的组件-用户先选择类型
        chooselabel = Label(self.f2,text='请选择物品类型：',font=('华文新魏',14),justify=LEFT,anchor='e',width=400)
        chooselabel.place(x=0,y=0,width=120,height=50)
        # 读取category文件中的物品类型并存在列表中
        f4 = open('category+attribute.txt','r',encoding='utf-8')
        fi4 = f4.readlines()
        typelst = []
        for lst in fi4:
            d = str(lst).strip('').split(",")
            typelst.append(d[0])   
        f4.close()
        # 创建用户选择组合框
        self.var = StringVar(self.general_root,value='')
        type_comb = Combobox(self.f2,textvariable=self.var,values=typelst)
        type_comb.place(x=0,y=40,width=200,height=30)

        # 创建提示用户输入关键字的label
        key_label = Label(self.f2,text='请输入物品关键词：',font=('华文新魏',14),justify=LEFT,anchor='w',width=400)
        key_label.place(x=250,y=10,width=200,height=30)
        # 创建用户输入关键字的entry
        self.searchkey = StringVar(self.general_root,value='')
        key_entry = Entry(self.f2,width=80,textvariable=self.searchkey)
        key_entry.place(x=250,y=40,width=200,height=30)
        # 创建按钮
        btn_search = Button(self.f2,text='查找',command =self.gototxt)
        btn_search.place(x=500,y=40,width=80,height=30)
        # 创建一个滚动文本框
        self.txt = ScrolledText(self.f2,font=('华文新魏',14),relief=SUNKEN)
        self.txt.place(x=180,y=100,width=300,height=200)
      

    def gototxt(self):
        self.txt.delete('1.0',END)
        self.varstr = self.var.get()
        self.searstr = self.searchkey.get()
        full_path = self.varstr +'.txt'
        f3 = open(full_path,'r',encoding='utf-8')
        fi3 = f3.readlines()
        self.objdic = {}
        lstinobj =[]
        for lst in fi3:
            d = str(lst).strip('').split("/")
            cnt = 0
            while cnt < len(d)-1:
                lstinobj.append(d[cnt+1])
                cnt = cnt + 1
            self.objdic[d[0]]= lstinobj
            lstinobj = []
        f3.close()
        self.pubilcinfo = ['物品名称：','物品说明：','所在地址：','联系人手机：','联系人邮箱：']
        # 查找物品特有信息,并存在列表attribute中
        f5 = open('category+attribute.txt','r',encoding='utf-8')
        fi5 = f5.readlines()
        self.attribute = []
        for lst in fi5:
            d = str(lst).strip('').split(",")
            if d[0] == self.varstr:
                self.attribute.extend(d[1:])
        f5.close()
        self.attri_number = len(self.attribute) # 记录物品特有信息个数
        # 根据关键词在key和value中查找
        if self.searstr == '':
            tkinter.messagebox.showinfo('提示','请输入关键词')
        else:
            keylst = self.objdic.keys()
            count = 0
            keysave = []
            for lst in keylst:
                keysave.append(lst) #将self.objdic.keys()的结果转化为列表
                if self.searstr in lst:
                    count = count+1
                    self.lst_1 = lst
                    self.showinfo()

            valuelst = self.objdic.values()
            count_2 = 0
        
            for lst in valuelst:
                count_2 = count_2 + 1
                i = 0
                max = 4+self.attri_number
                while i < max: 
                    i=i+1
                    if self.searstr in lst[i-1]:
                        count = count + 1
                        self.lst_1 = keysave[count_2-1]
                        self.showinfo()
                
            # 提示标签
            info = '共查询到'+str(count)+'条结果'
            result_label = Label(self.f2,text=info,font=('华文新魏',14),justify=LEFT,anchor='w',width=400)
            result_label.place(x=0,y=100,width=150,height=30)
    # 将查询到的信息写在文本框中
    def showinfo(self):
        
        # 组织格式       
        s = self.pubilcinfo[0] + self.lst_1 + '\n' +self.pubilcinfo[1] + self.objdic[self.lst_1][0] + '\n' +self.pubilcinfo[2] + self.objdic[self.lst_1][1] + '\n'+self.pubilcinfo[3] + self.objdic[self.lst_1][2] + '\n'+self.pubilcinfo[4] + self.objdic[self.lst_1][3] + '\n'  
        i = 1
        while i <= self.attri_number :
            s = s + self.attribute[i-1].strip('\n') +'：'+self.objdic[self.lst_1][3+i] + '\n'
            i=i+1
        self.txt.insert(END,s)


    # 定义添加函数
    def add(self):
        # 先将frame中之前的组件清除
        for widget in self.f2.winfo_children():
            widget.destroy()
        # 建立新的组件-用户先选择类型
        # 建立新的组件-用户先选择类型
        addlabel = Label(self.f2,text='请选择物品类型：',font=('华文新魏',14),justify=LEFT,anchor='e',width=400)
        addlabel.place(x=0,y=0,width=120,height=50)
        # 读取category文件中的物品类型并存在列表中
        f6 = open('category+attribute.txt','r',encoding='utf-8')
        fi6 = f6.readlines()
        add_typelst = []
        for lst in fi6:
            d = str(lst).strip('').split(",")
            add_typelst.append(d[0])   
        f6.close()
        # 创建用户选择组合框
        self.addvar = StringVar(self.general_root,value='')
        addtype_comb = Combobox(self.f2,textvariable=self.addvar,values=add_typelst)
        addtype_comb.place(x=0,y=40,width=200,height=30)
         # 创建按钮
        btn_add = Button(self.f2,text='确定',command =self.addintxt)
        btn_add.place(x=200,y=40,width=80,height=30)
        btn_add2 = Button(self.f2,text='清空',command =self.addintxt)
        btn_add2.place(x=300,y=40,width=80,height=30)
       

    #定义创建输入新信息的组件函数
    def addintxt(self):
        addvarstr = self.addvar.get()
        # 查找物品特有信息,并存在列表attribute_add中
        f7 = open('category+attribute.txt','r',encoding='utf-8')
        fi7 = f7.readlines()
        self.attribute_add = []
        for lst in fi7:
            d = str(lst).strip('').split(",")
            if d[0] == addvarstr:
                self.attribute_add.extend(d[1:])
        f7.close()

        self.general_root['height']=350 #增长窗口
        self.attriadd_number = len(self.attribute_add) # 记录物品特有信息个数
        self.pubilcinfo = ['物品名称：','物品说明：','所在地址：','联系人手机：','联系人邮箱：']# 共有信息
        publabel1 = Label(self.f2,text='请输入物品名称：',font=('华文新魏',12),justify=CENTER,width=30)
        publabel1.place(x=100,y=70,width=100,height=40)
        self.pub1 = StringVar(self.general_root,value='')
        self.entrypub1 = Entry(self.f2,width=40,textvariable=self.pub1)
        self.entrypub1.place(x=200,y=70,width=200,height=30)

        publabel2 = Label(self.f2,text='请输入物品说明：',font=('华文新魏',12),justify=CENTER,width=30)
        publabel2.place(x=100,y=100,width=100,height=40)
        self.pub2 = StringVar(self.general_root,value='')
        self.entrypub2 = Entry(self.f2,width=40,textvariable=self.pub2)
        self.entrypub2.place(x=200,y=100,width=200,height=30)

        publabel3 = Label(self.f2,text='请输入所在地址：',font=('华文新魏',12),justify=CENTER,width=30)
        publabel3.place(x=100,y=130,width=100,height=40)
        self.pub3 = StringVar(self.general_root,value='')
        self.entrypub3 = Entry(self.f2,width=40,textvariable=self.pub3)
        self.entrypub3.place(x=200,y=130,width=200,height=30)

        publabel4 = Label(self.f2,text='联系人手机：',font=('华文新魏',12),justify=RIGHT,anchor='e',width=30)
        publabel4.place(x=100,y=160,width=100,height=40)
        self.pub4 = StringVar(self.general_root,value='')
        self.entrypub4 = Entry(self.f2,width=40,textvariable=self.pub4)
        self.entrypub4.place(x=200,y=160,width=200,height=30)

        publabel5 = Label(self.f2,text='联系人邮箱：',font=('华文新魏',12),justify=RIGHT,anchor='e',width=30)
        publabel5.place(x=100,y=190,width=100,height=40)
        self.pub5 = StringVar(self.general_root,value='')
        self.entrypub5 = Entry(self.f2,width=40,textvariable=self.pub5)
        self.entrypub5.place(x=200,y=190,width=200,height=30)

        # 根据列表attribute_add中物品的特有信息，动态建立标签和输入文本框
        i=0
        self.pritry = []
        while i < len(self.attribute_add):
            prilabel = Label(self.f2,text = self.attribute_add[i].strip('\n')+'：',font=('华文新魏',12),justify=RIGHT,anchor='e',width=30)
            prilabel.place(x=100,y=190+30*(i+1),width=100,height=40)
            self.pri = StringVar(self.general_root,value='')
            self.prientry = Entry(self.f2,width=40,textvariable=self.pri)
            self.prientry.place(x=200,y=190+30*(i+1),width=200,height=30)
            i=i+1
            self.pritry.append(self.pri)
        # 创建一个按钮
        btn_complete = Button(self.f2,text='添加',command = self.addtotxt)
        btn_complete.place(x=400,y=190,width=80,height=30)
    def addtotxt(self):
        newinfor = []
        strpub1 = self.pub1.get()
        strpub2 = self.pub2.get()
        strpub3 = self.pub3.get()
        strpub4 = self.pub4.get()
        strpub5 = self.pub5.get()
        newinfor.append(strpub1)
        newinfor.append(strpub2)
        newinfor.append(strpub3)
        newinfor.append(strpub4)
        newinfor.append(strpub5)
        prinum = len(self.pritry)
        pri_i = 0
        while pri_i <prinum:
            newinfor.append(self.pritry[pri_i].get())
            pri_i = pri_i+1
        total = len(newinfor)
        add_i = 0
        if '' in newinfor:
            tkinter.messagebox.showwarning('提示','请将信息填写完整')
        # 打开相应的文件夹
        else:
            self.addvarstr = self.addvar.get()
            
            full_path_add = self.addvarstr +'.txt'
            f8 = open(full_path_add,'a',encoding='utf-8')
            while add_i < total-1:
                f8.write(newinfor[add_i])
                f8.write('/')
                add_i =add_i+1
            f8.write(newinfor[total-1])
            f8.write('\n')
            f8.close()
            
            # 提示成功窗口
            tkinter.messagebox.showwarning('提示','添加物品成功！')
             
  
    # 退出系统
    def cancel(self):
        answer = tkinter.messagebox.askquestion('提示','是否退出程序？')
        if answer=='yes':
            self.general_root.destroy()
        else:
            pass









root = Tk()
app = First(root)
root.mainloop()




