high_income = True
good_credit = False
student = True

# AND both condition is TRUE
# OR either condition is TRUE
# if high_income and good_credit:
#     print("Eligible")
# else:
#     print("Not eligible")

# if not student:
#     print("Eligible")
# else:
#     print("Not Eligible")
if (high_income or good_credit) and student:
    print("Eligible")
else:
    print("Not Eligible")

