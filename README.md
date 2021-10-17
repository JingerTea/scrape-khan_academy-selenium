# scrape-khan_academy-selenium

## Introduction

`scrape_khan_academy` is a python package to scrape all the questions from public Khan Academy, turn the data into .docx file. You can scrape any subject with this package.

Warning: This open source project is intended for academy research only. If you are using it for any commericial purposes, please refer to Khan Academy anti-scraping policies, they may blacklist ips making unauthenticated or unusual requests.

## Required Packages

```python
# Selenium
pip install selenium

# Webdriver-manager
pip install webdriver-manager

# Python-docx
pip install python-docx
```

## Example Usage 1

```python
from scrape_khana_academy.scraper import scraper

scraper("https://www.khanacademy.org/math/7th-engage-ny")
```

## Example Usage 2

```python
links = [
	"https://www.khanacademy.org/math/3rd-engage-ny",
	"https://www.khanacademy.org/math/4th-engage-ny",
	"https://www.khanacademy.org/math/5th-engage-ny",
]

for link in links:
	scraper(link)
```

## Example Export Directory Tree Structure

```
exports/
├── 7th_grade_Eureka_Math_EngageNY_/
│   └── 1_Module_1_Ratios_and_proportional_relationships/
│       ├── 1_Identify_proportional_relationships.docx
│       ├── 2_Proportional_relationships.docx
│       └── 3_Unit_rates.docx
└── temp/
    ├── Question1.png
    ├── Question2.png
    ├── Question3.png
    └── Question4.png
```
