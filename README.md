# banerjee-data-parser
Creates one csv file from multiple txt files collected in the field

# batch_process.py

This script will search for any text files within a given folder and convert
them to one .csv files containing:
Sample ID, Date, ng/ul, 260/280, 260/230

You might need to verify that the data was correctly entered.

# INSTALLATION
Make sure you are able to run python scripts.
You must have pandas installed. Install it by typing the following into an 
anaconda prompt or other shell.

'''
conda install pandas
'''

or

'''
pip install pandas
'''
    
# USAGE

Copy the path of the folder which contains the .txt files you wish to process.
In an anaconda prompt or other shell with python, type the following
    '''
    python batch_process.py "path"
    '''
Make sure that you put the path in quotations or you will get an error.
If you have issue, try to figure them out I guess. idk.

# CONTRIBUTORS
Justin Jee
