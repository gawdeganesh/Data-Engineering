# =======================================================================================================================

import pandas as pd
import streamlit as st

# =======================================================================================================================

# salary = float(input('Enter your annual salary (£):'))

st.sidebar.subheader("Company Income")
company_income = st.sidebar.number_input(
    label=f"Please enter your income here (£):", value=88800, step=1000
)
st.sidebar.subheader("Salary")
salary = st.sidebar.number_input(
    label=f"Please enter your salary here (£):", value=12570, step=1000
)
st.sidebar.subheader("Expenses")
expenses = st.sidebar.number_input(
    label=f"Please enter your expenses here (£):", value=2000, step=100
)

########################################################################################################################

# Income Tax Rates
personal_allowance = (
    12570  # the allowed "zero" tax rate that is allowed for all salaries
)
basic_rate_bracket = (
    37700  # the brackets for which the basic, higher and additional rate applies
)
higher_rate_bracket = 150000
# ---------------------------------------------
basic_rate_tax = 0.2
higher_rate_tax = 0.4
additional_rate_tax = 0.45
# ---------------------------------------------
# the salary that is taxable after subtracting the personal allowance
taxable_salary = float(salary - personal_allowance)
print(taxable_salary)

# National Insurance Rates
NI_threshold = 8632
class_1_lower_bracket = 50000  # The following statements help to calculate the national insurance contributions
class_1_lower_tax_rate = 0.12
class_1_higher_tax_rate = 0.02
NI_adjusted_salary = float(salary - NI_threshold)

# Dividend Tax Rates
Dividend_basic_rate_tax = 0.075
Dividend_higher_rate_tax = 0.325
Dividend_additional_rate_tax = 0.381
Dividend_allowance = 2000

Dividend_amount = company_income - salary - expenses - Dividend_allowance

# Corporation Tax Rate
Corporation_rate_tax = 0.19

########################################################################################################################

# INCOME TAX
if taxable_salary <= personal_allowance:
    income_tax = float(0)
elif taxable_salary <= basic_rate_bracket:
    income_tax = float(taxable_salary * basic_rate_tax)
elif taxable_salary <= higher_rate_bracket:
    income_tax = float(basic_rate_bracket * basic_rate_tax) + float(
        (taxable_salary - basic_rate_bracket) * higher_rate_tax
    )
elif taxable_salary >= (higher_rate_bracket + 1):
    income_tax = (
        float(basic_rate_tax * basic_rate_bracket)
        + float(higher_rate_bracket * higher_rate_tax)
        + float((taxable_salary - higher_rate_bracket) * additional_rate_tax)
    )
else:
    income_tax = 0

# NATIONAL INSURANCE
if taxable_salary <= class_1_lower_bracket:
    NI_contribution = taxable_salary * class_1_lower_tax_rate
elif taxable_salary <= higher_rate_bracket:
    NI_contribution = float(
        (class_1_lower_bracket - NI_threshold) * class_1_lower_tax_rate
    ) + float((taxable_salary - class_1_lower_bracket) * class_1_higher_tax_rate)
else:
    NI_contribution = 0

# CORPORATION TAX
Corporation_tax = (company_income - salary - expenses) * Corporation_rate_tax

# DIVIDEND TAX
if Dividend_amount <= basic_rate_bracket:
    Dividend_tax = float(Dividend_amount * Dividend_basic_rate_tax)
elif Dividend_amount <= higher_rate_bracket:
    Dividend_tax = float(basic_rate_bracket * Dividend_basic_rate_tax) + float(
        (Dividend_amount - basic_rate_bracket) * Dividend_higher_rate_tax
    )
elif Dividend_amount >= (higher_rate_bracket + 1):
    Dividend_tax = (
        float(basic_rate_tax * Dividend_basic_rate_tax)
        + float(higher_rate_bracket * Dividend_higher_rate_tax)
        + float((Dividend_amount - higher_rate_bracket) * Dividend_additional_rate_tax)
    )
else:
    Dividend_tax = "Not taxable! (there is most likely an error somewhere)"


Total_tax = round(NI_contribution + income_tax + Corporation_tax + Dividend_tax, 2)

# =======================================================================================================================

st.sidebar.subheader("Corporation Tax (%)")
Interest_rate_text = st.sidebar.subheader(
    round(
        Corporation_rate_tax * 100,
    )
)

st.subheader("Summary")
st.markdown(f"On a company income of **£{company_income:,}.**")
st.markdown(f'Your "salary" = £{salary:,}.')
st.markdown(f"Other income = £{company_income-salary:,}.")
st.subheader("Summary of Tax")
st.markdown(f"Total income tax = £{round(income_tax,):,}")
st.markdown(f"Total national insurance contribution = £{round(NI_contribution,):,}")
st.markdown(f"Total dividend tax = £{round(Dividend_tax,):,}")
st.markdown(f"Total corporation tax = £{round(Corporation_tax,):,}")
st.subheader("Take Home Pay")
st.markdown(f"Take-home pay = £{round(company_income-Total_tax,):,}")
st.markdown(f"Take-home income pay = £{round((salary-income_tax)/12,):,}")
st.markdown(
    f"Take-home dividend pay = £{round(((company_income-Total_tax)-(salary-income_tax))/12,):,}"
)
st.subheader(f"Pre Tax Pay (Monthly) = **£{round(company_income/12,):,}**")
st.subheader(f"Post Tax Pay (Monthly) = **£{round((company_income-Total_tax)/12,):,}**")
st.subheader(
    f"Thats **{round(((company_income-Total_tax)/12)/((company_income/12))*100):,}%**"
)

# =======================================================================================================================
