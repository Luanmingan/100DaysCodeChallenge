import time
from decorators import timer

@timer
def test_func():
    """A doc string."""
    print('program starts')
    time.sleep(1)
    print('program ends')


test_func()
print(test_func.__doc__)
