
# Web scraping Project from Tawhid Vai

This sript will scrape over 1.3 million data from artvee.com website




## Documentation

Create a new folder on your computer and open with vs code editor.

Now follow each step carefully.

Open terminal and create virtual environment with following command.


## Installation

#### create a virtual environment 

```bash
  python -m venv env
```
#### Active virtual environment 

```bash
  env\Scripts\activate
```
#### install scrapy library

```bash
  pip install scrapy
```
#### create a scrapy project

```bash
  scrapy startproject artvee .
```

#### create a scrapy spider

```bash
  scrapy genspider art_vee x
```

## Modifications

go to artvee/spiders directory and you'll find a file called art_vee.py.
replace the art_vee.py file with my given art_vee.py file

### method 1

Delete all the code in art_vee.py file and paste all code from my given art_vee.py file

### method 2
Delete that art_vee.py file and add my given art_vee.py file at the same place

## Now time to run that code on terminal

```bash
  scrapy crawl art_vee -o anyname.csv
```
### start scrapping 

