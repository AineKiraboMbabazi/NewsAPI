import unittest

from apicode.newapi import NewsApi


class NewsApiTest(unittest.TestCase):
    def setUp(self):
        self.headline_request = NewsApi()

    def test_user_has_selected_news_source(self):
        self.assertIn(self.headline_request.get_user_source(), ('nbc-news', 'cnbc',
                                                                'bbc-news', 'cnn'))

    def test_number_of_returned_headlines_is_less_or_equal_to_10(self):
        self.assertLessEqual(
            self.headline_request.sort_and_display_results(), 10)

    def test_Api_key_was_successfully_collected(self):
        self.assertEqual(self.headline_request.add_api_key(),
                         'c4cddefacee34761b2312384fcefb0be')

    def test_data_gets_retrived_from_the_newsapi(self):
        self.assertEqual(self.headline_request.check_status_code(), 200)


if __name__ == '__main__':
    unittest.main()
