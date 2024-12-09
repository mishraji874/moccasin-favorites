# from src import favorites
# from script.deploy import deploy_favorites
# import pytest

# @pytest.fixture(scope="function")
# def favorites_contract():
#     favorites_contract = deploy_favorites()
#     return favorites_contract

def test_starting_values(favorites_contract):
    # favorites_contract = favorites.deploy()
    
    # assert favorites_contract.retrieve() == 7
    
    
    # favorites_contract = deploy_favorites()
    assert favorites_contract.retrieve() == 77
    

def test_can_change_values(favorites_contract):
    # Arrange
    # favorites_contract = deploy_favorites()
    # Act
    favorites_contract.store(42)
    # Assert
    assert favorites_contract.retrieve() == 42
    
def test_can_add_person(favorites_contract):
    # Arrange
    new_person = "Becca"
    favorite_number = 16
    # favorites_contract = deploy_favorites()
    
    # Act
    favorites_contract.add_person(new_person, favorite_number)
    
    # Assert
    assert favorites_contract.list_of_people(0) == (favorite_number, new_person)