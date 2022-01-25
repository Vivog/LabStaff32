from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Combobox
from PIL import Image as PilImage
from PIL import ImageTk
import rootWindow
from os import remove, rename
import pathlib
from pathlib import Path
class DelStaf:
    def __init__(self):
        self.delStaff = Tk()
        self.delStaff.title('УДАЛЕНИЕ')
        pathIco = Path(pathlib.Path.cwd(), 'res', 'NDL6Ico.ico')
        self.delStaff.iconbitmap(pathIco)
        self.delStaff.geometry('+600+200')
        self.delStaff.resizable(False,False)
        self.delStaff.configure(bg='#0d4760')

        self.selectUserL = Label(self.delStaff, text='Выберите сотрудника:', justify=LEFT, font=('Times New Roman', 16),
                                 bg='#0d4760', fg='#0de02d', padx=5, pady=5)
        self.combo = Combobox(self.delStaff, value=DelStaf.readFile(self), font=('Times New Roman', 14),
                              state='readonly')
        self.combo.bind('<<ComboboxSelected>>', self.comboSelected)
        self.agreeB = Button(self.delStaff, text='Подтвердить', bg='#0de02d', font=('Times New Roman', 14),
                             activebackground='yellow', command=self.okButton)
        path_delUser_BI = Path(pathlib.Path.cwd(), 'res', 'buttonIcon', 'delUser.png')
        path_reset_BI = Path(pathlib.Path.cwd(), 'res', 'buttonIcon', 'reset.png')
        self.delUserButton = DelStaf.buttonImage(self,  path_delUser_BI)
        self.resetButton = DelStaf.buttonImage(self, path_reset_BI)
        self.FIO = ''
        self.tabel = ''
        self.prof = ''
        self.fioL = Label(self.delStaff, text='ФИО:', justify=LEFT, font=('Times New Roman', 16),
              bg='#0d4760', fg='#0de02d', padx=5, pady=5)
        self.fioLA = Label(self.delStaff, text=self.FIO, justify=LEFT, font=('Times New Roman', 16, 'bold'),
              bg='#0d4760', fg='#0de02d', padx=5, pady=5)

        self.tabelL = Label(self.delStaff, text='Табельный номер:', justify=LEFT, font=('Times New Roman', 16),
              bg='#0d4760', fg='#0de02d', padx=5, pady=5)
        self.tabelLA= Label(self.delStaff, text=self.tabel, justify=LEFT, font=('Times New Roman', 16, 'bold'),
              bg='#0d4760', fg='#0de02d', padx=5, pady=5)

        self.profL = Label(self.delStaff, text='Профессия:', justify=LEFT, font=('Times New Roman', 16),
              bg='#0d4760', fg='#0de02d', padx=5, pady=5)
        self.profLA = Label(self.delStaff, text=self.prof, justify=LEFT, font=('Times New Roman', 16, 'bold'),
              bg='#0d4760', fg='#0de02d', padx=5, pady=5)

        self.delUser = Button(self.delStaff, image=self.delUserButton, bg='#0de02d',
                              activebackground='yellow', command=self.delUserF)
        self.reset = Button(self.delStaff, image=self.resetButton, bg='#0de02d',
                            activebackground='yellow',
                            command=self.resetData)
        self.delStaff.protocol("WM_DELETE_WINDOW", lambda: self.on_closing())

    def on_closing(self):
        self.delStaff.destroy()
        root = rootWindow.RootWindow()
        root.run()


    def run(self):
        self.drawWidgets()
        self.delStaff.mainloop()

    def buttonImage(self, imageAdress):
        img = PilImage.open(imageAdress)
        img = img.resize((75, 75), PilImage.ANTIALIAS)
        self.buttonImage = ImageTk.PhotoImage(img)
        return self.buttonImage

    def drawWidgets(self):
        self.selectUserL.grid(row=0, column=0)
        self.combo.grid(row=0, column=1, padx=5, pady=5)



    def readFile(self):
        self.path_fio = Path(pathlib.Path.cwd(), 'res', 'txtFiles', 'fio.txt')
        f = open(self.path_fio, 'r')
        str = ''
        for line in f:
            str += line
        self.listF = str.splitlines()
        return self.listF

    def comboSelected(self, event):
        self.agreeB.grid(row=2, column=0)

    def okButton(self):
        index = self.listF.index(self.combo.get())
        with open(self.path_fio, 'r') as file:
            str = ''
            for line in file:
                str += line
            self.listF = str.splitlines()
        self.fioL.grid(row=0, column=0, sticky=W)
        self.fioLA.configure(text=self.listF[index])
        self.fioLA.grid(row=0, column=1, sticky=W)

        self.path_tabel = Path(pathlib.Path.cwd(), 'res', 'txtFiles', 'tabel.txt')
        with open(self.path_tabel, 'r') as file:
            str = ''
            for line in file:
                str += line
            self.listT = str.splitlines()
        self.tabelL.grid(row=1, column=0, sticky=W)
        self.tabelLA.configure(text=self.listT[index])
        self.tabelLA.grid(row=1, column=1, sticky=W)

        self.path_prof = Path(pathlib.Path.cwd(), 'res', 'txtFiles', 'prof.txt')
        with open(self.path_prof, 'r') as file:
            str = ''
            for line in file:
                str += line
            self.listP = str.splitlines()
        self.profL.grid(row=2, column=0, sticky=W)
        self.profLA.configure(text=self.listP[index])
        self.profLA.grid(row=2, column=1, sticky=W)

        self.delUser.grid(row=3, column=0, rowspan=3, sticky=E)
        self.reset.grid(row=3, column=1, rowspan=3, sticky=W)

        self.selectUserL.grid_forget()
        self.combo.grid_forget()
        self.agreeB.grid_forget()

    def delUserF(self):
        index = self.listF.index(self.combo.get())
        listFiles = ['adress.txt', 'birthDay.txt', 'fio.txt', 'bonus.txt',
                     'oklad.txt', 'phone.txt', 'prof.txt', 'tabel.txt', 'workPlace.txt']
        for i in range(0, len(listFiles)):
            path = Path(pathlib.Path.cwd(), 'res', 'txtFiles', f'{listFiles[i]}')
            with open(path, 'r') as file:
                str = ''
                for line in file:
                    str += line
                self.list = str.splitlines()
                del self.list[index]
            pathTemp = Path(pathlib.Path.cwd(), 'res', 'txtFiles', 'temp.txt')
            with open(pathTemp, 'w') as temp:
                temp.write(self.list[0])
                for i in range(1, len(self.list)):
                    temp.write(f'\n{self.list[i]}')
            remove(path)
            rename(pathTemp, path)
        result = mb.askokcancel('Удаление сотрудника', f'ФИО: {self.listF[index]}\n'
                                                f'Табельный номер: {self.listT[index]}')

        self.on_closing()


    def resetData(self):

        self.selectUserL.grid(row=0, column=0)
        self.combo.grid(row=0, column=1, padx=5, pady=5)

        self.agreeB.destroy()

        self.fioL.grid_forget()
        self.fioLA.grid_forget()

        self.tabelL.grid_forget()
        self.tabelLA.grid_forget()

        self.profL.grid_forget()
        self.profLA.grid_forget()

        self.delUser.grid_forget()
        self.reset.grid_forget()









if __name__ == '__main__':
    delStaff = DelStaf()
    delStaff.run()