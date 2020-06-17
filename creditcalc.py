from math import pow, log, ceil, floor
import argparse
# user = input("""What do you want to calculate?
# type "n" - for count of months,
# type "a" - for annuity monthly payment,
# type "p" - for credit principal:
# """)
def month_to_year(n):
    if n<12:
        print(f"You need {n} months to repay this credit!")
    elif n==12:
        print("You need 1 year to repay this credit!")
    elif n%12 != 0:
        print(f"You need {n//12} years and {n%12} months to repay this credit!")
    else:
        print(f"You need {n//12} years to repay this credit!")
def annuity_pay(p, i, n):
    i = (i/100)*(1/12)
    return p * ((i* pow(1+i,n))/ (pow(1+i,n)-1))
    #print(f"Your annuity payment = {ann_pay}! {ceil(ann_pay) * n - p}")
def credit_pp(a,i,n):
    i = (i/100)*(1/12)
    d = i * pow(1+i,n) / (pow(1+i,n) - 1)
    return floor(a / (d))
def n_pay(i,a,p):
    i = (i/100)*(1/12)
    x = a/ (a-i * p)
    return ceil(log(x, 1+i))
def user_choice(inp):
    if inp == "n":
        p = int(input("Enter credit principal: "))
        a = int(input("Enter monthly payment: "))
        i = float(input("Enter credit interest: "))
        month_to_year(n_pay(i,a,p))
    elif inp == "a":
        p = int(input("Enter credit principal: "))
        n = int(input("Enter count of periods: "))
        i = float(input("Enter credit interest: "))
        print(f"Your annuity payment = {ceil(annuity_pay(p,i,n))}!")
    else:
        a = float(input("Enter monthly payment: "))
        n = int(input("Enter count of periods: "))
        i = float(input("Enter credit interest: "))
        print(f"Your credit principal = {credit_pp(a,i,n)}!")
def dif_pay(p, n, i):
    i = (i/100)*(1/12)
    total = 0
    for m in range(1,n+1):
       d =  p / n + i * (p - (p * (m-1)) / n)
       total +=ceil(d)
       print(f"Month {m}: paid out {ceil(d)}")
    print(f"\nOverpayment = {total - p}")

#user_choice(user)

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--principal", help= "credit principal", type=int, default=0)
parser.add_argument("-a", "--payment", help="monthly payment", type=float, default=0)
parser.add_argument("-n", "--periods", help="number of payments", type=int, default=0)
parser.add_argument("-i", "--interest", help="nominal interest rate", type=float, default=0)
parser.add_argument("-t", "--type", help="differentiated or annuity payment")
arg = parser.parse_args()
if arg.interest == 0:
    print("Incorrect parameters")
elif arg.periods < 0 or arg.principal < 0 or arg.interest < 0 or arg.payment < 0:
    print("Incorrect parameters")
elif arg.type == "diff":
    dif_pay(arg.principal, arg.periods, arg.interest)
elif arg.type == "annuity":
    if arg.principal > 0 and arg.payment > 0:
        n = n_pay(arg.interest, arg.payment, arg.principal)
        month_to_year(n)
        print(f"Overpayment = {round(arg.payment * n - arg.principal)}")
    elif arg.principal > 0:
        ann_pay = annuity_pay(arg.principal, arg.interest, arg.periods)
        print(f"Your annuity payment = {ceil(ann_pay)}!")
        print(f"\nOverpayment = {ceil(ann_pay) * arg.periods - arg.principal}")
    elif arg.payment > 0:
        cre_pp = credit_pp(arg.payment,arg.interest,arg.periods)
        print(f"Your credit principal = {cre_pp}!")
        print(f"Overpayment = {round(arg.payment * arg.periods - cre_pp)}")

else:
    print("Incorrect parameters")
