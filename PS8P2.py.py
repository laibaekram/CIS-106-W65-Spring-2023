# Initialize the first two numbers of the sequence
a, b = 1, 1

# Loop through the first 20 numbers in the sequence
for i in range(20):
    # Print the current number in the sequence
    print(a, end=' ')

    # Update the first two numbers of the sequence
    a, b = b, a + b
  