def get_pay_rate(job_code):
    if job_code == 'L':
        return 25
    elif job_code == 'A':
        return 30
    elif job_code == 'J':
        return 50
    else:
        return 0

def get_gross_pay(hours_worked, pay_rate):
    if hours_worked <= 40:
        return hours_worked * pay_rate
    else:
        overtime_hours = hours_worked - 40
        overtime_pay_rate = pay_rate * 1.5
        return 40 * pay_rate + overtime_hours * overtime_pay_rate

last_name = input("Enter last name: ")
job_code = input("Enter job code: ")
hours_worked = float(input("Enter hours worked: "))

pay_rate = get_pay_rate(job_code)
if pay_rate == 0:
    print("Invalid job code entered")
else:
    gross_pay = get_gross_pay(hours_worked, pay_rate)
    print("Last name:", last_name)
    print("Gross pay:", gross_pay)