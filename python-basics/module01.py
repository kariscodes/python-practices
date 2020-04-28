# module01.py

maker = 'robot'

def calc(a, b):
    return a + b

class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def hello(self):
        print('Hello!')
        
    def info(self):
        print('My name is ' + self.name + '.')
        print("I'm " + str(self.age) + ' years old.')

if __name__ == '__main__':
    print('여기서부터는 테스트코드입니다!')
    print(maker)
    print(calc(3, 9))