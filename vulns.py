import os

print("--- Iniciando Busca de Vulnerabilidades (NSE) ---")
print("Isso pode demorar alguns minutos...")

# O script 'vuln' do nmap verifica as falhas mais conhecidas
comando = "nmap -sV --script vuln "ip da rede a se verificar"> storage/downloads/vulnerabilidades.txt"

os.system(comando)

print("---")
print("Concluído! Verifique o ficheiro 'vulnerabilidades.txt' nos Downloads.")
