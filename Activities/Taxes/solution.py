# Write a script that can calculate how much income tax you need to pay
# https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html
# Examples of the output can be seen in examples.txt

def calculate_tax(income, tax_bracket, tax_rate):
    total_tax = 0
    for i in range(len(tax_bracket)):
        taxable_amount = income
        if income >= tax_bracket[i]:
            taxable_amount = min(tax_bracket[i], taxable_amount)
        if i > 0:
            taxable_amount -= tax_bracket[i-1]
        if taxable_amount < 0:
            return total_tax
        tax = taxable_amount * tax_rate[i]
        print(f"You will need to pay ${tax:.2f}({tax_rate[i]*100:.2f}%) on the {'first' if i == 0 else 'next'} ${taxable_amount:.2f}")
        total_tax += tax
    return total_tax

if __name__ == "__main__":
    canada_federal_tax_bracket = [50197, 100392, 155625, 221708, float("inf")]
    canada_federal_tax_rate = [0.15, 0.205, 0.26, 0.29, 0.33]

    provincial_tax_bracket = {"bc" : [43070, 86141, 98901, 120094, 162832, 227091, float("inf")]}
    provincial_tax_rate = {"bc" : [0.0506, 0.077, 0.105, 0.1229, 0.147, 0.168, 0.205]}
    valid_input = False
    while not valid_input:
        try:
            income = float(input("What is your income: "))
            valid_input = True
        except:
            print("That is not a valid input")
        

    print("For federal taxes:")
    canada_federal_tax = calculate_tax(income, canada_federal_tax_bracket, canada_federal_tax_rate)
    print("For provincial taxes:")
    bc_tax = calculate_tax(income, provincial_tax_bracket["bc"], provincial_tax_rate["bc"])
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
    