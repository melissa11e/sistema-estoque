dicBasicos={
    'Arroz':{'Prato Grosso':10, 'Camila':12, 'Tia Joana':2},
    'feijão':{'carioca Camila':11, 'carioca Kisabor':4, 'preto Camila':26, 'preto Pantera':15},
    'Açúcar':{'Separado':28, 'Baixo Feliz':8,'Barquinhos':4},
    'Sal':{'Ganso': 15,'Coelho': 12},
    'Macarrão':{'Pato':5, 'Adrio':2, 'Barril':14},
    'Farinha de trigo':{'Bento':21, 'Chico':0},
    'Óleo':{"Soraya":15, "Enrolado":13,"Pesado":2},
    'Vinagre':{'Azedin':2, 'Docin':14, 'Imperio':13},
    'Molho de tomate':{'Desejo':22,'Einz':11},
    'Leite':{'Vaquinha': 17,'Mimosa': 17,'Mu': 17},
    'Lentilha':{'Opa': 33},
    'Pipoca':{'Corn':10,'Estouro':22,'Ita':7}
}
dicPetiscos={
     'Salgadinho':{'Dotos': 12,'Rusbe':10, 'Chetinho':19, 'Fofinho':3, 'Jogador':14 },
     'Biscoito':{'Maizen':20,'Track':44,'Passa Hora':12,'Wafe':32,'Anti Social':17},
     'Chocolate':{'Ela Dela':11,'Bislheteria':9,'Garota':16,'Prata Branca':60,'Nestla':14},
     'Amendoim':{'Alho':33,'Cebola e Salsa':4},
     'Bala':{'Grossi':17,'Hills':47}
     }
dicSaudaveis={
    'Verdura': {'Alface unid': 3,'Espinafre unid': 5,'Rúcula unid': 2,'Couve unid': 4},
    'Legume': {'Cenoura': 150,'Abobrinha': 60,'Batata': 202,'Cebola':95,'Pimentão Vermelho': 33},
    'Fruta': {'Maçã': 73,'Banana cachos': 30,'Laranja': 18,'Pera': 10,'Melancia':18,'Uva cachos':24,'morango caixa':23,
               'Melão':23, 'Ameixa':56, 'Tomate':89}
}

dicLimpeza={
    'Desinfetante':{'Lavanda':10,'Ocean':3,'Flores':12,'Citronela':8},
    'Detergente':{'Epy':12, 'Olhe':16},
    'Cloro':24
}

dicHigiene={
    'Sabonete': {'Lavanda': 15, 'Aloe Vera': 10, 'Coco': 8, 'Erva-Doce': 12},
    'Shampoo': {'Cabelos Normais': 20, 'Anticaspa': 14, 'Hidratante': 18},
    'Creme Dental': {'Hortelã': 30, 'Menta Fresca': 25, 'Clareador': 15},
    'Desodorante': {'Feminino Floral': 20,'Masculino Madeira': 15, 'Neutro': 25},
    'Papel Higiênico': {'Branco Simples': 40,'Folha Dupla': 30, 'Lavanda Perfumado': 25}
    }

estoque=[]
estoque.append(dicBasicos)
estoque.append(dicPetiscos)
estoque.append(dicSaudaveis)
estoque.append(dicLimpeza)
estoque.append(dicHigiene)

#for i2 in listaCompras:
#  print(i2)
i1=0
while True:
  r=input("Deseja adicionar mais? (sim/não)")
  if r!= 'sim':
   break
  else:
   c=input("Digite a categoria que deseja adicionar\n(b - básicos, p - petiscos, s- saudáveis, l - limpeza, h - higiêne):")
   p=input("Digite o produto que deseja adicionar: ")
   m=input("Digite a marca que deseja adicionar: ")
   q=int(input("Digite a quantidade: "))

   if c=='b':
    if m in dicBasicos[p]:
     valor = dicBasicos[p][m]
     dicBasicos[p][m]=valor+q
    else:
      dicBasicos[p][m]=q

   elif c=='p':
    if m in dicPetiscos[p]:
     valor = dicPetiscos[p][m]
     dicPetiscos[p][m]=valor+q
    else:
      dicPetiscos[p][m]=q

   elif c=='s':
    if m in dicSaudaveis[p]:
     valor = dicSaudaveis[p][m]
     dicSaudaveis[p][m]=valor+q
    else:
     dicSaudaveis[p][m]=q

   elif c=='l':
    if m in dicLimpeza[p]:
     valor = dicLimpeza[p][m]
     dicLimpeza[p][m]=valor+q
    else:
     dicLimpeza[p][m]=q

   elif c=='h':
    if m in dicHigiene[p]:
     valor=dicHigiene[p][m]
     dicHigiene[p][m]=valor+q
    else:
     dicHigiene[p][m]=q

   else:
    print("Categoria inválida.")
   i1+=i1

for categoria in estoque:
    print("=" * 50)
    for produtos, quantidade in categoria.items():
        print(f"{produtos}: {quantidade}")

