def add(a,b):
    print(a+b)

def sub(a,b):
    return a-b,a
add(10,20)
print(sub(100,20))

def hello(greeting="Hello", name="World"):
    print('%s,%s'%(greeting,name))
hello()
hello('Greetings','Deepa')
def print_param(*params):
    print(params)
print('Testing')
print_param(1, 2, 3)
def print_param1(**params):
    print(params)
print_param1(x=1,y=2,z=3)