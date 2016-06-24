from py_bing_search import PyBingWebSearch
import urllib
from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup
import copy


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
            self.scraped_html.append(urllib.urlopen(url).read())

    def get_paragraphs(self):
        """
        Take scraped HTML from earlier and return a list of paragraph strings.

        Returns:
            list[str]: List of strings of paragraph content.
        """
        result = []
        for webpage in self.scraped_html:
            soup = BeautifulSoup(webpage)
            paragraphs = soup.findAll('p')
            for par in paragraphs:
                if par.string is not None:
                    stripped_par = str(par.string)
                    result.append(stripped_par)
        return result

    def get_words(self, paragraphs):
        """
        Take list of paragraphs, get individual words and filter out non-ASCII text.

        Args:
            paragraphs (list[str]): List of paragraph strings.

        Returns:
            list[str]: List of lower-case words from paragraphs.
        """
        words = []
        for par in paragraphs:
            new_words = par.split(" ")
            filtered_words = [w.lower() for w in new_words if w.isalpha()]
            words.extend(filtered_words)
        print words
        return words
