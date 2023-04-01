class DividendCalculator:
    def __init__(self):
        pass

    @staticmethod
    def calculate_insurance():
        """

        :return:
        """
        dividend_yield = 23.11
        dividend_payouts_per_year = 12
        cost_of_insurance = 2511
        amount_invested_per_month = cost_of_insurance / 12
        months_invested = 12
        total_amount_in_stock = 0.0
        total_amount_invested = 0.0

        formatted_amount_invested_per_month = "{:0.2f}".format(amount_invested_per_month)

        for i in range(1, dividend_payouts_per_year + 1):
            # Dividend payout to DRIP first
            drip = total_amount_in_stock * ((dividend_yield/months_invested)/100)

            # Investing per month straight up
            total_amount_invested += amount_invested_per_month

            # Investing per month with DRIP
            total_amount_in_stock += amount_invested_per_month + drip

            formatted_total_amount_in_stock = "{:0.2f}".format(total_amount_in_stock)
            formatted_total_amount_invested = "{:0.2f}".format(total_amount_invested)
            formatted_total_dividends = "{:0.2f}".format(total_amount_in_stock-total_amount_invested)

            if i < 10:
                print(f'Month 0{i}: ${formatted_total_amount_in_stock}')
            else:
                print(f'Month {i}: ${formatted_total_amount_in_stock}')

        print(f'At {formatted_amount_invested_per_month} a month for insurance ${formatted_total_amount_invested} '
              f'invested, the final value is ${formatted_total_amount_in_stock} generating ${formatted_total_dividends} '
              f'in dividends')

    @staticmethod
    def calculate_taxes():
        """

        :return:
        """
        dividend_yield = 23.11
        dividend_payouts_per_year = 12
        cost_of_taxes = 6500
        amount_invested_per_month = cost_of_taxes/12
        months_invested = 12
        total_amount_in_stock = 0.0
        total_amount_invested = 0.0

        formatted_amount_invested_per_month = "{:0.2f}".format(amount_invested_per_month)

        for i in range(1, dividend_payouts_per_year + 1):
            # Dividend payout to DRIP first
            drip = total_amount_in_stock * ((dividend_yield / months_invested) / 100)

            # Investing per month straight up
            total_amount_invested += amount_invested_per_month

            # Investing per month with DRIP
            total_amount_in_stock += amount_invested_per_month + drip

            formatted_total_amount_in_stock = "{:0.2f}".format(total_amount_in_stock)
            formatted_total_amount_invested = "{:0.2f}".format(total_amount_invested)
            formatted_total_dividends = "{:0.2f}".format(total_amount_in_stock - total_amount_invested)

            if i < 10:
                print(f'Month 0{i}: ${formatted_total_amount_in_stock}')
            else:
                print(f'Month {i}: ${formatted_total_amount_in_stock}')

        print(f'At {formatted_amount_invested_per_month} a month for taxes ${formatted_total_amount_invested} '
              f'invested, the final value is ${formatted_total_amount_in_stock} generating ${formatted_total_dividends} '
              f'in dividends')


test = DividendCalculator
test.calculate_insurance()
test.calculate_taxes()
