#A biblioteca "os" fornece funções para interagir com o sistema operacional e
#foi utilizada neste script para manipulação de diretórios e arquivos.
import os

#A biblioteca "shutil" é uma biblioteca em Python que fornece funções para operações de alto nível relacionadas à manipulação de arquivos e diretórios. O nome "shutil" é uma abreviação de "shell utility", indicando que ela é projetada para oferecer utilidades semelhantes às encontradas em um shell (linha de comando) do sistema operacional.
import shutil

#Diretorio onde deverão ser criados a pastas para organização dos arquivos e onde estão os arquivos a serem organizados. 
#A biblioteca os.path.expanduser() é usada para expandir um caminho de diretório que começa com "~" para o diretório base do usuário atualmente logado. É usada neste script para criar caminhos de arquivo ou diretório que sejam específicos para o usuário logado no sistema operacional
ondeCriarPasta = os.path.expanduser("~/Desktop")

#Dicionario de diretório a serem criados que contem a listas de strings que representa as extensões que devem ser armazenadas em cada pastas.
dirs = {
	"Imagens": [".jpeg", ".jpg", ".png", ".gif"],
	"Documentos":[".doc", ".docx", ".pdf", ".txt"],
	"Arquivos": [".zip", ".rar"]
}

#Loop que passa pelo dicionário dirs e utiliza a função os.makedirs para criar as pastas especificada no dicionário dirs na pasta ondeCriarPasta, desde que ela não exista.
for dir_name in dirs:
	dir_path = os.path.join(ondeCriarPasta,dir_name)
	print('Caminho do diretorio criado:', dir_path)
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)
#Loop que usa a funcionalidade os.listdir para lista todos o conteúdo da pasta ondeCriarPasta, e usa a biblioteca os.path.isfile e função endswith para identificar se é uma arquivo com extensão especificada no dicionarios dirs.
#Se é arquivo e possui a extensão especificada, utiliza a biblioteca shutil.move para mover um arquivo de localização original_file_path para destination_folder.
for file_name in os.listdir(ondeCriarPasta):
	original_file_path = os.path.join(ondeCriarPasta, file_name)
	if os.path.isfile(original_file_path):
		for folder_name, extensions in dirs.items():
			for extension in extensions:
				if file_name.endswith(extension):
					destination_folder = os.path.join(ondeCriarPasta, folder_name)
					shutil.move(original_file_path, destination_folder)
