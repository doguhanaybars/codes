#interable
#iterate
#genarators
def genarator_function(num):
    for i in range(num):
        yield i*2
    
g = genarator_function(100)
next(g)
next(g)
print(next(g))
print(next(g))


