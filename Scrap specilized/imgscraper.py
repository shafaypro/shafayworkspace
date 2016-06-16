import image_scraper
import randomword
import os
path = 'E:\Python Workspace\Scrap specilized\Images'
image_scraper.scrape_images('https://imgur.com/',40,["jpg","png","gif","jpeg"],path,10000,False,False)