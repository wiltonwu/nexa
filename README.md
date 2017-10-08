![alt text](https://raw.githubusercontent.com/wiltonwu/nexa/master/nexa.png)

An Alexa skill for stock market information

## About
Nexa is an Amazon Alexa skill for stock market information and personalized recommendations.  This repository contains all the source code for the Nexa skill that can be run on your Alexa-enabled devices.

You can use Nexa to ask about stock information and personalized recommendations by using phrase such as...

#### Stock close, intraday high, and intraday low prices

* "Alexa, ask NASDAQ what is the price of Apple?"
* "Alexa, ask NASDAQ for Netflix stock price."
* "Alexa, ask NASDAQ what is the low price of Snapchat?"
* "Alexa, ask NASDAQ what is the high of Nvidia?"

#### Portfolio summaries
* "Alexa, ask NASDAQ for my portfolio update."
* "Alexa, ask NASDAQ to give me a portfolio update."

#### Personalized recommendations
* "Alexa, ask NASDAQ for some recommended stocks."

## Development
Nexa is written in Python2.7 and hosted on **Amazon Web Services**. Nexa primarily uses the [NASDAQ API](https://github.com/nasdaq/hack) for stock information retrieval. It integrates this data with **AWS Lambda** in order to provide a simplified, comprehensive user experience. Nexa also utilizes **Tensorflow** to implement latent factor analysis through SVD models to create personalized stock recommendations based off user portfolios.

## Acknowledgements
* [Amazon skills developer tutorial](https://developer.amazon.com/alexa-skills-kit/alexa-skill-quick-start-tutorial)
* [Research paper on collaborating filtering models by Yehuda Koren](http://www.cs.rochester.edu/twiki/pub/Main/HarpSeminar/Factorization_Meets_the_Neighborhood-_a_Multifaceted_Collaborative_Filtering_Model.pdf)
* [Machine learning algorithm template code by felipessalvatore](https://github.com/felipessalvatore/Recommender)
* [Movie recommendations with deep learning](https://medium.com/deep-systems/movix-ai-movie-recommendations-using-deep-learning-5903d6a31607)

## Creators
Nexa was developed by Wilton Wu, Justin Lu, Lawrence Jiang, and Ingrid Wu from the University of California, Berkeley for [Cal Hacks 4.0](https://calhacks.io/)
