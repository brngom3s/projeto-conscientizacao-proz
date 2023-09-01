import tkinter  # importando tKinter
from tkinter import *  # importando tudo que está dentro da biblioteca
from tkinter import ttk  # Importando a classe
from functools import partial
#import funcoes
# cores =========================================================
fundo_da_tela = "#87CEFA"  # cor hexadecimal
cor_quadro = "#00CED1"
escrito = "black"
cor_menu = "black"
arm_respostas = []
# janela mãe =============================================================
janela = Tk()
janela.title("Quiz da concientização")
janela.geometry("900x500+100+100")
janela.configure(bg=fundo_da_tela)
# import funcoes=======================================================


def acao_menu(botao):
    if (botao == botao1):
        menu["text"] = "certo"
        p1()
    else:
        encerramento = Label(
            janela, text="Programa encerrado, agradecemos a sua atenção ")
        encerramento.pack()


def p1():
    # limpando a tela
    botao1.destroy()  # funciona
    botao2.destroy()
    menu.destroy()
    menu_quadro.destroy()
    # pergunta 1 ================================================================================
    pergunta1 = LabelFrame(janela, text='''PRIMEIRA PERGUNTA
  Como podemos agir para manter o banheiro mais organizado?  
            ''',
                           font="arial 30 bold", background=fundo_da_tela, foreground=escrito)
    pergunta1.place(x=100, y=200)

    def resp(op):
        if (op == op1):
            a = Label(pergunta1, text="""Não é ético limpar os cabelos na pia
                antes de molhar todo o banheiro, devemos pensar nas próximas pessoas que usarão. 
                Molhar as mãos e não enxugar corretamente pode pingar no chão assim deixando o mesmo 
                sujo e bagunçado!""", font="arial 20", background=fundo_da_tela, foreground=escrito)
            arm_respostas.append(
                "1. A) Molhar os cabelos na pia e lavar as mãos sem enxugar corretamente!")
            a.pack()
        elif (op == op2):
            b = Label(pergunta1, text="""Parabéns, temos papéis-toalha disponíveis para uso geral, e também, 
                depois de nós outras pessoas vão utilizar o banheiro,
                logo, devemos pensar no próximo e em nós mesmos, mantendo a ordem do lugar público""", font="arial 14", background=fundo_da_tela, foreground=escrito)
            arm_respostas.append(
                "1. b)Enxugar as mãos corretamente tomando cuidado para não molhar todo o chão!")
            b.pack()
        else:
            pergunta1.destroy()
            p2()
    # opção 1
    op1 = Button(pergunta1, text='''A) Molhar os cabelos na pia e lavar as mãos sem enxugar corretamente!''',
                 font="arial 20", background=fundo_da_tela, foreground=escrito)
    op1["command"] = partial(resp, op1)
    op1.pack(pady=30)
    # op 2
    op2 = Button(pergunta1, text="[B] - Enxugar as mãos corretamente tomando cuidado para não molhar todo o chão!",
                 font="arial 20", background=fundo_da_tela, foreground=escrito)
    op2["command"] = partial(resp, op2)
    op2.pack()
    px = Button(pergunta1, text="Proxima pergunta -> ",
                font="arial 15", background=fundo_da_tela, foreground=escrito)
    px["command"] = partial(resp, px)
    px.pack(pady=80, anchor=SE, expand=True)
# pergunta 2===========================================


def p2():
    pergunta2 = LabelFrame(janela, text="Segunda Pergunta: Como podemos agir para conseguir conscientizar nossos colegas?",
                           font="arial 14", background=fundo_da_tela, foreground=escrito)
    pergunta2.pack()

    def resp(op):
        if (op == op1):
            a = Label(pergunta2, text="""Parabéns, todas mudanças começam por nós mesmos,
                 precisamos agir como inspiração para que todos à nossa volta melhorem conosco""", font="arial 14", background=fundo_da_tela, foreground=escrito)
            arm_respostas.append(
                "[A] - Aconselhar seus colegas através de exemplos e atitudes!")
            a.pack()
        elif (op == op2):
            b = Label(pergunta2, text="""Essa não é a melhor opção , não devemos repreender alguém sem ensinar o correto.
                é importante que as mudanças partam de nós mesmos, para que podemos colaborar 
                com a mudança dos outros à nossa volta!""", font="arial 14", background=fundo_da_tela, foreground=escrito)
            arm_respostas.append(
                "[B] - Repreender seus colegas e não fazer sua parte!")
            b.pack()
        else:
            pergunta2.destroy()
            p3()
    # opção 1
    op1 = Button(pergunta2, text="[A] - Aconselhar seus colegas através de exemplos e atitudes!",
                 font="arial 16", background=fundo_da_tela, foreground=escrito)
    op1["command"] = partial(resp, op1)
    op1.pack()
    # op 2
    op2 = Button(pergunta2, text="[B] - Repreender seus colegas e não fazer sua parte!",
                 font="arial 16", background=fundo_da_tela, foreground=escrito)
    op2["command"] = partial(resp, op2)
    op2.pack()
    px = Button(pergunta2, text="Proxima pergunta -> ",
                font="arial 16", background=fundo_da_tela, foreground=escrito)
    px["command"] = partial(resp, px)
    px.pack()
