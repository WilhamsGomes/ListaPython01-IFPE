valorVenda = float(input("Informe o valor da venda: "))

totalPagar = valorVenda * 0.90
valorParcela = totalPagar/3
comissaoAVista = totalPagar * 0.05
comissaoParcelado = valorVenda * 0.05

print(f"Total a pagar: {totalPagar}; Valor de cada parcela: {valorParcela}; Comissão se for a vista: {comissaoAVista}; Comissão se for parcelado: {comissaoParcelado}")