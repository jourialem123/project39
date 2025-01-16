working_days=int(input("Enter number of school days"))
absent=int(input("Enter the days you were absent"))
attended_classes=working_days-absent
per_attended=(attended_classes/working_days)*100

if per_attended<75:
    print("You will not sit in the exam")
    print("Your attendance is ",per_attended,"%") 

else:
    print("You will take the exam") 
    print("Your attendance is ",per_attended,"%")  




