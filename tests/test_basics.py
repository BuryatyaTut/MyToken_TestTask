
from brownie import accounts, reverts, MyToken

decimal = 10 ** 18



def test_initial_minting():
    # Arrange
    account = accounts[0]
    addresses = [accounts[1], accounts[2], accounts[3]]
    # Act
    token = MyToken.deploy(addresses, {'from': account})
    # Assert
    assert token.totalSupply() == 300000 * decimal

    for address in addresses:
        assert token.balanceOf(address) == 100000 * decimal

def test_mint():
    # Arrange
    account = accounts[0]
    addresses = [accounts[1]]
    token = MyToken.deploy(addresses, {'from': account})
    # Act
    token.mint(accounts[2], 50000 * decimal, {'from': account})
    # Assert
    assert token.balanceOf(accounts[2]) == 50000 * decimal

def test_burn():
    # Arrange
    account = accounts[0]
    addresses = [accounts[1]]
    token = MyToken.deploy(addresses, {'from': account})
    # Act
    token.burn(50000 * decimal, {'from': accounts[1]})
    # Assert
    assert token.balanceOf(accounts[1]) == 50000 * decimal

