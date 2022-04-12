CREATE DATABASE techstudent_info;

USE techstudent_info;

CREATE TABLE techstudent(
StudentNBR INT PRIMARY KEY, 
StudentName VARCHAR(100),
StudentLastName VARCHAR(100), 
City VARCHAR(80),	
PostCode VARCHAR(10),
Country VARCHAR(40)
);


EXPLAIN techstudent;

INSERT INTO techstudent (StudentNBR, StudentName, StudentLastName, City, PostCode, Country)
VALUES
(209, "Hannah", "Mashall", "Middlesbrough", "TS1 4AL", "UK"),
(301, "Warithz", "Jolly", "Darlington", "DL1 1HA", "UK"),
(446, "Deola", "Peters", "New York", "11434", "USA"),
(165, "Timmy", "Cole", "Portsmouth", "PO2 7NF", "UK"),
(850, "Corin", "Pinkerton", "Milton Keynes", "MK6 3PH", "UK"),
(899, "Sadia", "Noreen", "California", "90001", "USA"),
(760, "Pinky", "Sultan", "Queens", "11201", "USA"),
(151, "Sheriff", "Wallace", "Belvedere", "DA17 5DR", "UK"),
(194, "Perrie", "Russell", "Coventry", "CV4 8LG", "UK"),
(618, "Brigette", "Colby", "Chicago", "49501", "USA")
;

SELECT * FROM techstudent;

-- Create second table


CREATE TABLE assignment1(
maths_score INT NOT NULL PRIMARY KEY,
python_score INT,
scikit_score INT NOT NULL,
tensorflow_score VARCHAR (80)
);


EXPLAIN assignment1;

-- Add data
INSERT INTO assignment1 (maths_score, python_score , scikit_score, tensorflow_score)
VALUES
(45, 60 , 59,  75),
(60, 68 , 92,  78),
(71, 73 , 84,  80),
(93, 59 , 47,  43),
(87, 89 , 100,  79),
(63, 58 , 50,  67),
(78, 90 , 66,  49),
(55, 67 , 46,  74),
(49, 60 , 77,  80),
(77, 91 , 82,  90)
;

SELECT * FROM assignment1;

-- Updated python_score of 73
UPDATE assignment1
SET python_score = 37
WHERE maths_score = 71;

SELECT * FROM assignment1;

-- Joining tables

SELECT techstudent.StudentNBR , assignment1.python_score
FROM techstudent
INNER JOIN assignment1
ON techstudent.Country = assignment1.maths_score;

-- selecting data 
SELECT *
FROM techstudent
INNER JOIN assignment1
WHERE techstudent.Country = assignment1.maths_score AND assignment1.scikit_score = "84";

-- select using comparison operators
SELECT * FROM assignment1
WHERE python_score between 60 and 80;

SELECT * FROM techstudent;
drop database PostCode;
