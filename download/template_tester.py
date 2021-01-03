# =============================================================================
# TESTER
# =============================================================================

from template_exercises import *    # Change to the appropriate module

# Import any other necessary libraries
import numpy as np
import random

# =============================================================================
# DATA GENERATOR FUNCTIONS
# These functions should end with _t



# =============================================================================
# INPUTS

functions = []  #user function names
functions_t = []   #terster function names
args_num = []   #number of arguments per par
test_cases = [
    
    ]
results = []

# =============================================================================
# GENERATE RESULTS

for i in range(len(functions_t)):
    func = functions_t[i]
    results.append([])
    if args_num[i] == 1:
        for args in test_cases[i]:
            results[i].append(func(args))
    else:
        for args in test_cases[i]:
            results[i].append(func(*args))

# =============================================================================
# TESTER

score = 0
max_score = 0

for i in range(len(functions)):
    max_score += len(test_cases[i])
    func = functions[i]
    valid = 0
    submitted = 0
    for case in range(len(test_cases[i])):
        score += 1
        if args_num[i] == 1:
            res = func(test_cases[i][case])
        else:
            res = func(*test_cases[i][case])
        if "all" in dir(res):
            if  "all" in dir(results[i][case]):
                if results[i][case].all() != res.all():
                    score -= 1
                    if results[i][case] is not None and res is None:
                        submitted += 1
                    else:
                        valid += 1
                        print("Wrong result, expected {}, received {}".format(results[i][case], res))
            else:
                if results[i][case] != res.all():
                    score -= 1
                    if results[i][case] is not None and res is None:
                        submitted += 1
                    else:
                        valid += 1
                        print("Wrong result, expected {}, received {}".format(results[i][case], res))
        else:
            if  "all" in dir(results[i][case]):
                if results[i][case].all() != res:
                    score -= 1
                    if results[i][case] is not None and res is None:
                        submitted += 1
                    else:
                        valid += 1
                        print("Wrong result, expected {}, received {}".format(results[i][case], res))
            else:
                if results[i][case] != res:
                    score -= 1
                    if results[i][case] is not None and res is None:
                        submitted += 1
                    else:
                        valid += 1
                        print("Wrong result, expected {}, received {}".format(results[i][case], res))
    if submitted > 0:
        print("Exercise {} hasn't been submitted".format(i+1))
    elif valid == 0:        
        print("Exercise {} has valid solutions".format(i+1))

if score == 0:
    score_str = "0"
else:
    score_str = str(round(score/max_score*100, 1))
print("Your have finished {} % of this week exercises".format(score_str))
score = int(score/max_score*100)
