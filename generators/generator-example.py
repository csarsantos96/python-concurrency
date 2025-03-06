# A simple generator function
def my_gen():
    n =1
    print('First print, n is equal to {} '.format(n))
    # Generator function contains yield statements

    yield  n

    n += 1
    print('Second print n is equal to {} '.format(n))
    yield n

    n += 1
    print('third print and the last, n is equal to {} '.format(n))
    yield  n