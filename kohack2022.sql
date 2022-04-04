-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 04, 2022 at 08:56 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kohack2022`
--

-- --------------------------------------------------------

--
-- Table structure for table `kohanim`
--

CREATE TABLE `kohanim` (
  `name` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `pwd` varchar(100) NOT NULL,
  `gadol` tinyint(1) DEFAULT NULL,
  `doneIncense` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kohanim`
--

INSERT INTO `kohanim` (`name`, `username`, `pwd`, `gadol`, `doneIncense`) VALUES
('Herschel Cohen', 'hcohen1', '$2b$12$DvUB5Az690eqD2ETlnyXTe5Wi6HNksGpxk4fkCcKeVAHcq.Pik3Ke', 1, 1),
('Jonathan Kaplan', 'jkap123', '$2b$12$6FwaQ0Cu2kSRjIustspbJuEiCXhmMB1P1bjXfTKzaU.xanYfGnuti', 0, 1),
('Lior Stein', 'lstein12', '$2b$12$TyU12l6m1mDXHscARyvWQeUrAWKy.AVhEw7wbXDoSKIMyAgpP7Bk2', 0, 0),
('Ariel Rokeach', 'arielrokeach', '$2b$12$3I.HogoUFKw2l1nuXDXJFuzPbp33En6vulGi5HMtW4KRDnxf5BP86', 0, 0),
('Jonathan Whiteman', 'jwhite35', '$2b$12$bBTD3/w/bxrLZNO0cEZmseAi6ZvQ.s82YC6Bo45oRGIkiD8JxqSJq', 0, 1),
('Alon Weglein', 'aweg613', '$2b$12$m1oftr9kSN58itY869a22ufsBK.62uphLfy6ojhHKu4FpRkuuvozW', 0, 0),
('Roee Baker', 'rbakes12', '$2b$12$J9tvwNsFLSiUHqSuYtCc2OQ/FKYOHETHWNQp2k86W04qzqgj3syPa', 0, 1),
('Elazar Siegal', 'esieg123', '$2b$12$9a1Te73DyxpLEpTQDRrAL.l67lSRBbkwLOIpuqs6AO17FFGtAVliO', 0, 1),
('Itamar Ben-David', 'ibd1818', '$2b$12$uLgv2RHX7xYJR3.UYgr0Au2gJVkteLRp5XZ5f2VOiT/Qt2.iO38yy', 0, 0),
('Nadav Pekuel', 'nadav1973', '$2b$12$fKWj4x6I4fmGone9b.cfSOSNevm2cnPTRWNAKxiymVfPLG9WBs56y', 0, 0),
('Avihu Cohen', 'acohen24', '$2b$12$ZBrMc7gTny5QpFyM3SXeIOnDAaVCC2NoG.DDat6QX.3MNCLr43oWG', 0, 0),
('Avi Steinman', 'astein32', '$2b$12$m4IrTol0BwsMBmH3tCSv3eiDcwtcMqDFOCHbYhhSsRs5LSvkBLHzu', 0, 0),
('Aaron Levy', 'aaronl24613', '$2b$12$0vVUkCrro2x0eB/Y/dPgduQ54/I3zo2w3TV0EpuTw7rDr8L53nQiK', 0, 1),
('Ephraim Cohen', 'ecohen75', '$2b$12$hKafdg7SBjUgKElMfcHs/ueC4PlMH3K9pEz4YcayUnANvQmGWfk52', 0, 0),
('Eli Mizrachi', 'EEast613', '$2b$12$5757cO49bxGaWsH5J1uTs.dwcxOVnZCDuy5f5Lj7VzBjcEvezfDSW', 0, 0),
('Shmuel Kahn', 'skahn613', '$2b$12$jJ4vdcc7KGSkgudZj91Z.uCL99lsn3HoIU6sSdsA/BjYp8ClnYPsy', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `lottery`
--

CREATE TABLE `lottery` (
  `entries` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`entries`)),
  `winner_today` varchar(100) NOT NULL,
  `job` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lottery`
--

INSERT INTO `lottery` (`entries`, `winner_today`, `job`) VALUES
('[]', 'Itamar Ben-David', 'Cleaning the ashes from the Mizbeiach HaNechoshet'),
('[]', 'Roee Baker', 'Cleaning the ashes from the Mizbeiach HaZahav'),
('[]', 'Jonathan Kaplan', 'Slaughter the Korban Tamid'),
('[]', 'Ephraim Cohen', 'Sprinkle the blood of the Korban Tamid'),
('[]', 'Eli Mizrachi', 'Preparing the Menorah'),
('[]', 'Avi Steinman', 'Taking the head and right hindleg of the Korban Tamid to the Mizbeiach'),
('[]', 'Alon Weglein', 'Taking the tail and left hindleg of the Korban Tamid to the Mizbeiach'),
('[]', 'Elazar Siegal', 'Taking the two forelegs of the Korban Tamid to the Mizbeiach'),
('[]', 'Nadav Pekuel', 'Taking the breast and throat of the Korban Tamid to the Mizbeiach'),
('[]', 'Lior Stein', 'Taking the two flanks of the Korban Tamid to the Mizbeiach'),
('[]', 'Ariel Rokeach', 'Taking the intestines of the Korban Tamid to the Mizbeiach'),
('[]', 'Herschel Cohen', 'Taking the Korban Mincha accompanying the Korban Tamid to the Mizbeiach'),
('[]', 'Avihu Cohen', 'Taking the Kohens daily flour cakes accompanying the Korban Tamid to the Mizbeiach'),
('[]', 'Shmuel Kahn', 'Taking the wine libations accompanying the Korban Tamid to the Mizbeiach'),
('[]', 'Aaron Levy', 'Offer the Ketoret'),
('[]', 'Jonathan Whiteman', 'Offer the Korban Tamid on the Mizbeiach');

-- --------------------------------------------------------

--
-- Table structure for table `reservations`
--

CREATE TABLE `reservations` (
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `korban` varchar(100) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `cycle` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `reservations`
--

INSERT INTO `reservations` (`date`, `time`, `name`, `korban`, `username`, `cycle`) VALUES
('2023-01-01', '10:00:00', 'Jonathan Snyder', 'Korban Olah (childbirth, Nazir, Metzora)', 'johns35', 'AM'),
('2023-02-09', '12:00:00', 'Jonathan Snyder', 'Korban Asham (doubtful sin, ram)', 'johns35', 'PM'),
('2023-01-01', '03:00:00', 'Jonathan Snyder', 'Korban Chatat (two birds)', 'johns35', 'PM'),
('2023-01-01', '11:30:00', 'Jonathan Snyder', 'Korban Olah (childbirth, Nazir, Metzora)', 'johns35', 'AM'),
('2023-01-01', '09:00:00', 'Yehoshua Smith', 'Korban Asham (doubtful sin, ram)', 'yysmith613', 'AM'),
('2023-01-26', '02:00:00', 'Yehoshua Smith', 'Korban Olah (bird)', 'yysmith613', 'PM'),
('2023-01-01', '04:30:00', 'Yehoshua Smith', 'Korban Olah (childbirth, Nazir, Metzora)', 'yysmith613', 'PM'),
('2023-02-04', '02:30:00', 'Binyamin Goldman', 'Korban Chatat (two birds)', 'bgold123', 'PM'),
('2023-02-04', '10:30:00', 'Binyamin Goldman', 'Korban Olah (bird)', 'bgold123', 'AM'),
('2023-01-01', '04:00:00', 'Ephraim Fischer', 'Korban Chatat (kid/lamb)', 'efish1824', 'PM'),
('2023-02-07', '02:00:00', 'Roee Weglein', 'Korban Shelamim (Nazir Tahor)', 'lstein12', 'PM'),
('2023-01-01', '05:00:00', 'johnsmith', 'Korban Chatat (kid/lamb)', 'jsmith1', 'PM'),
('2023-01-27', '09:00:00', 'johnsmith', 'Korban Chatat (kid/lamb)', 'jsmith1', 'AM'),
('2023-01-13', '12:00:00', 'Ephraim Fischer', 'Korban Olah (other, sheep/goat/cattle)', 'efish1824', 'PM'),
('2023-01-03', '02:00:00', 'Binyamin Goldman', 'Korban Olah (convert)', 'bgold123', 'PM');

-- --------------------------------------------------------

--
-- Table structure for table `sanhedrin`
--

CREATE TABLE `sanhedrin` (
  `date` date DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `offender` varchar(100) DEFAULT NULL,
  `reason` varchar(100) DEFAULT NULL,
  `other` varchar(300) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sanhedrin`
