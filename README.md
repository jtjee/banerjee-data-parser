# banerjee-data-parser
Creates one csv file from multiple txt files collected in the field.

|Sample ID|Date|ng/ul|260/280|260/230|
|---------|----|-----|-------|-------|
|FOO1|01/01/2021|100|1.0|1.0|

Note: I do not plan to maintain this script.

# INSTALLATION
Make sure you are able to run python scripts.
You must have pandas installed. Install it by typing the following into an 
anaconda prompt or other shell. If using the linux terminal you will need to type ```pip3``` instead of ```pip```.

```
conda install pandas
```

or

```
pip install pandas
```
    
# USAGE

Copy the path of the folder which contains the .txt files you wish to process.
In an anaconda prompt or other shell with python, type the following
```
python batch_process.py "path"
```
Make sure that you put the path in quotations if there are spaces in it or you will get an error.
If you have issue, try to figure them out I guess. idk.

# CONTRIBUTORS
Justin Jee
Star Rodriguez
