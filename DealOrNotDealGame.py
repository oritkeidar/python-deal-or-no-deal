from random import randint
from time import sleep

def choosh_cases(TimesToPlay):
    print("It's time to choose " + str(TimesToPlay) + " brief cases")
    for i in range(TimesToPlay):
        sleep(1)
        x = input("\nChoose case number:")
        if x == your_case_choice:
            print("case no " + x + " is not valid for opening")
            x = input("Choose another case number:")
        sleep(2)
        print("the amount in case number " + x + " is: " + str(brief_cases["case"+ x]) + "$")
        brief_cases.pop("case" + x)

def bank_offer_func():
    print("\n")
    print(brief_cases.keys())
    sleep(2)
    print("\nLet's hear the bank offer.....:")
    sleep(2)
    print("\nBank offer is: " + str(round_offer) + "$")
    sleep(2)


brief_cases={"case1": "none", "case2": "none", "case3":"none", "case4": "none", "case5":"none", "case6": "none",
             "case7": "none", "case8":"none", "case9": "none", "case10": "none", "case11":"none", "case12":"none", "case13": "none"
             ,"case14": "none", "case15": "none", "case16": "none", "case17": "none", "case18": "none", "case19":"none","case20":
             "none", "case21":"none", "case22":"none", "case23":"none","case24":"none","case25":"none", "case26":"none"}

case_values=[0.01, 1, 5, 10,25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 20000, 50000
    ,75000,100000,200000, 300000, 400000,500000, 750000, 1000000]

for i in range(26):
    brief_cases["case" + str(i+1)] =(case_values.pop(randint(0, len(case_values) - 1)))

print(brief_cases)


name =(input("\nEnter your name:"))
sleep(1)
print("\nhello " + name +",lets play deal or no deal!!!")
sleep(2)
your_case_choice= input("\npick a case number between 1-26:")
your_case_value=(brief_cases["case"+ your_case_choice])
brief_cases.pop("case" + your_case_choice)
# print(str(your_case)+ "$")
# first opening cases- 6 cases

TimesToPlay = 6
new_value="0"
final_value="0"
while len(brief_cases)>=2:
    if TimesToPlay<1:
        TimesToPlay=1
    choosh_cases(TimesToPlay)
    sum_values =sum(brief_cases.values())
    sum_values_1 =sum_values +your_case_value
    bank_offer= sum_values_1 / (len(brief_cases) + 1)
    round_offer=randint(round(bank_offer*0.9),round(bank_offer*1.1))
    round_offer=str(round_offer)
    if len(round_offer)==4:
        round_offer = round_offer[:1] + "," + round_offer[1:]
    elif len(round_offer)==5:
        round_offer = round_offer[:2] + "," + round_offer[2:]
    elif len(round_offer) == 6:
        round_offer = round_offer[:3] + "," + round_offer[3:]
    bank_offer_func()
    deal_or_no_deal = input("\nDeal or no deal?")
    if deal_or_no_deal == "deal":
        print("congratulations, you won " + round_offer + "$")
        break
    elif len(brief_cases)==1:
        print("Time to reveal your case")
        sleep(2)
        print("Your case value is: " + str(your_case_value) + "$, congratulations!!!")
    else:
        print("Lets keep playing")

    TimesToPlay=TimesToPlay-1










