from src import sushiswap, harmony

rpc = harmony.Harmony()

con_model = harmony.contracts.CLNY
ticker_model = sushiswap.tickers.CLNY_ONE

clny_resp = sushiswap.get_pair(ticker_model)
contract = rpc.get_wrapped_contract(con_model)

supply = contract.total_supply()

if clny_resp is not None:
    print(f"Price: {clny_resp.price} {ticker_model}")

print(f"Total Supply: {supply} {con_model.name}")