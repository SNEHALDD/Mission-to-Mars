# Mission-to-Mars

## Analysis: 
The purpose of this project is to display images of Mars’s hemispheres on your own site and are the website user friendly. The webpage needs all 4 images of Hemispheres. In order to do that, we need BeautifulSoup and Splinter to scrape full-resolution images of Mars’s hemispheres and the titles of those images, store the scraped data on a Mongo database, use a web application to display the data, and alter the design of the web app to accommodate these images.

## Results: Provide a bulleted list with three major points from the analysis deliverables. Use images as support where needed.

### Deliverable 1 : Scrape High-Resolution Mars Hemisphere Images and Titles
Following steps have been performed to get High-Resolution Mars Hemisphere Images and Titles
- Used browser to visit the URL,
- Created a list to hold the images and titles.
- Retrieved the image urls and titles for each hemisphere.
- Printed the list that holds the dictionary of each image url and title.
- The output which shows image url and title is as follows-
<img width="1153" alt="hemisphere_image_urls" src="https://user-images.githubusercontent.com/106944351/185242017-7e56bd80-5a78-4f70-8f26-59f0ecb9dadc.png">



### Deliverable 2 : Update the Web App with Mars Hemisphere Images and Titles
- created a new dictionary in the data dictionary to hold a list of dictionaries with the URL string and title of each hemisphere image i.e.hemisphere_image_urls
- create a function that will scrape the hemisphere data i.e. def hemispheres(browser) which returns the scraped data as a list of dictionaries with the URL string and title of each hemisphere image.
- Output shows full-resolution images and the titles of the four hemisphere images, like the image below- 
<img width="1645" alt="Screen Shot 2022-08-17 at 2 07 31 PM" src="https://user-images.githubusercontent.com/106944351/185242161-ca7fbb81-f2c9-4e93-9bfe-ddab624efe2f.png">

### Deliverable 3 : Add Bootstrap 3 Components
- The web page is mobiles responsive.
- Bootstrap 3 components:
	1) Styling the "Scrape New Data" button - added "btn-block" which span the full width of a parent
	2) Added "btn-lg" which creates fancy larger button. 
	<img width="1680" alt="button" src="https://user-images.githubusercontent.com/106944351/185242205-e61bfc05-9995-4a3a-bc84-95bfc45a5b56.png">

	
	3) Customized the facts table - added "table-hover" o enable a hover state on table rows
	4) added "table-responsive" make them scroll horizontally on small devices
	<img width="1671" alt="table-responsive-hover-striped" src="https://user-images.githubusercontent.com/106944351/185242244-b1010b4c-bd57-4710-8f13-c43cf5fd9235.png">


	5) Added the hemisphere images as thumbnails, like the image below-
	<img width="1667" alt="hemisphere_thumbnail" src="https://user-images.githubusercontent.com/106944351/185242319-351ab7a2-ca73-4d90-ab8d-862082a218d9.png">

	7) Made changes in code so that we can see the webpage in smaller/medium/larger devices-
	<img width="1673" alt="Bootstap-Mobile_ _Desktop" src="https://user-images.githubusercontent.com/106944351/185242474-bcb1852c-3836-4662-a2af-e9db9c75f077.png">


## Summary:
This project shows results which are, Scraping High-Resolution Mars Hemisphere Images and Titles and Updating the Web App with Mars Hemisphere Images and Titles and also, we have a freedom to to use CSS stylesheets to make our webpage look pretty.