# pergunta 3 =========================================================


def p3():
    pergunta3 = LabelFrame(janela, text="Terceira Pergunta: Para promover um melhor clima entre os usuários do banheiro devemos:",
                           font="arial 14", background=fundo_da_tela, foreground=escrito)
    pergunta3.pack()

    def resp(op):
        if (op == op1):
            a = Label(pergunta3, text="""Isso aí, seguindo regras comuns em um ambiente é o princípio principal 
                de um bom convívio, precisamos de empatia para orientar e 
                disciplina para sermos exemplos.""", font="arial 14", background=fundo_da_tela, foreground=escrito)
            arm_respostas.append("1. [A] - Ter empatia e código de conduta!")
            a.pack()
        elif (op == op2):
            b = Label(pergunta3, text="""Seja o banheiro, ou outras áreas da escola,
                são de uso coletivo, e ser egoísta não resolve os problemas de forma geral.
                o correto é conscientizar seus colegas!
                Ser organizado é de extrema importância para gerar um clima 
                melhor entre os bens comuns da escola!""", font="arial 14", background=fundo_da_tela, foreground=escrito)
            arm_respostas.append(
                "1. [B] - Ser egoísta e e não ser organizado!")
            b.pack()
        else:
            pergunta3.destroy()
            p4()
    # opção 1
    op1 = Button(pergunta3, text="[A] - Ter empatia e código de conduta!",
                 font="arial 16", background=fundo_da_tela, foreground=escrito)
    op1["command"] = partial(resp, op1)
    op1.pack()
    # op 2
    op2 = Button(pergunta3, text="[B] - Ser egoísta e e não ser organizado!",
                 font="arial 16", background=fundo_da_tela, foreground=escrito)
    op2["command"] = partial(resp, op2)
    op2.pack()
    px = Button(pergunta3, text="Proxima pergunta -> ",
                font="arial 16", background=fundo_da_tela, foreground=escrito)
    px["command"] = partial(resp, px)
    px.pack()
# quarta pergunta ==============================================================


def p4():
    pergunta4 = LabelFrame(janela, text="Quarta Pergunta: Em sala de aula, o professor liga o ar condicionado e os alunos se encontram em divergencia sobre qual temperatura usar. Como você lidaria com essa situação?:",
                           font="arial 14", background=fundo_da_tela, foreground=escrito)
    pergunta4.pack()

    def resp(op):
        if (op == op1):
            a = Label(pergunta4, text="""Parabéns, essa atitude mostra que você é uma pessoa raciconal e empatica, vamos falar sobre os meios de resolver esse problema?""",
                      font="arial 14", background=fundo_da_tela, foreground=escrito)
            arm_respostas.append(
                "1. [A] - Encontrar, de uma maneira adequada, um consenso para que todos se encontrem em um ambiente agradável.")
            a.pack()
        elif (op == op2):
            b = Label(pergunta4, text="""Hmmmm, talvez essa não seja a melhor opção! Vamos rever isso? Se preocupar somente com você é uma atitude egoísta""",
                      font="arial 14", background=fundo_da_tela, foreground=escrito)
            arm_respostas.append(
                "1.[B] - Se preocupar somente em resolver o seu problema, de uma maneira em que você se encontre mais confortável")
            b.pack()
        else:
            pergunta4.destroy()
            p5()
    # opção 1
    op1 = Button(pergunta4, text="[A] - Encontrar, de uma maneira adequada, um consenso para que todos se encontrem em um ambiente agradável.",
                 font="arial 16", background=fundo_da_tela, foreground=escrito)
    op1["command"] = partial(resp, op1)
    op1.pack()
    # op 2
    op2 = Button(pergunta4, text="[B] - Se preocupar somente em resolver o seu problema, de uma maneira em que você se encontre mais confortável",
                 font="arial 16", background=fundo_da_tela, foreground=escrito)
    op2["command"] = partial(resp, op2)
    op2.pack()
    px = Button(pergunta4, text="Proxima pergunta -> ",
                font="arial 16", background=fundo_da_tela, foreground=escrito)
    px["command"] = partial(resp, px)
    px.pack()
