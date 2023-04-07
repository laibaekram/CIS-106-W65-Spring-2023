# Define cost per credit for in-district and out-of-district students
in_district_cost = 250.00
out_district_cost = 500.00

# Open the text file containing student data
with open('student_data.txt', 'r') as file:
    # Initialize variables to hold the total tuition and the number of students
    total_tuition = 0
    num_students = 0
    
    # Loop through each line in the file
    for line in file:
        # Split the line into the last name, district code, and number of credits
        last_name, district_code, credits = line.strip().split(',')
        credits = int(credits)
        
        # Determine the cost per credit based on the district code
        if district_code == 'I':
            cost_per_credit = in_district_cost
        elif district_code == 'O':
            cost_per_credit = out_district_cost
        else:
            print(f'Invalid district code: {district_code}')
            continue
        
        # Calculate the tuition owed
        tuition_owed = credits * cost_per_credit
        
        # Display the student's last name, credits taken, and tuition owed
        print(f'{last_name}: {credits} credits, ${tuition_owed:.2f}')
        
        # Add the tuition owed to the total tuition and increment the number of students
        total_tuition += tuition_owed
        num_students += 1
    
    # Display the total tuition and the number of students
    print(f'Total tuition owed: ${total_tuition:.2f}')
    print(f'Number of students: {num_students}')