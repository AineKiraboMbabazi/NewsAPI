[![Build Status](https://travis-ci.org/AineKiraboMbabazi/NewsAPI.svg?branch=NewsAPI)](https://travis-ci.org/AineKiraboMbabazi/NewsAPI)
[![Coverage Status](https://coveralls.io/repos/github/AineKiraboMbabazi/NewsAPI/badge.svg?branch=master)](https://coveralls.io/github/AineKiraboMbabazi/NewsAPI?branch=master)
# NewsAPI
User is offered a list of four news sources. User should be able to make a choice of a preferred news source. User gets back a list of the top 10 headlines from the preferred source. A news headline should have a title, description and a url in case the user needs to follow up on the news story.

# Installation and settup
## Clone the repository ##
```
$ git clone (https://github.com/AineKiraboMbabazi/NewsAPI.git
$ cd NewsAPI
```
## Installing virtualenv ##

If you do not have virtualenv installed. Use the command below to install it
```
pip install virtualenv
```
Create a virtual environment using virtualenv

For mac os, linux and windows users
```
$ virtualenv venv
```
Install the project dependancies
```
pip install -r requirements.txt
```
## Activating the virtual environment and setting environment variables ##
For windows users, you can activate the virtual environment by following the steps below
    
If you are using windows command prompt
```
cd venv/scripts && activate && cd ../..
```
if you are using git bash
```
source venv/scripts/activate
```
if you are using linux
```
source venv/bin/activate
```
After activating the virtual environment*
- Go to [Newsapi](https://newsapi.org/account)
- Get an api key 
- set the api key into your environment variables as follows

If you are using Linux
```
export API_KEY='The Api-key for the newsapi'
```

## Running the application locally ##
Make sure that you are in the newapi root folder.
To run the file in linux use
```
python newapi.py
```
To run the tests in linux
```
python -m unittest
```
