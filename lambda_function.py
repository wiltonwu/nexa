"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""
from company_tickers import COMPANY_TICKERS

import websocket
import threading
import time


def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run():
        ws.send("")
        time.sleep(1)
        ws.close()
    threading.Thread(target=run).start()

def get_stock_dict(ticker):

    websocket.enableTrace(True)

    url = 'ws://34.214.11.52/stream?symbol={}&start={}&end={}'.format(ticker, '20170717', '20170717')

    # Create new socket and connect to url to hit API
    ws = websocket.WebSocket()
    ws.connect(url)

    # send information and store response
    ws.send("")
    stock_info = ws.recv()

    stock_dict = eval(stock_info)

    return stock_dict

def get_close_price():
    return get_stock_dict()["Close"]


from __future__ import print_function


def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "StockPriceIntent":
        return get_stock_price_in_session(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

# --------------- Functions that control the skill's behavior ------------------


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Nasdaq Stock Skill. " \
                    "Please ask for a stock price by saying, " \
                    "what is the stock price of Nasdaq"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please ask for a stock price by saying, " \
                    "what is the stock price of Nasdaq"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_stock_price_in_session(intent, session):
    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'Company' in intent['slots']:
        company = intent['slots']['Company']['value']
        if company.upper() in COMPANY_TICKERS:
            stock_price = get_stock_dict(COMPANY_TICKERS[company])
            speech_output = "The stock price of " + company + " is " + stock_price + " dollars."
            reprompt_text = "Please ask for a stock price by saying, " \
                            "what is the stock price of Nasdaq"
        else:
            speech_output = "I'm not sure what that company is. Please try again."
            reprompt_text = "Please ask for a stock price by saying, " \
                            "what is the stock price of Nasdaq"
    else:
        speech_output = "I'm not sure what that company is. Please try again."
        reprompt_text = "Please ask for a stock price by saying, " \
                        "what is the stock price of Nasdaq"

    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

# --------------- Helpers that build all of the responses ----------------------


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }