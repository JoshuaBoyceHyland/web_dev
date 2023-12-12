-- MariaDB dump 10.19-11.2.2-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: BlackJackDB
-- ------------------------------------------------------
-- Server version	11.2.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `games`
--

DROP TABLE IF EXISTS `games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `games` (
  `gamertag` varchar(32) NOT NULL,
  `outcome` varchar(4) NOT NULL,
  `21s` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games`
--

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
INSERT INTO `games` VALUES
('Xx_TTV_MadJack69_xX','Loss','no'),
('JDawg','Win','yes'),
('FrogGranna','Win','no'),
('alwyn','Loss','no'),
('xxx_CDawg_xxx','Win','no'),
('PDawg','Loss','no'),
('Xx_TTV_MadJack69_xX','Loss','no'),
('FrogGranna','Win','no'),
('Ruark','Loss','no'),
('frodo','Win','no'),
('JDawg','Win','no'),
('MIA','Win','no'),
('MIA','Loss','no'),
('MIA','Win','no'),
('FrogGranna','Loss','no'),
('FrogGranna','Loss','no'),
('idk','Win','no'),
('PDawg','Loss','no'),
('Ruark','Loss','no'),
('kio','Win','no'),
('Ruark','Win','no'),
('kio','Loss','no'),
('The Legend 27','Win','yes'),
('JDawg','Win','yes'),
('kio','Loss','no'),
('xxx_CDawg_xxx','Win','no'),
('JDawg','Win','no'),
('alwyn','Win','yes'),
('The Legend 27','Loss','no'),
('idk','Loss','no'),
('The Legend 27','Loss','no'),
('frodo','Win','yes'),
('The Legend 27','Loss','no'),
('MIA','Loss','no'),
('xxx_CDawg_xxx','Win','no'),
('FrogGranna','Loss','no'),
('kio','Win','no'),
('alwyn','Win','no'),
('Xx_TTV_MadJack69_xX','Win','no'),
('alwyn','Win','no'),
('alwyn','Win','yes'),
('JDawg','Win','no'),
('Ruark','Loss','no'),
('PDawg','Win','no'),
('FrogGranna','Loss','no'),
('frodo','Loss','no'),
('frodo','Loss','no'),
('MIA','Loss','no'),
('Xx_TTV_MadJack69_xX','Win','no'),
('idk','Loss','no'),
('xxx_CDawg_xxx','Win','no'),
('idk','Loss','no'),
('The Legend 27','Win','yes'),
('MIA','Win','no'),
('kio','Win','no'),
('MIA','Win','no'),
('The Legend 27','Win','no'),
('Ruark','Loss','no'),
('idk','Win','no'),
('JDawg','Win','no'),
('PDawg','Win','yes'),
('The Legend 27','Loss','no'),
('idk','Win','no'),
('PDawg','Win','no'),
('The Legend 27','Loss','no'),
('idk','Win','yes'),
('xxx_CDawg_xxx','Win','yes'),
('MIA','Loss','no'),
('MIA','Win','yes'),
('MIA','Win','yes'),
('xxx_CDawg_xxx','Win','yes'),
('frodo','Loss','no'),
('frodo','Loss','no'),
('The Legend 27','Win','yes'),
('Xx_TTV_MadJack69_xX','Loss','no'),
('frodo','Win','yes'),
('Ruark','Win','yes'),
('idk','Loss','no'),
('JDawg','Loss','no'),
('JDawg','Loss','no'),
('idk','Loss','no'),
('frodo','Loss','no'),
('MIA','Win','no'),
('idk','Loss','no'),
('FrogGranna','Loss','no'),
('Ruark','Win','yes'),
('kio','Win','no'),
('MIA','Win','yes'),
('idk','Loss','no'),
('idk','Win','no'),
('frodo','Win','no'),
('The Legend 27','Win','no'),
('Xx_TTV_MadJack69_xX','Loss','no'),
('PDawg','Loss','no'),
('kio','Win','no'),
('kio','Win','no'),
('Xx_TTV_MadJack69_xX','Win','no'),
('frodo','Win','yes'),
('Ruark','Win','no'),
('FrogGranna','Win','no'),
('xxx_CDawg_xxx','Loss','no'),
('PDawg','Win','yes'),
('The Legend 27','Win','no'),
('xxx_CDawg_xxx','Loss','no'),
('FrogGranna','Win','yes'),
('alwyn','Loss','no'),
('frodo','Loss','no'),
('idk','Loss','no'),
('Ruark','Loss','no'),
('MIA','Loss','no'),
('The Legend 27','Loss','no'),
('xxx_CDawg_xxx','Win','no'),
('Ruark','Loss','no'),
('FrogGranna','Win','no'),
('MIA','Win','no'),
('xxx_CDawg_xxx','Win','yes'),
('xxx_CDawg_xxx','Loss','no'),
('Ruark','Loss','no'),
('PDawg','Loss','no'),
('frodo','Loss','no'),
('alwyn','Win','no'),
('Xx_TTV_MadJack69_xX','Loss','no'),
('Xx_TTV_MadJack69_xX','Win','no'),
('idk','Win','no'),
('Xx_TTV_MadJack69_xX','Win','no'),
('alwyn','Win','no'),
('MIA','Loss','no'),
('frodo','Loss','no'),
('Ruark','Loss','no'),
('idk','Win','no'),
('FrogGranna','Loss','no'),
('kio','Loss','no'),
('Xx_TTV_MadJack69_xX','Win','no'),
('frodo','Win','no'),
('frodo','Win','yes'),
('kio','Loss','no'),
('Ruark','Loss','no'),
('frodo','Win','no'),
('idk','Loss','no'),
('MIA','Win','no'),
('xxx_CDawg_xxx','Loss','no'),
('FrogGranna','Win','no'),
('kio','Loss','no'),
('kio','Loss','no'),
('Ruark','Loss','no'),
('MIA','Win','yes'),
('MIA','Loss','no'),
('Ruark','Loss','no'),
('PDawg','Loss','no'),
('xxx_CDawg_xxx','Loss','no');
/*!40000 ALTER TABLE `games` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gamestats`
--

DROP TABLE IF EXISTS `gamestats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gamestats` (
  `gamertag` varchar(32) NOT NULL,
  `winrate` int(2) NOT NULL,
  `HighestWinStreak` int(3) NOT NULL,
  `21s` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gamestats`
--

LOCK TABLES `gamestats` WRITE;
/*!40000 ALTER TABLE `gamestats` DISABLE KEYS */;
INSERT INTO `gamestats` VALUES
('JDawg',75,6,2),
('idk',44,3,1),
('alwyn',75,4,2),
('FrogGranna',50,3,1),
('PDawg',44,3,2),
('frodo',50,3,4),
('The Legend 27',50,3,3),
('xxx_CDawg_xxx',62,6,3),
('Xx_TTV_MadJack69_xX',55,3,0),
('Ruark',27,3,2),
('kio',50,5,0),
('MIA',61,4,4);
/*!40000 ALTER TABLE `gamestats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `players` (
  `gamertag` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players`
--

LOCK TABLES `players` WRITE;
/*!40000 ALTER TABLE `players` DISABLE KEYS */;
INSERT INTO `players` VALUES
('JDawg'),
('idk'),
('alwyn'),
('FrogGranna'),
('PDawg'),
('frodo'),
('The Legend 27'),
('xxx_CDawg_xxx'),
('Xx_TTV_MadJack69_xX'),
('Ruark'),
('kio'),
('MIA');
/*!40000 ALTER TABLE `players` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-11  0:41:44
