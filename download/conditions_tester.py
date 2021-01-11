
##### TESTER

from conditions_exercises import *
functions = [area, mean, check_for_snakes]

args_num = [2,2,1]
test_cases = [
    [[2, 3], [1.5, 2.007], [-3135462.5, 53872.9358], [0, 2], [3.43, 3.141], [5, 5]],
    [[5, 10], [1, 10204], [-3, 3], [-3746873.45, -235.5], [-398635.4654, 348128.5]],
    ["python", "notsnake", "anaconda", "nd padfh", "boa", "snake", "moonpie"]
]
results = [
    [6, 3.0105000000000004, -168916569965.8075, 0, 10.77363, 25],
    [7.5, 5102.5, 0.0, -1873554.475, -25253.482699999993],
    [True, False, True, False, True, True, False]
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
        print("Part {} hasn't been submitted".format(i+1))
    elif valid == 0:
        print("Part {} has valid solutions".format(i+1))

if score == 0:
    score_str = "0"
    score = 0
else:
    score_str = str(round(score/max_score*100, 1))
    score = int(score/max_score*100)
print("Your have finished {} % of this exercise.".format(score_str))
