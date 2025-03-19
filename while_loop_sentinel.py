# Initialize the sum variable
total_sum = 0

# Start an infinite loop
while True:
<<<<<<< HEAD
    # Prompt user for input
    user_input = input("Enter a number (or 'stop' to finish): ").strip().lower()

    # Check if the sentinel value "stop" is entered
    if user_input == "stop":
        break  # Exit the loop

    try:
        # Convert input to a float and add to total_sum
        number = float(user_input)
        total_sum += number
    except ValueError:
        print("Invalid input. Please enter a numeric value or 'stop'.")

# Print the final sum
print("The total sum is:", total_sum)
=======
   user_input = input("Enter a number (or 'stop' to finish): ")    
   if user_input.strip().lower() == "stop":
       break  # Exit the loop    
   try:
       number = float(user_input)
       total_sum += number
   except ValueError:
       print("Invalid input. Please enter a numeric value or 'stop'.")
       break  # Exit the loop
 print("The total sum is:", total_sum)
>>>>>>> c4ca6c98fd5efc12123068382363011d800cb448

