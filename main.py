from __future__ import print_function

from handlers import *


def lambda_handler(event, context):
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

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
    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    return get_welcome_response()


def on_intent(intent_request, session):
    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    if intent_name == "StockPriceIntent":
        return get_stock_price_in_session(intent, session)
    elif intent_name == "StockHighIntent":
        return get_stock_high_in_session(intent, session)
    elif intent_name == "StockLowIntent":
        return get_stock_low_in_session(intent, session)
    elif intent_name == "PortfolioUpdateIntent":
        return get_portfolio_update(intent, session)
    elif intent_name == "StockRecommendationIntent":
        return get_stock_recommendation_in_session(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.StopIntent":
        return get_end_response()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])