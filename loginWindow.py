from tkinter import *
from tkinter import messagebox as mb
import pathlib
from pathlib import Path
import rootWindow
from addStaff import AddStaff
from delStaff import DelStaf
class LoginWindow:
    def __init__(self, buttonClick, title='Вход в систему'):
        self.loginWindow = Tk()
        self.loginWindow.resizable(False, False)
        self.loginWindow.title(title)
        pathIco = Path(pathlib.Path.cwd(), 'res', 'NDL6Ico.ico')
        self.loginWindow.iconbitmap(pathIco)
        self.loginWindow.configure(bg='#0d4760')
        self.loginWindow.geometry('+600+200')
        self.buttonClick = buttonClick

        # обработка закрытия окна с крестика

        self.loginWindow.protocol("WM_DELETE_WINDOW", lambda: self.on_closing())
        self.path_LP =Path(pathlib.Path.cwd(), 'res', 'txtFiles', 'LP.txt')
        self.path_LP_Temp = Path(pathlib.Path.cwd(), 'res', 'txtFiles', 'LPTemp.txt')
        with open(self.path_LP, 'r') as file:
            str = ''
            for line in file:
                str+=line
            listLP = str.splitlines()
            self.login = listLP[0]
            self.password = listLP[1]

        textLogin = StringVar(value=None)
        textPassword = StringVar(value=None)
        self.textEmptyLogin = StringVar(value=None)
        self.textEmptyPassword = StringVar(value=None)

        self.loginL = Label(self.loginWindow, text='Введите логин: ', justify=LEFT, font=('Times New Roman', 14),
                            bg='#0d4760', fg='#0de02d')

        self.passwordL = Label(self.loginWindow, text='Введите пароль: ', justify=LEFT, font=('Times New Roman', 14),
                           bg='#0d4760', fg='#0de02d')

        self.loginE=Entry(self.loginWindow, font=('Times New Roman', 14), bg='#0d4760', fg='#0de02d', textvariable=textLogin)
        self.passwordE=Entry(self.loginWindow, font=('Times New Roman', 14),
                             textvariable=textPassword, bg='#0d4760', fg='#0de02d', show='*')

        self.enterB = Button(self.loginWindow, text='Вход', justify=CENTER, font=('Times New Roman', 14),
                             bg='#0d4760', fg='#0de02d', activebackground='yellow')
        self.cancelB = Button(self.loginWindow, text='Отмена', justify=CENTER, font=('Times New Roman', 14),
               bg='#0d4760', fg='#0de02d', activebackground='yellow',command=self.rootWindowRun)
        self.clearPoleB = Button(self.loginWindow, text='Очистить', justify=CENTER, font=('Times New Roman', 14),
                              bg='#0d4760', fg='#0de02d', activebackground='yellow', command=self.clearPoleF)

        self.mainMenu = Menu(bg='#0d4760', fg='#0de02d', font=('Times New Roman', 14), tearoff=0)
        self.passwordMenu = Menu(bg='#0d4760', fg='#0de02d', font=('Times New Roman', 14), tearoff=0)
        self.passwordMenu.add_command(label='Сменить пароль', command=self.passwordChange)
        self.mainMenu.add_cascade(label='Пароль', menu=self.passwordMenu)

    def run(self):
        LoginWindow.drawWidgets(self)
        self.loginWindow.config(menu=self.mainMenu)
        self.loginWindow.mainloop()

    def on_closing(self):
        self.loginWindow.destroy()
        root = rootWindow.RootWindow()
        root.run()

    def drawWidgets(self):
        self.loginL.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.loginE.grid(row=0, column=1, sticky=W + E)
        self.passwordL.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.passwordE.grid(row=1, column=1, sticky=W + E)

        self.enterB.configure(command=lambda : LoginWindow.entryOK(self))
        self.enterB.grid(row=2, column=0)
        self.cancelB.grid(row=2, column=1, sticky=W)
        self.clearPoleB.grid(row=2, column=1, sticky=E)

    def entryOK(self):
        if self.loginE.get()==self.login and self.passwordE.get()==self.password:
            import subprocess
            path = Path(pathlib.Path.cwd(), 'NDL6Staff.xlsx')
            path_excel = r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE"
            subprocess.Popen([path_excel, '\t', path])
            self.loginWindow.destroy()
            root = rootWindow.RootWindow()
            root.run()
            # if self.buttonClick == 'add':
            #     ad = AddStaff()
            #     ad.run()
            # elif self.buttonClick == 'remove':
            #     remove = DelStaf()
            #     remove.run()
            # elif self.buttonClick == 'edit':
            #     edit = Edit()
            #     edit.run()
        else:
            mb.showerror('Вход в систему', 'Вход запрещен!')

    def passwordChange(self):
        self.loginE.configure(textvariable=self.textEmptyLogin)
        self.passwordE.configure(textvariable=self.textEmptyPassword)
        self.loginL.configure(text='Введите старый логин: ')
        self.loginL.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.loginE.grid(row=0, column=1, sticky=W + E)
        self.passwordL.configure(text='Введите старый пароль: ')
        self.passwordL.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.passwordE.grid(row=1, column=1, sticky=W + E)
        self.enterB.configure(text='Проверить', command=lambda: LoginWindow.newPassword(self, self.login, self.password))
        self.enterB.grid(row=2, column=0)
        self.cancelB.grid(row=2, column=1, sticky=W)
        self.clearPoleB.grid(row=2, column=1, sticky=E)

    def newPassword(self, login, password):
        if self.loginE.get() == login and self.passwordE.get() == password:
            self.loginE.configure(textvariable=self.textEmptyLogin)
            self.passwordE.configure(textvariable=self.textEmptyPassword)
            self.loginL.configure(text='Введите новый логин: ')
            self.loginL.grid(row=0, column=0, sticky=W, padx=5, pady=5)
            self.loginE.grid(row=0, column=1, sticky=W + E)
            self.passwordL.configure(text='Введите новый пароль: ')
            self.passwordL.grid(row=1, column=0, sticky=W, padx=5, pady=5)
            self.passwordE.grid(row=1, column=1, sticky=W + E)
            self.enterB.configure(text='Сохранить',command=lambda: LoginWindow.savePassword(self, self.loginE.get(), self.passwordE.get()))
            self.enterB.grid(row=2, column=0)
            self.cancelB.grid(row=2, column=1, sticky=W)
            self.clearPoleB.grid(row=2, column=1, sticky=E)
            return (self.login, self.password)
        else:
            mb.showerror('Вход в систему', 'Вход запрещен!\nПароль или логин указан неверно!')

    def savePassword(self, login, password):
        result = mb.askokcancel('Сохранение нового логина и пароля', f'Новый логин:\t{login}\nНовый пароль:\t{password}')
        if result:
            with open('res//txtFiles//LPTemp.txt', 'w') as file:
                file.write(f'{login}\n')
                file.write(f'{password}')
            from os import rename, remove
            remove(self.path_LP)
            rename(self.path_LP_Temp, self.path_LP)
            self.rootWindowRun()
        else:
            self.loginL.configure(text='Введите логин: ')
            self.loginL.grid(row=0, column=0, sticky=W, padx=5, pady=5)
            self.loginE.grid(row=0, column=1, sticky=W + E)
            self.passwordL.configure(text='Введите пароль: ')
            self.passwordL.grid(row=1, column=0, sticky=W, padx=5, pady=5)
            self.passwordE.grid(row=1, column=1, sticky=W + E)
            self.enterB.configure(text='Вход')
            self.drawWidgets()

    def clearPoleF(self):
        self.loginE.grid_forget()
        self.passwordE.grid_forget()
        self.loginE.configure(textvariable=self.textEmptyLogin)
        self.passwordE.configure(textvariable=self.textEmptyPassword)
        self.loginE.grid(row=0, column=1, sticky=W + E)
        self.passwordE.grid(row=1, column=1, sticky=W + E)

    def rootWindowRun(self):
        self.loginWindow.destroy()
        root = rootWindow.RootWindow()
        root.run()





