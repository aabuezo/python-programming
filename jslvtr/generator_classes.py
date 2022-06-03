class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self


my_gen = FirstHundredGenerator()
print(my_gen)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))


# returning from a list (not generating numbers)
class FirstFiveIterator:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]
        self.i = 0  # first item in the list

    def __next__(self):
        if self.i < len(self.numbers):
            current = self.numbers[self.i]
            self.i += 1
            return current
        else:
            return StopIteration()


# iterator, NOT an iterable!
# my_iterator = FirstFiveIterator()
# for i in my_iterator:
#     print(i)


# class FirstHundredIterable:
#     def __iter__(self):
#         return FirstHundredGenerator()
#
#
# print(sum(FirstHundredIterable()))
# for i in FirstHundredIterable():
#     print(i)


print(sum(FirstHundredGenerator()))
# for i in FirstHundredGenerator():
#     print(i)


class AnotherIterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Focus']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]


for car in AnotherIterable():
    print(car)


my_numbers = [x for x in [1, 2, 3, 4, 5]]   # list comprehension
my_numbers_gen = (x for x in [1, 2, 3, 4, 5])   # generator comprehension
print(next(my_numbers_gen))
print(next(my_numbers_gen))
