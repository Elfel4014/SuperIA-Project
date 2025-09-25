from web3 import Web3
from solcx import compile_source

def compile_and_deploy_contract(w3, contract_source_code):
    """
    Compila um contrato Solidity e o implanta em uma rede Ethereum local (Ganache/Hardhat).
    :param w3: Instância Web3 conectada à rede.
    :param contract_source_code: Código fonte do contrato Solidity.
    :return: Objeto de contrato implantado e o hash da transação de implantação.
    """
    # Compila o contrato
    compiled_sol = compile_source(contract_source_code)
    contract_id, contract_interface = compiled_sol.popitem()

    # Obtém o bytecode e a ABI
    bytecode = contract_interface["bin"]
    abi = contract_interface["abi"]

    # Cria o objeto de contrato
    Contract = w3.eth.contract(abi=abi, bytecode=bytecode)

    # Obtém a conta padrão para implantação
    w3.eth.default_account = w3.eth.accounts[0]

    # Implanta o contrato
    tx_hash = Contract.constructor().transact()
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    contract_instance = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

    print(f"Contrato implantado em: {tx_receipt.contractAddress}")
    return contract_instance, tx_receipt.contractAddress

def interact_with_contract(contract_instance):
    """
    Interage com o contrato SimpleStorage implantado.
    :param contract_instance: Instância do contrato implantado.
    """
    # Chama a função get() (view function)
    initial_value = contract_instance.functions.get().call()
    print(f"Valor inicial armazenado: {initial_value}")

    # Chama a função set() (state-changing function)
    new_value = 42
    tx_hash = contract_instance.functions.set(new_value).transact()
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Valor atualizado para: {new_value}")

    # Chama a função get() novamente para verificar
    updated_value = contract_instance.functions.get().call()
    print(f"Valor atualizado armazenado: {updated_value}")

if __name__ == "__main__":
    # Conecta a uma rede Ethereum local (ex: Ganache ou Hardhat Node)
    # Certifique-se de que um nó local esteja rodando em http://127.0.0.1:8545
    try:
        w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
        if not w3.is_connected():
            raise Exception("Não foi possível conectar ao nó Ethereum local.")
        print("Conectado ao nó Ethereum local.")
    except Exception as e:
        print(f"Erro de conexão: {e}")
        print("Por favor, inicie um nó Ethereum local (ex: Ganache, Hardhat) em http://127.0.0.1:8545.")
        exit(1)

    # Carrega o código fonte do contrato
    with open("SimpleStorage.sol", "r") as f:
        contract_source_code = f.read()

    # Compila e implanta o contrato
    contract_instance, contract_address = compile_and_deploy_contract(w3, contract_source_code)

    # Interage com o contrato
    interact_with_contract(contract_instance)

