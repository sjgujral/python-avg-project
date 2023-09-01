#importing datetime module
import datetime

#function to calculate the average of numbers in a list
def calculate_average(numbers):
    try:
        #check if the input list is empty
        if len(numbers) == 0:
            raise ValueError("Input list is empty. Please provide some numbers.")

        #calculate the average
        total = sum(numbers)
        average = total / len(numbers)

        return average

    except ZeroDivisionError:
        print("Error: Division by zero! Please provide at least one number.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#main function
def main():
    print("Welcome to the Average Calculator!")

    #user input
    input_numbers = input("Enter a list of numbers separated by spaces: ").split()

    #convert the input strings to integers
    numbers = []
    for num in input_numbers:
        try:
            numbers.append(float(num))
        except ValueError:
            print(f"Warning: Skipping invalid input - {num}")

    #check if the user input has any valid numbers
    if not numbers:
        print("No valid numbers provided. Exiting.")
        return

    #calculate and display the average
    average = calculate_average(numbers)
    if average is not None:
        print(f"The average of the provided numbers is: {average}")

    #current date and time using the datetime module
    current_time = datetime.datetime.now()
    print(f"Program executed at: {current_time}")

if __name__ == "__main__":
    main()