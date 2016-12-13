import os
import re
import random
import timeit

def read_wiki():
    path_to_file = os.path.realpath('.')
    n = 0
    with open(os.path.join(path_to_file, 'simple_english_wikipedia.txt'), encoding="utf8") as file:
        for line in file:
            for char in line:
                if re.findall('([A-Z a-z ])', char):
                    n += 1
    return n
def calculate_zipf():
    zipf = {}
    probs_new = 0
    zipf_probabilities = {' ': 0.17840450037213465, '1': 0.004478392057619917,
                          '0': 0.003671824660673643, '3': 0.0011831834225755678,
                          '2': 0.0026051307175779174, '5': 0.0011916662329062454,
                          '4': 0.0011108979455528355, '7': 0.001079651630435706,
                          '6': 0.0010859164582487295, '9': 0.0026071152282516083,
                          '8': 0.0012921888323905763, '_': 2.3580656240324293e-05,
                          'a': 0.07264712490903191, 'c': 0.02563767289222365,
                          'b': 0.013368688579962115, 'e': 0.09688273452496411,
                          'd': 0.029857183586861923, 'g': 0.015076820473031856,
                          'f': 0.017232219565845877, 'i': 0.06007894642873102,
                          'h': 0.03934894249122837, 'k': 0.006067466280926215,
                          'j': 0.0018537015877810488, 'm': 0.022165129421030945,
                          'l': 0.03389465109649857, 'o': 0.05792847618595622,
                          'n': 0.058519445305660105, 'q': 0.0006185966212395744,
                          'p': 0.016245321110753712, 's': 0.055506530071283755,
                          'r': 0.05221605572640867, 'u': 0.020582942617121572,
                          't': 0.06805204881206219, 'w': 0.013964469813783246,
                          'v': 0.007927199224676324, 'y': 0.013084644140464391,
                          'x': 0.0014600810295164054, 'z': 0.001048859288348506}
    for char, prob in zipf_probabilities.items():
        probs_new += prob
        zipf[char] = probs_new
    return zipf

def calculate_uniform():
    uniform = {}
    probs_new = 0
    uniform_probabilities = {' ': 0.1875, 'a': 0.03125, 'c': 0.03125, 'b': 0.03125, 'e': 0.03125, 'd': 0.03125,
                             'g': 0.03125, 'f': 0.03125, 'i': 0.03125, 'h': 0.03125, 'k': 0.03125, 'j': 0.03125,
                             'm': 0.03125, 'l': 0.03125, 'o': 0.03125, 'n': 0.03125, 'q': 0.03125, 'p': 0.03125,
                             's': 0.03125, 'r': 0.03125, 'u': 0.03125, 't': 0.03125, 'w': 0.03125, 'v': 0.03125,
                             'y': 0.03125, 'x': 0.03125, 'z': 0.03125}

    for char, prob in uniform_probabilities.items():
          probs_new += prob
          uniform[char] = probs_new
    return uniform

def make_gibberish(prob, n, prob_name):
    i = 0
    words = ''
    find_char = []
    while i <= n:
        i += 1
        rand = random.random()
        for key, val in prob.items():
            if val >= rand:
                find_char.append(val)
        try:
            next_char_val = min(find_char) #finds the closest (smaller) value of the probability model to rand
        except(Exception):
            pass

        for char, val in prob.items():
            if next_char_val == val:
                next_char = char

        find_char = [] #reinitializes the array
        words += next_char
    save_file(words, prob_name)

def save_file(words, file_name):
    path_to_file = os.path.realpath('.')
    with open(os.path.join(path_to_file, file_name+'.txt'), 'w') as file_to_write:
        file_to_write.write(words)
        file_to_write.close()

def main():
    print('Counting chars in SEW please wait')
    #n = read_wiki() #89860319 number of letters and spaces
    n = 89860319
    zipf = calculate_zipf()
    uniform = calculate_uniform()
    print('Starting gibberish creation from zipf')
    timeit.timeit(make_gibberish(zipf, n, 'zipf'))
    print('zipf.txt Created')
    print('Starting gibberish creation from uniform probabilities')
    timeit.timeit(make_gibberish(uniform, n, 'uniform'))
    print('uniform.txt Created')

if __name__ == "__main__":
        main()