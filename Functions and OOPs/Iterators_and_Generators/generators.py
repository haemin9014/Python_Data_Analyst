#looks like a function but using iteration

#sample of function in python
def func(a,b):
    return a + b

#sampe of generator using yied
def generator_123():
    yield 1
    yield 2
    yield 3

print(type(generator_123()));
#how to use generator function
gen = generator_123();
print("since it is same as iteration, we could use next.");
print("using next, we could see %s" %next(gen));

