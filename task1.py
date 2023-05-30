import json
sciezka = input("Podaj sciezke do pliku: ")
def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f'Plik {file_path} nie istnieje.')
        return None
    except json.JSONDecodeError:
        print(f'Błąd w składni pliku JSON: {file_path}')
        return None

def main(sciezka):
    file_path = sciezka
    data = load_json_file(file_path)
    if data is not None:
        print(data)

if __name__ == '__main__':
    main(sciezka)