--

INSERT INTO `sanhedrin` (`date`, `name`, `offender`, `reason`, `other`, `username`) VALUES
('2023-02-17', 'Jonathan Snyder', 'Binyamin Goldman', 'Dispute', 'He sued my cousin and he is wrong', 'johns35'),
('2023-02-17', 'Jonathan Snyder', 'Jane Snyder', 'Marital', 'It turns out that this was a forbidden marriage', 'johns35'),
('2023-02-17', 'Binyamin Goldman', 'Shmuel Katz', 'Monetary', 'He did not pay back a loan', 'bgold123'),
('2023-02-17', 'Binyamin Goldman', 'Beis Din', 'Dispute', 'I was wrongfully put in Cheirim', 'bgold123'),
('2023-02-17', 'Yehoshua Smith', 'Chaim Klein', 'Report', 'He stole from my neighbor', 'yysmith613'),
('2023-01-01', 'Jonathan Snyder', 'Dr. Chaim Goldman', 'Monetary', 'He scammed me', 'johns35'),
('2023-04-08', 'Binyamin Goldman', 'Reuven Mizrachi', 'Monetary', 'He owes me $5', 'bgold123'),
('2023-01-01', 'Ephraim Fischer', 'Roee Wegleinj', 'Monetary', 'He owes me $5', 'efish1824'),
('2023-01-01', 'Ephraim Fischer', 'Roee WEglein', 'Monetary', 'He owes me $5', 'efish1824'),
('2023-01-01', 'Binyamin Goldman', 'Roee Weglein', 'Monetary', 'He owes me $5', 'bgold123');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `username` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `pwd` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`username`, `name`, `pwd`) VALUES
('bgold123', 'Binyamin Goldman', '$2b$12$XioFWrCPTR1HlR16su6IrepMoKzTcH2cQBjx7VWwYMvQ908hgWQNS'),
('johns35', 'Jonathan Snyder', '$2b$12$TVRYOXuzQv3WSJ0dz0fptuWYtX08NpBAfR.sFBSSb09wM1t0TD84u'),
('yysmith613', 'Yehoshua Smith', '$2b$12$6/6ISN3pOUpawxnH.63dS.7YUfWHu2JmA1SdQQ4ZBdo1xrls7cANS'),
('rweg613', 'Roee Weglein', '$2b$12$tdX7GWTnp9YpW.IyOOUy6e2w2ruusw6j.7w6.fX4iXlCs4/ZFA7du'),
('lstein12', 'Roee Weglein', '$2b$12$u4XOCbopJJPKgLXY.DYZLehc6RPXQA3INJP5GYC5QyUvA5NkrLUzC'),
('efish1824', 'Ephraim Fischer', '$2b$12$KX572riazuKY6L2FsM0.K.0ZsZdjilwr3VAai5aaooA/OarOCg7ha'),
('jsmith1', 'johnsmith', '$2b$12$KRNB4sl4HLm/HYDl9g4w3uNBjjv8YJ7gQoQpvL1n5uw6wDHn9S6cm'),
('SycoBak', 'Alon Baker', '$2b$12$nfkL9Tz3P0.pV7M9IQ5/dO14pwZQNHoiCZK2aKz4ZebVAo1m9bm2S');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
