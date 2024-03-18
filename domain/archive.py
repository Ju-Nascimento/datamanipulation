import csv


class Archive:
    def __init__(self, path_file):
        self.path_file = path_file

    def create_archive(self):
        dados = []
        while True:
            nome = input("Digite seu nome: ")
            if nome.lower() == 'sair':
                break

            matricula = input("Digite sua matrícula: ")
            if matricula.isdigit():  # Verifica se a entrada contém apenas dígitos
                matricula = int(matricula)  # Converte para inteiro se for válido
                curso = input("Digite o seu curso: ")
                dados.append([nome, matricula, curso])
            else:
                print("Matrícula inválida. Digite Novamente.")

        with open(self.path_file, 'w', encoding="utf-8", newline='') as file:
            csvwriter = csv.writer(file, delimiter=',')
            for row in dados:
                csvwriter.writerow(row)


# Instanciando a classe Archive e chamando o método create_archive
archive = Archive('exemplo.csv')
archive.create_archive()
