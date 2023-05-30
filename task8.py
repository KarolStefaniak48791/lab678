import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QCheckBox, QLineEdit, QLabel
from PyQt6.QtGui import QColor, QGuiApplication
import yaml
import json
import xmltodict
from yaml import SafeLoader
import pandas as pd
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Konwerter'
        self.left = 0
        self.top = 0
        self.width = 180
        self.height = 200
        self.initUI()
        self.file = ""
        self.new_file = ""
        self.directory = ""
        self.json_check = 0
        self.xml_check = 0
        self.yml_check = 0

    def initUI(self):

        #Ustawienie okna
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: {}".format(QColor(46, 46, 46).name()))
        qr = self.frameGeometry()
        cp = QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        #Przycisk do wybierania plikow
        button = QPushButton('Wybierz plik', self)
        button.setToolTip('Kliknij, aby wybrać plik')
        button.setStyleSheet("background-color: {}".format(QColor(100, 100, 100).name()))
        button.setStyleSheet("color: white")
        button.move(20,150)
        button.clicked.connect(self.WyborPliku)

        #Przycisk do generowania plikow
        button2 = QPushButton('Generuj', self)
        button2.setToolTip('Kliknij, aby wygenerowac')
        button2.setStyleSheet("background-color: {}".format(QColor(100, 100, 100).name()))
        button2.setStyleSheet("color: white")
        button2.move(100, 150)
        button2.resize(60, 25)
        button2.clicked.connect(self.PobierzNazwe)

        #json checkbox
        json_check = QCheckBox('.json', self)
        json_check.move(20, 40)
        json_check.setStyleSheet("color: white")
        json_check.stateChanged.connect(self.changeJSON)

        #yml checkbox
        yaml_check = QCheckBox('.yaml', self)
        yaml_check.move(20, 60)
        yaml_check.setStyleSheet("color: white")
        yaml_check.stateChanged.connect(self.changeYAML)

        #xml checkbox
        xml_check = QCheckBox('.xml', self)
        xml_check.move(20, 80)
        xml_check.setStyleSheet("color: white")
        xml_check.stateChanged.connect(self.changeXML)

        #Pole do wpisania nazwy nowego pliku
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 120)
        self.textbox.resize(140, 30)
        self.textbox.setStyleSheet("color: white")

        #Tekst Nazwa Nowego Pliku
        tekst = QLabel("Nazwa nowego pliku", self)
        tekst.move(20, 100)
        tekst.setStyleSheet("color: white")

        #Tekst Format Generowanego pliku
        tekst2 = QLabel("Format generowanego pliku", self)
        tekst2.move(20, 20)
        tekst2.setStyleSheet("color: white")

        #Blokada zmiany rozmiaru okna
        self.setFixedSize(self.width, self.height)

        self.show()

    def changeJSON(self, state):
        if state == 2:
            self.json_check = 1
        else:
            self.json_check = 0

    def changeYAML(self, state):
        if state == 2:
            self.yaml_check = 1
        else:
            self.yaml_check = 0

    def changeXML(self, state):
        if state == 2:
            self.xml_check = 1
        else:
            self.xml_check = 0

    def WyborPliku(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Wybierz plik", "", "Pliki (*.json *.xml *.yaml)")
        if fileName:
            self.file = fileName

    def PobierzNazwe(self):
        self.new_file = self.textbox.text()
        self.GenerujPlik()

    def GenerujPlik(self):
        if self.file.endswith(".json"):
            self.JsonGenerator()
        elif self.file.endswith(".yaml"):
            self.YamlGenerator()
        else:
            self.XmlGenerator()

    def JsonGenerator(self):
        if self.xml_check == 1:
            with open(f'{self.file}', 'r') as file:
                configuration_x = json.load(file)
            with open(f"{self.new_file}.xml", "w") as file:
                xmltodict.unparse(configuration_x, output=file)
        if self.yaml_check == 1:
            with open(f'{self.file}', 'r') as file:
                configuration_y = json.load(file)
            with open(f'{self.new_file}.yaml', 'w') as yaml_file:
                yaml.dump(configuration_y, yaml_file)
        if self.json_check == 1:
            with open(f'{self.file}', 'r') as file:
                configuration_j = json.load(file)
            with open(f'{self.new_file}.json', 'w') as json_file:
                json.dump(configuration_j, json_file)

    def YamlGenerator(self):
        if self.xml_check == 1:
            with open(f"{self.file}", "r") as yaml_file:
                configuration_x = yaml.load(yaml_file, Loader=SafeLoader)
            with open(f"{self.new_file}.xml", "w") as file:
                xml_string = xmltodict.unparse(configuration_x, output=file)
        if self.yaml_check == 1:
            with open(f'{self.file}', 'r') as file:
                configuration_y = yaml.safe_load(file)
            with open(f'{self.new_file}.yaml', 'w') as yaml_file:
                yaml.dump(configuration_y, yaml_file)
        if self.json_check == 1:
            with open(f'{self.file}', 'r') as file:
                configuration_j = yaml.safe_load(file)
            with open(f'{self.new_file}.json', 'w') as json_file:
                json.dump(configuration_j, json_file)

    def XmlGenerator(self):
        if self.xml_check == 1:
            configuration_x = pd.read_xml(f"{self.file}")
            configuration_x.to_xml(f"{self.new_file}.xml")
        if self.yaml_check == 1:
            with open(f"{self.file}", "r") as xml_file:
                configuration_y = xml_file.read()
            python_dict = xmltodict.parse(configuration_y)
            with open(f"{self.new_file}.yaml", "w") as file:
                yaml.dump(python_dict, file)
        if self.json_check == 1:
            with open(f'{self.file}', 'r') as file:
                configuration_j = xmltodict.parse(file.read())
            with open(f'{self.new_file}.json', 'w') as json_file:
                json.dump(configuration_j, json_file)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
