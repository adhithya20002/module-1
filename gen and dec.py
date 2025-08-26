# def gen_squares(limit):
#     for x in range(1,limit+1):
#         yield x*x
# squares=gen_squares(6)
# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares))


# def generator_function():
#     for i in range(1,6):
#         yield i
# gen=generator_function()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

##)
def even_numbers(n):
    for i in range(2,n+1,1):
        yield i
even=even_numbers()
print(next(even))
    


## Decorators))

# def outer(func):
#     def inner() :
#         print('I got decorated')
#         func()
#     return inner
# @outer
# def ordinary():
#     print("I am ordinary")
# ordinary()

