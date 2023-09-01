class printer():
    _colors_ = {
        **dict.fromkeys(("RED", "ERROR", "NO"), "\033[1;31m"),
        **dict.fromkeys(("GREEN", "OK", "YES"), "\033[0;32m"),
        **dict.fromkeys(("YELLOW", "WARN", "MAYBE"), "\033[0;93m"),
        "BLUE": "\033[1;34m",
        "CYAN": "\033[1;36m",
        "RESET": "\033[0;0m",
        "BOLD": "\033[;1m",
        "REVERSE": "\033[;7m"
    }


def menu():
    print(
        '''\033[36m                         [1] INICIAR QUIZ                                [2] FINALIZAR QUIZ\033[0;0m''')


def menu2():
    print(
        '''\033[36m                         [1] CONTINUAR COM O QUIZ                                [2] FINALIZAR QUIZ\033[0;0m''')
    print()


rodada = 0
opcao = 0


print('''\033[36m┌──────────────────────────────────────────────────────── •✧✧• ───────────────────────────────────────────────────────┐
                            -OLÁ, SEJAM BEM VINDOS À NOSSA CAMPANHA DE CONSCIENTIZAÇÃO-
└──────────────────────────────────────────────────────── •✧✧• ───────────────────────────────────────────────────────┘\033[0;0m''')
print()
print('''\033[36m                                                         MENU                                            
                            »»──────────────────────────　★　──────────────────────────««\033[0;0m''')

print()
print(
    '''\033[36m                         [1] INICIAR QUIZ                                [2] FINALIZAR QUIZ\033[0;0m''')


rodada = 0
opcao = 0

