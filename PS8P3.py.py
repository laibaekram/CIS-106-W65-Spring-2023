f = open("data.txt", "r")
total_bonus = 0
c = 0
lastname = f.readline()
while lastname != "":
  salary = f.readline()
  print()
  print("Employee Last Name:  ", lastname)
  print("Employee Salary: $", 
  format(float(salary),'10,.2f'))
  bonus = float(salary) * 0.10
  print("Employee Bonus: $", format(bonus, '10,.2f'))
  total_bonus = total_bonus + bonus
  c = c + 1
  lastname = f.readline()
f.close()
avg_bonus = total_bonus / c
print(" ")
print("Average Bonus: $", format(float(avg_bonus), '10,.2f'))