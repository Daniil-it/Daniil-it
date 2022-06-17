from tkinter import *
import math
import os
from PIL import Image, ImageTk 

#=================Создаём главный класс===================
class Parent(Frame):
    def __init__(self, parent):
         Frame.__init__(self, parent)
         print(parent.geometry())
         self.x_window = int(str(parent.geometry())[:str(parent.geometry()).index('x')]) # положение окна по х
         self.y_window = int(str(parent.geometry())[str(parent.geometry()).index('x')+1:str(parent.geometry()).index('+')]) # положение окна по y
         self.parent = parent
         self.setUI()
         self.sc1, self.sc2 = self.parent.winfo_screenwidth(), self.parent.winfo_screenheight()
         self.main_ui = True
         self.reshebnick_ui = False
         self.voluems_ui = False
         self.square_ui = False
         self.radiuses_ui = False
         self.discriminant_ui = False
         self.et_ui = False
         self.average_ui = False
         self.instruction_ui = False
         self.about_us_ui = False
         self.tumbler_size = False

         #================установка фона===================
    def background_ui(self, file):
        self.image = Image.open(file)
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)

         #================установка элементов===================
    def setUI(self):
        self.all_widgets = []
        self.pack(fill=BOTH, expand=1)  #-------- Размещаем активные элементы на родительском окне--------

        self.background_ui("background.jpg")
        self.background = Label(self, image=self.background_image, bd=0) #, width = self.x_window, heigh = self.y_window
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize)
        #-------- начальный экран--------
        self.main_widgets = []
        self.first = Button(self, text="Решебник", width=20, font='Arial 30 bold', command=lambda: self.reshebnick()) #-----кнопка------
        self.first.place(x=self.place_count(2, 1, 'hor', self.first.winfo_width()), y=self.place_count(4, 1, 'ver', self.first.winfo_height()))
        self.all_widgets.append(self.first)
        self.main_widgets.append(self.first)
        self.second = Button(self, text="Инструкция", width=20, font='Arial 30 bold', command=lambda: self.instruction()) #-----кнопка------
        self.second.place(x=self.place_count(2, 1, 'hor', self.second.winfo_width()), y=self.place_count(4, 2, 'ver', self.second.winfo_height()))
        self.all_widgets.append(self.second)
        self.main_widgets.append(self.second)
        self.third = Button(self, text="Информация\nоб авторе", width=20, font='Arial 30 bold', command=lambda: self.about_us()) #-----кнопка------
        self.third.place(x=self.place_count(2, 1, 'hor', self.third.winfo_width()), y=self.place_count(4, 3, 'ver', self.third.winfo_height()))
        self.all_widgets.append(self.third)
        self.main_widgets.append(self.third)
        self.exit = Button(self, text="Выход", width=7, font='Arial 24 bold', command=lambda: self.qutit()) #-----кнопка------
        self.exit.place(x=self.place_count(2, 1, 'hor', self.third.winfo_width()), y=self.place_count(4, 4, 'ver', self.third.winfo_height()))
        self.all_widgets.append(self.exit)
        self.main_widgets.append(self.exit)
        
        #-------- решебник--------
        self.reshebnick_widgets = []
        self.volume = Button(self, text="Объёмы", width=8, font='Arial 24 bold', command=lambda: self.volume_func()) #-----кнопка------
        self.all_widgets.append(self.volume)
        self.reshebnick_widgets.append(self.volume)
        self.square = Button(self, text="Площади", width=9, font='Arial 24 bold', command=lambda: self.squar_func()) #-----кнопка------
        self.all_widgets.append(self.square)
        self.reshebnick_widgets.append(self.square)
        self.radius = Button(self, text="Радиусы", width=9, font='Arial 24 bold', command=lambda: self.radius_func()) #-----кнопка------
        self.all_widgets.append(self.radius)
        self.reshebnick_widgets.append(self.radius)
        self.discriminant = Button(self, text="Дискриминант", width=15, font='Arial 24 bold', command=lambda: self.discriminant_func()) #-----кнопка------
        self.all_widgets.append(self.discriminant)
        self.reshebnick_widgets.append(self.discriminant)
        self.Existence_of_a_triangle = Button(self, text="Существование треугольника", width=29, font='Arial 24 bold', command=lambda: self.et_func()) #-----кнопка------
        self.all_widgets.append(self.Existence_of_a_triangle)
        self.reshebnick_widgets.append(self.Existence_of_a_triangle)
        self.arithmetic_mean = Button(self, text="Среднее арифметическое", width=25, font='Arial 24 bold', command=lambda: self.average_func()) #-----кнопка------
        self.all_widgets.append(self.arithmetic_mean)
        self.reshebnick_widgets.append(self.arithmetic_mean)
        self.back1 = Button(self, text="Назад", width=7, font='Arial 24 bold', command=lambda: self.main_view()) #-----кнопка------
        self.all_widgets.append(self.back1)
        self.reshebnick_widgets.append(self.back1)
        #-------- объемы--------
        self.volumies_widgets = []
        self.back11 = Button(self, text="<==", width=5, font='Arial 16 bold', command=lambda: self.reshebnick()) #-----кнопка------
        self.all_widgets.append(self.back11)
        self.volumies_widgets.append(self.back11)
        self.RPV_label = Label(self, text="Объем прямоугольной призмы", width=30, font='Arial 18 bold')
        self.all_widgets.append(self.RPV_label)
        self.volumies_widgets.append(self.RPV_label)
        self.RPV_formula = Label(self, text="Формула: V = HWL", width=20, font='Arial 16 bold')
        self.all_widgets.append(self.RPV_formula)
        self.volumies_widgets.append(self.RPV_formula)
        self.RPV_WL = Label(self, text="Ширина (W)", width=12, font='Arial 12 bold')
        self.all_widgets.append(self.RPV_WL)
        self.volumies_widgets.append(self.RPV_WL)
        self.RPV_HL = Label(self, text="Высота (H)", width=12, font='Arial 12 bold')
        self.all_widgets.append(self.RPV_HL)
        self.volumies_widgets.append(self.RPV_HL)
        self.RPV_LL = Label(self, text="Длина (L)", width=12, font='Arial 12 bold')
        self.all_widgets.append(self.RPV_LL)
        self.volumies_widgets.append(self.RPV_LL)
        self.RPV_WE = Entry(self, width=12, font='Arial 12 bold')
        self.all_widgets.append(self.RPV_WE)
        self.volumies_widgets.append(self.RPV_WE)
        self.RPV_HE = Entry(self, width=12, font='Arial 12 bold')
        self.all_widgets.append(self.RPV_HE)
        self.volumies_widgets.append(self.RPV_HE)
        self.RPV_LE = Entry(self, width=12, font='Arial 12 bold')
        self.all_widgets.append(self.RPV_LE)
        self.volumies_widgets.append(self.RPV_LE)
        self.RPV_answerL = Label(self, text="Ответ:", width=30, font='Arial 16 bold')
        self.all_widgets.append(self.RPV_answerL)
        self.volumies_widgets.append(self.RPV_answerL)
        self.RPV_answerB = Button(self, text="Расчитать", width=10, font='Arial 14 bold', command=lambda: self.RPV()) #-----кнопка------
        self.all_widgets.append(self.RPV_answerB)
        self.volumies_widgets.append(self.RPV_answerB)
        self.CV_label = Label(self, text="Объем цилиндра", width=30, font='Arial 18 bold')
        self.all_widgets.append(self.CV_label)
        self.volumies_widgets.append(self.CV_label)
        self.CV_formula = Label(self, text="Формула: V = pR^2H", width=20, font='Arial 16 bold')
        self.all_widgets.append(self.CV_formula)
        self.volumies_widgets.append(self.CV_formula)
        self.CV_HL = Label(self, text="Высота (H)", width=12, font='Arial 12 bold')
        self.all_widgets.append(self.CV_HL)
        self.volumies_widgets.append(self.CV_HL)
        self.CV_RL = Label(self, text="Радиус (R)", width=12, font='Arial 12 bold')
        self.all_widgets.append(self.CV_RL)
        self.volumies_widgets.append(self.CV_RL)
        self.CV_HE = Entry(self, width=12, font='Arial 12 bold')
        self.all_widgets.append(self.CV_HE)
        self.volumies_widgets.append(self.CV_HE)
        self.CV_RE = Entry(self, width=12, font='Arial 12 bold')
        self.all_widgets.append(self.CV_RE)
        self.volumies_widgets.append(self.CV_RE)
        self.CV_answerL = Label(self, text="Ответ:", width=30, font='Arial 16 bold')
        self.all_widgets.append(self.CV_answerL)
        self.volumies_widgets.append(self.CV_answerL)
        self.CV_answerB = Button(self, text="Расчитать", width=10, font='Arial 14 bold', command=lambda: self.CV()) #-----кнопка------
        self.all_widgets.append(self.CV_answerB)
        self.volumies_widgets.append(self.CV_answerB)
        #-------- Площади--------
        self.square_widgets = []
        self.back12 = Button(self, text="<==", width=5, font='Arial 16 bold', command=lambda: self.reshebnick()) #-----кнопка------
        self.all_widgets.append(self.back12)
        self.square_widgets.append(self.back12)
        self.Aoat_label = Label(self, text="Площадь треугольника", width=30, font='Arial 18 bold')
        self.all_widgets.append(self.Aoat_label)
        self.square_widgets.append(self.Aoat_label)
        self.Aoat_formula = Label(self, text="Формула: S = (1/2)*AH", width=20, font='Arial 16 bold')
        self.all_widgets.append(self.Aoat_formula)
        self.square_widgets.append(self.Aoat_formula)
        self.Aoat_aL = Label(self, text="Основание (a)", width=12, font='Arial 12 bold')
        self.all_widgets.append(self.Aoat_aL)
        self.square_widgets.append(self.Aoat_aL)
        self.Aoat_HL = Label(self, text="Высота (H)", width=12, font='Arial 12 bold')
        self.all_widgets.append(self.Aoat_HL)
        self.square_widgets.append(self.Aoat_HL)
        self.Aoat_aE = Entry(self, width=12, font='Arial 12 bold')
        self.all_widgets.append(self.Aoat_aE)
        self.square_widgets.append(self.Aoat_aE)
        self.Aoat_HE = Entry(self, width=12, font='Arial 12 bold')
        self.all_widgets.append(self.Aoat_HE)
        self.square_widgets.append(self.Aoat_HE)
        self.Aoat_answerL = Label(self, text="Ответ:", width=30, font='Arial 16 bold')
        self.all_widgets.append(self.Aoat_answerL)
        self.square_widgets.append(self.Aoat_answerL)
        self.Aoat_answerB = Button(self, text="Расчитать", width=10, font='Arial 14 bold', command=lambda: self.Aoat()) #-----кнопка------
        self.all_widgets.append(self.Aoat_answerB)
        self.square_widgets.append(self.Aoat_answerB)
        self.Aoac_label = Label(self, text="Площадь круга", width=30, font='Arial 18 bold')
        self.all_widgets.append(self.Aoac_label)
        self.square_widgets.append(self.Aoac_label)
        self.Aoac_formula = Label(self, text="Формула: S = piR^2", width=20, font='Arial 16 bold')
        self.all_widgets.append(self.Aoac_formula)
        self.square_widgets.append(self.Aoac_formula)
        self.Aoac_RL = Label(self, text="Радиус (R)", width=12, font='Arial 12 bold')
        self.all_widgets.append(self.Aoac_RL)
        self.square_widgets.append(self.Aoac_RL)
        self.Aoac_RE = Entry(self, width=12, font='Arial 12 bold')
        self.all_widgets.append(self.Aoac_RE)
        self.square_widgets.append(self.Aoac_RE)
        self.Aoac_answerL = Label(self, text="Ответ:", width=30, font='Arial 16 bold')
        self.all_widgets.append(self.Aoac_answerL)
        self.square_widgets.append(self.Aoac_answerL)
        self.Aoac_answerB = Button(self, text="Расчитать", width=10, font='Arial 14 bold', command=lambda: self.Aoac()) #-----кнопка------
        self.all_widgets.append(self.Aoac_answerB)
        self.square_widgets.append(self.Aoac_answerB)
        #-------- радиусы--------
        self.radius_widgets = []
        self.back13 = Button(self, text="<==", width=5, font='Arial 16 bold', command=lambda: self.reshebnick()) #-----кнопка------
        self.all_widgets.append(self.back13)
        self.radius_widgets.append(self.back13)
        self.rctil_label = Label(self, text="Радиус окружности через её длину", width=30, font='Arial 18 bold')
        self.all_widgets.append(self.rctil_label)
        self.radius_widgets.append(self.rctil_label)
        self.rctil_formula = Label(self, text="Формула: R = P/(2pi)", width=20, font='Arial 16 bold')
        self.all_widgets.append(self.rctil_formula)
        self.radius_widgets.append(self.rctil_formula)
        self.rctil_PL = Label(self, text="Длина окружности(P)", width=20, font='Arial 12 bold')
        self.all_widgets.append(self.rctil_PL)
        self.radius_widgets.append(self.rctil_PL)
        self.rctil_PE = Entry(self, width=12, font='Arial 12 bold')
        self.all_widgets.append(self.rctil_PE)
        self.radius_widgets.append(self.rctil_PE)
        self.rctil_answerL = Label(self, text="Ответ:", width=30, font='Arial 16 bold')
        self.all_widgets.append(self.rctil_answerL)
        self.radius_widgets.append(self.rctil_answerL)
        self.rctil_answerB = Button(self, text="Расчитать", width=10, font='Arial 14 bold', command=lambda: self.rctil()) #-----кнопка------
        self.all_widgets.append(self.rctil_answerB)
        self.radius_widgets.append(self.rctil_answerB)
        self.rctis_label = Label(self, text="Радиус окружности через площадь", width=30, font='Arial 18 bold')
        self.all_widgets.append(self.rctis_label)
        self.radius_widgets.append(self.rctis_label)
        self.rctis_formula = Label(self, text="Формула: R = (S/pi)^0.5", width=20, font='Arial 16 bold')
        self.all_widgets.append(self.rctis_formula)
        self.radius_widgets.append(self.rctis_formula)
        self.rctis_SL = Label(self, text="Площадь(S)", width=12, font='Arial 12 bold')
        self.all_widgets.append(self.rctis_SL)
        self.radius_widgets.append(self.rctis_SL)
        self.rctis_SE = Entry(self, width=12, font='Arial 12 bold')
        self.all_widgets.append(self.rctis_SE)
        self.radius_widgets.append(self.rctis_SE)
        self.rctis_answerL = Label(self, text="Ответ:", width=30, font='Arial 16 bold')
        self.all_widgets.append(self.rctis_answerL)
        self.radius_widgets.append(self.rctis_answerL)
        self.rctis_answerB = Button(self, text="Расчитать", width=10, font='Arial 14 bold', command=lambda: self.rctis()) #-----кнопка------
        self.all_widgets.append(self.rctis_answerB)
        self.radius_widgets.append(self.rctis_answerB)
        #-------- Дискриминант--------
        self.discriminant_widgets = []
        self.back14 = Button(self, text="<==", width=5, font='Arial 16 bold', command=lambda: self.reshebnick()) #-----кнопка------
        self.all_widgets.append(self.back14)
        self.discriminant_widgets.append(self.back14)
        self.dis_label = Label(self, text="Вычисление дискриминанта", width=30, font='Arial 18 bold')
        self.all_widgets.append(self.dis_label)
        self.discriminant_widgets.append(self.dis_label)
        self.dis_formula = Label(self, text="Формула: D = b^2-4ac", width=20, font='Arial 16 bold')
        self.all_widgets.append(self.dis_formula)
        self.discriminant_widgets.append(self.dis_formula)
        self.dis_aL = Label(self, text="a", width=12, font='Arial 12 bold')
        self.all_widgets.append(self.dis_aL)
        self.discriminant_widgets.append(self.dis_aL)
        self.dis_bL = Label(self, text="b", width=12, font='Arial 12 bold')
        self.all_widgets.append(self.dis_bL)
        self.discriminant_widgets.append(self.dis_bL)
        self.dis_cL = Label(self, text="c", width=12, font='Arial 12 bold')
        self.all_widgets.append(self.dis_cL)
        self.discriminant_widgets.append(self.dis_cL)
        self.dis_aE = Entry(self, width=12, font='Arial 12 bold')
        self.all_widgets.append(self.dis_aE)
        self.discriminant_widgets.append(self.dis_aE)
        self.dis_bE = Entry(self, width=12, font='Arial 12 bold')
        self.all_widgets.append(self.dis_bE)
        self.discriminant_widgets.append(self.dis_bE)
        self.dis_cE = Entry(self, width=12, font='Arial 12 bold')
        self.all_widgets.append(self.dis_cE)
        self.discriminant_widgets.append(self.dis_cE)
        self.dis_answerL = Label(self, text="Ответ:", width=30, font='Arial 16 bold')
        self.all_widgets.append(self.dis_answerL)
        self.discriminant_widgets.append(self.dis_answerL)
        self.dis_answerB = Button(self, text="Расчитать", width=10, font='Arial 14 bold', command=lambda: self.dis()) #-----кнопка------
        self.all_widgets.append(self.dis_answerB)
        self.discriminant_widgets.append(self.dis_answerB)
        #-------- Существование Треугольника--------
        self.et_widgets = []
        self.back15 = Button(self, text="<==", width=5, font='Arial 16 bold', command=lambda: self.reshebnick()) #-----кнопка------
        self.all_widgets.append(self.back15)
        self.et_widgets.append(self.back15)
        self.et_label = Label(self, text="Существование треугольника", width=30, font='Arial 18 bold')
        self.all_widgets.append(self.et_label)
        self.et_widgets.append(self.et_label)
        self.et_formula = Label(self, text="Формула: a+b>c, b+c>a, a+c>b", width=25, font='Arial 16 bold')
        self.all_widgets.append(self.et_formula)
        self.et_widgets.append(self.et_formula)
        self.et_aL = Label(self, text="a", width=12, font='Arial 12 bold')
        self.all_widgets.append(self.et_aL)
        self.et_widgets.append(self.et_aL)
        self.et_bL = Label(self, text="b", width=12, font='Arial 12 bold')
        self.all_widgets.append(self.et_bL)
        self.et_widgets.append(self.et_bL)
        self.et_cL = Label(self, text="c", width=12, font='Arial 12 bold')
        self.all_widgets.append(self.et_cL)
        self.et_widgets.append(self.et_cL)
        self.et_aE = Entry(self, width=12, font='Arial 12 bold')
        self.all_widgets.append(self.et_aE)
        self.et_widgets.append(self.et_aE)
        self.et_bE = Entry(self, width=12, font='Arial 12 bold')
        self.all_widgets.append(self.et_bE)
        self.et_widgets.append(self.et_bE)
        self.et_cE = Entry(self, width=12, font='Arial 12 bold')
        self.all_widgets.append(self.et_cE)
        self.et_widgets.append(self.et_cE)
        self.et_answerL = Label(self, text="Ответ:", width=30, font='Arial 16 bold')
        self.all_widgets.append(self.et_answerL)
        self.et_widgets.append(self.et_answerL)
        self.et_answerB = Button(self, text="Расчитать", width=10, font='Arial 14 bold', command=lambda: self.et()) #-----кнопка------
        self.all_widgets.append(self.et_answerB)
        self.et_widgets.append(self.et_answerB)
        #-------- Среднее арифметическое--------
        self.average_widgets = []
        self.back16 = Button(self, text="<==", width=5, font='Arial 16 bold', command=lambda: self.reshebnick()) #-----кнопка------
        self.all_widgets.append(self.back16)
        self.average_widgets.append(self.back16)
        self.average_label = Label(self, text="Среднее арифметическое", width=30, font='Arial 18 bold')
        self.all_widgets.append(self.average_label)
        self.average_widgets.append(self.average_label)
        self.average_formula = Label(self, text="Формула: (a1+a2+...+an)/n", width=25, font='Arial 16 bold')
        self.all_widgets.append(self.average_formula)
        self.average_widgets.append(self.average_formula)
        self.average_aL = Label(self, text="Введите значения элементов через пробел(a):", width=40, font='Arial 12 bold')
        self.all_widgets.append(self.average_aL)
        self.average_widgets.append(self.average_aL)
        self.average_aE = Entry(self, width=70, font='Arial 12 bold')
        self.all_widgets.append(self.average_aE)
        self.average_widgets.append(self.average_aE)
        self.average_answerL = Label(self, text="Ответ:", width=30, font='Arial 16 bold')
        self.all_widgets.append(self.average_answerL)
        self.average_widgets.append(self.average_answerL)
        self.average_answerB = Button(self, text="Расчитать", width=10, font='Arial 14 bold', command=lambda: self.average()) #-----кнопка------
        self.all_widgets.append(self.average_answerB)
        self.average_widgets.append(self.average_answerB)
        #-------- Инструкия --------
        self.instruction_widgets = []
        instruction_text = ''' Здравствуйте, раз вы открыли эту программу, моя обязанность ознакомить\n
вас с ней. Вы можете преходить по вкладкам с помощью кнопок на экране, так же\n
возвращаться обратно с помощью кнопки "Назад" или же "<=="\n
Так же на первой странице вы увидите переход на решебник, инструкцию и информацию об авторе\n
\tВ решебнике есть ещё несколько вкладок, подтем, в которые вы можете перейти\n
\tТам вы увидите автоматическое решение некоторых формул с их описанием и возможностью\n
\tввести значения. После их ввода требуется нажать кнопку "Расчитать",чтобы увидеть результат'''
        self.instruction_info = Label(self, text=instruction_text, width=100, heigh=100, font='Arial 16 bold')
        self.all_widgets.append(self.instruction_info)
        self.instruction_widgets.append(self.instruction_info)
        self.back2 = Button(self, text="Назад", width=7, font='Arial 24 bold', command=lambda: self.main_view()) #-----кнопка------
        self.all_widgets.append(self.back2)
        self.instruction_widgets.append(self.back2)
        #-------- Информаиция об авторе --------
        self.about_us_widgets = []
        instruction_text = ''' Решебник - это программа, которая поможет вам в нахождении\n
площади окружности, вычислении сущности треугольника, нахождении дискриминанта и т.д.\n
Не пользуйтесь этой программой для решения задач,\n
Ведь собственные знания важнее компьютерных\n
Программа служит для проверки решения\n
Желаю удачи\n\n
\t\t\tРазработчик: Зыков Даниил, ученик 9 класса'''
        self.about_us_info = Label(self, text=instruction_text, width=100, heigh=100, font='Arial 16 bold')
        self.all_widgets.append(self.about_us_info)
        self.about_us_widgets.append(self.about_us_info)
        self.back3 = Button(self, text="Назад", width=7, font='Arial 24 bold', command=lambda: self.main_view()) #-----кнопка------
        self.all_widgets.append(self.back3)
        self.about_us_widgets.append(self.back3)

        #================ровная растановка элементов===================
    def place_count(self, all_part, number_of_part, ver_hor, self_wh):
        if ver_hor == 'ver':
            y = math.floor(self.y_window/all_part*number_of_part)-math.ceil(self_wh/2)
            return y
        elif ver_hor == 'hor':
            x = math.floor(self.x_window/all_part*number_of_part)-math.ceil(self_wh/2)
            return x

        #================корректировка виджетов===================
    def _resize(self,event):
        self.x_window = int(str(self.parent.geometry())[:str(self.parent.geometry()).index('x')]) # положение окна по х
        self.y_window = int(str(self.parent.geometry())[str(self.parent.geometry()).index('x')+1:str(self.parent.geometry()).index('+')]) # положение окна по y
        self.image = self.img_copy.resize((self.x_window, self.y_window))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)

        if self.main_ui:
            self.first.place(x=self.place_count(2, 1, 'hor', self.first.winfo_width()), y=self.place_count(4, 1, 'ver', self.first.winfo_height()))
            self.second.place(x=self.place_count(2, 1, 'hor', self.second.winfo_width()), y=self.place_count(4, 2, 'ver', self.second.winfo_height()))
            self.third.place(x=self.place_count(2, 1, 'hor', self.third.winfo_width()), y=self.place_count(4, 3, 'ver', self.third.winfo_height()))
            self.exit.place(x=self.place_count(1, 1, 'hor', self.third.winfo_width()), y=self.place_count(5, 4, 'ver', self.exit.winfo_height()))

        if self.reshebnick_ui:
            self.volume.place(x=self.place_count(2, 1, 'hor', self.volume.winfo_width()), y=self.place_count(8, 1, 'ver', self.volume.winfo_height()))
            self.square.place(x=self.place_count(2, 1, 'hor', self.square.winfo_width()), y=self.place_count(8, 2, 'ver', self.square.winfo_height()))
            self.radius.place(x=self.place_count(2, 1, 'hor', self.radius.winfo_width()), y=self.place_count(8, 3, 'ver', self.radius.winfo_height()))
            self.discriminant.place(x=self.place_count(2, 1, 'hor', self.discriminant.winfo_width()), y=self.place_count(8, 4, 'ver', self.discriminant.winfo_height()))
            self.Existence_of_a_triangle.place(x=self.place_count(2, 1, 'hor', self.Existence_of_a_triangle.winfo_width()), y=self.place_count(8, 5, 'ver', self.Existence_of_a_triangle.winfo_height()))
            self.arithmetic_mean.place(x=self.place_count(2, 1, 'hor', self.arithmetic_mean.winfo_width()), y=self.place_count(8, 6, 'ver', self.arithmetic_mean.winfo_height()))
            self.back1.place(x=self.place_count(5, 4, 'hor', self.back1.winfo_width()), y=self.place_count(8, 7, 'ver', self.back1.winfo_height()))

        if self.voluems_ui:
            self.back11.place(x=self.place_count(12, 2, 'hor', self.back11.winfo_width()), y=self.place_count(18, 1, 'ver', self.back11.winfo_height()))
            self.RPV_label.place(x=self.place_count(7, 2, 'hor', self.RPV_label.winfo_width()), y=self.place_count(18, 2, 'ver', self.RPV_label.winfo_height()))
            self.RPV_formula.place(x=self.place_count(7, 2, 'hor', self.RPV_formula.winfo_width()), y=self.place_count(18, 3, 'ver', self.RPV_formula.winfo_height()))
            self.RPV_WL.place(x=self.place_count(7, 2, 'hor', self.RPV_WL.winfo_width()), y=self.place_count(18, 4, 'ver', self.RPV_WL.winfo_height()))
            self.RPV_HL.place(x=self.place_count(7, 4, 'hor', self.RPV_HL.winfo_width()), y=self.place_count(18, 4, 'ver', self.RPV_HL.winfo_height()))
            self.RPV_LL.place(x=self.place_count(7, 6, 'hor', self.RPV_LL.winfo_width()), y=self.place_count(18, 4, 'ver', self.RPV_LL.winfo_height()))
            self.RPV_WE.place(x=self.place_count(7, 2, 'hor', self.RPV_WE.winfo_width()), y=self.place_count(18, 5, 'ver', self.RPV_WE.winfo_height()))
            self.RPV_HE.place(x=self.place_count(7, 4, 'hor', self.RPV_HE.winfo_width()), y=self.place_count(18, 5, 'ver', self.RPV_HE.winfo_height()))
            self.RPV_LE.place(x=self.place_count(7, 6, 'hor', self.RPV_LE.winfo_width()), y=self.place_count(18, 5, 'ver', self.RPV_LE.winfo_height()))
            self.RPV_answerL.place(x=self.place_count(7, 3, 'hor', self.RPV_answerL.winfo_width()), y=self.place_count(18, 6, 'ver', self.RPV_answerL.winfo_height()))
            self.RPV_answerB.place(x=self.place_count(7, 6, 'hor', self.RPV_answerB.winfo_width()), y=self.place_count(18, 6, 'ver', self.RPV_answerB.winfo_height()))
            self.CV_label.place(x=self.place_count(7, 2, 'hor', self.CV_label.winfo_width()), y=self.place_count(18, 8, 'ver', self.CV_label.winfo_height()))
            self.CV_formula.place(x=self.place_count(7, 2, 'hor', self.CV_formula.winfo_width()), y=self.place_count(18, 9, 'ver', self.CV_formula.winfo_height()))
            self.CV_HL.place(x=self.place_count(7, 2, 'hor', self.CV_HL.winfo_width()), y=self.place_count(18, 10, 'ver', self.CV_HL.winfo_height()))
            self.CV_RL.place(x=self.place_count(7, 4, 'hor', self.CV_RL.winfo_width()), y=self.place_count(18, 10, 'ver', self.CV_RL.winfo_height()))
            self.CV_HE.place(x=self.place_count(7, 2, 'hor', self.CV_HE.winfo_width()), y=self.place_count(18, 11, 'ver', self.CV_HE.winfo_height()))
            self.CV_RE.place(x=self.place_count(7, 4, 'hor', self.CV_RE.winfo_width()), y=self.place_count(18, 11, 'ver', self.CV_RE.winfo_height()))
            self.CV_answerL.place(x=self.place_count(7, 3, 'hor', self.CV_answerL.winfo_width()), y=self.place_count(18, 12, 'ver', self.CV_answerL.winfo_height()))
            self.CV_answerB.place(x=self.place_count(7, 6, 'hor', self.CV_answerB.winfo_width()), y=self.place_count(18, 12, 'ver', self.CV_answerB.winfo_height()))

        if self.square_ui:
            self.back12.place(x=self.place_count(12, 2, 'hor', self.back12.winfo_width()), y=self.place_count(18, 1, 'ver', self.back12.winfo_height()))
            self.Aoat_label.place(x=self.place_count(7, 2, 'hor', self.Aoat_label.winfo_width()), y=self.place_count(18, 2, 'ver', self.Aoat_label.winfo_height()))
            self.Aoat_formula.place(x=self.place_count(7, 2, 'hor', self.Aoat_formula.winfo_width()), y=self.place_count(18, 3, 'ver', self.Aoat_formula.winfo_height()))
            self.Aoat_aL.place(x=self.place_count(7, 2, 'hor', self.Aoat_aL.winfo_width()), y=self.place_count(18, 4, 'ver', self.Aoat_aL.winfo_height()))
            self.Aoat_HL.place(x=self.place_count(7, 4, 'hor', self.Aoat_HL.winfo_width()), y=self.place_count(18, 4, 'ver', self.Aoat_HL.winfo_height()))
            self.Aoat_aE.place(x=self.place_count(7, 2, 'hor', self.Aoat_aE.winfo_width()), y=self.place_count(18, 5, 'ver', self.Aoat_aE.winfo_height()))
            self.Aoat_HE.place(x=self.place_count(7, 4, 'hor', self.Aoat_HE.winfo_width()), y=self.place_count(18, 5, 'ver', self.Aoat_HE.winfo_height()))
            self.Aoat_answerL.place(x=self.place_count(7, 3, 'hor', self.Aoat_answerL.winfo_width()), y=self.place_count(18, 6, 'ver', self.Aoat_answerL.winfo_height()))
            self.Aoat_answerB.place(x=self.place_count(7, 6, 'hor', self.Aoat_answerB.winfo_width()), y=self.place_count(18, 6, 'ver', self.Aoat_answerB.winfo_height()))
            self.Aoac_label.place(x=self.place_count(7, 2, 'hor', self.Aoac_label.winfo_width()), y=self.place_count(18, 8, 'ver', self.Aoac_label.winfo_height()))
            self.Aoac_formula.place(x=self.place_count(7, 2, 'hor', self.Aoac_formula.winfo_width()), y=self.place_count(18, 9, 'ver', self.Aoac_formula.winfo_height()))
            self.Aoac_RL.place(x=self.place_count(7, 2, 'hor', self.Aoac_RL.winfo_width()), y=self.place_count(18, 10, 'ver', self.Aoac_RL.winfo_height()))
            self.Aoac_RE.place(x=self.place_count(7, 2, 'hor', self.Aoac_RE.winfo_width()), y=self.place_count(18, 11, 'ver', self.Aoac_RE.winfo_height()))
            self.Aoac_answerL.place(x=self.place_count(7, 3, 'hor', self.Aoac_answerL.winfo_width()), y=self.place_count(18, 12, 'ver', self.Aoac_answerL.winfo_height()))
            self.Aoac_answerB.place(x=self.place_count(7, 6, 'hor', self.Aoac_answerB.winfo_width()), y=self.place_count(18, 12, 'ver', self.Aoac_answerB.winfo_height()))

        if self.radiuses_ui:
            self.back13.place(x=self.place_count(12, 2, 'hor', self.back13.winfo_width()), y=self.place_count(18, 1, 'ver', self.back13.winfo_height()))
            self.rctil_label.place(x=self.place_count(7, 2, 'hor', self.rctil_label.winfo_width()), y=self.place_count(18, 2, 'ver', self.rctil_label.winfo_height()))
            self.rctil_formula.place(x=self.place_count(7, 2, 'hor', self.rctil_formula.winfo_width()), y=self.place_count(18, 3, 'ver', self.rctil_formula.winfo_height()))
            self.rctil_PL.place(x=self.place_count(7, 2, 'hor', self.rctil_PL.winfo_width()), y=self.place_count(18, 4, 'ver', self.rctil_PL.winfo_height()))
            self.rctil_PE.place(x=self.place_count(7, 2, 'hor', self.rctil_PE.winfo_width()), y=self.place_count(18, 5, 'ver', self.rctil_PE.winfo_height()))
            self.rctil_answerL.place(x=self.place_count(7, 3, 'hor', self.rctil_answerL.winfo_width()), y=self.place_count(18, 6, 'ver', self.rctil_answerL.winfo_height()))
            self.rctil_answerB.place(x=self.place_count(7, 6, 'hor', self.rctil_answerB.winfo_width()), y=self.place_count(18, 6, 'ver', self.rctil_answerB.winfo_height()))
            self.rctis_label.place(x=self.place_count(7, 2, 'hor', self.rctis_label.winfo_width()), y=self.place_count(18, 8, 'ver', self.rctis_label.winfo_height()))
            self.rctis_formula.place(x=self.place_count(7, 2, 'hor', self.rctis_formula.winfo_width()), y=self.place_count(18, 9, 'ver', self.rctis_formula.winfo_height()))
            self.rctis_SL.place(x=self.place_count(7, 2, 'hor', self.rctis_SL.winfo_width()), y=self.place_count(18, 10, 'ver', self.rctis_SL.winfo_height()))
            self.rctis_SE.place(x=self.place_count(7, 2, 'hor', self.rctis_SE.winfo_width()), y=self.place_count(18, 11, 'ver', self.rctis_SE.winfo_height()))
            self.rctis_answerL.place(x=self.place_count(7, 3, 'hor', self.rctis_answerL.winfo_width()), y=self.place_count(18, 12, 'ver', self.rctis_answerL.winfo_height()))
            self.rctis_answerB.place(x=self.place_count(7, 6, 'hor', self.rctis_answerB.winfo_width()), y=self.place_count(18, 12, 'ver', self.rctis_answerB.winfo_height()))

        if self.discriminant_ui:
            self.back14.place(x=self.place_count(12, 2, 'hor', self.back14.winfo_width()), y=self.place_count(18, 1, 'ver', self.back14.winfo_height()))
            self.dis_label.place(x=self.place_count(7, 2, 'hor', self.dis_label.winfo_width()), y=self.place_count(18, 2, 'ver', self.dis_label.winfo_height()))
            self.dis_formula.place(x=self.place_count(7, 2, 'hor', self.dis_formula.winfo_width()), y=self.place_count(18, 3, 'ver', self.dis_formula.winfo_height()))
            self.dis_aL.place(x=self.place_count(7, 2, 'hor', self.dis_aL.winfo_width()), y=self.place_count(18, 4, 'ver', self.dis_aL.winfo_height()))
            self.dis_bL.place(x=self.place_count(7, 4, 'hor', self.dis_bL.winfo_width()), y=self.place_count(18, 4, 'ver', self.dis_bL.winfo_height()))
            self.dis_cL.place(x=self.place_count(7, 6, 'hor', self.dis_cL.winfo_width()), y=self.place_count(18, 4, 'ver', self.dis_cL.winfo_height()))
            self.dis_aE.place(x=self.place_count(7, 2, 'hor', self.dis_aE.winfo_width()), y=self.place_count(18, 5, 'ver', self.dis_aE.winfo_height()))
            self.dis_bE.place(x=self.place_count(7, 4, 'hor', self.dis_bE.winfo_width()), y=self.place_count(18, 5, 'ver', self.dis_bE.winfo_height()))
            self.dis_cE.place(x=self.place_count(7, 6, 'hor', self.dis_cE.winfo_width()), y=self.place_count(18, 5, 'ver', self.dis_cE.winfo_height()))
            self.dis_answerL.place(x=self.place_count(7, 3, 'hor', self.dis_answerL.winfo_width()), y=self.place_count(18, 6, 'ver', self.dis_answerL.winfo_height()))
            self.dis_answerB.place(x=self.place_count(7, 6, 'hor', self.dis_answerB.winfo_width()), y=self.place_count(18, 6, 'ver', self.dis_answerB.winfo_height()))

        if self.et_ui:
            self.back15.place(x=self.place_count(12, 2, 'hor', self.back15.winfo_width()), y=self.place_count(18, 1, 'ver', self.back15.winfo_height()))
            self.et_label.place(x=self.place_count(7, 2, 'hor', self.et_label.winfo_width()), y=self.place_count(18, 2, 'ver', self.et_label.winfo_height()))
            self.et_formula.place(x=self.place_count(7, 2, 'hor', self.et_formula.winfo_width()), y=self.place_count(18, 3, 'ver', self.et_formula.winfo_height()))
            self.et_aL.place(x=self.place_count(7, 2, 'hor', self.et_aL.winfo_width()), y=self.place_count(18, 4, 'ver', self.et_aL.winfo_height()))
            self.et_bL.place(x=self.place_count(7, 4, 'hor', self.et_bL.winfo_width()), y=self.place_count(18, 4, 'ver', self.et_bL.winfo_height()))
            self.et_cL.place(x=self.place_count(7, 6, 'hor', self.et_cL.winfo_width()), y=self.place_count(18, 4, 'ver', self.et_cL.winfo_height()))
            self.et_aE.place(x=self.place_count(7, 2, 'hor', self.et_aE.winfo_width()), y=self.place_count(18, 5, 'ver', self.et_aE.winfo_height()))
            self.et_bE.place(x=self.place_count(7, 4, 'hor', self.et_bE.winfo_width()), y=self.place_count(18, 5, 'ver', self.et_bE.winfo_height()))
            self.et_cE.place(x=self.place_count(7, 6, 'hor', self.et_cE.winfo_width()), y=self.place_count(18, 5, 'ver', self.et_cE.winfo_height()))
            self.et_answerL.place(x=self.place_count(7, 3, 'hor', self.et_answerL.winfo_width()), y=self.place_count(18, 6, 'ver', self.et_answerL.winfo_height()))
            self.et_answerB.place(x=self.place_count(7, 6, 'hor', self.et_answerB.winfo_width()), y=self.place_count(18, 6, 'ver', self.et_answerB.winfo_height()))

        if self.average_ui:
            self.back16.place(x=self.place_count(12, 2, 'hor', self.back16.winfo_width()), y=self.place_count(18, 1, 'ver', self.back16.winfo_height()))
            self.average_label.place(x=self.place_count(7, 2, 'hor', self.average_label.winfo_width()), y=self.place_count(18, 2, 'ver', self.average_label.winfo_height()))
            self.average_formula.place(x=self.place_count(7, 2, 'hor', self.average_formula.winfo_width()), y=self.place_count(18, 3, 'ver', self.average_formula.winfo_height()))
            self.average_aL.place(x=self.place_count(7, 3, 'hor', self.average_aL.winfo_width()), y=self.place_count(18, 4, 'ver', self.average_aL.winfo_height()))
            self.average_aE.place(x=self.place_count(7, 3, 'hor', self.average_aE.winfo_width()), y=self.place_count(18, 5, 'ver', self.average_aE.winfo_height()))
            self.average_answerL.place(x=self.place_count(7, 3, 'hor', self.average_answerL.winfo_width()), y=self.place_count(18, 6, 'ver', self.average_answerL.winfo_height()))
            self.average_answerB.place(x=self.place_count(7, 6, 'hor', self.average_answerB.winfo_width()), y=self.place_count(18, 6, 'ver', self.average_answerB.winfo_height()))

        if self.instruction_ui:
            self.instruction_info.place(x=self.place_count(2, 1, 'hor', self.instruction_info.winfo_width()), y=self.place_count(10, 4, 'ver', self.instruction_info.winfo_height()))
            self.back2.place(x=self.place_count(5, 4, 'hor', self.back2.winfo_width()), y=self.place_count(8, 7, 'ver', self.back2.winfo_height()))

        if self.about_us_ui:
            self.about_us_info.place(x=self.place_count(2, 1, 'hor', self.about_us_info.winfo_width()), y=self.place_count(10, 4, 'ver', self.about_us_info.winfo_height()))
            self.back3.place(x=self.place_count(5, 4, 'hor', self.back3.winfo_width()), y=self.place_count(8, 7, 'ver', self.back3.winfo_height()))

        self.parent.update_idletasks()

    def update_widgets(self, array_off):
        for i in self.all_widgets:
            o_o = False
            for j in array_off:
                if i==j:
                    o_o = True
                    break
            if not o_o:
                try:
                    i.place_forget()
                except:
                    pass

        for i in range(3):
            if self.tumbler_size:
                self.sc1+=1
                self.sc2-=1
            else:
                self.sc1-=1
                self.sc2+=1
            self.parent.geometry(str(math.ceil(self.sc1*0.9))+'x'+str(math.ceil(self.sc2*0.9))+'+'+str(math.floor(self.sc1*0.0))+'+'+str(math.floor(self.sc2*0.0)))

    def reshebnick(self):
        self.voluems_ui = False
        self.discriminant_ui = False
        self.main_ui = False
        self.square_ui = False
        self.about_us_ui = False
        self.reshebnick_ui = True
        self.instruction_ui = False
        self.radiuses_ui = False
        self.et_ui = False
        self.average_ui = False
        self.update_widgets(self.reshebnick_widgets)
        self.parent.title('Решебник')
        self.background_ui('bg1.jpg')

    def volume_func(self):
        self.main_ui = False
        self.reshebnick_ui = False
        self.square_ui = False
        self.instruction_ui = False
        self.et_ui = False
        self.voluems_ui = True
        self.about_us_ui = False
        self.average_ui = False
        self.discriminant_ui = False
        self.radiuses_ui = False
        self.update_widgets(self.volumies_widgets)
        self.parent.title('Объёмы')
        self.background_ui('bg2.jpg')

    def main_view(self):
        self.main_ui = True
        self.et_ui = False
        self.instruction_ui = False
        self.average_ui = False
        self.reshebnick_ui = False
        self.voluems_ui = False
        self.radiuses_ui = False
        self.discriminant_ui = False
        self.about_us_ui = False
        self.square_ui = False
        self.update_widgets(self.main_widgets)
        self.parent.title('Решебник')
        self.background_ui('background.jpg')

    def squar_func(self):
        self.main_ui = False
        self.instruction_ui = False
        self.et_ui = False
        self.reshebnick_ui = False
        self.about_us_ui = False
        self.average_ui = False
        self.radiuses_ui = False
        self.discriminant_ui = False
        self.square_ui = True
        self.voluems_ui = False
        self.update_widgets(self.square_widgets)
        self.parent.title('Площади')
        self.background_ui('bg2.jpg')

    def radius_func(self):
        self.main_ui = False
        self.reshebnick_ui = False
        self.et_ui = False
        self.average_ui = False
        self.instruction_ui = False
        self.discriminant_ui = False
        self.about_us_ui = False
        self.radiuses_ui = True
        self.square_ui = False
        self.voluems_ui = False
        self.update_widgets(self.radius_widgets)
        self.parent.title('Радиусы')
        self.background_ui('bg2.jpg')

    def discriminant_func(self):
        self.main_ui = False
        self.reshebnick_ui = False
        self.average_ui = False
        self.discriminant_ui = True
        self.instruction_ui = False
        self.et_ui = False
        self.radiuses_ui = False
        self.square_ui = False
        self.about_us_ui = False
        self.voluems_ui = False
        self.update_widgets(self.discriminant_widgets)
        self.parent.title('Дискриминант')
        self.background_ui('bg2.jpg')

    def et_func(self):
        self.main_ui = False
        self.reshebnick_ui = False
        self.discriminant_ui = False
        self.et_ui = True
        self.average_ui = False
        self.radiuses_ui = False
        self.square_ui = False
        self.instruction_ui = False
        self.about_us_ui = False
        self.voluems_ui = False
        self.update_widgets(self.et_widgets)
        self.parent.title('Существование треугольника')
        self.background_ui('bg2.jpg')

    def qutit(self):
        exit()

    def average_func(self):
        self.main_ui = False
        self.reshebnick_ui = False
        self.discriminant_ui = False
        self.et_ui = False
        self.average_ui = True
        self.radiuses_ui = False
        self.square_ui = False
        self.voluems_ui = False
        self.instruction_ui = False
        self.about_us_ui = False
        self.update_widgets(self.average_widgets)
        self.parent.title('Среднее арифметическое')
        self.background_ui('bg2.jpg')

    def instruction(self):
        self.main_ui = False
        self.reshebnick_ui = False
        self.discriminant_ui = False
        self.et_ui = False
        self.average_ui = False
        self.radiuses_ui = False
        self.square_ui = False
        self.voluems_ui = False
        self.instruction_ui = True
        self.about_us_ui = False
        self.update_widgets(self.instruction_widgets)
        self.parent.title('Инструкция')
        self.background_ui('bg1.jpg')
        self.instruction_info.place(x=self.place_count(2, 1, 'hor', self.instruction_info.winfo_width()), y=self.place_count(10, 1, 'ver', self.instruction_info.winfo_height()))
        self.back2.place(x=self.place_count(5, 4, 'hor', self.back2.winfo_width()), y=self.place_count(8, 7, 'ver', self.back2.winfo_height()))

    def about_us(self):
        self.main_ui = False
        self.reshebnick_ui = False
        self.discriminant_ui = False
        self.et_ui = False
        self.average_ui = False
        self.radiuses_ui = False
        self.square_ui = False
        self.voluems_ui = False
        self.instruction_ui = False
        self.about_us_ui = True
        self.update_widgets(self.about_us_widgets)
        self.parent.title('Об авторе')
        self.background_ui('bg1.jpg')
        self.about_us_info.place(x=self.place_count(2, 1, 'hor', self.about_us_info.winfo_width()), y=self.place_count(10, 1, 'ver', self.about_us_info.winfo_height()))
        self.back3.place(x=self.place_count(5, 4, 'hor', self.back3.winfo_width()), y=self.place_count(8, 7, 'ver', self.back3.winfo_height()))
        

    def RPV(self):
        RPV_end = 1
        for i in [self.RPV_WE.get(), self.RPV_HE.get(), self.RPV_LE.get()]:
            if not i.isdigit():
                self.RPV_answerL.configure(text="Введены некорректные значения", fg='red')
                return
            if int(i)==0:
                self.RPV_answerL.configure(text="Введены некорректные значения", fg='red')
                return
            RPV_end *= int(i)
        self.RPV_answerL.configure(text=f"Ответ: {RPV_end}", fg='black')

    def CV(self):
        for i in [self.CV_HE.get(), self.CV_RE.get()]:
            if not i.isdigit():
                self.CV_answerL.configure(text="Введены некорректные значения", fg='red')
                return
            if int(i) == 0:
                self.CV_answerL.configure(text="Введены некорректные значения", fg='red')
                return
        self.CV_answerL.configure(text=f"Ответ: {math.pi*int(self.CV_RE.get())**2*int(self.CV_HE.get())}", fg='black')

    def Aoat(self):
        for i in [self.Aoat_HE.get(), self.Aoat_aE.get()]:
            if not i.isdigit():
                self.Aoat_answerL.configure(text="Введены некорректные значения", fg='red')
                return
            if int(i)==0:
                self.Aoat_answerL.configure(text="Введены некорректные значения", fg='red')
                return
        self.Aoat_answerL.configure(text=f"Ответ: {0.5*int(self.Aoat_aE.get())*int(self.Aoat_HE.get())}", fg='black')

    def Aoac(self):
        if not self.Aoac_RE.get().isdigit():
            self.Aoac_answerL.configure(text="Введены некорректные значения", fg='red')
            return
        if int(self.Aoac_RE.get()) == 0:

            self.Aoac_answerL.configure(text="Введены некорректные значения", fg='red')
            return
        self.Aoac_answerL.configure(text=f"Ответ: {math.pi*int(self.Aoac_RE.get())**2}", fg='black')

    def rctil(self):
        if not self.rctil_PE.get().isdigit():
            self.rctil_answerL.configure(text="Введены некорректные значения", fg='red')
            return
        if int(self.rctil_PE.get()) == 0:
            self.rctil_answerL.configure(text="Введены некорректные значения", fg='red')
            return
        self.rctil_answerL.configure(text=f"Ответ: {int(self.rctil_PE.get())/(2*math.pi)}", fg='black')

    def rctis(self):
        if not self.rctis_SE.get().isdigit():
            self.rctis_answerL.configure(text="Введены некорректные значения", fg='red')
            return
        if int(self.rctis_SE.get()) == 0:
            self.rctis_answerL.configure(text="Введены некорректные значения", fg='red')
            return
        self.rctis_answerL.configure(text=f"Ответ: {(int(self.rctis_SE.get())/math.pi)**0.5}", fg='black')

    def dis(self):
        for i in [self.dis_aE.get(), self.dis_bE.get(), self.dis_cE.get()]:
            if not i.isdigit():
                self.dis_answerL.configure(text="Введены некорректные значения", fg='red')
                return
        a = int(self.dis_aE.get())
        b = int(self.dis_bE.get())
        c = int(self.dis_cE.get())
        self.dis_answerL.configure(text=f"Ответ: {b**2-4*a*c}", fg='black')

    def et(self):
        for i in [self.et_aE.get(), self.et_bE.get(), self.et_cE.get()]:
            if not i.isdigit():
                self.et_answerL.configure(text="Введены некорректные значения", fg='red')
                return
        a = int(self.et_aE.get())
        b = int(self.et_bE.get())
        c = int(self.et_cE.get())
        if a+b>c and b+c>a and a+c>b:
            self.et_answerL.configure(text="Треугольник Существует", fg='black')
        else:
            self.et_answerL.configure(text="Треугольник не Существует", fg='orange')

    def average(self):
        if self.average_aE.get() != '':
            try:
                time_array = self.average_aE.get().split()
                sum = 0
                for i in time_array:
                    sum+=int(i)
                self.average_answerL.configure(text=f"Ответ: {sum/len(time_array)}", fg='black')
            except:
                self.average_answerL.configure(text="Введены некорректные значения", fg='red')
                return
        else:
            self.average_answerL.configure(text="Введены некорректные значения", fg='red')
            return

#================Создаём главную функцию===================
def main():
    start = Tk()
    start.title('Решебник')
    sc1, sc2 = start.winfo_screenwidth(), start.winfo_screenheight()
    sc = str(math.ceil(sc1*0.9))+'x'+str(math.ceil(sc2*0.9))+'+'+str(math.floor(sc1*0.0))+'+'+str(math.floor(sc2*0.0))
    start.geometry(sc)
    start.update_idletasks()
    

    app = Parent(start)


    start.mainloop()

#===============Запускаем программу========================
if __name__ == "__main__":
    main()
