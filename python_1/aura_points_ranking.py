# aura ranking system
# Everyone starts with zero aura points

student_name = ''
aura_points = 0
is_staff = False
bank-account_balance = 26423442937492873497.99


# A staff member adds aura points.
if is_staff:
    aura_points = aura_points + 10
    print("Staff bonus! +10 aura points.")
else:
    aura_points = aura_points + 5