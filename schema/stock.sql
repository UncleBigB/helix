CREATE DATABASE  IF NOT EXISTS `stock` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `stock`;
-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: localhost    Database: stock
-- ------------------------------------------------------
-- Server version	5.7.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `stockdaykline`
--

DROP TABLE IF EXISTS `stockdaykline`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stockdaykline` (
  `date` date NOT NULL COMMENT '日期',
  `code` varchar(45) NOT NULL,
  `symbol` varchar(45) NOT NULL COMMENT '股票代码',
  `name` varchar(45) NOT NULL COMMENT '股票名称',
  `close` decimal(20,4) NOT NULL COMMENT '收盘价',
  `high` decimal(20,4) NOT NULL COMMENT '最高价',
  `open` decimal(20,4) NOT NULL COMMENT '开盘价',
  `low` decimal(20,4) NOT NULL COMMENT '最低价',
  `yestclose` decimal(20,4) NOT NULL COMMENT '昨收价',
  `updatevol` decimal(20,4) NOT NULL COMMENT '涨跌额',
  `updatepercent` decimal(20,4) NOT NULL COMMENT '涨跌幅',
  `turnoverrate` decimal(20,4) NOT NULL COMMENT '换手率',
  `volume` bigint(40) NOT NULL COMMENT '成交量',
  `turnover` decimal(20,4) NOT NULL COMMENT '成交额',
  `marketcap` decimal(20,4) NOT NULL,
  `circulation` decimal(20,4) NOT NULL COMMENT '流通市值',
  `quantity` bigint(20) NOT NULL DEFAULT '0' COMMENT '成交笔数',
  UNIQUE KEY `id` (`date`,`symbol`),
  KEY `symbol` (`symbol`),
  KEY `date` (`date`),
  KEY `code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `stocklists`
--

DROP TABLE IF EXISTS `stocklists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stocklists` (
  `symbol` varchar(10) NOT NULL,
  `code` varchar(10) NOT NULL,
  `name` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `type` varchar(45) NOT NULL,
  UNIQUE KEY `id_UNIQUE` (`symbol`),
  KEY `code` (`code`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-10 15:54:10
