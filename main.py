from cancelar_pedido import cancelar_pedido 
pedido = { 
    "numero_pedido":1,
    "status": "ABERTO"
}
cancelar_pedido(pedido)
print(pedido)