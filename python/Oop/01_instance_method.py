class Person:
    species = '사람'
    def greeting(self):
        print('안녕하세요!')

iu = Person()
iu.greeting()

print(Person.species)