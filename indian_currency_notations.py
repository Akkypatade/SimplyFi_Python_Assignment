
def to_indian_currency_notation(number):
  number_to_str = str(number) #Returns a number as a int but converting into string
  if len(number_to_str) <= 3:
    return number_to_str #If the length greater than or equal to 3 returning it as it is
  else:
    groups_of_three = [] #Creating an empty list which will append group of three numbers
    while number_to_str:
      groups_of_three.append(number_to_str[-3:]) #appending last three digit of the number
      number_to_str = number_to_str[:-3] 
    groups_of_three.reverse()
    return ','.join(groups_of_three) # Joining the whole number again

# Example usage
number = int(input("Enter the number of your choice: "))
indian_currency_str = to_indian_currency_notation(number)
print(indian_currency_str)