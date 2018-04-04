# Chapter 5 Exercise 4
# Python 3 version
import os

start_time = 0
LOOP_COUNT = 200
words = []
words_dict = {}
########################################################
# TIMER FUNCTIONS


def start_timer():
    global start_time
    (utime, stime) = os.times()[0:2]
    start_time = utime+stime


def end_timer(txt):
    (utime, stime) = os.times()[0:2]
    end_time = utime+stime
    print("{0:<12}: {1:01.3f} seconds".format(txt, end_time-start_time))


def load_data():
    global words
    script_dir = os.path.dirname(__file__)
    rel_path = "words"
    abs_file_path = os.path.join(script_dir, rel_path)
    words = open(abs_file_path).read().split('\n')


def brute_force():
    global words
    for i, word in enumerate(words):
        if word == 'Zulu':
            line = i
            return line
            break


def infunc():
    global words
    if 'Zulu' in words:
        return 1
    else:
        return 0


def index():
    global words
    return words.index('Zulu')


def dictionary():
    global words_dict
    return words_dict['Zulu']

########################################################
# MAIN

load_data()

# Brute force
line = 0
start_timer()
for i in range(1, LOOP_COUNT):
    line = brute_force()
end_timer("Brute_force")
print("Brute_force line number:", line)
line = 0

# index
start_timer()
for i in range(1, LOOP_COUNT):
    line = index()
end_timer("Index")
print("Index line number:", line)
line = 0

# in
start_timer()
for i in range(0, LOOP_COUNT):
    line = infunc()
end_timer("In")
line = 0

# Create a dictionary from the words list
i = 0
start_timer()

globals()['words_dict'] = dict(zip(words, range(len(words))))


for i in range(1, LOOP_COUNT):
    line = dictionary()
end_timer("Dictionary")

print("Dictionary line number:", line)
line = 0
