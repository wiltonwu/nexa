from builders import *
from mappings import name_to_ticker
from nasdaq import *

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


def get_end_response():
    card_title = 'Goodbye'
    session_attributes = {}
    reprompt_text = None

    speech_output = "Thank you for using the Nasdaq API!"
    should_end_session = True

    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

def get_stock_price_in_session(intent, session):
    card_title = intent['name']
    session_attributes = {}
    reprompt_text = None
    should_end_session = False

    if 'Company' in intent['slots']:
        company = intent['slots']['Company']['value']
        if company.upper() in name_to_ticker:
            stock_price = get_close_price(name_to_ticker[company.upper()])
            speech_output = "The stock price of " + company + " is " + str(stock_price) + " dollars."
        else:
            speech_output = "I'm not sure what that company is. Please try again."
    else:
        speech_output = "I'm not sure what that company is. Please try again."

    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def get_stock_high_in_session(intent, session):
    card_title = intent['name']
    session_attributes = {}
    reprompt_text = None
    should_end_session = False

    if 'Company' in intent['slots']:
        company = intent['slots']['Company']['value']
        if company.upper() in name_to_ticker:
            high_price = get_high_price(name_to_ticker[company.upper()])
            speech_output = "The high price of " + company + " is " + str(high_price) + " dollars."
        else:
            speech_output = "I'm not sure what that company is. Please try again."
    else:
        speech_output = "I'm not sure what that company is. Please try again."

    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def get_stock_low_in_session(intent, session):
    card_title = intent['name']
    session_attributes = {}
    reprompt_text = None
    should_end_session = False

    if 'Company' in intent['slots']:
        company = intent['slots']['Company']['value']
        if company.upper() in name_to_ticker:
            low_price = get_low_price(name_to_ticker[company.upper()])
            speech_output = "The low price of " + company + " is " + str(low_price) + " dollars."
        else:
            speech_output = "I'm not sure what that company is. Please try again."
    else:
        speech_output = "I'm not sure what that company is. Please try again."

    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def get_portfolio_update(intent, session):
    card_title = intent['name']
    session_attributes = {}
    reprompt_text = None
    should_end_session = False

    # Demo purposes using mock portfolio
    speech_output = 'Here is your portfolio. Nasdaq increased by 0.66 percentage points and closed at 71.49 dollars. ' \
                    'Microsoft increased by 0.73 percentage points and closed at 73.35 dollars. ' \
                    'Amazon increased by 0.5 percentage points and closed at 1010.04 dollars.'

    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def get_stock_recommendation_in_session(intent, session):
    card_title = intent['name']
    session_attributes = {}
    reprompt_text = None
    should_end_session = False

    # Demo purposes using mock portfolio
    speech_output = 'Based on your portfolio and current market performance, we recommend' \
                    'investing in Tesla, Nvidia, and CA Technologies.'

    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))