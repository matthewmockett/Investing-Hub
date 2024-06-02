from flask import Flask, jsonify # imports the flask for web dev, and jsonify to convert python dictionaries to JSON format
from tradingview_ta import TA_Handler, Interval # used to get the techincal analysis
import requests # used to make HTTP requests to external APIs

app = Flask(__name__) # initalizes a new Flask application

@app.route('/coin/<symbol>', methods=['GET'])
def getCoinData(symbol):
    ticker = TA_Handler(symbol=symbol, screener = 'crypto', exchange = 'KRAKEN', interval=Interval.INTERVAL_1_DAY)
    analysis = ticker.get_analysis()

    # Converts the analysis to a JSON format
    return jsonify({
        'summary':analysis.summary,
        'indicators': analysis.indicators
    })

@app.route('/howto', methods=['GET'])
def getHow():
    how_to_content = {
        "Introduction to Stock Metrics": "This section explains stock metrics like P/E ratio, market cap, etc.",
        "P/E Ratio": "Price to Earnings Ratio (P/E) is calculated by dividing the current market price by the earnings per share.",
    }
    return jsonify(how_to_content)

@app.route('/exchanges', methods=['GET'])
def getExchanges():
    url = "https://twelve-data1.p.rapidapi.com/cryptocurrency_exchanges"
    querystring = {"format":"json"}
    headers = {
        "X-RapidAPI-Key": "1763024452mshc405eceae43b488p1c71cfjsne2342607582c",  
        "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    exchanges_data = response.json()
    return jsonify(exchanges_data)

if __name__ == '__main__':
    app.run(debug=True)

