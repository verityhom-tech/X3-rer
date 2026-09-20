

class First_class:
    pass

class Secound_class(First_class):
    pass


print(issubclass(First_class, Secound_class))
print(issubclass(Secound_class, First_class))