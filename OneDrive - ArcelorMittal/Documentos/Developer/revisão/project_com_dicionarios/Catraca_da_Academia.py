# Dicionário com as matrículas e o status de pagamento
mensalidades = {
    "mat_001": "pago",
    "mat_002": "atrasado",
    "mat_003": "pago"
}

# Fila de pessoas tentando passar na catraca agora
fila_catraca = ["mat_001", "mat_999", "mat_002","mat_003"]

for matricula in fila_catraca:
    if matricula in mensalidades:
        if mensalidades[matricula] == "pago":
            print(f"✅ Catraca liberada para a matrícula {matricula}")
        else:
            print(f"⚠️ Acesso Bloqueado: A matrícula {matricula} possui pendências.")
    else:
        print(f"❌ Acesso Negado: Matrícula {matricula} não encontrada.")
