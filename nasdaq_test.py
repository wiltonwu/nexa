import sys
import websocket
import threading
import time
import requests
import argparse
from pprint import pprint
import numpy as np

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

def main():
    parser = argparse.ArgumentParser(description='gettin some market data')
    parser.add_argument('--start_date', required=True, help="Enter a valid start date in YYYYMMDD format")
    parser.add_argument('--end_date', required=True, help="Enter a valid end date in YYYYMMDD format")
    parser.add_argument('--symbols', required=True, help="Enter a ticker symbol or list of tickers. E.g. NDAQ or NDAQ,AAPL,MSFT")

    args = parser.parse_args()

    websocket.enableTrace(True)

    symbols = args.symbols.split(',')

    for symbol in symbols:
        url = 'ws://34.214.11.52/stream?symbol={}&start={}&end={}'.format(symbol, args.start_date, args.end_date)
 
        # Create new socket and connect to url to hit API
        ws = websocket.WebSocket()
        ws.connect(url)

        # send information and store reponse
        ws.send("")
        stock_info = ws.recv()

        stock_dict = eval(stock_info)

        print(stock_dict)

        ws.close()
        

if __name__ == "__main__":
   main() 

# def supres(ltp, n):
#     """
#     This function takes a numpy array of last traded price
#     and returns a list of support and resistance levels 
#     respectively. n is the number of entries to be scanned.
#     """
#     from scipy.signal import savgol_filter as smooth

#     #converting n to a nearest even number
#     if n%2 != 0:
#         n += 1
    
#     n_ltp = ltp.shape[0]

#     # smoothening the curve
#     ltp_s = smooth(ltp, (n+1), 3) 

#     #taking a simple derivative
#     ltp_d = np.zeros(n_ltp)
#     ltp_d[1:] = np.subtract(ltp_s[1:], ltp_s[:-1])
 
#     resistance = []
#     support = []
    
#     for i in xrange(n_ltp - n):
#         arr_sl = ltp_d[i:(i+n)]
#         first = arr_sl[:(n/2)] #first half
#         last = arr_sl[(n/2):] #second half
        
#         r_1 = np.sum(first > 0)
#         r_2 = np.sum(last < 0)

#         s_1 = np.sum(first < 0)
#         s_2 = np.sum(last > 0)

#         #local maxima detection
#         if (r_1 == (n/2)) and (r_2 == (n/2)): 
#             resistance.append(ltp[i+((n/2)-1)])

#         #local minima detection
#         if (s_1 == (n/2)) and (s_2 == (n/2)): 
#             support.append(ltp[i+((n/2)-1)])

#     return support, resistance