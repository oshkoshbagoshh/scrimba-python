# @Author: AJ Javadi
# @Email: amirjavadi25@gmail.com
# @Date: 2024-03-12 20:58:32
# @Last Modified by:   undefined
# @Last Modified time: 2024-03-12 20:58:32
# @Description: file:///Users/aj/Desktop/bootcamp/Scrimba/Scrimba_Python/activities/list-exercise.py

# =============================
#           CHALLENGE
# lemonade sold over 2 weeks, profit  for each lemondade is $1.5
# add another day to week 2 by capturing a number as input
# combine the two lists into the list called 'sales'
# calculate / print how much you have earned on
# Best day
# worst day
# seperately and in total
# hint: 3 prints total
# ==========================


sales_w1 = [7, 3, 42, 19, 15, 35, 9]
sales_w2 = [12, 4, 26, 10, 7, 28]
sales = []
new_day = input("Enter # of lemonades for new day:  ")
sales_w2.append(int(new_day))
sales.extend(sales_w1)
sales.extend(sales_w2)
# sales = sales_w1 + sales_w2

# option 1  - sort the list so it's ordered from lowest to highest and then slice it 
sales.sort()
worst_day_prof = sales[0] * 1.5
best_day_prof = sales[-1] * 1.5


# option 2  - use min + max
# worst_day_prof = min(sales) * 1.5 
# best_day_prof = max(sales) * 1.5


print(f"Worst day profit: ${worst_day_prof}")
print(f"Best day profit: ${best_day_prof}")
print(f"Combined profit: ${worst_day_prof + best_day_prof} ")
