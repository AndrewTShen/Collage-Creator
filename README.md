# Keyword Collage Creator

Collage Creator is an app that help you create a mosaic with images of your favorite things whether it be animals, hobbies, activities, anything that can be described in a picture! It is perfect for making a specialized gift for a loved one or can be used to make a powerful message using double meaning and juxtaposition. This project was built for Blueprint 2019.

## How It Works
Collage Creator works by allowing the user to input select keywords to query Pexel.com, a website for free stockphotos. The photos are then made into a mosaic that resembles a select input image.

## Requirements
- Python 2.7.13

### Python Packages
- Kivy 1.10.1
- Scrapy 1.6.0

## Instructions
1. Download the repository through `git clone git@github.com:AndrewTShen/Keyword-Collage-Creator.git` or by downloading the repository as a zip file.

2. Place the initial image to be collaged in the directory (`Keyword-Collage-Creator/imagescraper`) and rename it `image.jpg`. The image should be at `Keyword-Collage-Creator/image.jpg`.

3. Run the frontend app using `python frontend.py`. This should prompt a kivy app to open. Through this app, insert each keyword to be scraped into the box and click `Ok` after each keyword. Once satisfied with the keywords chosen, click `Submit` to create the mosaic.

## Samples

<img src="https://github.com/AndrewTShen/Keyword-Collage-Creator/blob/master/imagescraper/sample_original.jpg" alt="sample_original" width="500"/>
<img src="https://github.com/AndrewTShen/Keyword-Collage-Creator/blob/master/imagescraper/sample_mosaic.jpeg" alt="sample_mosaic" width="500"/>



## Acknowledgements
- Srinivasan Sathiamurthy for inspiring and helping to build this project.  
- Rob Dawson for writing `mosaic.py`, the main driver of the mosaic portion of the project. You can find the code for `mosiac.py` at this [respository](https://github.com/codebox/mosaic)
- Blueprint Mentors for helping to debug bits and pieces of code.  

