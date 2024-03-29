[![Netlify Status](https://api.netlify.com/api/v1/badges/36ba5654-56c5-47c8-91fc-ad07609975e6/deploy-status)](https://app.netlify.com/sites/evangelium/deploys)
# Evangelium API - Daily Gospel at your fingertips
Read-Only API to get the daily gospel in 7 different languages, [Check Repo](https://github.com/manasv/api-evangelium).

## Deployment
The deployment of the API is on [Netlify](https://www.netlify.com/)  and the build file is `builder.py`.

## Endpoints
The endpoints return data in json format:

- Readings per day : `https://evangelium.manuelsanchez.me/api/:language/days/:date`

Example :
- https://evangelium.manuelsanchez.me/api/es/days/2019-06-10
```json
{
    "0": {"title": "Example Title 1", "text": "Example Reading 1"}, 
    "1": {"title": "Example Title 2", "text": "Example Reading 2"}, 
    "2": {"title": "Example Title 3", "text": "Example Reading 3"}
}   
```

## Supported Languages

*   [es] Spanish 
*   [en] English 
*   [it] Italian 
*   [fr] French  
*   [pt] Portuguese 
*   [kr] Korean  
*   [de] German  


## Features WIP

As for now the API only gives the readings for the current day, and the next 6 days, woring to mantain history of the readings through time.

## Credits

For the guide and idea to host read only api on netlify: [@AntoineAugusti](https://github.com/AntoineAugusti)

## Licence
MIT
