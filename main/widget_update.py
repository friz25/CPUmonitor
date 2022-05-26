class Configore_widgets:

    def configure_cpu_bar(self):

        r = self.cpu.cpu_percent_return()
        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].configure(text=f'ядро {i+1} загружено на: {r[i]}%')
            self.list_pbar[i].configure(value=r[i])

        r2 = self.cpu.ram_usage()
        self.ram_lab.configure(text=f'RAM занято: {r2[2]}%, занято: {round(r2[3]/1048576)} Mb,'
                                    f'\n            свободно: {round(r2[1]/1048576)} Mb')


        self.wheel = self.after(1000, self.configure_cpu_bar)
        #.after позволяет циклически перезапускать функцию (каждую секунду)

    def configure_win(self): #чтоб при нажатии на кнопку "Двигать" появлялась рамка окна проги
        if self.wm_overrideredirect():
            self.overrideredirect(False)
        else:
            self.overrideredirect(True)
        self.update()

    def clear_win(self): #удаляем все графическте элементы окна
        for i in self.winfo_children(): #winfo_children() - хранит все созданные элементы окна
            i.destroy()
    def configure_minimal_win(self):
        self.bar_one.configure(value=self.cpu.cpu_one_return())
        self.ram_bar.configure(value=self.cpu.ram_usage()[2])
        self.wheel = self.after(1000, self.configure_minimal_win)