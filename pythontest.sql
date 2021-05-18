-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 19, 2021 at 10:31 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pythontest`
--

-- --------------------------------------------------------

--
-- Table structure for table `balanceinfo`
--

CREATE TABLE `balanceinfo` (
  `accno` varchar(10) NOT NULL,
  `balance` int(50) NOT NULL,
  `accholdername` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `balanceinfo`
--

INSERT INTO `balanceinfo` (`accno`, `balance`, `accholdername`) VALUES
('DS1551', 1000, 'Saad'),
('DS6731', 31000, 'Haider');

-- --------------------------------------------------------

--
-- Table structure for table `bills`
--

CREATE TABLE `bills` (
  `billno` varchar(20) NOT NULL,
  `billtype` varchar(20) NOT NULL,
  `amount` int(20) NOT NULL,
  `status` varchar(20) NOT NULL,
  `familyno` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bills`
--

INSERT INTO `bills` (`billno`, `billtype`, `amount`, `status`, `familyno`) VALUES
('E2095', 'Electricity', 5000, 'Paid', 'DSA10623'),
('G5096', 'Gas', 3000, 'Paid', 'DSA10623'),
('G5065', 'Gas', 3000, 'Not Paid', 'DSA10622'),
('E2056', 'Electricity', 4000, 'Paid', 'DSA10622');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `name` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL,
  `empid` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`name`, `username`, `email`, `pass`, `empid`) VALUES
('Muneeb Farrukh', 'MuneebAli', 'muneeb@gmail.com', '123', 'E101'),
('Haroon', 'HaroonRashid', 'haroon@gmail.com', '123', 'E209'),
('Mohsin', 'Mohisn Ahmed', 'mohsin@gmail.com', '123', 'E685'),
('Haider', 'HaiderAli', 'haider@gmail.com', '123', 'E985');

-- --------------------------------------------------------

--
-- Table structure for table `last_login`
--

CREATE TABLE `last_login` (
  `no` int(20) NOT NULL,
  `accno` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `last_login`
--

INSERT INTO `last_login` (`no`, `accno`) VALUES
(1, 'DS2800'),
(2, 'DS2800'),
(3, 'DS2800'),
(4, 'DS2800'),
(5, 'DS2800'),
(6, 'DS5190'),
(7, 'DS2800'),
(8, 'DS6731'),
(9, 'DS6731'),
(10, 'DS1551');

-- --------------------------------------------------------

--
-- Table structure for table `loan`
--

CREATE TABLE `loan` (
  `accno` varchar(10) NOT NULL,
  `loanamount` int(30) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `loan`
--

INSERT INTO `loan` (`accno`, `loanamount`, `status`) VALUES
('DS6731', 50000, 'Pending');

-- --------------------------------------------------------

--
-- Table structure for table `manager`
--

CREATE TABLE `manager` (
  `email` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `manager`
--

INSERT INTO `manager` (`email`, `pass`) VALUES
('muneeb@gmail.com', '123');

-- --------------------------------------------------------

--
-- Table structure for table `useraccount`
--

CREATE TABLE `useraccount` (
  `name` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `accno` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `useraccount`
--

INSERT INTO `useraccount` (`name`, `email`, `pass`, `gender`, `accno`) VALUES
('Saad', 'saad@gmail.com', '123', 'Male', 'DS1551'),
('Haider', 'haider@gmail.com', '123', 'Male', 'DS6731');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `balanceinfo`
--
ALTER TABLE `balanceinfo`
  ADD PRIMARY KEY (`accno`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`empid`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `last_login`
--
ALTER TABLE `last_login`
  ADD PRIMARY KEY (`no`);

--
-- Indexes for table `manager`
--
ALTER TABLE `manager`
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `useraccount`
--
ALTER TABLE `useraccount`
  ADD UNIQUE KEY `accno` (`accno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `last_login`
--
ALTER TABLE `last_login`
  MODIFY `no` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
