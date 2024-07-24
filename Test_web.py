
class MyClass:
    '''
    description
    '''
    color = 'red'
    ch = 2

    def __str__(self):
        return f'qwe {self.color}'
a = MyClass()

print(MyClass.ch)
print(a)
a.ch = 5
print(MyClass.ch)
print(a.ch)
print(isinstance(a, MyClass))

