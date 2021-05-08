key = "YOUR KEY HERE"
secret = "YOUR SECRET HERE"
import sys
import ccxt

exchange = ccxt.ftx({
    'apiKey': key,
    'secret': secret
})

# create and execute a scaled order
def scaled_order(side, symbol, amount, num_orders):
    params = {'postOnly': True}
    exchange.create_order(symbol, "limit", side, 0.01, 62000, params)


# parse function name and args and call function
def main():
    func_name = sys.argv[1]
    args = sys.argv[2:]
    globals()[func_name](*args)


if __name__ == "__main__":
    main()