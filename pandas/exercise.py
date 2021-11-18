import numpy as np
import pandas as pd

from numpy.random import randn

# 1)
salaries = pd.read_csv('2_pandas_Salaries.csv')
print(salaries.columns)
print()

# 2)
print(salaries.info())
print()

# 3)
basePay = salaries.iloc[0:10000]['BasePay']
print(basePay.mean())
print()

# 4)
totalPayBenefits = salaries['TotalPayBenefits']
print(totalPayBenefits.max())
print()

# 5)
joseph = salaries[salaries['EmployeeName'] == 'JOSEPH DRISCOLL']
print(joseph['JobTitle'])
print()

# 6)
print(joseph['TotalPay'])
print()

# 7)
top = salaries.iloc[salaries['TotalPayBenefits'].idxmax()]
print(top['EmployeeName'])
print()

# 8)
bottom = salaries.iloc[salaries['TotalPayBenefits'].idxmin()]
print(bottom['EmployeeName'])
print()

# 9)
byYear = salaries.groupby('Year')
print(byYear['TotalPay'].mean())
print()

# 10)
uniqueTitles = salaries['JobTitle']
print(str(uniqueTitles.nunique()) + ' unique job titles')
print()

# 11)
byTitle = salaries.groupby('JobTitle')
# byTitle.sort_values()
print(byTitle.count())
