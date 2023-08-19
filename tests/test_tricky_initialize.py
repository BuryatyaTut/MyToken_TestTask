from brownie import accounts, MyToken

decimal = 10 ** 18

# def test_initial_minting_overload():
#     # Arrange
#     account = accounts[0]
#     addresses = [accounts[1], accounts[2], accounts[3], accounts[4],accounts[5],accounts[6],accounts[7],accounts[8],accounts[9],accounts[10], accounts[0]]
#     # Act
#     # with reverts("ERC20: mint amount exceeds max total supply"):
#     token = MyToken.deploy(addresses, {'from': account})
    

def test_initial_same_adress():
    # Arrange
    account = accounts[0]
    addresses = [accounts[1], accounts[2], accounts[1]]

    # Act
    token = MyToken.deploy(addresses, {"from": account})

    # Assert
    assert token.balanceOf(accounts[1]) == 100000 * decimal


def test_initial_minting_none():
    # Arrange
    account = accounts[0]
    addresses = []
    # Act
    token = MyToken.deploy(addresses, {'from': account})
    # Assert
    assert token.totalSupply() == 0