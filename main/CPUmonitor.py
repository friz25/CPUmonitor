import tkinter as tk
from tkinter import ttk
import sys
from process import CpuBar
from widget_update import Configore_widgets

class Application(tk.Tk, Configore_widgets):
    #создали окно интерфейс
    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes('-alpha', 1) #прозрачность от 0 до 1
        self.attributes('-topmost', True) #поверх всех окон
        self.overrideredirect(True) #убираем рамку окна
        self.resizable(False, False)
        self.title('CPU-RAM usage monitor bar')

        self.cpu = CpuBar()
        self.run_set_ui()

    def run_set_ui(self): #запускает элементы (полной версии) окна
        self.set_ui()
        self.make_bar_cpu_usage()
        self.configure_cpu_bar()

    #Виджеты окна
    def set_ui(self):
        # создали кнопку, для удобства - через переменную
        exit_but = ttk.Button(self, text='Закрыть прогу', command=self.app_exit)
        exit_but.pack(fill=tk.X) #один из 3х упаковщиков (еще есть grid(),по столбцам и строкам, и place(),по сетке)

        self.bar2 = ttk.LabelFrame(self, text='Управление') #(!)создали Фрейм (будем засовывать в него кнопки и т.д.)
        self.bar2.pack(fill=tk.X)

        self.combo_win = ttk.Combobox(self.bar2,
                                      values=["Скрыть","Не скрывать","мин"],
                                      width=11, state='readonly')
        self.combo_win.current(1)
        self.combo_win.pack(side=tk.LEFT)

        ttk.Button(self.bar2, text='двигать', command=self.configure_win).pack(side=tk.LEFT)
        ttk.Button(self.bar2, text='>>>').pack(side=tk.LEFT)

        self.bar = ttk.LabelFrame(self, text='Нагрузка')
        self.bar.pack(fill=tk.BOTH)

        self.bind_class('Tk', '<Enter>', self.enter_mouse)
        self.bind_class('Tk', '<Leave>', self.leave_mouse)
        self.combo_win.bind('<<ComboboxSelected>>', self.choise_combo)

    def make_bar_cpu_usage(self):
        ttk.Label(self.bar, text=f'физ-е ядра: {self.cpu.cpu_count}, лог-е ядра: {self.cpu.cpu_count_logical}',
                  anchor = tk.CENTER).pack(fill=tk.X)

        self.list_label = []
        self.list_pbar = []

        for i in range(self.cpu.cpu_count_logical):
            self.list_label.append(ttk.Label(self.bar, anchor=tk.CENTER))
            self.list_pbar.append(ttk.Progressbar(self.bar, length=100))#Создаём 4 полоски (Прогрессбары)
        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].pack(fill=tk.X)
            self.list_pbar[i].pack(fill=tk.X)

        self.ram_lab = ttk.Label(self.bar, text='', anchor=tk.CENTER)
        self.ram_lab.pack(fill=tk.X)
        self.ram_bar = ttk.Progressbar(self.bar, length=100)
        self.ram_bar.pack(fill=tk.X)

    def make_minimal_win(self):
        self.bar_one = ttk.Progressbar(self, length=100)
        self.bar_one.pack(side=tk.LEFT)

        self.ram_bar = ttk.Progressbar(self, length=100)
        self.ram_bar.pack(side=tk.LEFT)

        ttk.Button(self, text='full', command=self.make_full_win, width=5).pack(side=tk.RIGHT)

        ttk.Button(self, text='move', command=self.configure_win, width=5).pack(side=tk.RIGHT)

        self.update()
        self.configure_minimal_win()

    def enter_mouse(self, event):
        if self.combo_win.current() == 0 or 1:
            self.geometry('')
    def leave_mouse(self, event):
        if self.combo_win.current() == 0:
            self.geometry(f'{self.winfo_width()}x1')
    def choise_combo(self, event):
        if self.combo_win.current() == 2:
            self.enter_mouse('')
            self.unbind_class('Tk', '<Enter>')
            self.unbind_class('Tk', '<Leave>')
            self.combo_win.unbind('<<ComboboxSelected>>')
            self.after_cancel(self.wheel)
            self.clear_win()
            self.update()
            self.make_minimal_win()
    def make_full_win(self):
        self.after_cancel(self.wheel)#прерываем цыкл обновлений данных (окошка в уменьшенной версии )
        self.clear_win() #удаляем все элементы окна ( уменьшенной версии )
        self.update()
        self.run_set_ui() #запускает элементы (полной версии) окна
        self.enter_mouse('')
        self.combo_win.current(1)#возвращаем значение списка в режим "не скрывать"

    # закрывает окошко, убивает процесс нашей программы
    def app_exit(self):
        self.destroy()
        sys.exit()
if __name__ == '__main__':
    root = Application()
    root.mainloop()