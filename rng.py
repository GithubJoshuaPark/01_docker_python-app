from random import randint

min_number = int(input("Enter the minimum number: "))
max_number = int(input("Enter the maximum number: "))

if(max_number < min_number):
  print("The maximum number should be greater than the minimum number")
else:
  rnd_number = randint(min_number, max_number)
  print(f"Random number between {min_number} and {max_number} is: {rnd_number}")

def calculate_weight_gain(weight, height, bmi):
    normal_weight_lower = 18.5 * (height * height)  # Minimum normal BMI is 18.5
    if bmi < 18.5:
        weight_to_gain = normal_weight_lower - weight
        return weight_to_gain
    return 0

def calculate_weight_loss(weight, height, bmi):
    normal_weight_upper = 24.9 * (height * height)  # Maximum normal BMI is 24.9
    if bmi >= 25:
        weight_to_lose = weight - normal_weight_upper
        return weight_to_lose
    return 0

def calculate_bmi():
    while True:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in cm: ")) / 100  # Convert cm to meters

        bmi = weight / (height * height)

        print(f"\nYour BMI is: {bmi:.2f}")

        # Determine health status
        if bmi < 18.5:
            print("You are underweight")
            weight_to_gain = calculate_weight_gain(weight, height, bmi)
            print(f"You need to gain {weight_to_gain:.2f} kg to reach normal weight")
        elif 18.5 <= bmi < 25:
            print("You have a normal weight")
        elif bmi >= 25:
            print("You are overweight" if bmi < 30 else "You are obese")
            weight_to_lose = calculate_weight_loss(weight, height, bmi)
            print(f"You need to lose {weight_to_lose:.2f} kg to reach normal weight")

        try_again = input("\nDo you want to calculate again? (yes/no): ").lower()
        if try_again != 'yes':
            print("Thank you for using BMI calculator. Goodbye!")
            break

# Start BMI calculator after random number generator
calculate_bmi()