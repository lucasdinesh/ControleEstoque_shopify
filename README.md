# ControleEstoque_shopify
  Este é um projeto para controle de estoque de um E-commerce usando:
    - API da plataforma de E-commerce shopify;
    - PYQT5 - Interface Gráfica;
    - SMTPlib - Para envio de email;
    - openpyxl - Para gerar as planilhas.
  
  Onde sozinho e sem nenhuma conhecimento prévio da API soluciono o problema de gerenciamento de pedidos de forma eficaz.
  Ao  pegar dados da API gera uma planilha com: Pedido, Status(confirmado ou pendente), Envio(Pac ou SEDEX), Forma de pagamento(Pagseguro ou Paypal), Feito, Enviado. 
Ainda verifica se o cliente esta com o endereço errado por um padrão de endereço, se estiver errado, envia um email para confirmação do endereço.
