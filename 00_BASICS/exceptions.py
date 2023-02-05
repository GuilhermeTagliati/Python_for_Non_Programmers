# try:
#     # code that may cause exception
# except:
#     # code to run when exception occurs


# try:
#  print(x)

# except:
#  print("An exception occurred")


# try:
#     numerator = 10
#     denominator = 0

#     result = numerator/denominator

#     print(result)
# except:
#     print("Error: Denominator cannot be 0.")


try:
    even_numbers = [2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")