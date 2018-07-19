'''
name='小明'
def say_hello():
    print('hello 1')
    print('hello 2')
    print('hello 3')
print(name)
say_hello()

def sum_2_num():
    num1=10
    num2=20
    result=num1+num2
    print('%d+%d=%d'%(num1,num2,result))
sum_2_num()

def sum_2_num(num1,num2):
    result=num1+num2
    print('%d+%d=%d'%(num1,num2,result))
sum_2_num(50,20)
'''
def sum_2_num(num1,num2):
    return num1+num2
result=sum_2_num(10,20)
print('计算结果是%d'%result)
