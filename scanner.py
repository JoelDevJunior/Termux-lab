import os
import datetime

# Pega a data e hora atual para o relatório
data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

print(f"--- Iniciando Auditoria de Rede: {data_hora} ---")

# O comando -sV tenta descobrir as versões dos serviços
# O comando --open mostra apenas as portas que estão realmente abertas
comando = "nmap -sV --open 192.168.15.0/24 > storage/downloads/auditoria_rede.txt"

os.system(comando)

print("---")
print("Sucesso! O relatório detalhado foi gerado.")
print("Local: Downloads/auditoria_rede.txt")

