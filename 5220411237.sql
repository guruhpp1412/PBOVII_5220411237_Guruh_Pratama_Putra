-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 11, 2024 at 02:44 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5220411237`
--

-- --------------------------------------------------------

--
-- Table structure for table `evangelion`
--

CREATE TABLE `evangelion` (
  `id_corp` int(12) NOT NULL,
  `nama_corp` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `evangelion`
--

INSERT INTO `evangelion` (`id_corp`, `nama_corp`) VALUES
(12345, 'Nerv Jepang'),
(12348, 'Nerv Jerman'),
(12349, 'Nerv Amerika'),
(12350, 'Nerv Rusia'),
(12351, 'Nerv Inggris');

-- --------------------------------------------------------

--
-- Table structure for table `pilot`
--

CREATE TABLE `pilot` (
  `id_pilot` int(12) NOT NULL,
  `nama_pilot` varchar(100) NOT NULL,
  `umur` int(20) NOT NULL,
  `asal_pilot` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pilot`
--

INSERT INTO `pilot` (`id_pilot`, `nama_pilot`, `umur`, `asal_pilot`) VALUES
(146, 'Lengley Asuka', 14, 'Jerman'),
(212, 'Ayanami Rei', 14, 'Jepang'),
(245, 'Ikari Shinji', 14, 'Jepang'),
(342, 'Makinami Mari', 32, 'Inggris'),
(432, 'Nagisa Kaworu', 777, 'Bulan');

-- --------------------------------------------------------

--
-- Table structure for table `unit`
--

CREATE TABLE `unit` (
  `id_unit` int(12) NOT NULL,
  `nama_unit` varchar(100) NOT NULL,
  `asal_unit` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `unit`
--

INSERT INTO `unit` (`id_unit`, `nama_unit`, `asal_unit`) VALUES
(0, 'EVA-00', 'Nerv Jepang'),
(1, 'EVA-01', 'Nerv Jepang'),
(2, 'EVA-02', 'Nerv Jerman'),
(5, 'EVA-05', 'Nerv Inggris'),
(6, 'EVA-06', 'Bulan');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `evangelion`
--
ALTER TABLE `evangelion`
  ADD PRIMARY KEY (`id_corp`);

--
-- Indexes for table `pilot`
--
ALTER TABLE `pilot`
  ADD PRIMARY KEY (`id_pilot`);

--
-- Indexes for table `unit`
--
ALTER TABLE `unit`
  ADD PRIMARY KEY (`id_unit`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
