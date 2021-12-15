# Griffin Stepler, CIS345, iCourse, A3
import csv


def log_transaction(transactions):
    """
    Accepts a list of lists: transactions, opens or creates transactions.csv,
    writes the contents of transactions[] to the .csv
    Quotes values with delimiters using double quotes: '"'
    """
    with open('transactions.csv', 'a', newline='') as fp:
        writer = csv.writer(fp, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(transactions)


# example output has a weird space between '$' and <money>.
# This space is not replicated because it is not documented outside of
# the example output images.
def format_money(money):
    """
    Accepts a dollar amount and returns it formatted with '$'
    and two decimal places
    """
    dollars = f'${money:,.2f}'
    return dollars


if __name__ == "__main__":
    cash = 344.54
    print(format_money(cash))
