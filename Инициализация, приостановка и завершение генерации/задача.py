def f():
    print('Initialization')
    yield 'one'
    print('Continue...')
    yield 'two'
    print('Stopping...')


i = f()
try:
    print(next(i))
    print(next(i))
    print(next(i))
except StopIteration:
    print('Завершены возвраты значений')
finally:
    print('Завершение')