while opcao != 2:
    if rodada == 0:
        print()
        opcao = int(
            input("\033[36m                                               SELECIONE UMA OPÇÃO: \033[0;0m"))
        print()
    else:
        if rodada >= 1:
            print()
            menu2()
            print()
            opcao = int(
                input("\033[36m                                               SELECIONE UMA OPÇÃO: \033[0;0m"))
            print()

        # Pergunta 1
    if opcao == 1:
        if rodada == 0:
            print()
            print(
                "\033[33m Primeira Pergunta: Como podemos agir para manter o banheiro mais organizado? \033[0;0m")
            print()
            print()
            print()
            print(
                "[A] - Molhar os cabelos na pia e lavar as mãos sem enxugar corretamente!")
            print()
            print(
                "[B] - Enxugar as mãos corretamente tomando cuidado para não molhar todo o chão!")
            print()
            quest1 = input("\033[36m Digite sua resposta: \033[0;0m")
            print()
            if quest1 == "A" or quest1 == "a":
                print(
                    "\033[31m Não é ético limpar os cabelos na pia,antes de molhar todo o banheiro, devemos pensar nas próximas pessoas que usarão.\033[0;0m")
                print(
                    "\033[31m Molhar as mãos e não enxugar corretamente pode pingar no chão assim deixando o mesmo sujo e bagunçado!\033[0;0m")
                print()
                rodada += 1
            elif quest1 == "B" or quest1 == "b":
                print('''\033[32m Parabéns, temos papéis-toalha disponíveis para uso geral, e também, depois de nós outras pessoas vão utilizar o banheiro,
logo, devemos pensar no próximo e em nós mesmos, mantendo a ordem do lugar público.  \033[0;0m''')
                print()
                rodada += 1

        # Pergunta 2
        elif rodada == 1:
            print(
                "\033[33m Segunda Pergunta: Como podemos agir para conseguir conscientizar nossos colegas? \033[0;0m")
            print()
            print()
            print()
            print(
                "[A] - Aconselhar seus colegas através de exemplos e atitudes!")
            print()
            print(
                "[B] - Repreender seus colegas e não fazer sua parte!")
            print()
            quest2 = input("\033[36m Digite sua resposta: \033[0;0m")
            print()
            if quest2 == "A" or quest2 == "a":
                print("\033[32m Parabéns, todas mudanças começam por nós mesmos, precisamos agir como inspiração para que todos à nossa volta melhorem conosco. \033[0;0m")
                print()
                rodada += 1
            elif quest2 == "B" or quest2 == "b":
                print(
                    "\033[31m Essa não é a melhor opção , não devemos repreender alguém sem ensinar o correto \033[0;0m")
                print("\033[31m  é importante que as mudanças partam de nós mesmos, para que podemos colaborar com a mudança dos outros à nossa volta! \033[0;0m")
                print()
                rodada += 1

        # Pergunta 3
        elif rodada == 2:
            print(
                "\033[33m Terceira Pergunta: Para promover um melhor clima entre os usuários do banheiro devemos: \033[0;0m")
            print()
            print()
            print()
            print("[A] - Ter empatia e código de conduta!")
            print()
            print("[B] - Ser egoísta e e não ser organizado!")
            print()
            quest3 = input("\033[36m Digite sua resposta: \033[0;0m")
            print()
            if quest3 == "A" or quest3 == "a":
                print("\033[32m Isso aí, seguindo regras comuns em um ambiente é o princípio principal de um bom convívio, precisamos de empatia para orientar e disciplina para sermos exemplos.  \033[0;0m")
                print()
                rodada += 1
            elif quest3 == "B" or quest3 == "b":
                print("\033[31m Seja o banheiro, ou outras áreas da escola,são de uso coletivo, e ser egoísta não resolve os problemas de forma geral. \033[0;0m")
                print(
                    "\033[31m o correto é conscientizar seus colegas! \033[0;0m")
                print(
                    "\033[31m Ser organizado é de extrema importância para gerar um clima melhor entre os bens comuns da escola! \033[0;0m")
                print()
                rodada += 1

            # Pergunta 4
        elif rodada == 3:
            print("\033[33m Quarta Pergunta: Em sala de aula, o professor liga o ar condicionado e os alunos se encontram em divergencia sobre qual temperatura usar. Como você lidaria com essa situação? \033[0;0m")
            print()
            print()
            print()
            print("[A] - Encontrar, de uma maneira adequada, um consenso para que todos se encontrem em um ambiente agradável.")
            print()
            print("[B] - Se preocupar somente em resolver o seu problema, de uma maneira em que você se encontre mais confortável.")
            print()
            quest4 = input("\033[36m Digite sua resposta: \033[0;0m")
            print()
            if quest4 == "A" or quest4 == "a":
                print("\033[32m Parabéns, essa atitude mostra que você é uma pessoa raciconal e empatica, vamos falar sobre os meios de resolver esse problema? \033[0;0m")
                print()
                rodada += 1
            elif quest4 == "B" or quest4 == "b":
                print(
                    "\033[31m Hmmmm, talvez essa não seja a melhor opção! Vamos rever isso? Se preocupar somente com você é uma atitude egoísta.  \033[0;0m")
                print()
                rodada += 1

            # Pergunta 5
        elif rodada == 4:
            print("\033[33m Quinta Pergunta: Em uma instituição de estudo, na qual você encontre uma sala organizada e se mantenha nela durante o horario de aula, qual é a maneira mais adequada de deixar a mesma no final? \033[0;0m")
            print()
            print()
            print()
            print("[A] - Junte seus materiais, confira se tudo esta organizado mantendo a sala adequada para a proxima aula.")
            print()
            print("[B] - Apenas saia.")
            print()
            quest5 = input("\033[36m Digite sua resposta: \033[0;0m")
            print()
            if quest5 == "A" or quest5 == "a":
                print(
                    "\033[32m Essa é uma atitude correta, assim você facilita a vida do proximo e também dos auxliares de limpeza. \033[0;0m")
                print()
                rodada += 1
            elif quest5 == "B" or quest5 == "b":
                print(
                    "\033[31m Hmmm, mais uma vez uma atitude egoísta. Você tem certeza que essa é a melhor escolha? vamos falar sobre...  \033[0;0m")
                print()
                rodada += 1

            # Pergunta 6
        elif rodada == 5:
            print("\033[33m Sexta Pergunta: Em uma situação em que você perceba que seus colegas de classe estão colaborando para deixar a sua instituição de estudo desorganizada, o que você faria a respeito? \033[0;0m")
            print()
            print()
            print()
            print("[A] - Conversaria com a pessoa, e daria exemplos para tentar auxiliar na melhoria dela como aluno, influenciando a ser uma pessoa mais educacada e organizada.")
            print()
            print("[B] - Me preocuparia apenas em fazer a sua parte.")
            print()
            quest6 = input("\033[36m Digite sua resposta: \033[0;0m")
            print()
            if quest6 == "A" or quest6 == "a":
                print(
                    "\033[32m Essa é uma atitude legal, com o seu comportamento você pode ajudar o outro a ser melhor. \033[0;0m")
                print()
                rodada += 1
            elif quest6 == "B" or quest6 == "b":
                print("\033[31m Você tem certeza? fazer a sua parte com toda certeza é válido, mas talvez so isso não seja o suficiente...Vamos conversar?   \033[0;0m")
                print()
                rodada += 1

            # Pergunta 7
        elif rodada == 6:
            print("\033[33m Sétima Pergunta: Você e seu colega de sala estão almoçando juntos e seu colega suja toda a mesa e sai sem limpar. Você: \033[0;0m")
            print()
            print()
            print()
            print("[A] - Limpa sozinho.")
            print()
            print(
                "[B] - Chama ele e explica que mais pessoas vão usar aquela mesa além dele e ajuda-o a limpar.")
            print()
            quest7 = input("\033[36m Digite sua resposta: \033[0;0m")
            print()
            if quest7 == "A" or quest7 == "a":
                print("\033[31m Se você limpar sozinho, seu colega não vai entender que mais pessoas vão usar aquela mesa e não vai se colocar no lugar do próximo. \033[0;0m")
                print()
                rodada += 1
            elif quest7 == "B" or quest7 == "b":
                print("\033[32m Chamando ele e explicando a situação, ele vai entender a situação e entender que que se outra pessoa fizesse o mesmo, ele teria que comer na mesa suja, oque não é nada legal \033[0;0m")
                print()
                rodada += 1

            # Pergunta 8
        elif rodada == 7:
            print("\033[33m Oitava Pergunta: Como devemos agir diante de uma situação onde alguém pega o seu lanche que estava na geladeira? \033[0;0m")
            print()
            print()
            print()
            print(
                "[A] - Briga com a pessoa, leva a situação até a direção e abre uma denúncia.")
            print()
            print(
                "[B] - Conversa com o colega, explica a situação e pede para que não faça novamente.")
            print()
            quest7 = input("\033[36m Digite sua resposta: \033[0;0m")
            print()
            if quest7 == "A" or quest7 == "a":
                print("\033[31m Brigar com a pessoa, e levá-lo à diretoria só irá piorar a situação e causar uma situação desconfortável para ambos, às vezes ele mesmo cometeu algum engano, então vamos coversar primeiro, pois tudo conversado é entendido. \033[0;0m")
                print()
                rodada += 1
            elif quest7 == "B" or quest7 == "b":
                print("\033[32m Isso mesmo, tudo conversado é entendido, às vezes pode ter acontecido algum engano, ou algo do gênero, conversar evita que a situação piore, e ajuda a solucionar educadamente o problema. \033[0;0m")
                print()
                rodada += 1

            # Pergunta 9
        elif rodada == 8:
            print("\033[33m Nona Pergunta: Você está esquentando seu almoço no microondas e sem querer acaba sujando o mesmo. Você: \033[0;0m")
            print()
            print()
            print()
            print("[A] - Finge que nada aconteceu e sai.")
            print()
            print(
                "[B] - Você retira e lava o prato do microondas, e também limpa o aparelho.")
            print()
            quest7 = input("\033[36m Digite sua resposta: \033[0;0m")
            print()
            if quest7 == "A" or quest7 == "a":
                print("\033[31m Depois de usarmos o microondas, outras pessoas também usarão, então se coloque o no lugar dele e pense se gostaria de utilizar o aparelho todo sujo de comida.  \033[0;0m")
                print()
                rodada += 1
            elif quest7 == "B" or quest7 == "b":
                print("\033[32m Isso aí, do mesmo jeito que você gostaria de utilizar o microondas limpo, o próximo colega que utilizará depois de você gostaria também, assim deixamos o ambiente limpo, e mantemos os aparelhos higienizados  \033[0;0m")
                print()
                rodada += 1

            # Última Rodada
        elif rodada == 9:
            print()
            print()
            print("\033[36m    ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊  ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ \033[0;0m")
            print("\033[36m    ┊ ┊ ┊ ┊                                                                                                    ┊ ┊ ┊ ┊ \033[0;0m")
            print("\033[36m    ┊ ┊ ┊ ┊                     PARABÉNS, TERMINAMOS AQUI NOSSO QUIZ CONSCIENTIZANTE,                          ┊ ┊ ┊ ┊")
            print('''\033[36m    ┊ ┊ ┊ ┊    CONTAMOS COM TODOS VOCÊS PARA QUE JUNTOS POSSAMOS CRIAR UM AMBIENTE MAIS AMIGÁVEL E HIGIÊNICO,  ┊ ┊ ┊ ┊
    ★ ┊ ┊ ┊           E ASSIM DEIXAR NOSSO LEGADO COMO AS PRIMEIRAS TURMAS DA ESCOLA PROZ EDUCAÇÃO!!           ┊ ┊ ┊ ✯
      ★ ┊ ┊                                                                                                    ┊ ┊ ★
        ★ ┊                                                                                                    ┊ ✯
          ★                                                                                                    ★ \033[0;0m''')

            break

        # Finalização
    elif opcao != 1 and opcao != 2:
        print("\033[35m Digite uma opcao válida! \033[0;0m")
    else:
        if opcao == 2:
            print(
                "\033[31m                       PROGRAMA FINALIZADO! ESPERAMOS TER CONTRIBUÍDO PARA SUA AUTO-EVOLUÇÃO, VOLTE SEMPRE!  \033[0;0m")
            print()
            break
