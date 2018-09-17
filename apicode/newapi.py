import requests
import inquirer
import textwrap
import os
from inquirer.themes import GreenPassion


class NewsApi:
    # function for picking the news source from the user
    def get_user_source(self):
        questions = [
            inquirer.List('sources',
                          message="From which news source would you like to acquire your headlines?",
                          choices=['nbc-news', 'cnbc',
                                   'bbc-news', 'cnn'],
                          ),


        ]
        # theme adds a green background to the items in the list
        answers = inquirer.prompt(questions, theme=GreenPassion())
        print(answers['sources'])

        return answers['sources']
    # function to retrieve a product key for the environment variable

    def add_api_key(self):
        if('API_KEY' in os.environ) == False:
            raise ValueError(
                "Access Denied ..., you dont have a product key in your environment variables")
        return os.environ.get('API_KEY')

    # function for collecting data for from the API

    def fetch_data(self, newssource):

        api_key = self.add_api_key()

        url = 'https://newsapi.org/v2/top-headlines?sources='+newssource + \
            '&apiKey='+api_key+'&pageSize=10'
        return requests.get(url)
    # function for checking whether the api call was successfull

    def check_status_code(self):
        api_response = self.fetch_data(self.get_user_source())
        print("Status code:", api_response.status_code)
        if api_response.status_code == 200:
            print("your query was successful, wait will we retrieve your data, thank you")

        return api_response.status_code
    # function for storing the response for manipulation

    def store_api_response(self):
        api_response = self.fetch_data(self.get_user_source())
        response_data = api_response.json()
        headlineArticles = response_data['articles']

        return headlineArticles

    def sort_and_display_results(self):
        content = self.store_api_response()
        article_count = 1
        print('articles length', len(content))
        print("\t", '{:=^100}'.format('.'))
        print("\t", '{: ^100}'.format('Top 10 Headlines from '))
        print("\t", '{:=^100}'.format('.'))
        for article in content:
            print("\t", '{:_^100}'.format(article_count))
            print("\t", "TITLE : ", "\t", article['title'])
            print("\t", "DESCRIPTION: ",  "\t", textwrap.fill(
                article['description'], width=100))

            print("\t", "URL : ",  "\t", textwrap.fill(
                article['url'], width=100))
            article_count += 1
        return len(content)
