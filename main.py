from collections import Counter,defaultdict
import matplotlib.pyplot as plt

def fread(fname):
    with open(fname,mode='r') as f:
        contents = f.read()
    return contents.lower()
def letter_counter(input_str):
    mushed = ''.join(e for e in input_str if e.isalpha() and e not in [ 'à', 'â', 'æ', 'ç', 'è', 'é', 'ê', 'î', 'œ'])
    letter_count = Counter(mushed)
    new_d = dict(letter_count)
    keys = list(new_d.keys())
    keys.sort()
    result = defaultdict()
    for key in keys:
        result[key] = new_d[key]
    return result

def plot(data):
    plt.bar(range(len(data)), list(data.values()), align='center')
    plt.xticks(range(len(data)), list(data.keys()))


#boo
