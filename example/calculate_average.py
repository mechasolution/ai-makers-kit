scores = [37, 93, 59, 82]

def calculate_average(scores):
    if len(scores) == 0:
        return 0
    
    sum = 0
    for score in scores:
        sum = sum + score
    return sum / len(scores)

result = calculate_average(scores)
print(result)