import tkinter
from tkinter import *
from tkinter import ttk

co0 = "#FFFFFF"
co1 = "#333333"
co2 = "#fcc058"
co3 = "#38576b"
co4 = "#3297a8"
co5 = "#fff873"
co6 = "#fcc058"
co7 = "#e85151"
co8 = co4
co10 = "#fcfbf7"
fundo = "#3b3b3b"

janela = Tk()
janela.title('')
janela.geometry('260x370')
janela.configure(bg=fundo)

#Criando lógica

jogador_1 = 'X'
jogador_2 = 'O'

score_1 = 0
score_2 = 0

table = [['1', '2', '3'], ['4', '5','6'], ['7', '8', '9']]

jogando = 'X'
joga = ''
contador = 0
cor=co8
contador_de_rodada = 0

# Criando frames #

frame_top = Frame(janela, width=240, height=100, bg=co1, relief="raised")
frame_top.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_bottom = Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_bottom.grid(row=1, column=0, sticky=NW)

# Configurando o frame TOP #

app_x = Label(frame_top, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7)
app_x.place(x=25, y=10)
app_x = Label(frame_top, text='Jogador 1', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_x.place(x=17, y=70)
app_x_pontos = Label(frame_top, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_x_pontos.place(x=80, y=20)

app_separator = Label(frame_top, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_separator.place(x=110, y=20)

app_0 = Label(frame_top, text=score_1, height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4)
app_0.place(x=170, y=10)
app_0 = Label(frame_top, text='Jogador 2', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_0.place(x=165, y=70)
app_0_pontos = Label(frame_top, text=score_2, height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_0_pontos.place(x=130, y=20)





def start_game():
     btn_jogar.place(x=800, y=350)

     def handleGame(i):
         global jogando
         global contador
         global jogar
         global cor

         if i==str(1):

             if bot0['text'] == '':

                 if jogando =='X':
                     cor=co7
                 if jogando=='O':
                     cor=co8

                 bot0['fg'] = cor
                 bot0['text'] = jogando
                 table[0][0] = jogando

                 if jogando =='X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                 else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                 contador+=1

         if i==str(2):

             if bot1['text'] == '':

                 if jogando == 'X':
                     cor=co7
                 if jogando == 'O':
                     cor=co8

                 bot1['fg'] = cor
                 bot1['text'] = jogando
                 table[0][1] = jogando

                 if jogando =='X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                 else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                 contador+=1

         if i==str(3):

             if bot2['text'] == '':

                 if jogando == 'X':
                     cor=co7
                 if jogando == 'O':
                     cor=co8

                 bot2['fg'] = cor
                 bot2['text'] = jogando
                 table[0][2] = jogando

                 if jogando =='X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                 else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                 contador+=1

         if i==str(4):

             if b0['text'] == '':

                 if jogando == 'X':
                     cor=co7
                 if jogando == 'O':
                     cor=co8

                 b0['fg'] = cor
                 b0['text'] = jogando
                 table[1][0] = jogando

                 if jogando =='X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                 else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                 contador+=1

         if i==str(5):

             if b1['text'] == '':

                 if jogando == 'X':
                     cor=co7
                 if jogando == 'O':
                     cor=co8

                 b1['fg'] = cor
                 b1['text'] = jogando
                 table[1][1] = jogando

                 if jogando =='X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                 else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                 contador+=1

         if i==str(6):

             if b2['text'] == '':

                 if jogando == 'X':
                     cor=co7
                 if jogando == 'O':
                     cor=co8

                 b2['fg'] = cor
                 b2['text'] = jogando
                 table[1][2] = jogando

                 if jogando =='X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                 else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                 contador+=1

         if i==str(7):

             if btn0['text'] == '':

                 if jogando == 'X':
                     cor=co7
                 if jogando == 'O':
                     cor=co8

                 btn0['fg'] = cor
                 btn0['text'] = jogando
                 table[2][0] = jogando

                 if jogando =='X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                 else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                 contador+=1

         if i==str(8):

             if btn1['text'] == '':

                 if jogando == 'X':
                     cor=co7
                 if jogando == 'O':
                     cor=co8

                 btn1['fg'] = cor
                 btn1['text'] = jogando
                 table[2][1] = jogando

                 if jogando =='X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                 else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                 contador+=1

         if i==str(9):

             if btn2['text'] == '':

                 if jogando == 'X':
                     cor=co7
                 if jogando == 'O':
                     cor=co8

                 btn2['fg'] = cor
                 btn2['text'] = jogando
                 table[2][2] = jogando

                 if jogando =='X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                 else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                 contador+=1

         if contador >= 5:
            if str(table[0][0]) == str(table[0][1]) == str(table[0][2]) != "":
                winner(jogando)
            elif table[1][0] == table[1][1] == table[1][2] != "":
                winner(jogando)
            elif table[2][0] == table[2][1] == table[2][2] != "":
                winner(jogando)
                # Colunas
            elif table[0][0] == table[1][0] == table[2][0] != "":
                winner(jogando)
            elif table[0][1] == table[1][1] == table[2][1] != "":
                winner(jogando)
            elif table[0][2] == table[1][2] == table[2][2] != "":
                winner(jogando)
                 # Diagonais
            elif table[0][0] == table[1][1] == table[2][2] != "":
                winner(jogando)
            elif table[0][2] == table[1][1] == table[2][0] != "":
                winner(jogando)
            else:
                pass

            if contador >= 9:
                print('Score draw!')

     def winner(i):
        global table
        global score_1
        global score_2
        global contador
        global contador_de_rodada

        #Limpando a tabela
        bot0['text']=''
        bot1['text'] = ''
        bot2['text'] = ''
        b0['text'] = ''
        b1['text'] = ''
        b2['text'] = ''
        btn0['text'] = ''
        btn1['text'] = ''
        btn2['text'] = ''

        bot0['state'] = 'disable'
        bot1['state'] = 'disable'
        bot2['state'] = 'disable'
        b0['state'] = 'disable'
        b1['state'] = 'disable'
        b2['state'] = 'disable'
        btn0['state'] = 'disable'
        btn1['state'] = 'disable'
        btn2['state'] = 'disable'

        app_vencedor = Label(frame_bottom,text='' ,width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
        app_vencedor.place(x=40, y=220)

        if i == "X":
            score_2 += 1
            app_vencedor['text'] = 'Jogador 2 venceu'
            app_0_pontos['text'] = score_2
        if i == "O":
            score_1 += 1
            app_vencedor['text'] = 'Jogador 1 venceu'
            app_x_pontos['text'] = score_1
        if i == 'Score draw!':
            app_vencedor['text'] = 'Score draw!'

        def start():
            bot0['text'] = ''
            bot1['text'] = ''
            bot2['text'] = ''
            b0['text'] = ''
            b1['text'] = ''
            b2['text'] = ''
            btn0['text'] = ''
            btn1['text'] = ''
            btn2['text'] = ''

            bot0['state'] = 'normal'
            bot1['state'] = 'normal'
            bot2['state'] = 'normal'
            b0['state'] = 'normal'
            b1['state'] = 'normal'
            b2['state'] = 'normal'
            btn0['state'] = 'normal'
            btn1['state'] = 'normal'
            btn2['state'] = 'normal'



            app_vencedor.destroy()
            btn_jogar.destroy()

        btn_jogar = Button(frame_bottom, command=start, text='Proxima rodada', height=1, font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)
        btn_jogar.place(x=70, y=197)

        def game_over():
            btn_jogar.destroy()
            app_vencedor.destroy()

            terminar()

        if contador_de_rodada>=5:
            game_over()
        else:
            contador_de_rodada+=1
            table = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            contador = 0


     def terminar():
         global table
         global contador_de_rodada
         global score_2
         global score_1
         global contador

         table = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
         contador_de_rodada = 0
         score_1 = 0
         score_2 = 0

         bot0['state'] = 'disable'
         bot1['state'] = 'disable'
         bot2['state'] = 'disable'
         b0['state'] = 'disable'
         b1['state'] = 'disable'
         b2['state'] = 'disable'
         btn0['state'] = 'disable'
         btn1['state'] = 'disable'
         btn2['state'] = 'disable'

         app_game_over = Label(frame_bottom, text='Jogo acabou', width=17, relief='flat', anchor='center',font=('Ivy 8 bold'), bg=co1, fg=co2)
         app_game_over.place(x=25, y=90)

         def play_again():
             app_0_pontos['text'] = '0'
             app_x_pontos['text'] = '0'
             app_game_over.destroy()
             btn_jogar_dnv.destroy()

         btn_jogar_dnv = Button(frame_bottom, command=play_again, text='Jogar de novo', width=10, height=1, font=('Ivy 10 bold'),overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)
         btn_jogar_dnv.place(x=80, y=197)




     # Criando linhas verticais
     app_col = Label(frame_bottom, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'),bg=co0)
     app_col.place(x=90, y=15)
     app_col = Label(frame_bottom, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'),bg=co0)
     app_col.place(x=157, y=15)

     # Criando linhas horizontais

     app_row = Label(frame_bottom, text='', width=46, relief='flat', padx=2, pady=1, anchor='center',font=('Ivy 5 bold'), bg=co0)
     app_row.place(x=30, y=63)
     app_row = Label(frame_bottom, text=' ', width=46, relief='flat', padx=2, pady=1, anchor='center',font=('Ivy 5 bold'), bg=co0)
     app_row.place(x=30, y=127)

     # Linha 0

     bot0 = Button(frame_bottom, command=lambda: handleGame('1'), text='', width=3, height=1, font=('Ivy 20 bold'),overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
     bot0.place(x=30, y=15)
     bot1 = Button(frame_bottom, command=lambda: handleGame('2'), text='', width=3, height=1, font=('Ivy 20 bold'),overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
     bot1.place(x=96, y=15)
     bot2 = Button(frame_bottom, command=lambda: handleGame('3'), text='', width=3, height=1, font=('Ivy 20 bold'),overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
     bot2.place(x=163, y=15)

     # Linha 1#

     b0 = Button(frame_bottom, command=lambda: handleGame('4'), text='', width=3, height=1, font=('Ivy 20 bold'),overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
     b0.place(x=30, y=75)
     b1 = Button(frame_bottom, command=lambda: handleGame('5'), text='', width=3, height=1, font=('Ivy 20 bold'),overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
     b1.place(x=96, y=75)
     b2 = Button(frame_bottom, command=lambda: handleGame('6'), text='', width=3, height=1, font=('Ivy 20 bold'),overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
     b2.place(x=163, y=75)

     # Linha2#

     btn0 = Button(frame_bottom, command=lambda: handleGame('7'), text='', width=3, height=1, font=('Ivy 20 bold'),overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
     btn0.place(x=30, y=135)
     btn1 = Button(frame_bottom, command=lambda: handleGame('8'), text='', width=3, height=1, font=('Ivy 20 bold'),overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
     btn1.place(x=96, y=135)
     btn2 = Button(frame_bottom, command=lambda: handleGame('9'), text='', width=3, height=1, font=('Ivy 20 bold'),overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
     btn2.place(x=163, y=135)


#Botao jogar#
btn_jogar = Button(frame_bottom, command=start_game ,text='Jogar', width=10, height=1,font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)
btn_jogar.place(x=85, y=197)

janela.mainloop()