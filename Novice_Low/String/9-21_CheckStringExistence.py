""" Write a program that checks if a substring 'ee' and 'ab' exists in a given string. """
""" Output 'Yes' or 'No', depending on whether a substring 'ee' and 'ab' exists in a given string respectively. """

string = input()

print("Yes", end=" ") if 'ee' in string else print("No", end=" ")
print("Yes") if 'ab' in string else print("No")
