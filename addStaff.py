from tkinter import *
from tkinter import messagebox as mb
from PIL import Image as PilImage
from PIL import ImageTk
import rootWindow
import pathlib
from pathlib import Path
class AddStaff:
    def __init__(self):
        self.ad = Tk()
        self.ad.title('ДОБАВЛЕНИЕ')
        pathIco = Path(pathlib.Path.cwd(), 'res', 'NDL6Ico.ico')
        self.ad.iconbitmap(pathIco)
        self.ad.geometry('+100+5')
        self.ad.resizable(False,False)

        self.ad.configure(bg='#0d4760')

        self.textFamily = StringVar(value='Иванов')
        self.textName = StringVar(value='Иван')
        self.textSername = StringVar(value='Иванович')
        self.textTabel = StringVar(value='XXXXX')
        self.textWorkLace = StringVar(value='XXXX')
        self.textOklad = StringVar(value='10000')
        self.textOverOklad = StringVar(value='0')
        self.textTel = StringVar(value='066-5850-123')
        self.textAdress = StringVar(value='просп. Мира 1, кв. 15')
        self.textBirthDay = StringVar(value='01.01.2001')
        self.textEmpty  = StringVar(value='')
        self.familyEntry = Entry(self.ad, font=('Times New Roman', 14),
                                bg='#0d4760', fg='#0de02d', textvariable=self.textFamily)
        self.nameEntry = Entry(self.ad, font=('Times New Roman', 14),
                                 bg='#0d4760', fg='#0de02d', textvariable=self.textName)
        self.sernameEntry = Entry(self.ad, font=('Times New Roman', 14),
                                 bg='#0d4760', fg='#0de02d', textvariable=self.textSername)
        self.FIO = f'{self.familyEntry.get()} {self.nameEntry.get()[0]}.{self.sernameEntry.get()[0]}.'

        self.tabelEntry = Entry(self.ad, font=('Times New Roman', 14),
                                  bg='#0d4760', fg='#0de02d', textvariable=self.textTabel)
        self.workPlaceEntry = Entry(self.ad, font=('Times New Roman', 14),
                                bg='#0d4760', fg='#0de02d', textvariable=self.textWorkLace)
        self.okladEntry = Entry(self.ad, font=('Times New Roman', 14),
                                  bg='#0d4760', fg='#0de02d', textvariable=self.textOklad)
        self.overOkladEntry = Entry(self.ad, font=('Times New Roman', 14),
                                  bg='#0d4760', fg='#0de02d', textvariable=self.textOverOklad)
        self.telEntry = Entry(self.ad, font=('Times New Roman', 14),
                                  bg='#0d4760', fg='#0de02d', textvariable=self.textTel)
        self.adressEntry = Entry(self.ad, font=('Times New Roman', 14),
                                  bg='#0d4760', fg='#0de02d', textvariable=self.textAdress)
        self.birthDayEntry = Entry(self.ad, font=('Times New Roman', 14),
                                  bg='#0d4760', fg='#0de02d', textvariable=self.textBirthDay)

        self.choise = IntVar(value=0)
        self.choiseK = IntVar(value=0)

        path_addUser_BI = Path(pathlib.Path.cwd(), 'res', 'buttonIcon', 'addUser.png')
        path_reset_BI = Path(pathlib.Path.cwd(), 'res', 'buttonIcon', 'reset.png')

        self.addButton = AddStaff.buttonImage(self, path_addUser_BI)
        self.resetButton = AddStaff.buttonImage(self, path_reset_BI)

        # обработка закрытия окна с крестика
        self.ad.protocol("WM_DELETE_WINDOW", lambda: self.on_closing())

    def on_closing(self):
        self.ad.destroy()
        root = rootWindow.RootWindow()
        root.run()

    def run(self):
        AddStaff.drawWidgets(self)
        self.ad.mainloop()

    def buttonImage(self, imageAdress):
        img = PilImage.open(imageAdress)
        img = img.resize((150, 150), PilImage.ANTIALIAS)
        self.buttonImage = ImageTk.PhotoImage(img)
        return self.buttonImage

    def drawWidgets(self):
        Label(self.ad, text='Фамилия', justify=LEFT, font=('Times New Roman', 16),
              bg='#0d4760', fg='#0de02d',padx=5, pady=5).grid(row=0, column=0, sticky=W)
        self.familyEntry.grid(row=1, column=0,padx=5, pady=5)
        Label(self.ad, text='Имя', justify=LEFT, font=('Times New Roman', 16),
              bg='#0d4760', fg='#0de02d',padx=5, pady=5).grid(row=0, column=1, sticky=W)
        self.nameEntry.grid(row=1, column=1,padx=5, pady=5)
        Label(self.ad, text='Отчество', justify=LEFT, font=('Times New Roman', 16),
              bg='#0d4760', fg='#0de02d',padx=5, pady=5).grid(row=0, column=2, sticky=W)
        self.sernameEntry.grid(row=1, column=2,padx=5, pady=5)

        Label(self.ad, text='Табельный номер', justify=LEFT, font=('Times New Roman', 16),
              bg='#0d4760', fg='#0de02d', padx=5, pady=5).grid(row=2, column=0, sticky=W)
        self.tabelEntry.grid(row=3, column=0, padx=5, pady=5)

        Label(self.ad, text='Профессия', justify=LEFT, font=('Times New Roman', 16),
              bg='#0d4760', fg='#0de02d', padx=5, pady=5).grid(row=4, column=0, sticky=W)
        self.ingener = Radiobutton(self.ad, text='инженер-исследователь', justify=LEFT, font=('Times New Roman', 14),
                                  bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                  variable=self.choise, value=1).grid(row=5, column=0, sticky=W)
        self.electronik = Radiobutton(self.ad, text='инженер-электроник', justify=LEFT, font=('Times New Roman', 14),
                                   bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                   variable=self.choise, value=2).grid(row=5, column=1, sticky=W)
        self.mehanik = Radiobutton(self.ad, text='испытатель-механик двигателей', justify=LEFT, font=('Times New Roman', 14),
                                   bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                   variable=self.choise, value=3).grid(row=6, column=0, sticky=W)
        self.slesar = Radiobutton(self.ad, text='слесарь-испытатель', justify=LEFT, font=('Times New Roman', 14),
                                   bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                   variable=self.choise, value=4).grid(row=6, column=1, sticky=W)
        self.reaip = Radiobutton(self.ad, text='регулировщик РЭАиП', justify=LEFT, font=('Times New Roman', 14),
                                   bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                   variable=self.choise, value=5).grid(row=7, column=0, sticky=W)

        Label(self.ad, text='Категория', justify=LEFT, font=('Times New Roman', 16),
              bg='#0d4760', fg='#0de02d', padx=5, pady=5).grid(row=8, column=0, sticky=W)
        self.withOut = Radiobutton(self.ad, text='без категории', justify=LEFT, font=('Times New Roman', 14),
                                   bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                   variable=self.choiseK, value=1
                                   ).grid(row=9, column=0, sticky=W)
        self.kat2 = Radiobutton(self.ad, text='II категории', justify=LEFT, font=('Times New Roman', 14),
                                      bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                      variable=self.choiseK, value=2
                                ).grid(row=9, column=1, sticky=W)
        self.kat1 = Radiobutton(self.ad, text='I категории', justify=LEFT,
                                   font=('Times New Roman', 14),
                                   bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                   variable=self.choiseK, value=3
                                ).grid(row=10, column=0, sticky=W)
        self.ved = Radiobutton(self.ad, text='ведущий', justify=LEFT, font=('Times New Roman', 14),
                                  bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                  variable=self.choiseK, value=4
                               ).grid(row=10, column=1, sticky=W)


        Label(self.ad, text='Рабочее место', justify=LEFT, font=('Times New Roman', 16),
              bg='#0d4760', fg='#0de02d', padx=5, pady=5).grid(row=11, column=0, sticky=W)
        self.workPlaceEntry.grid(row=12, column=0, padx=5, pady=5)

        Label(self.ad, text='Оклад', justify=LEFT, font=('Times New Roman', 16),
              bg='#0d4760', fg='#0de02d', padx=5, pady=5).grid(row=13, column=0, sticky=W)
        self.okladEntry.grid(row=14, column=0, padx=5, pady=5)

        Label(self.ad, text='Надбавка в %', justify=LEFT, font=('Times New Roman', 16),
              bg='#0d4760', fg='#0de02d', padx=5, pady=5).grid(row=15, column=0, sticky=W)
        self.overOkladEntry.grid(row=16, column=0, padx=5, pady=5)

        Label(self.ad, text='Номер телефона', justify=LEFT, font=('Times New Roman', 16),
              bg='#0d4760', fg='#0de02d', padx=5, pady=5).grid(row=17, column=0, sticky=W)
        self.telEntry.grid(row=18, column=0, padx=5, pady=5)

        Label(self.ad, text='Адрес', justify=LEFT, font=('Times New Roman', 16),
              bg='#0d4760', fg='#0de02d', padx=5, pady=5).grid(row=19, column=0, sticky=W)
        self.adressEntry.grid(row=20, column=0, padx=5, pady=5)

        Label(self.ad, text='Дата дня рождения', justify=LEFT, font=('Times New Roman', 16),
              bg='#0d4760', fg='#0de02d', padx=5, pady=5).grid(row=21, column=0, sticky=W)
        self.birthDayEntry.grid(row=22, column=0, padx=5, pady=5)


        self.adPerson = Button(self.ad, image=self.addButton, bg='#0de02d',
                                     activebackground='yellow',
                               command=self.addUser
                               ).grid(row=14, column=1, rowspan=4)
        self.resetPerson = Button(self.ad, image=self.resetButton, bg='#0de02d',
                               activebackground='yellow',
                                  command=lambda: AddStaff.resetData(self)).grid(row=14, column=2, rowspan=4)

    def resetData(self):
        self.familyEntry.configure(textvariable=self.textEmpty)
        self.nameEntry.configure(textvariable=self.textEmpty)
        self.sernameEntry.configure(textvariable=self.textEmpty)
        self.tabelEntry.configure(textvariable=self.textEmpty)
        self.workPlaceEntry.configure(textvariable=self.textEmpty)
        self.okladEntry.configure(textvariable=self.textEmpty)
        self.overOkladEntry.configure(textvariable=self.textEmpty)
        self.telEntry.configure(textvariable=self.textEmpty)
        self.adressEntry.configure(textvariable=self.textEmpty)
        self.birthDayEntry.configure(textvariable=self.textEmpty)
        self.choise = IntVar(value=0)
        self.choiseK = IntVar(value=0)
    def writeData(self):
        self.FIO = f'{self.familyEntry.get()} {self.nameEntry.get()[0]}.{self.sernameEntry.get()[0]}.'
        listEntry = [self.FIO,
                     self.tabelEntry.get(), self.workPlaceEntry.get(), self.okladEntry.get(),
                     self.overOkladEntry.get(), self.telEntry.get(), self.adressEntry.get(),
                     self.birthDayEntry.get()]
        listFileName = ['fio.txt', 'tabel.txt', 'workPlace.txt', 'oklad.txt', 'bonus.txt', 'phone.txt',
                        'adress.txt', 'birthDay.txt']
        for j in range(0, len(listEntry)):
            path = Path(pathlib.Path.cwd(), 'res', 'txtFiles', f'{listFileName[j]}')
            with open(path, 'a') as file:
                file.write(f'\n{listEntry[j]}')
        self.profValue()

    def addUser(self):
        self.FIO = f'{self.familyEntry.get()} {self.nameEntry.get()[0]}.{self.sernameEntry.get()[0]}.'
        answer = mb.askokcancel('Добавление сотрудника',
                       f'ФИО: {self.FIO}\n'
                       f'Табельный номер: {self.tabelEntry.get()}')
        if answer:
            self.writeData()
            self.on_closing()


    def profValue(self):
        i = 'инженер-исследователь'
        e = 'инженер-электроник'
        file = open(Path(pathlib.Path.cwd(),  'res', 'txtFiles', 'prof.txt'), 'a')
        if self.choise.get() == 1:
            if self.choiseK.get() == 1:
                file.write(f'\n{i} без категории')
            elif self.choiseK.get() == 2:
                file.write(f'\n{i} II категории')
            elif self.choiseK.get() == 3:
                file.write(f'\n{i} I категории')
            elif self.choiseK.get() == 4:
                file.write(f'\nведущий {i}')
            file.close()
        elif self.choise.get() == 2:
            if self.choiseK.get() == 1:
                file.write(f'\n{e} без категории')
            elif self.choiseK.get() == 2:
                file.write(f'\n{e} II категории')
            elif self.choiseK.get() == 3:
                file.write(f'\n{e} I категории')
            elif self.choiseK.get() == 4:
                file.write(f'\nведущий {e}')
            file.close()
        elif self.choise.get() == 3:
            file.write('\nиспытатель-механик двигателей')
            file.close()
        elif self.choise.get() == 4:
            file.write('\nслесарь-испытатель')
            file.close()
        elif self.choise.get() == 5:
            file.write('\nрегулировщик РЭАиП')
            file.close()
        elif not self.choise.get():
            mb.showinfo('Пустое поле', 'Укажите профессию')

    def checkEntry(self, entry):
        if not entry:
            mb.showinfo('Пустое поле', 'Не все поля заполнены')




