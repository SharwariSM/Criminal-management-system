CREATE TABLE `criminal`(
 `Case_id` VARCHAR(45) NOT NULL , 
 `Criminal_id` VARCHAR(45) NULL ,
 `Criminal_name` VARCHAR(45) NULL ,
 `Nick_name` VARCHAR(45) NULL ,
 `arrest_date` VARCHAR(45) NULL ,
 `dateOfcrime` VARCHAR(45) NULL ,
 `address` VARCHAR(45) NULL ,
 `age` VARCHAR(45) NULL ,
 `occupation` VARCHAR(45) NULL ,
 `BirthMark` VARCHAR(45) NULL ,
 `crimeType` VARCHAR(45) NULL ,
 `fatherName` VARCHAR(45) NULL ,
 `gender` VARCHAR(45) NULL ,
 `wanted` VARCHAR(45) NULL ,
  PRIMARY KEY (`Case_id`))

CREATE TABLE `management`.`login` (
  `userid` VARCHAR(10) NOT NULL,
  `password` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`userid`));

SELECT * FROM management.criminal;
