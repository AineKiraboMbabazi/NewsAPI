import requests
import inquirer
import os
import texttable as tt
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
        print("News Source : ", answers['sources'])

        return answers['sources']
    # function to retrieve a product key for the environment variable

    def get_api_key(self):
        os.environ.get('API_KEY')
        if 'API_KEY' not in os.environ:
            raise ValueError(
                "Access Denied ..., you dont have a key in your environment variables, add api-key to your environment variables")
        return os.environ.get('API_KEY')

    # function for collecting data for from the API

    def fetch_data(self, newssource):

        api_key = self.get_api_key()

        url = 'https://newsapi.org/v2/top-headlines?sources='+newssource + \
            '&apiKey='+api_key+'&pageSize=10'

        return (requests.get(url))
    # function for checking whether the api call was successfull

    def check_status_code(self):
        api_response = self.fetch_data(self.get_user_source())
        print("Status code:", api_response.status_code)
        if api_response.status_code == 200:
            print("your query was successful, wait will we retrieve your data, thank you")

        return api_response.status_code
    # function for storing the response for manipulation

    def store_api_response(self):
        selectedSource = self.get_user_source()
        api_response = (self.fetch_data(selectedSource)).json()

        headlineArticles = api_response['articles']

        return headlineArticles, selectedSource

    def display_results(self):

        content = self.store_api_response()
        article_count = 1
        source_selected = str(content[1])
        modifier = "="*110
        numberofitems = str(len(content[0]))
        title = "TOP 10 HEADLINES FROM : "
        #creating the header for the display table.
        print('%s %s \n %s \n \t\t\t %s %s \n %s' % ('Headlines retrieved : ',
                                                     numberofitems, modifier, title, source_selected, modifier))
        #creating and styling the table
        tab = tt.Texttable()
        tab.set_cols_width([20, 85])
        tab.set_cols_align(["l", "l"])
        for article in content[0]:
            #populating the display table
            row = ["Headline Count ", article_count]
            tab.add_row(row)
            row = ["TITLE : ",  article['title']]
            tab.add_row(row)
            row = ["DESCRIPTION: ",  article['description']]
            tab.add_row(row)
            row = ["URL: ",  article['url']]
            tab.add_row(row)
            row = ["",  ""]
            tab.add_row(row)
            article_count += 1

        s = tab.draw()
        print(s)
        return len(content)


if __name__ == '__main__':
    test = NewsApi()
    test.display_results()
