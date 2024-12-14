dictionary = [
    {
        "nome": "exemplo",
        "peso": 2.0,
        "id": 1,
        "tamanho": 1.5
    },
    {
        "nome": "Exemplo",
        "peso": 1.5,
        "id": 2,
        "tamanho": 1.0
    },
    {
        "nome": "exemplo",
        "peso": 2.5,
        "id": 15,
        "tamanho": 1.0
    }
]

def getRegister(dictionary, term):
    def compare(dictionaryItem):
        for key, value in dictionaryItem.items():
            if isinstance(value, type(term)) and value == term:
                return True
            
    result = list(filter(compare, dictionary))
    
    if result:
        for i in result:
            print(i)
    else:
        print("Nenhum registro encontrado!")

