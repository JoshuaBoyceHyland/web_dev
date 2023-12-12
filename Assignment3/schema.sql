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

insert into players (gamertag) values ("JDawg");
insert into Players (gamertag) values ("idk"  );
insert into Players (gamertag) values ("alwyn");
insert into Players (gamertag) values ("FrogGranna");
insert into Players (gamertag) values ( "PDawg");
insert into Players (gamertag) values ("frodo" );
insert into Players (gamertag) values ("The Legend 27");
insert into Players (gamertag) values ("xxx_CDawg_xxx");
insert into Players (gamertag) values ("Xx_TTV_MadJack69_xX");
insert into Players (gamertag) values ("Ruark");
insert into Players (gamertag) values ("kio");
insert into Players (gamertag) values ("MIA");


    