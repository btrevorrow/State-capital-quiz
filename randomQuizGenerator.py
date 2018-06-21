#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
    
states = list(capitals.keys())
capList = list(capitals.values())
    
# Generate 35 quiz files.
for quizNum in range(35):
       # Create the quiz and answer key files.
       quizFile = open('quiz' + str(quizNum + 1) + '.txt', 'w')
       ansFile = open('answers' + str(quizNum + 1) + '.txt', 'w')     

       # Write out the header for the quiz.
       quizFile.write("""This multiple choice quiz will test your knowledge of
                      US state capitals! (Quiz no. """ + str(quizNum + 1) 
                      + "\n\n")
       ansFile.write("These are the answers to quiz no. " + str(quizNum + 1) 
                     + "\n\n")

       # Shuffle the order of the states.
       random.shuffle(states)

       # Loop through all 50 states, making a question for each.
       qNum = 1
       for state in states:
           answer = capitals[state]
           choices = [answer]
           #Remaining choices taken from list with answer removed
           i = capList.index(answer)
           answerRemoved = capList[:i] + capList[i+1:]
           choices += random.sample(answerRemoved, 3)
           random.shuffle(choices)
           
           quizFile.write(str(qNum) + ". What is the state capital of " 
                          + state + "?\n" + 
                          '(a) ' + choices[0] + '\n'
                          '(b) ' + choices[1] + '\n'
                          '(c) ' + choices[2] + '\n'
                          '(d) ' + choices[3] + '\n\n')
           ansFile.write(str(qNum) + '. ' + answer + '\n\n')
           qNum += 1
       
       quizFile.close()
       ansFile.close()
    