#4. Create a list of numbers from 1 to 20. Write a for loop that iterates through the list, converts each number to a string, and creates a new list with these string values. Print the new list.
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
stringValue=[]
for number in list:
    numToStr=str(number)
    stringValue.append(numToStr)
print(stringValue)