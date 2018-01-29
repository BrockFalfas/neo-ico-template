from thor.common.storage import StorageAPI

class Token():
    """
    Basic settings for an NEP5 Token and crowdsale
    """

    name = 'Thor token'

    symbol = 'THR'

    decimals = 8

    # This is the script hash of the address for the owner of the token
    # This can be found in ``neo-python`` with the walet open, use ``wallet`` command
    # To-do: create a owner wallet address for thor token and update here
    owner = b'\xaf\x12\xa8h{\x14\x94\x8b\xc4\xa0\x08\x12\x8aU\nci[\xc1\xa5'

    in_circulation_key = b'in_circulation'

    total_supply = 100000000 * 100000000  # 100m total supply * 10^8 ( decimals)

    initial_amount = 25000000 * 100000000  # 25m to owners * 10^8

    # for now assume 1 dollar per token, and one neo = 160 dollars * 10^8
    tokens_per_neo = 160 * 100000000

    # for now assume 1 dollar per token, and one gas = 55 dollars * 10^8
    tokens_per_gas = 55 * 100000000

    # maximum amount you can mint in the limited round ( 500 neo/person * 40 Tokens/NEO * 10^8 )
    max_exchange_limited_round = 500 * 40 * 100000000

    # when to start the crowdsale
    # To-Do: Update this block time
    block_sale_start = 875000

    # when to end the initial limited round
    # To-Do: Update this block time
    limited_round_end = 875000 + 10000


    def crowdsale_available_amount(self):
        """

        :return: int The amount of tokens left for sale in the crowdsale
        """
        storage = StorageAPI()

        in_circ = storage.get(self.in_circulation_key)

        available = self.total_supply - in_circ

        return available


    def add_to_circulation(self, amount:int, storage:StorageAPI):
        """
        Adds an amount of token to circlulation

        :param amount: int the amount to add to circulation
        :param storage:StorageAPI A StorageAPI object for storage interaction
        """
        current_supply = storage.get(self.in_circulation_key)

        current_supply += amount

        storage.put(self.in_circulation_key, current_supply)



    def get_circulation(self, storage:StorageAPI):
        """
        Get the total amount of tokens in circulation

        :param storage:StorageAPI A StorageAPI object for storage interaction
        :return:
            int: Total amount in circulation
        """
        return storage.get(self.in_circulation_key)

