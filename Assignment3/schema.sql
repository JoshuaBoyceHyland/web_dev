create database BlackJackDB;

grant all on BlackJackDB.* to 'josh'@'localhost' identified by 'password';

exit 

mysql -u josh -p BlackJackDB


create table Games(
gamertag varchar(32) not null,
outcome varchar(4) not null,
21s varchar(3) not null);



create table GameStats(
gamertag varchar(32) not null, 
winrate int(2) not null, 
HighestWinStreak int(3) not null, 
21s int(3) not null);

create table Players(
    gamertag varchar(32) not null);

source players.sql; 
    