# pergunta 5 ======================================


def p5():
    pergunta5 = LabelFrame(janela, text="Quinta Pergunta: Em uma instituição de estudo, na qual você encontre uma sala organizada e se mantenha nela durante o horario de aula, qual é a maneira mais adequada de deixar a mesma no final?",
                           font="arial 14", background=fundo_da_tela, foreground=escrito)
    pergunta5.pack()

    def resp(op):
        if (op == op1):
            a = Label(pergunta5, text="""Essa é uma atitude correta, assim você facilita a vida do proximo e também dos auxliares de limpeza.""",
                      font="arial 14", background=fundo_da_tela, foreground=escrito)
            arm_respostas.append(
                "1. [A] - Junte seus materiais, confira se tudo esta organizado mantendo a sala adequada para a proxima aula")
            a.pack()
        elif (op == op2):
            b = Label(pergunta5, text="""Hmmm, mais uma vez uma atitude egoísta. Você tem certeza que essa é a melhor escolha? vamos falar sobre...  !""",
                      font="arial 14", background=fundo_da_tela, foreground=escrito)
            arm_respostas.append("[B] - Apenas saia.")
            b.pack()
        else:
            pergunta5.destroy()
            p6()
    # opção 1
    op1 = Button(pergunta5, text="[A] - Junte seus materiais, confira se tudo esta organizado mantendo a sala adequada para a proxima aula",
                 font="arial 16", background=fundo_da_tela, foreground=escrito)
    op1["command"] = partial(resp, op1)
    op1.pack()
    # op 2
    op2 = Button(pergunta5, text="[B] - Apenas saia.",
                 font="arial 16", background=fundo_da_tela, foreground=escrito)
    op2["command"] = partial(resp, op2)
    op2.pack()
    px = Button(pergunta5, text="Proxima pergunta -> ",
                font="arial 16", background=fundo_da_tela, foreground=escrito)
    px["command"] = partial(resp, px)
    px.pack()
# pergunta 6 ===============================================


def p6():
    pergunta = LabelFrame(janela, text="Sexta Pergunta: Em uma situação em que você perceba que seus colegas de classe estão colaborando para deixar a sua instituição de estudo desorganizada, o que você faria a respeito?",
                          font="arial 14", background=fundo_da_tela, foreground=escrito)
    pergunta.pack()

    def resp(op):
        if (op == op1):
            a = Label(pergunta, text="""Essa é uma atitude legal, com o seu comportamento você pode ajudar o outro a ser melhor.""",
                      font="arial 14", background=fundo_da_tela, foreground=escrito)
            arm_respostas.append(
                "[A] - Conversaria com a pessoa, e daria exemplos para tentar auxiliar na melhoria dela como aluno, influenciando a ser uma pessoa mais educacada e organizada.")
            a.pack()
        elif (op == op2):
            b = Label(pergunta, text="""Você tem certeza? fazer a sua parte com toda certeza é válido, mas talvez so isso não seja o suficiente...Vamos conversar?""",
                      font="arial 14", background=fundo_da_tela, foreground=escrito)
            arm_respostas.append(
                "[B] - Me preocuparia apenas em fazer a sua parte. ")
            b.pack()
        else:
            pergunta.destroy()
            p7()
    # opção 1
    op1 = Button(pergunta, text="[A] - Conversaria com a pessoa, e daria exemplos para tentar auxiliar na melhoria dela como aluno, influenciando a ser uma pessoa mais educacada e organizada.",
                 font="arial 16", background=fundo_da_tela, foreground=escrito)
    op1["command"] = partial(resp, op1)
    op1.pack()
    # op 2
    op2 = Button(pergunta, text="[B] - Me preocuparia apenas em fazer a sua parte.",
                 font="arial 16", background=fundo_da_tela, foreground=escrito)
    op2["command"] = partial(resp, op2)
    op2.pack()
    px = Button(pergunta, text="Proxima Pergunta", font="arial 16",
                background=fundo_da_tela, foreground=escrito)
    px["command"] = partial(resp, px)
    px.pack()
