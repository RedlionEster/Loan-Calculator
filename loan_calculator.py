import argparse
import math

# Create an ArgumentParser object and define the command-line arguments
parser = argparse.ArgumentParser(description="Loan Calculator")
parser.add_argument("--type", choices=["annuity", "diff"], help="Type of payment (annuity or diff)")
parser.add_argument("--principal", type=float, help="Loan principal amount")
parser.add_argument("--periods", type=int, help="Number of months for repayment")
parser.add_argument("--interest", type=float, help="Loan interest rate")
parser.add_argument("--payment", type=float, help="Annuity payment amount (annuity only)")

# Parse the command-line arguments
args = parser.parse_args()

if args.type is None:
    print("Incorrect parameters")
elif args.type == "diff":
    if args.payment is not None:
        print("Incorrect parameters")
    else:
        principal = args.principal
        periods = args.periods
        interest = args.interest / 1200  # Convert annual interest rate to monthly
        overpayment = 0

        for m in range(1, periods + 1):
            d = math.ceil(principal / periods + interest * (principal - principal * (m - 1) / periods))
            overpayment += d
            print(f"Month {m}: payment is {d}")

        print("\nOverpayment =", overpayment - principal)

elif args.type == "annuity":
    if args.payment is None:
        if None not in (args.principal, args.periods, args.interest):
            principal = args.principal
            periods = args.periods
            interest = args.interest / 1200  # Convert annual interest rate to monthly

            annuity_payment = principal * (interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1)
            annuity_payment = math.ceil(annuity_payment)
            overpayment = annuity_payment * periods - principal
            print(f"Your annuity payment = {annuity_payment}!")
            print("\nOverpayment =", overpayment)
        else:
            print("Incorrect parameters")
    elif args.principal is None:
        if None not in (args.payment, args.periods, args.interest):
            payment = args.payment
            periods = args.periods
            interest = args.interest / 1200  # Convert annual interest rate to monthly

            principal = payment / ((interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1))
            overpayment = payment * periods - principal
            print(f"Your loan principal = {principal}!")
            print("\nOverpayment =", overpayment)
        else:
            print("Incorrect parameters")
    elif args.periods is None:
        if None not in (args.principal, args.payment, args.interest):
            principal = args.principal
            payment = args.payment
            interest = args.interest / 1200  # Convert annual interest rate to monthly

            periods = math.log(payment / (payment - interest * principal), 1 + interest)
            periods = math.ceil(periods)
            years = periods // 12
            months = periods % 12

            years_str = '' if years == 0 else '1 year' if years == 1 else f'{years} years'
            and_str = '' if years == 0 or months == 0 else 'and'
            months_str = '' if months == 0 else '1 month' if months == 1 else f'{months} months'

            print(f"It will take {years_str} {and_str} {months_str} to repay this loan!")
            overpayment = payment * periods - principal

            print("\nOverpayment =", overpayment)
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
