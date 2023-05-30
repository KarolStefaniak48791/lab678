import yaml
sciezka = input("Podaj sciezke pliku yaml: ")

def load_yaml_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except FileNotFoundError:
        print(f'Plik {file_path} nie istnieje.')
        return None
    except yaml.YAMLError as e:
        print(f'Błąd w składni pliku YAML: {file_path}')
        print(e)
        return None

def main(sciezka):
    file_path = sciezka
    data = load_yaml_file(file_path)
    if data is not None:
        print(data)

if __name__ == '__main__':
    main(sciezka)