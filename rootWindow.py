import os.path
import pathlib
import tkinter.filedialog
from tkinter import *
from tkinter import messagebox as mb
from PIL import Image as PilImage
from PIL import ImageTk
from loginWindow import LoginWindow
from sort import Sort
from pathlib import Path
import pandas as pd
class RootWindow:
    def __init__(self, resizeable=(False, False)):
        self.root = Tk()
        self.root.geometry('+100+5')
        self.root.resizable(resizeable[0], resizeable[1])
        pathIco = Path(pathlib.Path.cwd(), 'res', 'NDL6Ico.ico')
        self.root.iconbitmap(pathIco)
        self.root.title('LabInfo')
        self.root.configure(bg='#0d4760')
        self.df = pd.read_excel(Path(pathlib.Path.cwd(),  'NDL6Staff.xlsx'))

        #обработка закрытия окна с крестика
        self.root.protocol("WM_DELETE_WINDOW", lambda: RootWindow.on_closing(self))
        self.choise_group = IntVar(value=1)
        self.choise_age = IntVar(value=20)
        self.choise_oklad = IntVar(value=6000)
        self.path_buttons_image()
        self.buttons_image()
        self.radio_buttons(self.choise_group, self.choise_age, self.choise_oklad)
        self.buttons("NDL6Staff")
        self.labels()

    def on_closing(self):
        if mb.askokcancel("Закрытие LabInfo", "Вы хотите закрыть LabInfo?"):
            self.root.destroy()

    def run(self):
        self.drawWidgets()
        self.buttonTabel.invoke()
        self.rb_grid_fogget()
        self.root.mainloop()

    def buttonImage(self, imageAdress):
        img = PilImage.open(imageAdress)
        img = img.resize((135, 135), PilImage.ANTIALIAS)
        self.buttonImage = ImageTk.PhotoImage(img)
        return  self.buttonImage

    def path_buttons_image(self):
        global path_addUser_BI
        global path_adress_BI
        global path_averOklad_BI
        global path_birthday_BI
        global path_bonus_BI
        global path_editUser_BI
        global path_folder_BI
        global path_listGroup_BI
        global path_oklad_BI
        global path_phone_BI
        global path_prof_BI
        global path_removeUser_BI
        global path_sortDown_BI
        global path_sortUp_BI
        global path_tabel_BI
        global path_workPlace_BI

        path_addUser_BI = Path(pathlib.Path.cwd(), 'res', 'buttonIcon', 'addUser.png')
        path_adress_BI = Path(pathlib.Path.cwd(), 'res', 'buttonIcon', 'adress.png')
        path_averOklad_BI = Path(pathlib.Path.cwd(), 'res', 'buttonIcon', 'averageOklad.png')
        path_birthday_BI = Path(pathlib.Path.cwd(), 'res', 'buttonIcon', 'birthday.png')
        path_bonus_BI = Path(pathlib.Path.cwd(), 'res', 'buttonIcon', 'bonus.png')
        path_editUser_BI = Path(pathlib.Path.cwd(), 'res', 'buttonIcon', 'editUser.png')
        path_folder_BI = Path(pathlib.Path.cwd(), 'res', 'buttonIcon', 'folder.png')
        path_listGroup_BI = Path(pathlib.Path.cwd(), 'res', 'buttonIcon', 'listGroup.png')
        path_oklad_BI = Path(pathlib.Path.cwd(), 'res', 'buttonIcon', 'oklad.png')
        path_phone_BI = Path(pathlib.Path.cwd(), 'res', 'buttonIcon', 'phone.png')
        path_prof_BI = Path(pathlib.Path.cwd(), 'res', 'buttonIcon', 'prof.png')
        path_removeUser_BI = Path(pathlib.Path.cwd(), 'res', 'buttonIcon', 'removeUser.png')
        path_sortDown_BI = Path(pathlib.Path.cwd(), 'res', 'buttonIcon', 'sortDown.png')
        path_sortUp_BI = Path(pathlib.Path.cwd(), 'res', 'buttonIcon', 'sortUp.png')
        path_tabel_BI = Path(pathlib.Path.cwd(), 'res', 'buttonIcon', 'tabel.png')
        path_workPlace_BI = Path(pathlib.Path.cwd(), 'res', 'buttonIcon', 'workPlace.png')

    def radio_buttons(self, choise_group, choise_age, choise_oklad):

        # choise Group
        self.NDL6RB = Radiobutton(self.root, text='НИЛ-6', justify=LEFT, font=('Times New Roman', 16),
                                  bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                  variable=choise_group, value=1, command=self.selected_Group)
        self.GPRB = Radiobutton(self.root, text='ГПиТИ', justify=LEFT, font=('Times New Roman', 16),
                                bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                variable=choise_group, value=2, command=self.selected_Group)
        self.GIBRB = Radiobutton(self.root, text='ГИБП', justify=LEFT, font=('Times New Roman', 16),
                                 bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                 variable=choise_group, value=3, command=self.selected_Group)
        self.GIMRB = Radiobutton(self.root, text='ГИМП', justify=LEFT, font=('Times New Roman', 16),
                                 bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                 variable=choise_group, value=4, command=self.selected_Group)
        self.GARB = Radiobutton(self.root, text='ГОиАИ', justify=LEFT, font=('Times New Roman', 16),
                                bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                variable=choise_group, value=5, command=self.selected_Group)
        self.GNORB = Radiobutton(self.root, text='ГНСИТ', justify=LEFT, font=('Times New Roman', 16),
                                 bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                 variable=choise_group, value=6, command=self.selected_Group)

        # sort Age
        self.sort_20_30_RB = Radiobutton(self.root, text='20 - 30', justify=LEFT, font=('Times New Roman', 18, 'bold'),
                                  bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                  variable=choise_age, value=30)
        self.sort_30_40_RB = Radiobutton(self.root, text='30 - 40', justify=LEFT, font=('Times New Roman', 18, 'bold'),
                                bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                variable=choise_age, value=40)
        self.sort_40_50_RB = Radiobutton(self.root, text='40 - 50', justify=LEFT, font=('Times New Roman', 18, 'bold'),
                                 bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                 variable=choise_age, value=50)
        self.sort_50_60_RB = Radiobutton(self.root, text='50 - 60', justify=LEFT, font=('Times New Roman', 18, 'bold'),
                                 bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                 variable=choise_age, value=60)
        self.sort_60_70_RB = Radiobutton(self.root, text='60 - 70', justify=LEFT, font=('Times New Roman', 18, 'bold'),
                                bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                variable=choise_age, value=70)
        self.sort_70_RB = Radiobutton(self.root, text='   > 70', justify=LEFT, font=('Times New Roman', 18, 'bold'),
                                 bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                 variable=choise_age, value=80)

        # sort Oklad
        self.sort_7_9_RB = Radiobutton(self.root, text='7000-9000', justify=LEFT, font=('Times New Roman', 18, 'bold'),
                                         bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                         variable=choise_oklad, value=7000)
        self.sort_9_11_RB = Radiobutton(self.root, text='9000-11000', justify=LEFT, font=('Times New Roman', 18, 'bold'),
                                         bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                         variable=choise_oklad, value=9000)
        self.sort_11_13_RB = Radiobutton(self.root, text='11000-13000', justify=LEFT, font=('Times New Roman', 18, 'bold'),
                                         bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                         variable=choise_oklad, value=11000)
        self.sort_13_15_RB = Radiobutton(self.root, text='13000-15000', justify=LEFT, font=('Times New Roman', 18, 'bold'),
                                         bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                         variable=choise_oklad, value=13000)
        self.sort_15_RB = Radiobutton(self.root, text='> 15000', justify=LEFT, font=('Times New Roman', 18, 'bold'),
                                         bg='#0d4760', fg='black', selectcolor='#0de02d', activebackground='yellow',
                                         variable=choise_oklad, value=15000)

    def buttons_image(self):
        self.averOklad_BI = RootWindow.buttonImage(self, path_averOklad_BI)
        self.add_BI = RootWindow.buttonImage(self, path_addUser_BI)
        self.editBI = RootWindow.buttonImage(self, path_editUser_BI)
        self.removeBI = RootWindow.buttonImage(self, path_removeUser_BI)
        self.folderBI = RootWindow.buttonImage(self, path_folder_BI)
        self.listGroupBI = RootWindow.buttonImage(self, path_listGroup_BI)
        self.tabelBI = RootWindow.buttonImage(self, path_tabel_BI)
        self.okladBI = RootWindow.buttonImage(self, path_oklad_BI)
        self.profBI = RootWindow.buttonImage(self, path_prof_BI)
        self.workPlaceBI = RootWindow.buttonImage(self, path_workPlace_BI)
        self.premiaBI = RootWindow.buttonImage(self, path_bonus_BI)
        self.phoneBI = RootWindow.buttonImage(self, path_phone_BI)
        self.adressBI = RootWindow.buttonImage(self, path_adress_BI)
        self.birthDayBI = RootWindow.buttonImage(self, path_birthday_BI)
        self.sortUpButton_BI = RootWindow.buttonImage(self, path_sortUp_BI)
        self.sortDownButton_BI = RootWindow.buttonImage(self, path_sortDown_BI)
        self.birthDay_Rate_BI = PhotoImage(width=135, height=22)

    def buttons(self, sheet_name):
        self.averOklad_B = Button(self.root, image=self.averOklad_BI, bg='#0de02d', activebackground='yellow',
                                  text='unclicked',
                                  command=self.averOklad)
        self.add_staff_B = Button(self.root, image=self.add_BI, bg='#0de02d', activebackground='yellow',
               command=self.addUserRun)
        self.edit_staff_B = Button(self.root, image=self.editBI, bg='#0de02d', activebackground='yellow',
               command=self.editUserRun)
        self.remove_staff_B = Button(self.root, image=self.removeBI, bg='#0de02d', activebackground='yellow',
               command=self.delUserRun)
        self.folderB = Button(self.root, image=self.folderBI, bg='#0de02d', activebackground='yellow',
                              text='Открыть файлы',
                              command=self.openFolder)
        self.listGroup_B = Button(self.root, image=self.listGroupBI, bg='#0de02d',
                                  activebackground='yellow', text='unclicked',
                                  command=lambda: RootWindow.listGroup(self))
        self.buttonTabel = Button(self.root, image=self.tabelBI, bg='#0de02d', activebackground='yellow',
                                  command=lambda: self.infoStaffX(Sort.sortByKey(Sort(), 'FIO', 'Tabel', True, sheet_name)[0],
                                                                  Sort.sortByKey(Sort(), 'FIO', 'Tabel', True, sheet_name)[1],
                                                                  'FIO',
                                                                  'Tabel',  sheet_name, 2, True, False))
        self.buttonOklad = Button(self.root, image=self.okladBI, bg='#0de02d', activebackground='yellow',
                                  command=lambda: self.infoStaffX(Sort.sortByValue(Sort(), 'FIO', 'Oklad', True, int, sheet_name)[0],
                                                                  Sort.sortByValue(Sort(), 'FIO', 'Oklad', True, int, sheet_name)[1],
                                                                  'FIO', 'Oklad', sheet_name, 2, False, False))
        self.buttonProf = Button(self.root, image=self.profBI, bg='#0de02d', activebackground='yellow',
                                 command=lambda: self.infoStaffX(
                                     Sort.sortByValue(Sort(), 'FIO', 'Prof', True, str, sheet_name)[0],
                                     Sort.sortByValue(Sort(), 'FIO', 'Prof', True, str, sheet_name)[1], 'FIO', 'Prof',
                                     sheet_name, 3, True, False))
        self.buttonRabMesto = Button(self.root, image=self.workPlaceBI, bg='#0de02d', activebackground='yellow',
                                     command=lambda: self.infoStaffX(
                                         Sort.sortByKey(Sort(), 'FIO', 'WorkPlace', True, sheet_name)[0],
                                         Sort.sortByKey(Sort(), 'FIO', 'WorkPlace', True, sheet_name)[1], 'FIO', 'WorkPlace',
                                     sheet_name, 2, True, False))
        self.bonusB = Button(self.root, image=self.premiaBI, bg='#0de02d', activebackground='yellow',
                             command=lambda: self.infoStaffX(Sort.sortByValue(Sort(), 'FIO', 'Bonus', True, int, sheet_name)[0],
                                                             Sort.sortByValue(Sort(), 'FIO', 'Bonus', True, int, sheet_name)[1],
                                                             'FIO', 'Bonus', sheet_name,  2, False, False))
        self.buttonTelefon = Button(self.root, image=self.phoneBI, bg='#0de02d', activebackground='yellow',
                                    command=lambda: self.infoStaffX(Sort.sortByKey(Sort(), 'FIO', 'Phone', True, sheet_name)[0],
                                                                    Sort.sortByKey(Sort(), 'FIO', 'Phone', True, sheet_name)[1], 'FIO',
                                                                    'Phone', sheet_name, 2, True, False))
        self.buttonAdress = Button(self.root, image=self.adressBI, bg='#0de02d', activebackground='yellow',
                                   command=lambda: self.infoStaffX(Sort.sortByKey(Sort(), 'FIO', 'Adress', True, sheet_name)[0],
                                                                   Sort.sortByKey(Sort(), 'FIO', 'Adress', True, sheet_name)[1], 'FIO',
                                                                   'Adress', sheet_name, 3, True, False))
        self.buttonBirthDay = Button(self.root, image=self.birthDayBI, bg='#0de02d', activebackground='yellow',
                                     command=lambda: self.infoStaffX(Sort.sortByDate(Sort(), 'FIO', 'Birthday', True, sheet_name)[0],
                                                                     Sort.sortByDate(Sort(), 'FIO', 'Birthday', True, sheet_name)[1],
                                                                     'FIO', 'Birthday', sheet_name, 3, False, True
                                                                     ))

        self.sortUpB = Button(self.root, image=self.sortUpButton_BI, bg='#0de02d', activebackground='yellow')
        self.sortDownB = Button(self.root, image=self.sortDownButton_BI, bg='#0de02d', activebackground='yellow')

    def labels(self):
        self.infoStaffAL = Label(self.root, text='', justify=LEFT, font=('Times New Roman', 13),
                                 bg='#0d4760', fg='#0de02d')
        self.infoStaffBL = Label(self.root, text='', justify=LEFT, font=('Times New Roman', 13),
                                 bg='#0d4760', fg='#0de02d')

    def drawWidgets(self):
        self.averOklad_B.grid(row=0, column=0)
        self.add_staff_B.grid(row=0, column=2)
        self.edit_staff_B.grid(row=0, column=3)
        self.remove_staff_B.grid(row=0, column=4)
        self.folderB.grid(row=0, column=5)
        self.listGroup_B.grid(row=0, column=7)
        self.buttonTabel.grid(row=5, column=0)
        self.buttonOklad.grid(row=5, column=1)
        self.buttonProf.grid(row=5, column=2)
        self.buttonRabMesto.grid(row=5, column=3)
        self.bonusB.grid(row=5, column=4)
        self.buttonTelefon.grid(row=5, column=5)
        self.buttonAdress.grid(row=5, column=6)
        self.buttonBirthDay.grid(row=5, column=7)

    def infoStaffX(self, listTextA, listTextB, column_x, column_y, sheet_name, columnspan=2, str=True, date=False):
        self.infoStaffAL.grid(row=6, column=0, columnspan=columnspan, sticky=N)
        self.infoStaffBL.grid(row=6, column=3, columnspan=columnspan, sticky=N)
        self.infoStaffAL.configure(text=listTextA)
        self.infoStaffAL.grid(row=6, column=0, columnspan=columnspan, sticky=N)
        self.infoStaffBL.configure(text=listTextB)
        self.infoStaffBL.grid(row=6, column=3, columnspan=columnspan, sticky=N)
        self.sortUpDownB(column_x, column_y, sheet_name, columnspan, str, date)

    def sortUpDownB(self, column_x, column_y, sheet_name, columnspan=2, str=True, date=False):
        self.sortUpB.grid_forget()
        self.sortDownB.grid_forget()
        self.sort_age_buttons_fogget()
        self.sort_oklad_buttons_fogget()
        if str == True and date == False:
            self.sortUpB.configure(
                command=lambda: self.infoStaffX(
                    Sort.sortByKey(Sort(), column_x, column_y, True, sheet_name)[0],
                    Sort.sortByKey(Sort(), column_x, column_y, True, sheet_name)[1],
                    column_x, column_y, sheet_name, columnspan, str, date))
            if column_y == 'Bonus':
                self.sortUpB.grid_forget()
                self.sortUpB.grid(row=6, column=6, sticky=N)
            else:
                self.sortUpB.grid_forget()
                self.sortUpB.grid(row=6, column=7, sticky=N)
            self.sortDownB.configure(
                command=lambda: self.infoStaffX(
                    Sort.sortByKey(Sort(), column_x, column_y, False, sheet_name)[0],
                    Sort.sortByKey(Sort(), column_x, column_y, False, sheet_name)[1],
                    column_x, column_y, sheet_name, columnspan, str, date))
            if column_y == 'Bonus':
                self.sortDownB.grid_forget()
                self.sortDownB.grid(row=6, column=7, sticky=N)
            else:
                self.sortDownB.grid_forget()
                self.sortDownB.grid(row=6, column=7, sticky=N, pady=140)
        elif str == False and date == False:
            self.sortUpB.configure(
                command=lambda: self.infoStaffX(
                    Sort.sortByValue(Sort(), column_x, column_y, True, int, sheet_name)[0],
                    Sort.sortByValue(Sort(), column_x, column_y, True, int, sheet_name)[1],
                    column_x, column_y, sheet_name, columnspan, str, date))
            if column_y == 'Bonus':
                self.sortUpB.grid_forget()
                self.sortUpB.grid(row=6, column=6, sticky=N)
            else:
                self.sortUpB.grid_forget()
                self.sortUpB.grid(row=6, column=7, sticky=N)
            self.sortDownB.configure(
                command=lambda: self.infoStaffX(
                    Sort.sortByValue(Sort(), column_x, column_y, False, int, sheet_name)[0],
                    Sort.sortByValue(Sort(), column_x, column_y, False, int, sheet_name)[1],
                    column_x, column_y, sheet_name, columnspan, str, date))
            if column_y == 'Bonus':
                self.sortDownB.grid_forget()
                self.sortDownB.grid(row=6, column=7, sticky=N)
            else:
                self.sortDownB.grid_forget()
                self.sortDownB.grid(row=6, column=7, sticky=N, pady=140)
            if column_y == 'Oklad':
                self.sort_oklad_command(column_x, column_y, sheet_name, columnspan, str, date)
                self.sort_7_9_RB.grid(row=6, column=5, columnspan=2, sticky=N+W)
                self.sort_9_11_RB.grid(row=6, column=5, columnspan=2, sticky=N+W, pady=45)
                self.sort_11_13_RB.grid(row=6, column=5, columnspan=2, sticky=N+W, pady=90)
                self.sort_13_15_RB.grid(row=6, column=5, columnspan=2, sticky=N+W, pady=135)
                self.sort_15_RB.grid(row=6, column=5, columnspan=2, sticky=N+W, pady=180)
                self.sort_Up_Down_oklad_Select(self.choise_oklad, column_x, column_y, sheet_name, columnspan, str, date)
            else: self.sort_oklad_buttons_fogget()
        elif str == False and date == True:
            self.sort_age_command(column_x, column_y, sheet_name, columnspan, str, date)

            self.sort_20_30_RB.grid(row=6, column=6, sticky=N+W)
            self.sort_30_40_RB.grid(row=6, column=6, sticky=N+W, pady=45)
            self.sort_40_50_RB.grid(row=6, column=6, sticky=N+W, pady=90)
            self.sort_50_60_RB.grid(row=6, column=6, sticky=N+W, pady=135)
            self.sort_60_70_RB.grid(row=6, column=6, sticky=N+W, pady=180)
            self.sort_70_RB.grid(row=6, column=6, sticky=N+W, pady=225)

            self.sort_Up_Down_Select(self.choise_age, column_x, column_y, sheet_name, columnspan, str, date)
            self.sortUpB.grid(row=6, column=7, sticky=N + E)
            self.sortDownB.grid(row=6, column=7, sticky=N, pady=140)

    def sort_age_command(self, column_x, column_y, sheet_name, columnspan, str, date):
        self.sort_20_30_RB.configure(
            command=lambda: self.infoStaffX(
                Sort.sort_BY_age(Sort(), 20, 30, True, sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
        self.sort_30_40_RB.configure(
            command=lambda: self.infoStaffX(
                Sort.sort_BY_age(Sort(), 30, 40, True, sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
        self.sort_40_50_RB.configure(
            command=lambda: self.infoStaffX(
                Sort.sort_BY_age(Sort(), 40, 50, True, sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
        self.sort_50_60_RB.configure(
            command=lambda: self.infoStaffX(
                Sort.sort_BY_age(Sort(), 50, 60, True, sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
        self.sort_60_70_RB.configure(
            command=lambda: self.infoStaffX(
                Sort.sort_BY_age(Sort(), 60, 70, True,sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
        self.sort_70_RB.configure(
            command=lambda: self.infoStaffX(
                Sort.sort_BY_age(Sort(), 70, 90, True, sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))

    def sort_oklad_command(self, column_x, column_y, sheet_name, columnspan, str, date):
        self.sort_7_9_RB.configure(
            command=lambda: self.infoStaffX(
                Sort.sort_BY_oklad(Sort(), 7000, 9000, True, sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
        self.sort_9_11_RB.configure(
            command=lambda: self.infoStaffX(
                Sort.sort_BY_oklad(Sort(), 9000, 11000, True, sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
        self.sort_11_13_RB.configure(
            command=lambda: self.infoStaffX(
                Sort.sort_BY_oklad(Sort(), 11000, 13000, True, sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
        self.sort_13_15_RB.configure(
            command=lambda: self.infoStaffX(
                Sort.sort_BY_oklad(Sort(), 13000, 15000, True, sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
        self.sort_15_RB.configure(
            command=lambda: self.infoStaffX(
                Sort.sort_BY_oklad(Sort(), 15000, 25000, True, sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
        self.sort_Up_Down_oklad_Select(self.choise_oklad, column_x, column_y, sheet_name, columnspan, str, date)


    def sort_Up_Down_Select(self, choise_age, column_x, column_y, sheet_name, columnspan, str, date):
        select = choise_age.get()
        if select == 30:
            self.sortUpB.configure(
                    command=lambda: self.infoStaffX(
                        Sort.sort_BY_age(Sort(), 20, 30, True, sheet_name), '',
                        column_x, column_y, sheet_name, columnspan, str, date))
            self.sortDownB.configure(
            command=lambda: self.infoStaffX(
                Sort.sort_BY_age(Sort(), 20, 30, False,sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
        elif select == 40:
            self.sortUpB.configure(
                    command=lambda: self.infoStaffX(
                        Sort.sort_BY_age(Sort(), 30, 40, True, sheet_name), '',
                        column_x, column_y, sheet_name, columnspan, str, date))
            self.sortDownB.configure(
            command=lambda: self.infoStaffX(
                Sort.sort_BY_age(Sort(), 30, 40, False,sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
        elif select == 50:
            self.sortUpB.configure(
                    command=lambda: self.infoStaffX(
                        Sort.sort_BY_age(Sort(), 40, 50, True, sheet_name), '',
                        column_x, column_y, sheet_name, columnspan, str, date))
            self.sortDownB.configure(
            command=lambda: self.infoStaffX(
                Sort.sort_BY_age(Sort(), 40, 50, False,sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
        elif select == 60:
            self.sortUpB.configure(
                    command=lambda: self.infoStaffX(
                        Sort.sort_BY_age(Sort(), 50, 60, True, sheet_name), '',
                        column_x, column_y, sheet_name, columnspan, str, date))
            self.sortDownB.configure(
            command=lambda: self.infoStaffX(
                Sort.sort_BY_age(Sort(), 50, 60, False, sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
        elif select == 70:
            self.sortUpB.configure(
                    command=lambda: self.infoStaffX(
                        Sort.sort_BY_age(Sort(), 60, 70, True, sheet_name), '',
                        column_x, column_y, sheet_name, columnspan, str, date))
            self.sortDownB.configure(
            command=lambda: self.infoStaffX(
                Sort.sort_BY_age(Sort(), 60, 70, False,sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
        elif select == 80:
            self.sortUpB.configure(
                    command=lambda: self.infoStaffX(
                        Sort.sort_BY_age(Sort(), 70, 90, True, sheet_name), '',
                        column_x, column_y, sheet_name, columnspan, str, date))
            self.sortDownB.configure(
            command=lambda: self.infoStaffX(
                Sort.sort_BY_age(Sort(), 70, 90, False), '',
                column_x, column_y, sheet_name, columnspan, str, date))
        else:
            self.sortUpB.configure(
                command=lambda: self.infoStaffX(
                    Sort.sortByDate(Sort(), column_x, column_y, True, sheet_name)[0],
                    Sort.sortByDate(Sort(), column_x, column_y, True,sheet_name)[1],
                    column_x, column_y, sheet_name, columnspan, str, date))
            self.sortDownB.configure(
                command=lambda: self.infoStaffX(
                    Sort.sortByDate(Sort(), column_x, column_y, False,sheet_name)[0],
                    Sort.sortByDate(Sort(), column_x, column_y, False,sheet_name)[1],
                    column_x, column_y, sheet_name, columnspan, str, date))

    def sort_Up_Down_oklad_Select(self, choise_oklad, column_x, column_y, sheet_name, columnspan, str, date):
        select = choise_oklad.get()
        if select == 7000:
            self.sortUpB.configure(command=lambda: self.infoStaffX(
                Sort.sort_BY_oklad(Sort(), 7000, 9000, True, sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
            self.sortDownB.configure(command=lambda: self.infoStaffX(
                Sort.sort_BY_oklad(Sort(), 7000, 9000, False,sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))

        elif select == 9000:
            self.sortUpB.configure(command=lambda: self.infoStaffX(
                Sort.sort_BY_oklad(Sort(), 9000, 11000, True, sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
            self.sortDownB.configure(command=lambda: self.infoStaffX(
                Sort.sort_BY_oklad(Sort(), 9000, 11000, False, sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
        elif select == 11000:
            self.sortUpB.configure(command=lambda: self.infoStaffX(
                Sort.sort_BY_oklad(Sort(), 11000, 13000, True, sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
            self.sortDownB.configure(command=lambda: self.infoStaffX(
                Sort.sort_BY_oklad(Sort(), 11000, 13000, False,sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
        elif select == 13000:
            self.sortUpB.configure(command=lambda: self.infoStaffX(
                Sort.sort_BY_oklad(Sort(), 13000, 15000, True, sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
            self.sortDownB.configure(command=lambda: self.infoStaffX(
                Sort.sort_BY_oklad(Sort(), 13000, 15000, False, sheet_name), '',
                column_x, column_y, sheet_name, columnspan, str, date))
        elif select == 15000:
            self.sortUpB.configure(
                command=lambda: self.infoStaffX(
                    Sort.sort_BY_oklad(Sort(), 15000, 25000, True, sheet_name), '',
                    column_x, column_y, sheet_name, columnspan, str, date))
            self.sortDownB.configure(
                command=lambda: self.infoStaffX(
                    Sort.sort_BY_oklad(Sort(), 15000, 25000, False,sheet_name), '',
                    column_x, column_y, sheet_name, columnspan, str, date))
        else:
            self.sortUpB.configure(
                command=lambda: self.infoStaffX(
                    Sort.sortByValue(Sort(), column_x, column_y, True, int, sheet_name)[0],
                    Sort.sortByValue(Sort(), column_x, column_y, True, int, sheet_name)[1],
                    column_x, column_y, sheet_name, columnspan, str, date))
            self.sortDownB.configure(
                command=lambda: self.infoStaffX(
                    Sort.sortByValue(Sort(), column_x, column_y, False, int, sheet_name)[0],
                    Sort.sortByValue(Sort(), column_x, column_y, False, int, sheet_name)[1],
                    column_x, column_y, sheet_name, columnspan, str, date))


    def sort_age_buttons_fogget(self):
        self.sort_20_30_RB.grid_forget()
        self.sort_30_40_RB.grid_forget()
        self.sort_40_50_RB.grid_forget()
        self.sort_50_60_RB.grid_forget()
        self.sort_60_70_RB.grid_forget()
        self.sort_70_RB.grid_forget()

    def sort_oklad_buttons_fogget(self):
        self.sort_7_9_RB.grid_forget()
        self.sort_9_11_RB.grid_forget()
        self.sort_11_13_RB.grid_forget()
        self.sort_13_15_RB.grid_forget()
        self.sort_15_RB.grid_forget()

    def path_serverF(self):
        path_cort = ("path_server.txt", "path_backup.txt")
        path = "res/txtFiles/"
        str = ''
        list_path = []
        for i in range(0,2):
            with open (Path(pathlib.Path.cwd(), path, path_cort[i]), 'r') as file:
                for line in file:
                    str += line
                list = str.splitlines()
                list_path.append(list[0])
                str = ''
        path_server = list_path[0]
        path_backup = list_path[1]
        path_all = [path_server, path_backup]
        mb_text = ['Укажите директорию с данными','Укажите директорию с архивом']
        for i in range(0, 2):
            if not os.path.exists(path_all[i]):
                if mb.showinfo("Укажите путь", mb_text[i]):
                    path_all[i] = tkinter.filedialog.askdirectory()
                    with open(Path(pathlib.Path.cwd(), path, 'path_tmp.txt'), 'w') as file:
                        file.write(path_all[i])
                    os.remove(Path(pathlib.Path.cwd(), path, path_cort[i]))
                    os.rename(Path(pathlib.Path.cwd(), path, 'path_tmp.txt'),
                              Path(pathlib.Path.cwd(), path, path_cort[i]))
        return (path_server, path_backup)

    def openFolder(self):
        import os
        import shutil
        path_server = self.path_serverF()[0]
        path_backup = self.path_serverF()[1]

        try:
            for src_dir, dirs, files in os.walk(path_server):
                dst_dir = src_dir.replace(path_server, path_backup, 1)
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)
                for file_ in files:
                    srs_file = os.path.join(src_dir, file_)
                    dst_file = os.path.join(dst_dir, file_)
                    if os.path.exists(dst_file):
                        os.remove(dst_file)
                    shutil.copy(srs_file, dst_dir)
            os.startfile(os.path.realpath(path_server))
        except IOError:
            mb.showinfo('Сервер не доступен', "Загружаю внутреннию копию")
            os.startfile(os.path.realpath(path_backup))

    def averOklad(self):
        if self.averOklad_B['text'] == "unclicked":
            df = pd.read_excel(Path(pathlib.Path.cwd(), 'NDL6Staff.xlsx'))
            aver = int(df['Oklad'].mean())
            aver = round(aver)
            strAverOklad = f"{aver}"
            all_sum = 0
            for i in range(0, len(df.Oklad)):
                all_sum += df.Oklad[i] + int(df.Oklad[i] * (df.Bonus[i] / 100))
            averZar = all_sum / len(df.Oklad)
            averZar = round(averZar)
            strAverZar = f'{averZar}'
            strAverL = f'{strAverOklad}\n{strAverZar}'
            self.averZarL = Label(self.root,
                                    text=strAverL, justify=LEFT, font=('Times New Roman', 36, 'bold'),
                                    bg='#0d4760', fg='#0de02d').grid(row=0, column=1, columnspan=1, sticky=W+E)
            self.averOklad_B['text'] = "clicked"
        elif self.averOklad_B['text'] == "clicked":
            strAverL = '    \n    '
            self.averZarL = Label(self.root,
                                  text=strAverL, justify=LEFT, font=('Times New Roman', 36, 'bold'),
                                  bg='#0d4760', fg='#0de02d').grid(row=0, column=1, columnspan=1, sticky=W + E)
            self.averOklad_B['text'] = "unclicked"

    def listGroup(self):
        if self.listGroup_B['text'] == "unclicked":
            self.folderB.grid_forget()
            self.NDL6RB.grid(row=0, column=5, sticky=W + N)
            self.GPRB.grid(row=0, column=6, sticky=W + N)
            self.GIBRB.grid(row=0, column=5, sticky=W)
            self.GIMRB.grid(row=0, column=6, sticky=W)
            self.GARB.grid(row=0, column=5, sticky=W + S)
            self.GNORB.grid(row=0, column=6, sticky=W + S)
            self.listGroup_B.configure(text='clicked')
        elif self.listGroup_B['text'] == "clicked":
            self.rb_grid_fogget()
            self.folderB.grid(row=0, column=5)
            self.listGroup_B.configure(text='unclicked')

    def rb_grid_fogget(self):
        self.NDL6RB.grid_forget()
        self.NDL6RB.grid_forget()
        self.GPRB.grid_forget()
        self.GIBRB.grid_forget()
        self.GIMRB.grid_forget()
        self.GARB.grid_forget()
        self.GNORB.grid_forget()

    def selected_Group(self):
        cort = ("NDL6Staff", 'GP', 'GIB', 'GIM', 'GOI', 'GNO')
        for i in range(0, len(cort)):
            if self.choise_group.get()==i+1:
                self.infoStaffAL.grid_forget()
                self.infoStaffBL.grid_forget()
                self.sortDownB.grid_forget()
                self.sortUpB.grid_forget()
                self.buttons(cort[i])
                self.run()

    def addUserRun(self):
        self.root.destroy()
        ad = LoginWindow('add')
        ad.run()

    def delUserRun(self):
        self.root.destroy()
        delStaf = LoginWindow('remove')
        delStaf.run()

    def editUserRun(self):
        self.root.destroy()
        edit = LoginWindow('edit')
        edit.run()








