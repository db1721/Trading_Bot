from menu_option_one.search_for_data_of_specific_stock_yfinance import SearchForStockData

etf_list = ['ORC', 'CSCO', 'IBM', 'CRF', 'CLM', 'ARR', 'IVR', 'NYMT', 'AGNC', 'EFC', 'O', 'DX', 'NLY', "STAG", 'RYLD',
            'XYLD', 'MVO', 'IEP', 'QYLD', 'LDI', 'ECC', 'GAIN', 'YYY', 'GECC', 'KBWD', 'OKE', 'RA', 'TROW',
            'DIVO', 'IRM', 'DHS', 'MAIN', 'VICI', 'ARCC', 'AMZA', 'DKL', 'OUSA', 'MRO', 'LTC', 'PSEC', 'UVV', 'TEF',
            'CIF', 'CSSEP', 'PBT', 'VALE', 'CRT', 'TWO', 'GLDI', 'NUSI', 'USOI', 'SBLK', 'SLVO', 'ZIM']

simple_list = ['CLM', 'XYLD', 'QYLD']

iv_dict = {}

for stock in simple_list:
    run = SearchForStockData(stock)
    try:
        iv_dict.update(run.benjamin_graham_intrinsic_value())
    except:
        pass

# for key, value in iv_dict.items():
#     print(f'{key}: {value}')
