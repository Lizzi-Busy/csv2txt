# run this program break a csv file into separate text files

################## INSTRUCTION ###################
# 1.edit the values of indir, colname, outdir below
# 2.save change to the py file
# 3.open cmd (or any console emulator of your choice)
# 4.cd into the directory of the py file
# 5.type 'python csv2txt.py' or 'python3 csv2txt.py'
# 6.wait to see the results :)

import pandas as pd


indir = '<enter the pathfile of your csv file>'
colname = '<enter the column you wish to convert>'
outdir = '<enter your preferred output directory>'

def csv2txt(indir, colname, outdir):
    """break a csv column into multiple txt files"""

    with open(indir, encoding="utf8", errors='ignore') as f:
        df = pd.read_csv(f)
        # loop through all reviews
        for i in range(len(df)):
            # single out review body
            txtbody = df.body[i]

            # write to txt file
            # edit 'txtname' below if you prefer custom filenames
            txtname = outdir  + "text" + str(i+1) + ".txt"
            f = open(txtname,"w")
            f.write(txtbody)

            f.close()
