import requests
from bs4 import BeautifulSoup
import json
import argparse
from pathlib import Path 

def fetch_url(url, output):
    fpath = Path(f"{output}")
    if not fpath.exists():
        headers = {'User-Agent':'Safari/537.36'}
        response = requests.get(url, headers=headers)
        with open(fpath, 'w') as file:
            file.write(response.text)
    with open(fpath) as f:
        return f.read()

def parse_articles(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Select all <li> elements with the 'data-carousel-item' attribute
    list_items = soup.find_all('ol', class_= 'list-widget__content list-unstyled')
    articles = list_items[0].find_all('li')
    trending_articles = []
    
    for i, article in enumerate(articles):
        if i < 5:  # Assuming you want to scrape only the first 5 articles
            if article:
                a_tag = article.find('a', class_='article-card__image-link')
                if a_tag:
                    title = a_tag.get('aria-label', 'No title')
                    url = a_tag.get('href', 'No URL')
                    excerpt = a_tag.find('p', class_='article-card__excerpt').text if a_tag.find('p', class_='article-card__excerpt') else 'No excerpt'

                    trending_articles.append({
                        'title': title,
                        'url': url,
                        'excerpt': excerpt
                    })
    
    return trending_articles
       

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Scrape trending articles from the Montreal Gazette website.')
    parser.add_argument('-o', '--output', required=True, help='Output file name for the scraped data.')
    args = parser.parse_args()

    # URL of the page to scrape
    url = 'https://montrealgazette.com/'
    

    html_content = fetch_url(url, output=args.output)
    articles = parse_articles(html_content)

    # Write the result to the output file
    with open(args.output, 'w') as file:
        json.dump(articles, file, indent=4)

    print(f'Trending articles have been written to {args.output}')

if __name__ == '__main__':
    main()
