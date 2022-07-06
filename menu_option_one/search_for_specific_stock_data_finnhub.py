import finnhub
import pandas as pd
import yfinance as yf

from calculations.calculations import Calculations

stock_ticker = 'iep'.upper()

# Setup client
finnhub_client = finnhub.Client(api_key="sandbox_cb2s03qad3i3uh8vjfo0")

# get data on this ticker
ticker_data = yf.Ticker(stock_ticker)

# # Stock candles
# res = finnhub_client.stock_candles(stock_ticker, 'D', 1590988249, 1591852249)
# print(res)

# # Convert to Pandas Dataframe
# print(pd.DataFrame(res))

# # Aggregate Indicators
# print(finnhub_client.aggregate_indicator(stock_ticker, 'D'))
#
# # Basic financials
# print(finnhub_client.company_basic_financials(stock_ticker, 'all'))
#
# # Earnings surprises
# print(finnhub_client.company_earnings(stock_ticker, limit=5))
#
# EPS estimates
eps_dict = finnhub_client.company_eps_estimates(stock_ticker, freq='quarterly')
# print(eps_dict)
count = 1
for key, value in eps_dict.items():
    if key == 'data':
        if not value:
            eps = 0
        else:
            for dictionary in value:
                for key2, value2 in dictionary.items():
                    # Grab newest EPS
                    if key2 == 'epsAvg' and count == 1:
                        eps = value2
                        count += 1
                        break
print(eps)

# Growth Rate
growth_rate = 0
analysis = ticker_data.get_analysis(as_dict=True)
print(analysis)
for key, value in analysis.items():
    if key == 'Growth':
        for key2, value2 in value.items():
            if key2 == '+5Y':
                # print(f'Growth Rate: {value2}')
                growth_rate = value2
        break
