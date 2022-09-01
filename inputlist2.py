n = int(input("Enter the number of elements: "))

a = list(map(int,input("\nEnter the values: ").strip().split()))[:n]

print("The list is: ",a)