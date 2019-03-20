# Scrapi
A simple web scrapper which is based on web api.
what you have to do just a post request with the url and the attrbute you want and you are good to go.

## Prerequisites
```
pip install flask_restful flask urllib bs4 
```
## How to send request
Send a post request lke-
```
{
"url":"https://github.com/",
"attribute":"p"
}
```

attribue defines the html attribute which is going to be scrapped from the requested url.

## Run
```
python minutes_scrap.py 
```
and the api is hosted.
