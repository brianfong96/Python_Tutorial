# Write a script that can calculate how much income tax you need to pay
# https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html
# Examples of the output can be seen in examples.txt
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
    