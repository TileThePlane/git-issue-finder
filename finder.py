import requests
import bs4
import argparse

# search language "l=python"
# search page "&p=#"
# search issue "&type=Issues"
# starts query "&q="
    # query label 'label%3A"good+first+issue"'
    # query archived "archived%3Afalse
    # query users "user%3Anasa+user%3Adefense-cyber-crime-center+user%3Agsa"
    # query open status "is%3Aopen"



if __name__ == "__main__":
    print("Github Issue Search: helping you find relevant issues on github.")
    print("For a complete list of arguments try: gif help")


issue_request_url = ('https://github.com/search?'
                     'l=Python'
                     '&p=1'
                     '&type=Issues'
                     '&q={}')
print(issue_request_url)
issue_html = requests.get(issue_request_url).text
print(issue_html)