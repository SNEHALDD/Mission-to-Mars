
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt


def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    
    news_title, news_paragraph = mars_news(browser)
    hemisphere_image_urls = hemispheres(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemispheres": hemisphere_image_urls
    }

    # Stop webdriver and return data
    browser.quit()
    print (data)
    return data


def mars_news(browser):

    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)


    # set up the HTML parser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')

        slide_elem.find('div', class_='content_title')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()
        
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    except AttributeError:
        return None, None

    return news_title, news_p


def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)


    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()


    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

     # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
        img_url_rel

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    img_url

    return img_url

# Mars facts
# scrape the entire table with Pandas' .read_html() function Instead of scraping each row, or the data in each <td />
def mars_facts():
    try:
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)

    #  Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped table-hover table-responsive")

if __name__ == "__main__":

      # If running as script, print scraped data
    print(scrape_all())


def hemispheres(browser):
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    html = browser.html
    mars_soup = soup(html, 'html.parser')
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    images_div = mars_soup.find_all('div', class_='description')
    images=[]
    for i in images_div:
        images.append(i.find('a'))
    print(images)

    for img in images:
        img_url = img.get('href')
        img_url = url+img_url
        img_url
        browser.visit(img_url)
        html = browser.html
        marsDownload_soup = soup(html, 'html.parser')
        images_d = marsDownload_soup.find('div', class_="downloads")
        images_h = marsDownload_soup.find('h2', class_="title").text
        #print(images_h)
        images_d_anchor = images_d.find_all('a')[0]
        images_href = images_d_anchor.get('href')
            #print(images_href)
        images_href_url = url+ images_href
        #print(images_href_url)
        hemispheres = {}
        hemispheres['img_url'] = images_href_url
        hemispheres['title'] = images_h
        hemisphere_image_urls.append(hemispheres)

    return hemisphere_image_urls 

