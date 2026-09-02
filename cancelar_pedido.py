def cancelar_pedido(pedido):

    if pedido is None:
        print("\nPedido não encontrado.")
        return None

    if pedido["status"] =="CANCELADO":
        print(
            f"\nO pedido n°{pedido['numero_pedido']}"
        "já está cancelado.")
    

    





