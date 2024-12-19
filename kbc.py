import random
questions =[
    {
        "ques":"Ouestion : What is a Computer",
        "option":" 1.Water Machine \n 2.Electronic device \n 3.Fire Machine",
        "ans":2
    },
    {
        "ques":"Ouestion : What is the full form of CD",
        "option":" 1.Compact Disc \n 2.Connect Disc \n 3.Contract Disc",
        "ans":1
    },
    {
        "ques":"Ouestion : What is the full form of CU",
        "option":" 1.Compact Unit \n 2.Control Unit\n 3.Confuse Unit",
        "ans":2
    },
]
random.shuffle(questions)
score = 0
 
for question in questions:
    print(question["ques"])
    print(question["option"])
    UserAns = int(input("Please enter your answer : "))
    if UserAns == question["ans"]:
        print("Right Answer")
        score += 1
    else:
        print("Wrong Answer")
        

print(score)
