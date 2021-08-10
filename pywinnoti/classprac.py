class prac:
    def __init__(self):
        self.first = 1
        self.send = 2

    def plus(self):
        self.first += 1
        self.send += 12
    


    def main(self):
        print('alpa')
        print(f'{self.first}\n{self.send}')
        self.plus()
        print(f'{self.first}\n{self.send}')











if __name__ == "__main__":
    temp = prac()
    temp.main()