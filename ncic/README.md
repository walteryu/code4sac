# 2019 NSF Civic Innovation Challenge - Web Application

## Code for Sacramento - Contest Entry

### Problem Statement

Resilience: Communities are at a high risk from flooding and erosion. How can we use data and technology tools, like sensing and mapping, to help protect our communities?

### Introduction

The Civic Innovation Challenge aims to leverage social science, data, and technology to address complex community challenges, enhance job growth and economic competitiveness, and address equity in our communities.

### Planning Documents

1. [Outline Presentation](https://drive.google.com/open?id=1iYygMCW_3ObGEFmXPtv7GQbgXOOSSOVZo7EJr0g58PQ)
2. [Links and Resources](https://drive.google.com/open?id=1qJcdZpiONlpN7lYasD9VFbptphpdHHspmR13mkkPpfc)

### Software and Tools

Software used for this project are as follows:

1. [ESRI Open Data GIS Portal](https://hub.arcgis.com/pages/open-data)
2. [Google Earth Pro](https://www.google.com/earth/versions/)
3. [Node.js](https://nodejs.org/en/)
4. [Express.js](https://expressjs.com/)
5. [NPM Package Manager](https://www.npmjs.com/)
6. [QGIS](https://qgis.org/en/site/forusers/download.html)

## Installation

Clone Github repository, then run locally as follows:

1. GIS Data Layers - Open Shapefiles with QGIS (open-source)
2. Google Earth and KML Data Layers - Open with Google Earth Desktop
3. Node.js Web Application - Install dependences and run on local server
4. Node.js Deployment - Heroku instructions listed below for reference

## Node.js Web Application

Node.js web app using the ESRI JS API and as listed below; it visualizes various GIS layers for additional analysis.

1. [Visit Web Application](https://ncic.herokuapp.com/)
2. Shows ESRI AGOL major US cities and freeway layers
3. Developed using Node.js and Express web frameworks
4. ESRI and Heroku templates used as referenced below

Details about the map and feature layers:

1. [ACOE/AGOL Portal](https://geoplatform-usace.opendata.arcgis.com/)
2. [Sacramento Open Data GIS Portal](https://data-sacramentocounty.opendata.arcgis.com/)
3. [Sacramento Watershed Program GIS Portal](https://data.sacriver.org/)

## References:

Web app was developed using these templates/tutorials:

1. [ESRI/JS API: 2D Map Template](http://arcg.is/2nytHZt)
2. [ESRI JS API: Layer Template](http://arcg.is/2nyNuIe)
3. [ESRI AGOL: US Major Cities Layer](http://arcg.is/2nyyvht)
4. [Heroku Node.js Tutorial](http://bit.ly/2nyFTJN)

# Heroku Node.js Tutorial Instructions

A barebones Node.js app using [Express.js](http://expressjs.com/).

This application supports the [Getting Started with Node on Heroku](https://devcenter.heroku.com/articles/getting-started-with-nodejs) article - check it out.

## Running Locally

Make sure you have [Node.js](http://nodejs.org/) and the [Heroku Toolbelt](https://toolbelt.heroku.com/) installed.

```sh
$ git clone git@github.com:heroku/node-js-getting-started.git # or clone your own fork
$ cd node-js-getting-started
$ npm install
$ npm start
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```
$ heroku create
$ git push heroku master
$ heroku open
```
or

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Heroku Documentation

For more information about using Node.js on Heroku, see these Dev Center articles:

- [Getting Started with Node.js on Heroku](https://devcenter.heroku.com/articles/getting-started-with-nodejs)
- [Heroku Node.js Support](https://devcenter.heroku.com/articles/nodejs-support)
- [Node.js on Heroku](https://devcenter.heroku.com/categories/nodejs)
- [Best Practices for Node.js Development](https://devcenter.heroku.com/articles/node-best-practices)
- [Using WebSockets on Heroku with Node.js](https://devcenter.heroku.com/articles/node-websockets)
