import yaml
def save_yaml_file(data, file_path):
    try:
        with open(file_path, 'w') as file:
            yaml.dump(data, file)
        print(f'Zapisano dane do pliku: {file_path}')
    except Exception as e:
        print(f'Wystąpił błąd podczas zapisu danych: {str(e)}')

def main(sciezka):
    data = {
        'przykladowy': 'yaml',
    }
    file_path = 'ścieżka/do/pliku.yml'
    save_yaml_file(data, file_path)

if __name__ == '__main__':
    main()