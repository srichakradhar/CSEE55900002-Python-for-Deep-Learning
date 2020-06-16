"""
CSEE 5590 0002 Python for Deep Learning
ICP 3
author: Srichakradhar Reddy
student ID: 16298670
email: snp8b@umsystem.edu

Write a simple program that parse a Wiki page mentioned below
and follow the instructions: https://en.wikipedia.org/wiki/Deep_learning
* Print out the title of the page
* Find all the links in the page (‘a’ tag)
* Iterate over each tag(above) then return the link using attribute "href" using get
* Save all the links in the file
"""

from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException
from contextlib import closing


class WebPageReader:
    """
    safe wrapper for gracefully reading web pages.
    """

    def read_web_content(self, web_url):
        try:
            with closing(get(web_url, stream=True)) as response:
                if (self.validate_response(response)):
                    return response.content
                else:
                    return None

        except RequestException as requestException:
            print(
                "Exception raised while consuming {0} - {1}".format(web_url, str(requestException)))
            return None

    def validate_response(self, response):
        html_type = response.headers['Content-Type']
        return (response.status_code == 200
                and html_type is not None
                and html_type.lower().find('html') > -1)


def main():
    # Initialize the web page reader
    webPageReader = WebPageReader()

    # load the content from the web page
    raw_html = webPageReader.read_web_content(
        "https://en.wikipedia.org/wiki/Deep_learning")

    # initialize the HTML parser
    soup = BeautifulSoup(raw_html, 'html.parser')

    print("Title of the page: {0}".format(soup.title.string))

    # Initialize variables to store links
    number_of_links = 0
    links = []

    # collect links from 'a' tags' href attribute
    for link in soup.find_all('a'):
        number_of_links += 1
        links.append(link.get('href'))

    print("Number of links in the page are {0}".format(number_of_links))

    # save all links to a text file
    with open('links.txt', 'w') as f:
        f.writelines("%s\n" % link for link in links)


if __name__ == "__main__":
    main()