# Pergunta 7


def p7():
    pergunta3 = LabelFrame(janela, text="Sétima Pergunta: Você e seu colega de sala estão almoçando juntos e seu colega suja toda a mesa e sai sem limpar. Você:",
                           font="arial 14", background=fundo_da_tela, foreground=escrito)
    pergunta3.pack()

    def resp(op):
        if (op == op1):
            a = Label(pergunta3, text="""Se você limpar sozinho, seu colega não vai entender que mais pessoas vão usar aquela mesa e não vai se colocar no lugar do próximo.""",
                      font="arial 14", background=fundo_da_tela, foreground=escrito)
            arm_respostas.append("[A] - Limpa sozinho")
            a.pack()
        elif (op == op2):
            b = Label(pergunta3, text=""" Chamando ele e explicando a situação, ele vai entender a situação e entender que que se outra pessoa fizesse o mesmo, ele teria que comer na mesa suja, oque não é nada legal """,
                      font="arial 14", background=fundo_da_tela, foreground=escrito)
            arm_respostas.append(
                "[B] - Chama ele e explica que mais pessoas vão usar aquela mesa além dele e ajuda-o a limpar")
            b.pack()
        else:
            pergunta3.destroy()
            p8()
    # opção 1
    op1 = Button(pergunta3, text="[A] - Limpa sozinho.",
                 font="arial 16", background=fundo_da_tela, foreground=escrito)
    op1["command"] = partial(resp, op1)
    op1.pack()
    # op 2
    op2 = Button(pergunta3, text="[B] - Chama ele e explica que mais pessoas vão usar aquela mesa além dele e ajuda-o a limpar.",
                 font="arial 16", background=fundo_da_tela, foreground=escrito)
    op2["command"] = partial(resp, op2)
    op2.pack()
    px = Button(pergunta3, text="Proxima pergunta", font="arial 16",
                background=fundo_da_tela, foreground=escrito)
    px["command"] = partial(resp, px)
    px.pack()
# Pergunta 8 ================================================


def p8():
    pergunta = LabelFrame(janela, text="Oitava Pergunta: Como devemos agir diante de uma situação onde alguém pega o seu lanche que estava na geladeira?",
                          font="arial 14", background=fundo_da_tela, foreground=escrito)
    pergunta.pack()

    def resp(op):
        if (op == op1):
            a = Label(pergunta, text="""Brigar com a pessoa, e levá-lo à diretoria só irá piorar a situação e causar uma situação desconfortável para ambos, às vezes ele mesmo cometeu algum engano, então vamos coversar primeiro, pois tudo conversado é entendido""",
                      font="arial 14", background=fundo_da_tela, foreground=escrito)
            arm_respostas.append(
                "[A] - Briga com a pessoa, leva a situação até a direção e abre uma denúncia.")
            a.pack()
        elif (op == op2):
            b = Label(pergunta, text="""Isso mesmo, tudo conversado é entendido, às vezes pode ter acontecido algum engano, ou algo do gênero, conversar evita que a situação piore, e ajuda a solucionar educadamente o problema""",
                      font="arial 14", background=fundo_da_tela, foreground=escrito)
            arm_respostas.append(
                "[B] - Conversa com o colega, explica a situação e pede para que não faça novamente.")
            b.pack()
        else:
            pergunta.destroy()
            p9()
    # opção 1
    op1 = Button(pergunta, text="[A] - Briga com a pessoa, leva a situação até a direção e abre uma denúncia",
                 font="arial 16", background=fundo_da_tela, foreground=escrito)
    op1["command"] = partial(resp, op1)
    op1.pack()
    # op 2
    op2 = Button(pergunta, text="[B] - Conversa com o colega, explica a situação e pede para que não faça novamente",
                 font="arial 16", background=fundo_da_tela, foreground=escrito)
    op2["command"] = partial(resp, op2)
    op2.pack()
    px = Button(pergunta, text="Proxima Pergunta", font="arial 16",
                background=fundo_da_tela, foreground=escrito)
    px["command"] = partial(resp, px)
    px.pack()
# pergunta 9


