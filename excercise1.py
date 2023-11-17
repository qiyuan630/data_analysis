print("hello world")
print('中文'.encode('utf-8'))
#print('中文'.encode('ascii'))
'''
纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
'''
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
'''这个tuple定义的时候有3个元素，分别是'a'，'b'和一个list。不是说tuple一旦定义后就不可变了吗？怎么后来又变了？
'''
'''表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，
tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！'''

#match语句除了可以匹配简单的单个值外，还可以匹配多个值、匹配一定范围，并且把匹配后的值绑定到变量：
age = 15

match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')


#递归函数

#汉诺塔的移动可以用递归函数非常简单地实现。
def move (n,a,b,c):
    if n == 1:
        print(a,"-->",c)
    else:
        move(n-1,a,c,b)
        print(a,"-->",c)
        move(n-1,b,a,c)
move(1,"a","b","c")

#高阶函数
#map()函数接收两个参数，一个是函数，一个是Iterable，
#map将传入的函数依次作用到序列的每个元素，
#并把结果作为新的Iterator返回。
def f(x):
    return x*x
r = map(f,[1,2,3,4,5,6])
h =list(r)
print(h)
#再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
#reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x,y):
    return x + y
a = reduce(add,[1,3,5,7,9])
print(a)


from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。输入：['adam', 'LISA', 'barT']，
# 输出：['Adam', 'Lisa', 'Bart']：
from functools import reduce
def anheqiao(s):
    def heqiao(a):
        return a.title()
    def an(s):
        return s.lower()
    return map(heqiao, map(an, s))
anheqiao1 = anheqiao(['adam', 'LISA', 'barT'])
print(list(anheqiao1))

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(s):
    def p(x,y):
        return x*y
    return reduce(p,s)
prod1 = prod([3,5,7,9])
print(prod1)

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    DIGITS = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'.':'.'}
    def fn(a,b):
        if b=='.':
            return a
        return a*10+b
    def fm(s):
        return DIGITS[s]
    n = s.index('.')
    return reduce(fn,map(fm,s))/10**n

print(str2float("123.456"))

def str2float(s):

    return reduce(lambda x, y: x + y/(10**len(str(y))),map(lambda str:reduce(lambda x, y: x * 10 + y, [ord(x)-48 for x in str]),s.split('.')))
#这里的ord()函数是返回对应的ascii码值。

#filter
#和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
#注意filter的函数返回的也是一个iterator，是一个惰性序列。
def _odd_iter():
    n=1
    while True:
        n = n+2
        yield n

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_palindrome(n):
    t = 0
    tmp = n
    while tmp!=0:
        t *= 10
        t += tmp%10
        tmp = tmp//10
    return t==n

#sorted
#此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
sorted([36, 5, -12, 9, -21], key=abs)
#sorted([36, 5, -12, 9, -21], key=abs)
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

#假设我们用一组tuple表示学生名字和成绩：
#L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L2 = sorted(L,key = by_name)
print(L2)

#利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createcounter():
    j = 0
    def counter():
        nonlocal j
        j+=1
        return j
    return counter
#请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
#请用匿名函数改造下面的代码：
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)
L = list(filter(lambda x: x%2 ==1, range(1, 20)))
print(L)

#装饰器
#函数对象有一个__name__属性（注意：是前后各两个下划线），可以拿到函数的名字
def now():
    print("2023年11月16日")
f = now
print(now.__name__)
print(f.__name__)

#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import functools
def log(time):
    def decorator(func):
        @functools.wraps(func)
        def metric(*args, **kwargs):
            print('%s executed in %s ms' % (func.__name__, time))
            return func(*args, **kwargs)
        return metric
    return decorator

#time = input("请输入当前代码运行的时间")
time = 23.08
@log(time)
def now():
    pass
print(now())