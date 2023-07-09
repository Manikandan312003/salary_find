#salary
def SalaryCalculate(week):
    total_hrs,bonous,salary=0,0,0
    for i in range(7):
        total_hrs+=week[i]
        salary+=week[i]*100
        if i==0:
            bonous+=50*week[i]
        if i==6:
            bonous+=week[i]*25
        if week[i]>8:
            bonous+=15*(week[i]-8)
    if total_hrs>40:
        salary+=(total_hrs-40)*25
    return salary+bonous
hours=list(map(int,input().split()))
print(SalaryCalculate(hours))