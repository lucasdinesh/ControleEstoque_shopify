from receber import *
import getpass
from envia_email import Email


def executa(pedido_parada, nome_arquivo, enviaremail):
    get_endereco=Endereco()
    campos_pedido = Pedido()
    arquivo_excel = openpyxl.Workbook()
    planilha1 = arquivo_excel.active
    planilha1.title = "Planilha1"
    planilha_end_errado = arquivo_excel.create_sheet("endereco errado")
    valores = ("PEDIDO", "STATUS", "ENVIO", "QUANT ITENS", "FORMA PAGAMENTO", "FEITO", "ENVIADO")
    planilha1.append(valores)
    planilha_end_errado.append(valores)
    email = Email()
    orders = ShopifyApp()
    numero_pedido = 0
    try:
        for contador in range(0, 8):
            pedidos = orders.get_pedidos(contador + 1)
            pedidos = pedidos['orders']
            for key in pedidos:
                if numero_pedido == int(pedido_parada):
                    break
                else:
                    numero_pedido = campos_pedido.get_numero_pedido(key)
                    if key['cancelled_at'] != None:
                        orders.cancelado(numero_pedido, planilha1)
                    else:
                        forma_pagamento = campos_pedido.get_forma_pagamento(key)
                        status_pagamento = campos_pedido.get_status_pagamento(key)
                        if bool(get_endereco.recebe_endereco(key, 1)) == True:
                            end_part1 = get_endereco.recebe_endereco(key,1)
                            end_part2 = get_endereco.recebe_endereco(key,2)
                        else:
                            end_part1 = get_endereco.get_endereco_de_outra_forma(key, 1)
                            end_part2 = get_endereco.get_endereco_de_outra_forma(key, 2)
                        processado= campos_pedido.get_andamento_pedido(key)
                        forma_envio= campos_pedido.get_forma_envio(key)
                        email_cliente = campos_pedido.get_email_cliente(key)
                        nome_cliente= campos_pedido.get_nome_cliente(key)
                        pedido_enderrado=numero_pedido
                        if processado == None:
                            processado=''
                        else: processado= 'OK'
                        items = campos_pedido.get_quantidade_itens(key)
                        validacao_end = orders.valida_endereco(end_part1, end_part2)
                        if validacao_end == True or forma_pagamento == 'PagSeguro':
                            orders.insere_tupla(numero_pedido, status_pagamento, forma_envio, items, forma_pagamento,processado,
                                                planilha1)
                        else:
                            numero_pedidoaux= '**'+str(numero_pedido)
                            orders.insere_tupla(numero_pedidoaux, status_pagamento, forma_envio, items, forma_pagamento,processado,
                                                planilha1)
                            orders.insere_tupla(numero_pedido, status_pagamento, forma_envio, items, forma_pagamento,processado
                                                ,planilha2=planilha_end_errado)
                            if enviaremail == True:
                                email.enviar_email(email_cliente,nome_cliente,pedido_enderrado)


        orders.colore_celula(planilha1)
        orders.colore_celula(planilha_end_errado)
        arquivo_excel.save(r'/Users/' + getpass.getuser() + f'/Desktop/{nome_arquivo}.xlsx')


    except Exception as error:
        print('Erro ao executar codigo', error)

