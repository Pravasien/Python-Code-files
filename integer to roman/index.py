class Roman:
    def __init__(self):
        # dictionary already created by user
        self.map = {
            1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
            6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',
            10: 'X', 50: 'L', 100: 'C'
        }

    def get(self):
        try:
            return int(input('Enter number: '))
        except ValueError:
            # repeat prompt until valid integer
            return self.get()

    def conv(self, n):
        # simple lookup using the existing dictionary
        return self.map.get(n, 'Number not in dictionary')


if __name__ == '__main__':
    roman = Roman()
    num = roman.get()
    print('Roman numeral:', roman.conv(num))