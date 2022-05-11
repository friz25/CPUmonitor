class Configore_widgets:

    def configore_cpu_bar(self):

        r = self.cpu.cpu_percent_return()
        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].configure(text=f'ядро {i+1} загружено на: {r[i]}%')
            self.list_pbar[i].configure(value=r[i])

        self.after(1000, self.configore_cpu_bar)