# Thoughtful Robot

This is a scrapper that get data from New York Times(www.nytimes.com) and save the images and text in the folder output.

## Setting up the environment:

 - Make sure you have python 3.9 or higher installed

 - Make sure you have the chromedriver installed and matching your chrome version

Create the environment
```
python3 -m venv venv
```
Activate the environment:
```
source venv/bin/activate
```
Install de dependencies:
```
pip install -r requirements.txt
```
## Defining the attributtes to run the scrapper
Create a .env file based on env.example, and set the search variables :
    - SEARCH_TEXT
    - SECTION (available options:Arts/Books/Business/Movies/New York/Opinion/Sports/Style/Travel/U.S./World)
    - NUMBER_OF_MONTHS

## Start the scrapper
Run tasks.py