#
# # Company Executives
# print(finnhub_client.company_executive(stock_ticker))
#
# # Company News
# # Need to use _from instead of from to avoid conflict
# print(finnhub_client.company_news(stock_ticker, _from="2020-06-01", to="2020-06-10"))
#
# # Company Peers
# print(finnhub_client.company_peers(stock_ticker))
#
# # Company Profile
# print(finnhub_client.company_profile(symbol=stock_ticker))
# print(finnhub_client.company_profile(isin='US0378331005'))
# print(finnhub_client.company_profile(cusip='037833100'))
#
# # Company Profile 2
# print(finnhub_client.company_profile2(symbol=stock_ticker))
#
# # Revenue Estimates
# print(finnhub_client.company_revenue_estimates(stock_ticker, freq='quarterly'))
#
# # List country
# print(finnhub_client.country())
#
# # Crypto Exchange
# print(finnhub_client.crypto_exchanges())
#
# # Crypto symbols
# print(finnhub_client.crypto_symbols('BINANCE'))
#
# # Economic data
# print(finnhub_client.economic_data('MA-USA-656880'))
#
# # Filings
# print(finnhub_client.filings(symbol=stock_ticker, _from="2020-01-01", to="2020-06-11"))
#
# # Financials
# print(finnhub_client.financials(stock_ticker, 'bs', 'annual'))
#
# # Financials as reported
# print(finnhub_client.financials_reported(symbol=stock_ticker, freq='annual'))
#
# # Forex exchanges
# print(finnhub_client.forex_exchanges())
#
# # Forex all pairs
# print(finnhub_client.forex_rates(base='USD'))
#
# # Forex symbols
# print(finnhub_client.forex_symbols(stock_ticker))
#
# # Fund Ownership
# print(finnhub_client.fund_ownership(stock_ticker, limit=5))
#
# # General news
# print(finnhub_client.general_news('forex', min_id=0))
#
# # Investors ownership
# print(finnhub_client.ownership(stock_ticker, limit=5))
#
# # IPO calendar
# print(finnhub_client.ipo_calendar(_from="2020-05-01", to="2020-06-01"))
#
# # Major developments
# print(finnhub_client.press_releases(stock_ticker, _from="2020-01-01", to="2020-12-31"))
#
# # News sentiment
# print(finnhub_client.news_sentiment(stock_ticker))
#
# # Pattern recognition
# print(finnhub_client.pattern_recognition(stock_ticker, 'D'))
#
# # Price target
# print(finnhub_client.price_target(stock_ticker))
#
# # Quote
# print(finnhub_client.quote(stock_ticker))
#
# # Recommendation trends
# print(finnhub_client.recommendation_trends(stock_ticker))
#
# # Stock dividends
# print(finnhub_client.stock_dividends(stock_ticker, _from='2019-01-01', to='2020-01-01'))
#
# # Stock dividends 2
# print(finnhub_client.stock_basic_dividends(stock_ticker))
#
# # Stock symbols
# print(finnhub_client.stock_symbols('US')[0:5])
#
# # Transcripts
# print(finnhub_client.transcripts('AAPL_162777'))
#
# # Transcripts list
# print(finnhub_client.transcripts_list(stock_ticker))
#
# # Earnings Calendar
# print(finnhub_client.earnings_calendar(_from="2020-06-10", to="2020-06-30", symbol="", international=False))
#
# # Covid-19
# print(finnhub_client.covid19())
#
# # Upgrade downgrade
# print(finnhub_client.upgrade_downgrade(symbol=stock_ticker, _from='2020-01-01', to='2020-06-30'))
#
# # Economic code
# print(finnhub_client.economic_code()[0:5])
#
# # Economic calendar
# print(finnhub_client.calendar_economic('2021-01-01', '2021-01-07'))
#
# # Support resistance
# print(finnhub_client.support_resistance(stock_ticker, 'D'))
#
# # Technical Indicator
# print(
#     finnhub_client.technical_indicator(symbol=stock_ticker, resolution='D', _from=1583098857, to=1584308457, indicator='rsi',
#                                        indicator_fields={"timeperiod": 3}))
#
# # Stock splits
# print(finnhub_client.stock_splits(stock_ticker, _from='2000-01-01', to='2020-01-01'))
#
# # Forex candles
# print(finnhub_client.forex_candles('OANDA:EUR_USD', 'D', 1590988249, 1591852249))
#
# # Crypto Candles
# print(finnhub_client.crypto_candles('BINANCE:BTCUSDT', 'D', 1590988249, 1591852249))
#
# # Tick Data
# print(finnhub_client.stock_tick(stock_ticker, '2020-03-25', 500, 0))
#
# # BBO Data
# print(finnhub_client.stock_nbbo(stock_ticker, "2020-03-25", 500, 0))
#
# # Indices Constituents
# print(finnhub_client.indices_const(symbol=f"^{stock_ticker}"))
#
# # Indices Historical Constituents
# print(finnhub_client.indices_hist_const(symbol=f"^{stock_ticker}"))
#
# # ETFs Profile
# print(finnhub_client.etfs_profile(stock_ticker))
# print(finnhub_client.etfs_profile(isin="US78462F1030"))
#
# # ETFs Holdings
# print(finnhub_client.etfs_holdings(stock_ticker))
# print(finnhub_client.etfs_holdings(isin="US00214Q1040", skip=2))
# print(finnhub_client.etfs_holdings("IPO", date='2022-03-10'))
#
# # ETFs Sector Exposure
# print(finnhub_client.etfs_sector_exp(stock_ticker))
#
# # ETFs Country Exposure
# print(finnhub_client.etfs_country_exp(stock_ticker))
#
# # International Filings
# print(finnhub_client.international_filings('RY.TO'))
# print(finnhub_client.international_filings(country='GB'))
#
# # SEC Sentiment Analysis
# print(finnhub_client.sec_sentiment_analysis('0000320193-20-000052'))
#
# # SEC similarity index
# print(finnhub_client.sec_similarity_index(stock_ticker))
#
# # Bid Ask
# print(finnhub_client.last_bid_ask(stock_ticker))
#
# # FDA Calendar
# print(finnhub_client.fda_calendar())
#
# # Symbol lookup
# print(finnhub_client.symbol_lookup('apple'))
#
# # Insider transactions
# print(finnhub_client.stock_insider_transactions(stock_ticker, '2021-01-01', '2021-03-01'))
#
# # Mutual Funds Profile
# print(finnhub_client.mutual_fund_profile(stock_ticker))
# print(finnhub_client.mutual_fund_profile(isin="US9229087286"))
#
# # Mutual Funds Holdings
# print(finnhub_client.mutual_fund_holdings(stock_ticker))
# print(finnhub_client.mutual_fund_holdings(isin="US9229087286", skip=2))
#
# # Mutual Funds Sector Exposure
# print(finnhub_client.mutual_fund_sector_exp(stock_ticker))
#
# # Mutual Funds Country Exposure
# print(finnhub_client.mutual_fund_country_exp(stock_ticker))
#
# # Revenue breakdown
# print(finnhub_client.stock_revenue_breakdown(stock_ticker))
#
# # Social sentiment
# print(finnhub_client.stock_social_sentiment('GME'))
#
# # Investment Themes
# print(finnhub_client.stock_investment_theme('financialExchangesData'))
#
# # Supply chain
# print(finnhub_client.stock_supply_chain(stock_ticker))
#
# # Company ESG
# print(finnhub_client.company_esg_score(stock_ticker))
#
# # Earnings Quality Score
# print(finnhub_client.company_earnings_quality_score(stock_ticker, 'quarterly'))
#
# # Crypto Profile
# print(finnhub_client.crypto_profile('BTC'))
#
# # EBITDA Estimates
# print(finnhub_client.company_ebitda_estimates(stock_ticker, freq="quarterly"))
#
# # EBIT Estimates
# print(finnhub_client.company_ebit_estimates(stock_ticker, freq="quarterly"))
#
# # USPTO Patent
# print(finnhub_client.stock_uspto_patent(stock_ticker, "2021-01-01", "2021-12-31"))
#
# # Visa application
# print(finnhub_client.stock_visa_application(stock_ticker, "2021-01-01", "2022-06-15"))
#
# # Insider sentiment
# print(finnhub_client.stock_insider_sentiment(stock_ticker, '2021-01-01', '2022-03-01'))
#
# # Bond Profile
# print(finnhub_client.bond_profile(isin='US912810TD00'))
#
# # Bond price
# print(finnhub_client.bond_price('US912810TD00', 1590988249, 1649099548))
#
# # Lobbying
# print(finnhub_client.stock_lobbying(stock_ticker, "2021-01-01", "2022-06-15"))
#
# # USA Spending
# print(finnhub_client.stock_usa_spending("LMT", "2021-01-01", "2022-06-15"))

# ben_graham = Calculations()
# ben_graham.benjamin_graham_intrinsic_value()

# if __name__ == '__main__':
#     run = SearchForStockData('xyld')
#     run.print_stock_info()
