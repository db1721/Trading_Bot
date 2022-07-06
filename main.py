from menu_option_one.search_for_data_of_specific_stock_yfinance import SearchForStockData


def run_bot():
    # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
    # Use a breakpoint in the code line below to debug your script.
    print(f'Welcome to the Webull Trading Bot')
    while True:
        user_input = input('Select an option from the menu\n'
                           '1. See information about a specific stock\n'
                           '2. Create a personal ETF of stocks of your choice\n')

        if user_input == '1':
            user_input1 = input('What stock would you like to see the information for?')
            SearchForStockData(user_input1)
            exit(1)
        else:
            print('Please enter a number from the menu')


if __name__ == '__main__':
    run_bot()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
