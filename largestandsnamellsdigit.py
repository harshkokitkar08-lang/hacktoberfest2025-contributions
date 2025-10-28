def find_largest_smallest_digit(number):
 
  if number == 0:
    print("The number is zero. Largest and smallest digit is 0.")
    return 0, 0

  s_number = str(abs(number))  # Convert to string and handle negative numbers
  largest_digit = int(s_number[0])
  smallest_digit = int(s_number[0])

  for digit in s_number[1:]:
    digit_int = int(digit)
    if digit_int > largest_digit:
      largest_digit = digit_int
    if digit_int < smallest_digit:
      smallest_digit = digit_int

  return largest_digit, smallest_digit

# Example usage:

num1 = 9876543210
largest1, smallest1 = find_largest_smallest_digit(num1)
if largest1 is not None:
  print(f"Largest digit in {num1}: {largest1}")
  print(f"Smallest digit in {num1}: {smallest1}")

num2 = -5082
largest2, smallest2 = find_largest_smallest_digit(num2)
if largest2 is not None:
  print(f"Largest digit in {num2}: {largest2}")
  print(f"Smallest digit in {num2}: {smallest2}")
