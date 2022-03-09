class Dog:

    def __init__(self, dog_type):
        self.dog_type: str = dog_type

    def get_race(self) -> str:
        return self.dog_type


class Jackrusses(Dog):

    def __init__(self, dog_type, name):
        super().__init__(dog_type)
        self.name = name

    def get_name(self) -> str:
        return f"{self.get_race()}: {self.name}"


if __name__ == '__main__':
    d = Jackrusses("dog", "Jack")
    print(d.get_name())