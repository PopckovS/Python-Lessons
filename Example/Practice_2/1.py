

def func1():
    class Bank():
        """
        Условие:
            Пользователь делает вклад в размере a рублей сроком на years лет
            под 10% годовых (каждый год размер его вклада увеличивается на 10%.
            Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже
            будут проценты).

        Задача:
        Написать класс bank, принимающая аргументы a и years, и возвращающую
        сумму, которая будет на счету пользователя.
        """

        def __init__(self, summ, years):
            self.checkArguments(summ, years)
            self.percent = 1.10
            self.summ = summ
            self.years = years
            self.result = self.summ
            self.GetResultForYears()

        def ShowResult(self):
            print("Сумма {summ} под '{percent}' на {years} лет = {result}".format(
                summ=self.summ,
                percent=self.percent,
                years=self.years,
                result=self.result
            ))

        def GetResultForYears(self):
            for i in range(self.years):
                self.result = self.GetResultForYear(self.result, self.percent)
                print(self.result)
                print(i)

        def GetResultForYear(self, summ, percent):
            return summ * percent

        def checkArguments(self, summ, years):
            try:
                summ = float(summ)
                years = int(years)
            except:
                print("Сумма и год должны быть числами")
                raise

    bank = Bank(1000, 3)
    bank.ShowResult()


func1()
