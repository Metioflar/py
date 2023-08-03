listaProdutos = []

totalProdutos = 0



while True:



    print("============ lista de compras ============")

    print("======= 1 - adicionar produtos     =======")

    print("======= 2 - ver a lista de produtos =======")

    print("======= 3 - atualizar produtos      =======")

    print("======= 4 - remover produto         =======")

    print("======= 5 - encerrar programa       =======")



    opc = int(input("opções: "))



    match opc:

        case 1:

            nomeProdutos = input("que tipo de produtos: ").strip().upper()

            contProdutos = int(input("quantos produtos: "))

            valorPorProduto = float(input("Quanto é o produto: "))

            valorTotalProduto = valorPorProduto * contProdutos

            

            conteudoLista = {

                "produto" : nomeProdutos, "valor" : valorPorProduto, "quantidade" : contProdutos, "total" : valorTotalProduto

            }

            

            listaProdutos.append(conteudoLista)

            

            totalProdutos += valorTotalProduto





            print(f"{nomeProdutos} adicionado na lista de compras")

            

        case 2:         

            for i in listaProdutos:

                print()

                print(f"Produto {i['produto']}")

                print(f"Valor R$ {i['valor']}")

                print(f"Quantidade {i['quantidade']}")

                print(f"Total R$ {i['total']}")

                

            print(f"valor total de todos so produtos - R$ {totalProdutos}")



        

        case 3:

            

            findProdutoUpdate = input("digite o produto que deseja atualizar: ").strip().upper()

            for index in listaProdutos:

                if index["produto"] == findProdutoUpdate:

                    print("produto encontrado no dicionario")

                    

                    newProduto = input("Digite o nome do novo produto: ").strip().upper()

                    newCont = int(input("Digite a quantidade do novo produto: "))

                    newValor = float(input("Digite o valor do novo produto: "))

                    

                    totalProdutos -= index["total"]

                    

                    index["produto"] = newProduto

                    index["quantidade"] = newCont

                    index["valor"] = newValor

                    index["total"] = newValor*newCont



                    totalProdutos += index["total"]



                    print("produto atualizado")

                    break



            else:

                print("produto não encontrado no sistema")



        case 4:

            RemoveByName = input("Digite o numero do produto que você deseja remover: ").strip().upper()



            for index in listaProdutos:

                if index["produto"] == RemoveByName:

                    listaProdutos.remove(index)

                    print("produto removido")

                    break

            else:

                print("Produto não encontrado")



        case 5:

            break



        case _:

            print("valor não definido")
