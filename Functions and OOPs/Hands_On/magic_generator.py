def generator_Magic(n1):
    # Write your code here
    for i in range(3, n1 + 1):
        yield i * ((i**2)+1)/2