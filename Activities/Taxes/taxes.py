# Write a script that can calculate how much income tax you need to pay
# https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html
# Here is an example of the output below
"""
What is your income: 100000
For federal taxes:
You will need to pay $7529.55(15.00%) on the first $50197.00
You will need to pay $10209.61(20.50%) on the next $49803.00
For provincial taxes:
You will need to pay $2179.34(5.06%) on the first $43070.00
You will need to pay $3316.47(7.70%) on the next $43071.00
You will need to pay $1339.80(10.50%) on the next $12760.00
You will need to pay $135.07(12.29%) on the next $1099.00

    Your income is $100000.00.

    You will have to pay $17739.17 for federal tax.
    This is 17.74% of your income.

    You will have to pay $6970.68 for bc provincial tax.
    This is 6.97% of your income.

    You will have to pay a total of $24709.84 in taxes.
    This is 24.71% of your income.

    After taxes you will have $75290.16.
"""
if __name__ == "__main__":
    valid_input = False
    while not valid_input:
        try:
            income = float(input("What is your income: "))
            valid_input = True
        except:
            print("That is not a valid input")
        

    print("For federal taxes:")
    # TODO
    print(f"You will need to pay ${0:.2f}({0:.2f}%) on the {'first/next'} ${0:.2f}")
    canada_federal_tax = 0
    # /TODO

    print("For provincial taxes:")
    # TODO
    print(f"You will need to pay ${0:.2f}({0:.2f}%) on the {'first/next'} ${0:.2f}")
    bc_tax = 0
    # /TODO

    total_taxes = canada_federal_tax + bc_tax
    income_after_tax = income - total_taxes

    print(f"""
    Your income is ${income:.2f}.

    You will have to pay ${canada_federal_tax:.2f} for federal tax.
    This is {canada_federal_tax/income * 100:.2f}% of your income.

    You will have to pay ${bc_tax:.2f} for bc provincial tax.
    This is {bc_tax/income * 100:.2f}% of your income.

    You will have to pay a total of ${total_taxes:.2f} in taxes.
    This is {total_taxes/income * 100:.2f}% of your income.

    After taxes you will have ${income_after_tax:.2f}.
    """)
    