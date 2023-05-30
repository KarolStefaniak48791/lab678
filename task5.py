import xml.etree.ElementTree as ET
sciezka = input("Podaj sciezke do pliku xml")
def load_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except FileNotFoundError:
        print(f'Plik {file_path} nie istnieje.')
        return None
    except ET.ParseError as e:
        print(f'Błąd w składni pliku XML: {file_path}')
        print(e)
        return None

def main(sciezka):
    file_path = sciezka
    root = load_xml_file(file_path)
    if root is not None:
        print(root)

if __name__ == '__main__':
    main(sciezka)