from nada_dsl import *

def nada_main():

    party1 = Party(name="party1")

    int1 = SecretInteger(Input(name = "int1", party = party1))
    int2 = SecretInteger(Input(name="int2", party = party1))

    diff = int1-int2

    if abs(diff)<=1: #choosing to consider +- 0.01 hour as equal
        result = 0
    elif diff > 0: # int1 is the larger value
        result = 1
    else:
        result = -1 #int1 is the smaller value
    
    return [Output(result, "result", party1)]



    