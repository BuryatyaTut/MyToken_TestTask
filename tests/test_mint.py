from brownie import accounts, reverts, MyToken

decimal = 10 ** 18


def test_mint_not_owner():
    # Arrange
    account = accounts[0]
    addresses = [accounts[1]]
    token = MyToken.deploy(addresses, {'from': account})
    # Act & Assert
    with reverts("Ownable: caller is not the owner"):
        token.mint(accounts[2], 50000 * decimal, {'from': accounts[2]})

def test_total_supply_limit():
    # Arrange
    account = accounts[0]
    addresses = [accounts[1]]
    token = MyToken.deploy(addresses, {'from': account})
    # Act and Assert
    with reverts("ERC20: mint amount exceeds max total supply"):
        token.mint(accounts[2], 900001 * decimal, {'from': account})