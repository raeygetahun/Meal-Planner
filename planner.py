from mealplanner import *
import random
daysinweek=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
mealplan=[]
def weekly():
    for days in daysinweek:
        mealplan.append(days)
        mealplan.append(" Breakfast: {} \n Lunch: {} \n Dinner:{}".
        format(random.choice(allbreakfast),random.choice(all_lunch),random.choice(alldinner)))
        
def daily():
    mealplan.append(" Breakfast: {} \n Lunch: {} \n Dinner:{}".
        format(random.choice(allbreakfast),random.choice(all_lunch),random.choice(alldinner)))
        
                                                     
# print(mealplan)
  