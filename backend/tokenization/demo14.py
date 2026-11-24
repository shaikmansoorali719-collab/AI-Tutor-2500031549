#reading keys and values in the dictionaey

n = int(input("Enter no.of entries :"))

student ={}
for i in range(n):
    key = input("Enter Key:")
    value = input("Enter Value:")
    student[key] = value

print(student)