import os


def start_timer():
    """ This is help for start_timer() """
    global start_time
    time = os.times()
    start_time = time[0] + time[1]


def end_timer(message="End Time"):
    """ This is help for end_timer() """
    global start_time
    time = os.times()
    end_time = time[0] + time[1]
    total_time = end_time - start_time
    print(f"{message:12}: {total_time:01.3f} seconds")

start_timer()
script_dir = os.path.dirname(__file__)
rel_path = "words"
abs_file_path = os.path.join(script_dir, rel_path)
lines = 0
for row in open(abs_file_path):
    lines += 1
print(lines)
end_timer()
