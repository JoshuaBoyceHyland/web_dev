create database BlackJackDB

create table gameStats(
gamertag varchar(32) not null,
outcome varchar(4) not null,
hits int(2) not null,
bust varchar(3) not null,
21s varchar(3) not null,
blackjack varchar(3) not null);
    