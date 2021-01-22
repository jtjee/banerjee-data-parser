import os
import pandas as pd
import time
import argparse
import sys

def strippify(filename):
    f = open(filename)
    text = f.read()
    f.close()
    nsplit = text.split('\n')
    for n in nsplit:
        if len(n.split('\t'))==13:
            f = open(filename.replace('.txt', '_stripped.csv'), 'a')
            f.write((n.split('\t')[0]
                        + ',' + n.split('\t')[2]
                        + ',' + n.split('\t')[4]
                        + ',' + n.split('\t')[7]
                        + ',' + n.split('\t')[8] + '\n'))
            f.close()

def batch_strippify(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                strippify(os.path.join(root, file))

def batch_convert_csv(folder):
    df = 0
    i=0
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".csv"):
                try:
                    d = pd.read_csv(os.path.join(root, file))
                    df = pd.concat([df, d], ignore_index=True)
                except:
                    df = pd.read_csv(os.path.join(root, file))
            i+=1
    df.to_csv(folder+'/DNA_extraction_data.csv')
    return i

if __name__ == '__main__':
    print('Processing Files')
    if len(sys.argv) != 2:
        print('ERROR: Please only specify one argument')
        sys.exit()

    start = time.time()
    folder = sys.argv[1]
    batch_strippify(folder)
    i = batch_convert_csv(folder)
    print('Converted {} Files in {} seconds'.format(i, round(time.time()-start,2)))