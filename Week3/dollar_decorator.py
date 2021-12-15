from functools import wraps


def dollar_amount(func):
    """outer function"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper function"""
        dollars = func(*args, **kwargs)
        return f'$ {dollars:,.2f}'
    return wrapper


@dollar_amount
def bill_plus_tax_tip(bill, tax=0.09, tip=0.2):
    return (1 + tax + tip) * bill


@dollar_amount
def update_balance(balance, transaction=0):
    return balance + transaction


print(bill_plus_tax_tip(28.78, tip=0.12))  # 28.78 will go into *args, 0.12 into **kwargs
bal = 2000.45
formatted_balance = update_balance(bal, -200.05)
print(formatted_balance)
