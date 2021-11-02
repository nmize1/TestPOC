import random

NUM_QUESTIONS = 20
LEVEL_UP = 3

r1 = {"Questions" : ["This is a level 1 question", "Level 1 question 2", "Level 1 question 3"],
      "Answer"    : [["Answer 1", "Answer 2", "Answer 3", "Answer 4"], ["Answer 1", "Answer 2", "Answer 3", "Answer 4"], ["Answer 1", "Answer 2", "Answer 3", "Answer 4"]],
      "Correct"   : ["1", "2", "3"],
      "NumCorrect": 0
     }

r2 = {"Questions" : ["This is a level 2 question", "Level 2 question 2", "Level 2 question 3"],
      "Answer"    : [["Answer 1", "Answer 2", "Answer 3", "Answer 4"], ["Answer 1", "Answer 2", "Answer 3", "Answer 4"], ["Answer 1", "Answer 2", "Answer 3", "Answer 4"]],
      "Correct"   : ["1", "2", "3"],
      "NumCorrect": 0
     }

r3 = {"Questions" : ["This is a level 3 question", "Level 3 question 2", "Level 3 question 3"],
      "Answer"    : [["Answer 1", "Answer 2", "Answer 3", "Answer 4"], ["Answer 1", "Answer 2", "Answer 3", "Answer 4"], ["Answer 1", "Answer 2", "Answer 3", "Answer 4"]],
      "Correct"   : ["1", "2", "3"],
      "NumCorrect": 0
     }

ranks = [r1, r2, r3]

rank = 0
q = 1

while(q <= NUM_QUESTIONS):
    qnum = random.randint(0, len(ranks[rank]["Questions"]) - 1)
    question = ranks[rank]["Questions"][qnum]
    print(question + "\n")
    for answer in ranks[rank]["Answer"][qnum]:
        print(answer + "\n")
    inp = input()
    if(inp == ranks[rank]["Correct"][qnum]):
        print("Correct!\n")
        ranks[rank]["NumCorrect"] = ranks[rank]["NumCorrect"] + 1
    else:
        print("Incorrect!\n")
        ranks[rank]["NumCorrect"] = ranks[rank]["NumCorrect"] - 1

    if(ranks[rank]["NumCorrect"] >= LEVEL_UP):
        rank = rank + 1
    elif(ranks[rank]["NumCorrect"] < 0):
        if(rank > 0):
            rank = rank - 1
        ranks[rank]["NumCorrect"] = 0

    print("You're currently rank " + str(rank + 1) + "\n")
    q = q + 1
    if rank >= 3:
        q = NUM_QUESTIONS + 1
