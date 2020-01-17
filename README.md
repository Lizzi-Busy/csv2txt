# csv2txt

python program to break csv column into multiple txt files (a byproduct of my nlp project)

## Inspiration

Well, this all started off with my complaint:

> It's 2020 and those NLP tools still do not support csv!

Imagine that you had scraped a whole bunch of texts into a single csv file, you were happy and you'd never been more ready for corpus analysis. Then you opened `AntConc` and realized the software could only take txt sources. That discovery ruined your day...

There are a number of csv-txt converters available online. But most of them either:
* throw the entire csv file into one single txt file, or
* allow you to break each row into a single txt, which contains all the metadata/extra stuff you've entered in the same row, whether you like it or not.

