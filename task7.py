import xml.etree.ElementTree as ET
def save_xml_file(data, file_path):
    try:
        root = ET.Element('root')
        for key, value in data.items():
            element = ET.SubElement(root, key)
            element.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(file_path)
        print(f'Zapisano dane do pliku: {file_path}')
    except Exception as e:
        print(f'Wystąpił błąd podczas zapisu danych: {str(e)}')

def main():
    data = {
        'przykladowy': 'xml',
    }
    file_path = 'ścieżka/do/pliku.xml'
    save_xml_file(data, file_path)

if __name__ == '__main__':
    main()