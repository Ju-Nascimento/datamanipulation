import csv

class Archive:
    def __init__(self, path_file):
        self.path_file = path_file

    def create_archive(self, dados):
        with open(self.path_file, 'w', encoding="utf-8", newline='') as file:
            csvwriter = csv.writer(file, delimiter=',')
            for row in dados:
                csvwriter.writerow(row)

# Definindo os dados fora da classe
dados = [
    ['Nome', 'Matricula', 'Curso'],
    ['Juan', 2504, 'ADS'],
    ['Joãozinho', 1015, 'Sistemas'],
    ['Maria', 2023, 'Redes']
]

# Instanciando a classe Archive e chamando o método create_archive
archive = Archive('exemplo.csv')
archive.create_archive(dados)
