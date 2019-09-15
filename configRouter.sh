#!/usr/bin/expect -f
#Autor: Jonathan Ferreira
#Esse script executa uma conexão telnet com o roteador TP-LINK modelo TL-WR849

#caso algo dê errado a execução do script terminará em 20 segundos
set timeout 20
#Definindo a  variável que recebeo IP do roteador
set name [lindex $argv 0]
#Definindo a variável que recebe o user
set user [lindex $argv 1]
#Defininfo a variável que recebe o password
set password [lindex $argv 2]
#iniciando a conexão telnet com o roteador
spawn telnet $name
#Espera pedir o username:
#expect "'^]'." sleep .1;
#send "\r";
sleep .1;
expect "username:"
send "$user\r"
#Espera pedir o password
sleep .1
expect "password:"
send "$password\r"
#Realiza o login
sleep .1
send "\r"
#Define uma configação sem senha  para o roteador
sleep .1
send "wlctl set --sec none\r"

#espera a interação do usuário
interact


