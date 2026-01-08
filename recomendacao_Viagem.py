# Sistema de Recomendação de Viagem
# Prática 1 - Fundamentos de Python para IA

def coletar_preferencias():
    """Função para coletar as preferências do usuário"""
    clima = input("Você prefere clima quente ou frio? ").strip().lower()
    ambiente = input("Prefere lugares com natureza ou paisagens urbanas? ").strip().lower()
    try:
        orçamento = float(input("Qual é o seu orçamento disponível para a viagem (em R$)? "))
    except ValueError:
        print("Entrada inválida! Digite apenas números para o orçamento.")
        orçamento = float(input("Qual é o seu orçamento disponível para a viagem (em R$)? "))
    
    return clima, ambiente, orçamento


def recomendar_destino(clima, ambiente, orçamento, destinos):
    """Função que avalia as opções e retorna uma recomendação"""
    recomendados = []
    
    for destino in destinos:
        if (destino["clima"] == clima and
            destino["ambiente"] == ambiente and
            orçamento >= destino["preco"]):
            recomendados.append(destino)
    
    if recomendados:
        escolhido = recomendados[0]  # pega o primeiro compatível
        print(f"\n✨ Recomendação de viagem: {escolhido['nome']}")
        print(f"Justificativa: Clima {escolhido['clima']}, ambiente {escolhido['ambiente']} "
              f"e preço médio de R${escolhido['preco']}.")
    else:
        print("\n😕 Não encontramos um destino compatível com suas preferências. "
              "Tente ajustar seu orçamento ou preferências.")


def main():
    # Lista de destinos com características
    destinos = [
        {"nome": "Rio de Janeiro", "clima": "quente", "ambiente": "urbano", "preco": 2000},
        {"nome": "Gramado", "clima": "frio", "ambiente": "urbano", "preco": 2500},
        {"nome": "Chapada dos Veadeiros", "clima": "quente", "ambiente": "natureza", "preco": 1500},
        {"nome": "Bariloche", "clima": "frio", "ambiente": "natureza", "preco": 4000},
        {"nome": "Fernando de Noronha", "clima": "quente", "ambiente": "natureza", "preco": 5000},
        {"nome": "Salvador", "clima": "quente", "ambiente": "urbano", "preco": 2200},
        {"nome": "Curitiba", "clima": "frio", "ambiente": "urbano", "preco": 1800},
        {"nome": "Pantanal", "clima": "quente", "ambiente": "natureza", "preco": 3000},
        {"nome": "Machu Picchu", "clima": "frio", "ambiente": "natureza", "preco": 3500},
        {"nome": "Lisboa", "clima": "quente", "ambiente": "urbano", "preco": 4500},
        {"nome": "Paris", "clima": "frio", "ambiente": "urbano", "preco": 6000},
        {"nome": "Cancún", "clima": "quente", "ambiente": "natureza", "preco": 5500},
        {"nome": "Toronto", "clima": "frio", "ambiente": "urbano", "preco": 7000},
        {"nome": "Dubai", "clima": "quente", "ambiente": "urbano", "preco": 8000}
    ]
    
    print("=== Sistema de Recomendação de Viagem ===")
    clima, ambiente, orçamento = coletar_preferencias()
    recomendar_destino(clima, ambiente, orçamento, destinos)


if __name__ == "__main__":
    main()