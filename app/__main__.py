import os
import pickle
from time import sleep



os.system('cls' if os.name == 'nt' else 'clear')
for c in range(7):
	print()
	print()
	print()
	print()
	print(f"\033[3{c+1}m{'Carregando Menu':^50}\033[m")
	sleep(.1)
	os.system('cls' if os.name == 'nt' else 'clear')
	
	
	
Lista = []
filmes = []
total = 0
meusFilmes = []
saldo = 150
compra = add_1 = erro_1 = erro_2 = erro_3 = erro_4 = erro_5 = False
continua = True



while True:
	try:
		arquivo = open("filmes","rb")
		Lista = pickle.load(arquivo)
		arquivo.close()
		break
	except:
		arquivo = open("filmes","wb")
		lista =[
		{"id":0,"nome":"atum","preço":45.0,"desc":"pos vida do vida do nemo"},
		{"id":1,'nome':"bacon","preço":15.0,"desc":"era uma vez, Peter Porc"},
		{"id":2,"nome":"Titanic","preço":20.0,"desc":"sei lá"},
		{"id":3,"nome":"Homem de ferro 1","preço":50.0,"desc":"Brabo demais"},
		{"id":4,"nome":"Homem de ferro 2","preço":10.,"desc":"assssssd"},
		{"id":5,"nome":"homem de ferro 3","preço":120.,"desc":"bjhkbjvj "},
		{"id":6,"nome":"Cap América 1","preço":12.0,"desc":"juhjhj"},
		{"id":7,"nome":"Cap América 2","preço":45.5,"desc":"bhgjgh"},
		{"id":8,"nome":"cap América 3","preço":64.56,"desc":"juhjhj"},
		{"id":9,"nome":"Thor Ragnarok","preço":21.0,"desc":"hygug"}
		]
		pickle.dump(lista, arquivo)
		arquivo.close()
		continue
		
		
		
#meus filmes
while True:
	try:
		arquivo = open("atum","rb")
		meusFilmes = pickle.load(arquivo)
		arquivo.close()
		break
	except:
		arquivo = open("atum","wb")
		arquivo.close()
		break



while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	print()
	print()
	print()
	print(f"\033[36m{'-'*15}=Barba_Negra_Films={'-'*15}\033[m")
	print()
	print(f"""\t[ 1 ] MOSTRAR FILMES
	[ 2 ] MEUS FILMES ({len(meusFilmes)})
	[ 3 ] Carrinho ({len(filmes)}) total: R$ {total:.2f}
	[ 4 ] Carteira
	[ 5 ] Perfil
	[ X ] SAIR
	""")
	print("nao entendi muito bem pq das 3 aspas")

	optM = input("\t\tOq deseja Fazer: ")
	try:
#opçao 1 do menu: Ver tds os filmes
		if int(optM) == 1:
			while continua:
				os.system('cls' if os.name == 'nt' else 'clear')
				
				if len(Lista) == 0:
					break
				print()
				if erro_1:
					print("\033[31mErro_1: opção inválida 2\033[m")
					erro_1 = False
				if erro_4:
					print(f"\033[35mErro_4: este Filme já é seu,\n meus Filmes para assisti-lo!\033[m")
					erro_4 = False
				if erro_5:
					print(f"\033[35mErro_5: este Filme já está em seu carrinho\033[m")
					erro_5 = False
				if add_1:
					print(f"\033[32m\nO filme: '{filmes[-1]['nome']}' foi adicionado no carrinho\033[m")
					print()
					print(f"\033[36m{'-'*20:<15}=Filmes Lançamento={'-'*10}\033[m")
					print(f"{len(Lista)} no total")
					print(f"[ {'n° ':<1} ]{' Nome':^30} R$ {'preço':>6}")
					print()
					add_1 = False
				for i,v in enumerate(Lista):
					print(f"[ {i+1:<1} {Lista[i]['nome']:^30} R$ {Lista[i]['preço']:>6.2f}")
				print()
				print(f"\033[31m[ X ]\033[m {'para sair':^30}")
				print()
				
				opt = input("selecione o filme: ").lower().strip()
				if opt == "x":
					break
				elif opt.isnumeric():
					opt = int(opt) -1
				try:
					for i,v in enumerate(meusFilmes):
						if Lista[opt]['id'] == meusFilmes[i]['id']:
							erro_4 = True
						
						if Lista[opt]['id'] in filmes:
							erro_5 = True
					if erro_4 or erro_5:
						continue
					else:
						total += Lista[opt]["preço"]
						filmes.append(Lista[opt])
						del Lista[opt]
						add_1 = True
				except:
					erro_1 = True
			
			
			
			
