import json

def save_json_file(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f'Zapisano dane do pliku: {file_path}')
    except Exception as e:
        print(f'Wystąpił błąd podczas zapisu danych: {str(e)}')

def main():
    data = {
        'przykladowy': 'json',
    }
    file_path = 'ścieżka/do/pliku.json'  # Przykładowa ścieżka do pliku .json
    save_json_file(data, file_path)

if __name__ == '__main__':
    main()