def compute_tuition(credit_hours, district_code):
    if district_code == 'I':
        return 250 * credit_hours
    elif district_code == 'O':
        return 550 * credit_hours
    else:
        return 0

last_name = input("Enter student last name: ")
credit_hours = int(input("Enter credit hours: "))
district_code = input("Enter district code (I or O): ")

tuition_owed = compute_tuition(credit_hours, district_code)
if tuition_owed == 0:
    print("Invalid district code entered")
else:
    print("Student name:", last_name)
    print("Tuition owed:", tuition_owed)