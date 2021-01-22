import os
import pandas as pd
import time
import sys
import io

def batch_convert_csv(folder):
    i = 0
    first = True
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                text = open(os.path.join(root, file)).read()
                textn = text.split('\n\n')
                data = io.StringIO(textn[0])
                if first:
                    df = pd.read_csv(data, sep="\t")
                    first = False
                else:
                    df = pd.concat([df, pd.read_csv(data, sep="\t")], ignore_index=True)
                i += 1
    df_filtered = df[['Sample ID', 'Date ', 'ng/ul ', '260/280 ', '260/230 ']]
    df_filtered.to_csv(folder + '/data.csv', index=False)
    return i

if __name__ == '__main__':
    print('Processing Files')
    if len(sys.argv) != 2:
        print('ERROR: Please only specify one argument')
        sys.exit()
    folder = sys.argv[1]
    start = time.time()
    i = batch_convert_csv(folder)
    print('Converted {} Files in {} seconds'.format(i, round(time.time()-start,2)))