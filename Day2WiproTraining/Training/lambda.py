add = lambda a,b: a+b
print(add(4,5))
multi=lambda c,d:c*d
print(multi(20,20))
maxnum=lambda x,y: x if x>y else y
print(maxnum(10,40))


numbers=[1,2,3,4,5]
result=map(lambda x:x*2,numbers)
print(list(result))