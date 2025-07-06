
numberLargest = int(input("Enter Largest number : "))
numberSmallest = int(input("Enter Smallest number :"))

while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLarfest = numberStore

print("HCF is :",numberLargest)