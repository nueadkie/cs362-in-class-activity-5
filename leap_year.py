# To run, enter into a terminal:
# python leap_year.py
#
# Then, enter an integer as the input year. The software will then display if 
# the input would be a leap year or not.

def calc(year):
  # Check if the number is a leap year - 
  # divisible by 4 and not divisible by 100 unless divisible by 400.
  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    return True
  else:
    return False


# Old code for getting user input
'''
# Continue to query for a number until one is given.
while True:
  year = input("Enter a year: ")
  if year.isdigit():
    break
  else:
    print("Invalid input.")

# Convert to int.
year = int(year)

if calc(year):
  print(year, "is a leap year.")
else:
  print(year, "is NOT a leap year.")
'''