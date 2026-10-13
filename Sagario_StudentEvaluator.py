import time
#import time to have a pause before the program

def display_header():
   print("Student Performance Evaluator!")
   print("------------------------------")
   print("")
# defining the function header

display_header()
time.sleep(2)

def eva_performance():
    stud_info = input("Enter Name")

#defining the second function

eva_performance()

stud_info2 = float(input("Enter assessment score"))
stud_info3 = float(input("Enter assessment score"))
stud_info4 = float(input("Enter last assessment score"))
perf = stud_info2 + stud_info3 + stud_info4 / 3

# assigning variables

def display_report():
     if perf <= 100:
        print("Outstanding")
     elif perf <= 90:
        print("Very satisfactory")
     elif perf <= 80:
        print("Satisfactory")
     elif perf <= 70:
        print("Fairly satisfactory")
     elif perf <= 75:
        print("Needs  improvement")


display_report()

#displaying the report