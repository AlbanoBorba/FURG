import time
from multiprocessing import Process, Value, Lock

counter_lock = Lock()
counter = 0

def search_word(text, term):
    global counter
    with counter_lock:
        counter += text.count(term)

def parallel_search_word(text, size, term, num_processes):
    jobs = []
    chars_per_string = size/num_processes
    now = 0
    for i in xrange(num_processes):
        p = Process(target=search_word,
                    args=(text[now:now+chars_per_string], term))
        jobs.append(p)
        p.start()
        now += chars_per_string
    
    for job in jobs:
        job.join()

def main():
    global counter
    text = "You are not iterating through the words in the string, you are iterating through the characters in the string. To iterate through the words, you would first need to split the string into words , using str.split() , and then iterate through that . Example - ".lower()
    term = " you "
    num_processes = 2
    total = ""

    for i in xrange(1000000):
        total += text

    size = len(total)

    now = time.time()
    parallel_search_word(total, size, term, num_processes)
    print counter
    print time.time() - now

    now = time.time()
    print total.count(term)
    print time.time() - now

main()