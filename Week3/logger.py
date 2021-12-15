from functools import wraps
import time
import logging


def logger(func):
    logging.basicConfig(filename='{}.log'.format(func.__name__),
                        level=logging.INFO)
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper function"""
        logging.info(f'Ran - args: {args}\tkwargs: {kwargs}')
        return func(*args, **kwargs)
    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper function"""
        start = time.time()
        data = func(*args, **kwargs)
        duration = time.time() - start
        print(f'{func.__name__} ran in {duration} seconds')
        return data
    return wrapper


@timer
@logger  # timer(logger(bill_plus_tax_tip))
def bill_plus_tax_tip(bill, tax=0.09, tip=0.2):
    """Calculate bill plus tax and tip"""
    return (1 + tax + tip) * bill


print(bill_plus_tax_tip(20, tip=0.25))
print(bill_plus_tax_tip(56.97, tax=0.1))
print(bill_plus_tax_tip(118.75, tax=0.18))
