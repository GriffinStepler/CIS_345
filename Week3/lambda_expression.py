# Lambda Expressions - Anonymous Functions
# they allow you to create a simple throwaway function; especially useful in terminal environments
# lambda args: expression
sum = lambda x: x + x
dollar_formatter = lambda amount: f'$ {amount:,.2f}'
concat = lambda str1, str2: str1 + str2

print(sum(4))
print(dollar_formatter(4.3))
print(concat('Hey, my name is ', 'Griffin'))

# why would we ever use these instead of just defining a function?
cube = lambda num: num ** 3
cubes = [cube(i) for i in range(1, 11)]
print(cubes)
