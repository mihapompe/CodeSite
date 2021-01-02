
##### TESTER

from conditions_exercises import *
functions = [area, mean, check_for_snakes, even, pick_ice_cream, leap, parse]

args_num = [2,2,1,1,2,1,1]
test_cases = [
    [[2, 3], [1.5, 2.007], [-3135462.5, 53872.9358], [0, 2], [3.43, 3.141], [5, 5]],
    [[5, 10], [1, 10204], [-3, 3], [-3746873.45, -235.5], [-398635.4654, 348128.5]],
    ["python", "notsnake", "anaconda", "nd padfh", "boa", "snake", "moonpie"],
    [3, 4, 8, 84384, -37563, 843.3, 0, 0.1],
    [[-50, "sad"], [3, "happy"], [4, "motivated"], [6, "angry"], [31, "sad"], [300, "happy"], [11, "motivated"], [15, "angry"],],
    [2000, 0, 1000, 400, 100, 2058, 3545, 1254, 8456],
    ["Hey Microsoft has 20492045 employees.", "What are you saying that Apple employs 309758379 people.", "Breaking news Caterpillar has now got whoping 23670000 employees!"],
]
results = [
    [6, 3.0105000000000004, -168916569965.8075, 0, 10.77363, 25],
    [7.5, 5102.5, 0.0, -1873554.475, -25253.482699999993],
    [True, False, True, False, True, True, False],
    [False, True, True, True, False, False, True, False],
    [None, 'strawberry', 'strawberry', None, 'vanilla', 'vanilla', 'chocolate', 'blueberry'],
    [True, True, False, True, False, False, False, False, True],
    ['Microsoft is increasing their number of employees to 22541249', 'Apple is increasing their number of employees to 340734216', 'Caterpillar is increasing their number of employees to 26037000']
]


score = 0
max_score = 0

### Generate results from week#_solve
for i in range(len(functions)):         #For each function
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

import requests 
r = requests.post('http://127.0.0.1:8080/exercise_results/mihapompe', data={'module_number': 1, 'exercise_number': 1, 'score': score})