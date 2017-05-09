## scrapnifty  (https://scrapnifty.herokuapp.com/): 

stand-alone web app using CherryPy to scrape the 'Nifty 50' table values every 5 minutes

(https://scrapnifty.herokuapp.com/): 

1) Build a stand-alone web app using CherryPy.


2) Scrape the 'Nifty 50' table values (http://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G) every 5 minutes (in the background and on a different thread) and persist in a Redis instance.

3) On the webapp, display the values stored in Redis in a cards layout (unlike the original table). Use valid HTML5 + CSS3 to make the view look nice (eg: http://www.sketchappsources.com/resources/source-image/messages-cards-rahulbhadauria.png)

4) Commit the code to a Github repo, host the app on a free Heroku or AWS instance and submit the details.



### Status:

Basic functionality completed

* scrap every 5 minutes
* minimal UI
* deployed on Heroku



#### pending :

* Unwanted two cards in the last row
* More deatils in card
* Insted of json fetching use selenium to scrap (selenium need some fixing on my computer. some geckodriver issues)
* Update UI


 