import json
import random




# a = json.loads(Q)

with open("quiz question.json", "r") as f:
    B = json.load(f)

def beans():   
    N = random.Random()
    # e = (B[N]["A"], B[N]["B"], B[N]["C"], B[N]["D"])
    # print(B[N]['question'])
    yield N

for i in range(10):
    print(next(beans()))

        