#opçao 2 menu : MEUS FILMES
		elif int(optM) == 2:
			while True:
				os.system('cls' if os.name == 'nt' else 'clear')
				sleep(1)
				print("\033[33m-"*10,"=Meus Filmes=","-"*10,"\033[m")
				if len(meusFilmes) == 0:
					print('Seus filmes ficarão aqui')
				else:
					for i,v in enumerate(meusFilmes):
						print(f"\033[33m {meusFilmes[i]['nome']}\n\t\033[36mDescrição  {meusFilmes[i]['desc']}\033[m")
				sair = input(f"\033[31m{'[ X ]':<5}\033[m {'para sair':^20}").lower().split()
				if "x" in sair:
					break
					
					
					
					
					
#Opçao 3 do menu: Carrinho
		elif int(optM) == 3:
			while True:
				os.system('cls' if os.name == 'nt' else 'clear')
				print()
				if erro_1:
					print("\033[31mErro_1: opção inválida 2\033[m")
					erro_1 = False
				if erro_2:
					print(f"\033[35mErro_2: Seu carrinho esta vazio!\033[m")
					erro_2 = False
				if erro_3:
					print(f"\033[31mErro_3: Saldo Insuficiente:\nvc tem R${saldo:.2f} na carteira\033[m")
					erro_3 = False
				if compra:
					print("""\033[32m
Compra efetuada com sucesso,
acesse a opção '[ 2 ] meus Filmes' no menu inicial
para poder assistir!\033[m
""")
					compra = False
					
					
					
				print()
				print("\033[33m-"*10,"=Carrinho=","-"*10,"\033[m")
				print(f"\033[34mSaldo: R$ {saldo:.2f}\033[m")
				print(f"\033[34m FILMES: {len(filmes)}\033[m")
				print()
				for i,v in enumerate(filmes):
					print(f"\033[33m n° {i + 1} - {filmes[i]['nome']},  PREÇO: {filmes[i]['preço']:.2f}\033[m")
				print(f"\033[34mTotal: R$ {total:.2f}\033[m")
				pedi = input("""
	[ 1 ] Remover ítem
	[ 2 ] Finalizar Compra
	[ X ] Voltar ao menu anterior
	
	Oque deseja fazer: """)
				try:
					if pedi.lower() == "x":
						break
					elif len(filmes) == 0:
						erro_2 = True
						continue
					if int(pedi) == 1:
							print()
							for i,v in enumerate(filmes):
								print(f"{i+1} - {filmes[i]['nome']}")
							print()
							sel = input("Qual filme deseja Remover:  ")
							try:
								sel = int(sel) -1
								Lista.append(filmes[sel])
								total -= filmes[sel]['preço']
								del filmes[sel]
								os.system('cls' if os.name == 'nt' else 'clear')
								print()
								print()
								print(f"\033[32m{'item removido':^50}\033[m")
								sleep(2)
							except:
								os.system('cls' if os.name == 'nt' else 'clear')
								print()
								print (f"\033[31m{'erro ao remover item':^50}\033[m")
								sleep(2)
								
								
					elif int(pedi) == 2:
						if saldo >= total >0:
							saldo -= total
							total -= total
							arquivo = open("atum","wb")
							pickle.dump(filmes, arquivo)
							arquivo.close()
							for i,v in enumerate(filmes):
								meusFilmes.append(filmes[i])
							del filmes[:]
							compra = True
						elif total == 0:
							erro_2 = True
						else:
							erro_3= True
							
						
				except:
					erro_1 = True
					continue
					
					
					
					
					
					
					
		elif optM > 3:
			print("Esta opçao ainda não disponível")
			sleep(2)
			continue
			
			
			
					
#Opçao # do menu: Sair
	except:
		if optM.lower() == "x":
			print()
			print()
			os.system('cls' if os.name == 'nt' else 'clear')
			print("Obrigado por acessar nossos serviços.")
			break
