from datetime import date
today=date.today()
cyear=today.year
fyear=int(input("Enter future year : "))
leaps=[year for year in range(cyear,fyear+1) if((year%4==0) or (year%100!=0) and (year%400==0))]
print(leaps)
