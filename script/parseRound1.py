import re
import json
from pprint import pprint
input_file = "Round1_2.txt"
output_file = "Round1.json"

result = []

with open(input_file, 'r') as fp:
    currentCategory = None
    currentQuestion = None
    for line in fp:
        m = re.match("(.*): (.*)", line)
        if m is None:
            continue
        key = m.group(1)
        statement = m.group(2)
        if key.upper() == "CATEGORY":
            if currentCategory is not None:
                result.append(currentCategory.copy())
            currentCategory = {}
            currentCategory['name'] = statement
            currentCategory['easy'] = []
            currentCategory['medium'] = []
            currentCategory['hard'] = []
        if key.upper() in {"QE", "QM", "QH"} and currentCategory is not None:
            currentQuestion = {}
            currentQuestion['question'] = statement
            currentQuestion['state'] = False
            currentQuestion['incorrectAnswers'] = []
            currentQuestion['img'] = ''
            answer_match = re.match("(.*): (.*)", fp.readline())
            count = 0
            print(statement)
            while answer_match is not None:
                if count == 0 and answer_match[1] == 'IMG':
                    currentQuestion['img'] = answer_match[2]
                elif count == 0 and answer_match[1] == "A":
                    currentQuestion['correctAnswer'] = answer_match[2]
                    count += 1
                else:
                    currentQuestion['incorrectAnswers'].append(answer_match[2])
                answer_match = re.match("(.*): (.*)", fp.readline())
            if key.upper() == "QE":
                currentCategory['easy'].append(currentQuestion.copy())
            elif key.upper() == "QM":
                currentCategory['medium'].append(currentQuestion.copy())
            elif key.upper() == "QH":
                currentCategory['hard'].append(currentQuestion.copy())

result.append(currentCategory.copy())
with open(output_file, 'w') as fp2:
    json.dump(result, fp2, indent=2)
