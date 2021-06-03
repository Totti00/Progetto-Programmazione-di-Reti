#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Elaborato Programmazione di Reti
            a.a. 2020/2021
            Totaro Giacomo
         Matricola: 0000915504
              Traccia 2
             Web Server
'''

import sys, signal
import http.server
import socketserver

import os
import ast

# Legge il numero della porta dalla riga di comando, e mette default 8080
if sys.argv[1:]:
  port = int(sys.argv[1])
else:
  port = 8080
  
# ThreadingTCPServer per gestire più richieste
server = socketserver.ThreadingTCPServer(('',port), http.server.SimpleHTTPRequestHandler )

# la parte iniziale è identica per tutte le varie pagine
header_html = """
<html>
    <head>
        <link rel="icon" type="image/jpg" sizes="32x32" href="../img/ausl.jpg">
        <style>
            h1 {
                text-align: center;
                margin: 0;
            }
            table {width:70%;}
            img {
                max-width:400;
                max-height:400px;
                width:auto;
            }
            td {width: 33%;}
            p {text-align:justify;}
            td {
                padding: 20px;
                text-align: center;
            }
            .topnav {
  		        overflow: hidden;
  		        background-color: #70aeff;
  		    }
            .topnav a {
  		        float: left;
  		        color: #000000;
  		        text-align: center;
  		        padding: 14px 16px;
  		        text-decoration: none;
  		        font-size: 17px;
  		    }        
  		    .topnav a:hover {
  		        background-color: #ddd;
  		        color: black;
  		    }        
  		    .topnav a.active {
  		        background-color: #064229;
  		        color: white;
  		    }
        </style>
    </head>
    <body>
        <title>Ospedale Infermi di Rimini</title>
"""
                            
# la barra di navigazione è identica per tutte le varie pagine
navigation_bar = """
        <br>
        <br>
        <br>
        <div class="topnav">
            <a class="active" href="http://127.0.0.1:{port}/">Home</a>
  		    <a href="http://127.0.0.1:{port}/htmlFile/neurologia.html">Neurologia </a>
            <a href="http://127.0.0.1:{port}/htmlFile/ginecologia.html">Ginecologia</a>
            <a href="http://127.0.0.1:{port}/htmlFile/cardiologia.html">Cardiologia</a>
            <a href="http://127.0.0.1:{port}/htmlFile/radiologia.html">Radiologia</a>
            <a href="http://127.0.0.1:{port}/htmlFile/urologia.html">Urologia</a>
            <a href="http://127.0.0.1:{port}/htmlFile/analisi.html">Analisi cliniche</a>
            <a href="http://127.0.0.1:{port}/RelazioneWebServer.pdf" download="RelazioneWebServer.pdf" style="float: right">Download info</a>
            <a href="http://127.0.0.1:{port}/htmlFile/orari.html" style="float: right">Orari Visite</a>
  		</div>
        <br><br>
""".format(port=port)

# la parte finale è identica per tutte le varie pagine
footer_html= """
    </body>
</html>
"""

#Inizializza le varie pagine del sito
def refresh():
    global header_html        
    print("updating all contents")
    create_page_neurologia()
    create_page_analisi()
    create_page_cardiologia()
    create_page_ginecologia()
    create_page_orari()
    create_page_radiologia()
    create_page_urologia()
    create_index_page()
    print("finished update")
    
#Creazione della pagina Neurologia
def create_page_neurologia():
    fill_pages("neurologia")
    
#Creazione della pagina Analisi cliniche
def create_page_analisi():
    fill_pages("analisi")

#Creazione della pagina Cardiologia
def create_page_cardiologia():
    fill_pages("cardiologia")
    
#Creazione della pagina Ginecologia
def create_page_ginecologia():
    fill_pages("ginecologia")
    
#Creazione della pagina Orari
def create_page_orari():
    fill_pages("orari")

#Creazione della pagina Radiologia
def create_page_radiologia():
    fill_pages("radiologia")
    
#Creazione della pagina Urologia
def create_page_urologia():
    fill_pages("urologia")
    

    
#metodo che riempie le varie pagine prendendo le info dai rispettivi .txt
def fill_pages(namePage):
    message = header_html + "<h1>Ospedale Infermi di Rimini</h1>" + navigation_bar
    f = open('./htmlFile/'+namePage+'.html','w', encoding="utf-8")
    try:
        fpage = open('./RepartiTxt/'+namePage+'.txt', 'r', encoding="utf-8")
        for line in fpage:
            message = message + line

        message = message + footer_html
    except:
        pass
    f.write(message)
    f.close()
    

# metodo che riempie la tabella della pagina index
def fill_table_index(message):
    link_map = "https://www.google.com/maps?ll=44.04783,12.58932&z=13&t=m&hl=it&gl=US&mapclient=embed&q=44%C2%B002%2752.2%22N+12%C2%B035%2721.6%22E+44.047830,+12.589320@44.04783,12.58932"
    title_map = "Visualizza mappa piu' grande"
    url_image_map = "./img/mappa.jpg"
    
    link_h = "https://it.wikipedia.org/wiki/Ospedale_Infermi_di_Rimini"
    title_h = "Un po' di storia... nato nel 1974."
    url_image_h = "./img/aerea.jpg"
    
    message = message + "<tr>"
    message = message + '<td><a href="' + link_map + '"><img src="' + url_image_map + '"><br><p>'+ title_map + '</p></a></td><td></td>'
    message = message + '<td><a href="' + link_h + '"><img src="' + url_image_h + '"><br><p>'+ title_h + '</p></a></td>'
    message = message + "</tr>"
    return message
    
    
# creazione della pagina index.html
def create_index_page():
    message = header_html + "<h1>Ospedale Infermi di Rimini</h1>" + navigation_bar
    
    f = open('index.html','w', encoding="utf-8")
    try:
        message = message + """<table align="center">"""
        message = message + """<tr><th colspan="4"><h2>Dove si trova ? Quando e' stato costruito ?</h2></th></tr>"""
        message = fill_table_index(message)
        message = message + "</table>"
        message = message + footer_html
    except:
        pass
    f.write(message)
    f.close()

#Se il file delle credenziali non esiste, lo inizializzo con due account, se no ritorna il file
def initCredentials(filePath):
    if not os.path.exists(filePath):
        startingAccounts = {'admin' : 'admin', 'giacomo' : 'totaro'}
        writeCredentialsOnFile(startingAccounts, filePath)
    credentials = getCredentials_from_file(filePath)
    return credentials
    
#Metodo che scrive le credenziali sul file, sia quelle di base (se il file non esiste) sia per i nuovi utenti.
def writeCredentialsOnFile(credentials, credentialsFile):
    with open(credentialsFile,'w') as file:
        file.write(str(credentials))
#Metodo cuore del login, controlla se l'utente esiste o no. Se non esiste, chiede se si vuole registrare.
def authentication(credenziali):
    time = 0
    dentro=0
    while time < 4 and dentro == 0:                                     #Max 4 volte può sbagliare
        username = input("[+] Enter the username : ")
        password = input("[+] Enter the password : ")
        if (username in credenziali.keys() and credenziali[username] == password):
            print("[+] Authentication Completed !\n")
            dentro=1
        else:
            print("[-] Authentication Failed for user : {} \n".format(username))
            time = time + 1
            
    #chiedo all'utente, se ancora non ha passato il login, se si vuole registrare
    if time==4:
        risposta=input("\n[-] Authentication Failed !\n[+] Do you want to continue ad register it? [y/n] : ")
        if risposta !="n":
            credenziali[username] = password
            fileP = os.path.expanduser('~/.credenziali.txt')
            writeCredentialsOnFile(credenziali, fileP)
            print("[+] Authentication Completed -> new user {} registered !\n".format(username))
        else:
            print("\n[-] Quitting....\n")
            server.server_close()
            sys.exit(0)

#Estrae tutte le credenziali dal file passatogli in input
def getCredentials_from_file(credentialsFile):
    with open(credentialsFile,'r') as file:
        return ast.literal_eval(file.read())
    
    

# definiamo una funzione per permetterci di uscire dal processo tramite Ctrl-C
def signal_handler(signal, frame):
    print( '\nExiting http server (Ctrl+C pressed)')
    try:
      if(server):
        server.server_close()
    finally:
      # fermo il thread del refresh senza busy waiting
      sys.exit(0)
      
# metodo che viene chiamato al "lancio" del server
def main():
    #Assicura che da tastiera usando la combinazione
    #di tasti Ctrl-C termini in modo pulito tutti i thread generati
    server.daemon_threads = True 
    
    #il Server acconsente al riutilizzo del socket anche se ancora non è stato
    #rilasciato quello precedente, andandolo a sovrascrivere
    server.allow_reuse_address = True  
    
    #interrompe l'esecuzione se da tastiera arriva la sequenza (CTRL + C) 
    signal.signal(signal.SIGINT, signal_handler)

    #Salvo il percorso del file contenente le credenziali
    credentialsFile = os.path.expanduser('~/.credenziali.txt')
    
    #Estrapolo i vari account
    credenziali = initCredentials(credentialsFile)
    
    #Controllo se i dati inseriti esistano nel file
    authentication(credenziali)
    
    #invoco il metodo per generare i contenuti ovvero le pagine
    refresh();     
    
    # entra nel loop infinito
    try:
      while True:
        server.serve_forever()
    except KeyboardInterrupt:
      pass
    server.server_close()

if __name__ == "__main__":
    main()
             
