"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:

file = open('questions.txt', 'r')
lines = file.readlines()
file.close()

line_count = len(lines)
score = 0
for line in lines:
    q, a = line.split('=')
    user_answer = int(input(f'{q} = '))
    if user_answer == int(a):
        score += 1

result = open('result.txt', 'w')
result.write(f'Your final score is {score}/{line_count}')
result.close()
