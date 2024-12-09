from src import favorites
from moccasin.config import get_active_network

def deploy_favorites():
    favorites_contract = favorites.deploy()
    starting_number = favorites_contract.retrieve()
    print(f"Starting number is {starting_number}")
    
    favorites_contract.store(77)
    ending_number = favorites_contract.retrieve()
    print(f"Ending number is {ending_number}")
    
    active_network = get_active_network()
    print(active_network)
    
    if active_network.has_explorer():
        result = active_network.moccasin_verify(favorites_contract)
        result.wait_for_verification()

    return favorites_contract

def moccasin_main():
    deploy_favorites()