class Dog:
    type = None
    name = None
    age = None

    def bar(self):
        print(f"小狗{self.name}汪汪汪!")


dog = Dog()
dog.name = "小北"
dog.bar()
