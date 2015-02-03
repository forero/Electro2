import csv as csv
import numpy as np


#count students and tasks
csvfile = open("tablero.csv", "r")
content = csv.reader(csvfile)
n_students = 0


for line in content:
    n_times = len(line) - 1
    n_students = n_students+1
csvfile.close()


#load arrays and lists
csvfile = open("tablero.csv", "r")
content = csv.reader(csvfile)
random = np.random.random(n_students)

names = [ ]
grades = np.zeros((n_students, n_times))

n_students = 0
for line in content:
    names.append(line[0])
    for task_i in range(n_times):
        grades[n_students, task_i] = float(line[task_i+1])
    n_students = n_students + 1
csvfile.close()


# pick the names for the different tasks from those who don't have a grade yet
picked = 1
for task_i in range(n_times):
    if picked:
        left = np.where(np.int_(grades[:,task_i])==-1)
        left = left[0]
        if np.size(left):
            print "Task %d"%(task_i)            
            print "Es el turno de %s"%(names[np.random.choice(left)])
            picked = 0
