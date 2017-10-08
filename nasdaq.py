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


def get_high_price(ticker):
    return get_stock_dict(ticker)["High"]


def get_low_price(ticker):
    return get_stock_dict(ticker)["Low"]


def get_close_price(ticker):
    return get_stock_dict(ticker)["Close"]