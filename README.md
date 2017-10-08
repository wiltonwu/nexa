![alt text](https://raw.githubusercontent.com/wiltonwu/nexa/master/nexa.png)

# nexa
An Alexa skill for stock market information

## About
Nexa is an Amazon Alexa skill for stock market infromation and personalized recommendations.  This repository contains all the source code for the nexa skill that can be run on your Alexa-enabled devices.

You can use Nexa to ask about stock information and personalized recommendations by using phrase such as...

#### Stock close, intraday high, and intraday low prices

* "Alexa, ask NASDAQ what is the price of Apple?"
* "Alexa, ask NASDAQ for Netflix stock price."
* "Alexa, ask NASDAQ what is the low price of Snapchat?"
* "Alexa, ask NASDAQ what is the high of Nvidia?"

#### Portfolio summaries
* "Alexa, ask NASDAQ for my portfolio update."
* "Alexa, aks NASDAW to give me a portfolio update."

#### Personalized recommendations
* "Alexa, ask NASDAQ for some recommended stocks."

## Development
Nexa is written in python 2.7 and hosted on Amazon Web Services. Nexa primarily uses the [NASDAQ API](https://github.com/nasdaq/hack). It also utilizes tensorflow to create the personalized stock recommendations with machine learning.

## Creators
Nexa was developed by Wilton Wu, Justin Lu, Lawrence Jiang, and Ingrid Wu from the University of California, Berkeley for [Cal Hacks 4.0](https://calhacks.io/)
