# Mission_to_Mars

## Analysis: The purpose of this project is to display images of Mars’s hemispheres on your own site and are the website user friendly. The webpage needs all 4 images of Hemispheres. In order to do that, we need BeautifulSoup and Splinter to scrape full-resolution images of Mars’s hemispheres and the titles of those images, store the scraped data on a Mongo database, use a web application to display the data, and alter the design of the web app to accommodate these images.

## Results: Provide a bulleted list with three major points from the analysis deliverables. Use images as support where needed.



### Deliverable 1 : Scrape High-Resolution Mars Hemisphere Images and Titles
Following steps have been performed to get High-Resolution Mars Hemisphere Images and Titles
- Used browser to visit the URL,
- Created a list to hold the images and titles.
- Retrieved the image urls and titles for each hemisphere.
- Printed the list that holds the dictionary of each image url and title.
- The output which shows mage url and title is as follows-


### Deliverable 2 : Update the Web App with Mars Hemisphere Images and Titles
- created a new dictionary in the data dictionary to hold a list of dictionaries with the URL string and title of each hemisphere image i.e.hemisphere_image_urls
- create a function that will scrape the hemisphere data i.e. def hemispheres(browser) which returns the scraped data as a list of dictionaries with the URL string and title of each hemisphere image.
- Output shows full-resolution images and the titles of the four hemisphere images, like the image below- 


### Deliverable 3 : Add Bootstrap 3 Components
- The web page is mobiles responsive.
- Bootstrap 3 components:
	1) Styling the "Scrape New Data" button - added "btn-block" which span the full width of a parent
	2) Added "btn-lg" which creates fancy larger button. 
	
	3) Customized the facts table - added "table-hover" o enable a hover state on table rows
	4) added "table-responsive" make them scroll horizontally on small devices

	5) Added the hemisphere images as thumbnails, like the image below-
	6) Made changes in code so that we can see the webpage in smaller/medium/larger devices-

## Summary:
This project shows results which are, Scraping High-Resolution Mars Hemisphere Images and Titles and Updating the Web App with Mars Hemisphere Images and Titles and also, we have a freedom to to use CSS stylesheets to make our webpage look pretty.

