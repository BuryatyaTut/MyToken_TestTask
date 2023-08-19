from brownie import accounts, reverts, MyToken

decimal = 10 ** 18

def test_burn_over_balance():
    # Arrange
    account = accounts[0]
    adressses = [accounts[1], accounts[2]]

    # Act
    token = MyToken.deploy(adressses, {"from": account})

    with reverts("ERC20: burn amount exceeds balance"):
        token.burn(100 * decimal, {"from": account})
