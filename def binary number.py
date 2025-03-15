
n = 33  # Change this to any number you want

# If n is 0, print "0" directly
if n == 0:
    print("0")
else:
    binary = ""  # Start with an empty string

    while n > 0:
        remainder = n % 2  # Get remainder (0 or 1)
        binary = str(remainder) + binary  # Add remainder at the front here first str(1) +"" to transfer to "1"        n = n // 2  # Divide n by 2

    print("Binary:", binary)  # Print the final binary number

