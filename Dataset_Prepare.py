import json, re

# Percorso del file JSON da leggere
file_input = "./dataset2.json"

# Percorso del file di output
file_output = "./dataset2-2.json"

# Chiavi da estrarre dal file JSON
Key1 = "instruction"
Key2 = "source_code"

# Leggi il file JSON
with open(file_input, "r") as file:
    data = json.load(file)

def clear_code(code):
    # Sostituisco la tabulazione con il suo carattere di escape
    formatted_code = code.replace('    ', '\t')
    formatted_code = formatted_code.replace('""""', '"')
    formatted_code = formatted_code.replace('""', '"')
    # Rimmuovo i commenti, * significa qualsiasi cosa, ? significa 0 o 1 occorrenza, + significa 1 o più occorrenze
    formatted_code = re.sub(r'/\*.*?\*/', '', formatted_code, flags=re.DOTALL)
    formatted_code = re.sub(r'/\*\*.*?\*/', '', formatted_code, flags=re.DOTALL)
    formatted_code = re.sub(r'\*', '', formatted_code)
    formatted_code = re.sub(r'//.*', '', formatted_code)
    formatted_code = re.sub(r'///.*','',formatted_code)
    # Sostituisco le virgole in eccesso con uno spazio
    formatted_code = re.sub(r',,,,,,+', ' ', formatted_code)
    # Rimuovo la distanza in eccesso
    formatted_code = re.sub(r'\n  \n  +', '\n', formatted_code)
    formatted_code = re.sub(r'\n\n+', '\n', formatted_code)
    return formatted_code

def clear_text(text):
    formatted_text = text.replace('"', '\'')
    formatted_text = re.sub(r'\.(?!\s*$)', ',', formatted_text)
    return formatted_text

new_data = []

for dat in data:
    # Estrai le due chiavi specifiche
    value1 = dat.get(Key1)
    value2 = dat.get(Key2)

    # Verifica se value1 contiene '<h2>' in quanto indice di input_text mancante
    if '<h2>' not in value1:
        value2 = clear_code(value2)
        value1 = clear_text(value1)

        new_data.append({
            'input_text': value1,
            'output_code': value2
        })
    

# Salva i nuovi dati nel file di output come JSON
with open(file_output, "w") as file:
    json.dump(new_data, file, indent=4)