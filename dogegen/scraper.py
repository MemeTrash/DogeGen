from py_bing_search import PyBingWebSearch


class Scraper(object):
    """
    Web scraper that finds search results for a string; uses Bing for searching.
    Takes these results and returns a list of ASCII words from each one's <p> segments.
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.search_results = []
        self.scraped_html = []

    def get_words_for(self, inp_str):
        """
        Scrape words from search results for an input string.

        Args:
            inp_str: String to search for.

        Returns:
            list[str]: List of words in <p>'s of scraped webpages.
        """
        self.search_for(inp_str)
        self.get_html_from_results()
        return self.get_words(self.get_paragraphs())

    def search_for(self, inp_str, num_results=10):
        """
        Search for a string on Bing, store results in self.

        Args:
            inp_str: String to search for.
            num_results: Number of results to use from search.
        """
        web_search = PyBingWebSearch(self.api_key, inp_str, web_only=False)
        self.search_results = web_search.search(limit=num_results, format='json')

    def get_html_from_results(self):
        """
        Get strings of HTML from all search results, store in self.
        """
        for result in self.search_results:
            url = result.url
            # TODO: get HTML from url
            print url

    def get_paragraphs(self):
        pass

    def get_words(self, paragraphs):
        pass
