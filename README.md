# csv2txt

python script to break csv into multiple txt files (a byproduct of my nlp project)

## Inspiration & Description

Well, this all started off with my complaint:

> It's 2020 and those NLP tools still do not support csv! (｡•ˇ‸ˇ•｡)

Imagine that you had scraped a whole bunch of texts into a single csv file, you were happy and you'd never been more ready for corpus analysis. Then you opened `AntConc` and realized the software could only take txt sources. That discovery ruined your day...

<p align="center">
  <img src=/image/facepalm2.jpg align='center' width=300/>
</p>

There are a number of csv-txt converters available online. But most of them either:
* throw the entire csv file into one single txt, or
* allow you to break each row into a single txt, which contains all the metadata/extra stuff you've entered in the same row, whether you like it or not.

After a few trials of the existing tools I decided to create a converter on my own. Currently the program `csv2txt.py` has the following functionality:

* find a csv file from your local directory,
* pick a specific column of your choice,
* convert the content of each cell to a single txt, and
* output the txts to a directory of your choice
* (more to come in the next release...)

## Demo

before: a messy csv file with texts in column I (shaded below) and metadata in columns A-H

<p align="center">
  <img src=/image/screenshot01.jpg width=80%/>
</p>

after: each cell converted to a single txt file, which can be processed / analyzed by AntConc!

<p align="center">
  <img src=/image/screenshot02.jpg width=70%/>
</p>

## Some ideas for later versions

* create a user interface
* allow custom txt names based on metadata
