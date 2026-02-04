class Parent:
    def __init__(self, eye, aggr):
        self.eye = eye
        self.aggr = aggr

    def display(self):
        print('The eye color is ', self.eye)
        print('Aggressive in nature ', self.aggr)

class child(Parent):
    def __init__(self, name, age, eye, aggr):
        self.name = name
        self.age = age
        #Parent.__init__(self, eye, aggr)
        super().__init__(eye, aggr)

    def display(self):
        print('The name is ', self.name)
        print('The age is ', self.age)
        #Parent.display(self)
        super().display()

c1 = child('Pingu', 8, 'Hazel', True)
c1.display()