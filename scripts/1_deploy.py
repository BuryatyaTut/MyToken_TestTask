from brownie import accounts, config, MyToken

decimal = 10 ** 18


def main():
    account = accounts.add(config["wallets"]["from_key"])
    addresses = []
    erc20 = MyToken.deploy(addresses, {"from": account})