def p9():
    pergunta = LabelFrame(janela, text="Nona Pergunta: Você está esquentando seu almoço no microondas e sem querer acaba sujando o mesmo. Você:",
                          font="arial 14", background=fundo_da_tela, foreground=escrito)
    pergunta.pack()

    def resp(op):
        if (op == op1):
            a = Label(pergunta, text="""Depois de usarmos o microondas, outras pessoas também usarão, então se coloque o no lugar dele e pense se gostaria de utilizar o aparelho todo sujo de comida.""",
                      font="arial 14", background=fundo_da_tela, foreground=escrito)
            arm_respostas.append("[A] - Finge que nada aconteceu e sai.")
            a.pack()
        elif (op == op2):
            b = Label(pergunta, text="""Isso mesmo, tudo conversado é entendido, às vezes pode ter acontecido algum engano, ou algo do gênero, conversar evita que a situação piore, e ajuda a solucionar educadamente o problema""",
                      font="arial 14", background=fundo_da_tela, foreground=escrito)
            arm_respostas.append(
                "Isso aí, do mesmo jeito que você gostaria de utilizar o microondas limpo, o próximo colega que utilizará depois de você gostaria também, assim deixamos o ambiente limpo, e mantemos os aparelhos higienizados")
            b.pack()
        else:
            pergunta.destroy()
            hist()
    # opção 1
    op1 = Button(pergunta, text="[A] - Finge que nada aconteceu e sai.",
                 font="arial 16", background=fundo_da_tela, foreground=escrito)
    op1["command"] = partial(resp, op1)
    op1.pack()
    # op 2
    op2 = Button(pergunta, text="[B] - Você retira e lava o prato do microondas, e também limpa o aparelho",
                 font="arial 16", background=fundo_da_tela, foreground=escrito)
    op2["command"] = partial(resp, op2)
    op2.pack()
    px = Button(pergunta, text="Proxima Pergunta", font="arial 16",
                background=fundo_da_tela, foreground=escrito)
    px["command"] = partial(resp, px)
    px.pack()
# resultados ============================================================


def hist():
    result = LabelFrame(janela, text="Vamos mostrar o seu hitórico de respostas: ",
                        font="arial 16", background=fundo_da_tela, foreground=escrito)
    result.pack()
    cont = 1
    for i in arm_respostas:
        mostrar = Label(
            result, text=f"Pergunta {cont}: {i}", font="arial 16", background=fundo_da_tela, foreground=escrito)
        mostrar.pack()
        cont += 1


# menu============================================
quadro1 = PanedWindow(janela, width=480, height=100,
                      relief="raised", bg=cor_quadro)  # primeiro final janela
quadro1.pack(fill=BOTH, expand=0)
titulo_quadro1 = Label(quadro1, text="QUIZ DA CONCIENTIZAÇÃO",
                       background=cor_quadro, foreground='white', font="Arial  20")
# o método pack interliga um widget pai em um filho para exibir, dentro dos parenteses você pode formatar
titulo_quadro1.pack()
apresentacao_quadro = PanedWindow(
    janela, bg=fundo_da_tela, width=200, height=400)
apresentacao_quadro.pack(padx=20, pady=20, ipadx=20, ipady=20)
apresentacao = Label(apresentacao_quadro, text='''           OLÁ, SEJAM BEM VINDOS À NOSSA CAMPANHA DE CONSCIENTIZAÇÃO 
            DESENVOLVIMENTO DE SISTEMAS - PERÍODO MANHÃ''',
                     font="Times 25", background=fundo_da_tela, foreground="black")
apresentacao.grid(row=10, column=10)

menu_quadro = Frame(janela, background=fundo_da_tela)
menu_quadro.pack(fill=BOTH)
menu = LabelFrame(menu_quadro, text="              Menu:                ", font="Times 40", fg=escrito,
                  background=fundo_da_tela, bd=3, labelanchor=N, highlightcolor="purple", width=50, height=500)
menu.pack(anchor=CENTER, expand=True)
botao1 = Button(menu, text="Iniciar quiz", font="arial 25",
                background=fundo_da_tela, foreground=escrito)
botao1["command"] = partial(acao_menu, botao1)
botao1.pack(padx=10, pady=10)
botao2 = Button(menu, text="Sair", font="arial 25",
                background=fundo_da_tela, foreground=escrito)
botao2["command"] = partial(acao_menu, botao2)
botao2.pack(padx=10, pady=10)


janela.mainloop()
