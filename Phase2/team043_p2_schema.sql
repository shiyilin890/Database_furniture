DROP DATABASE IF EXISTS `cs6400_sp21_team043`; 
SET default_storage_engine=InnoDB;
SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE DATABASE IF NOT EXISTS cs6400_sp21_team043 
    DEFAULT CHARACTER SET utf8mb4 
    DEFAULT COLLATE utf8mb4_unicode_ci;
USE cs6400_sp21_team043;

-- GRANT SELECT, INSERT, UPDATE, DELETE, FILE ON *.* TO 'team043'@'localhost';
-- GRANT ALL PRIVILEGES ON `team043`.* TO 'team043'@'localhost';
-- GRANT ALL PRIVILEGES ON `cs6400_sp21_team043`.* TO 'team043'@'localhost';
-- FLUSH PRIVILEGES;

-- Tables 

CREATE TABLE Store (
  storeID int(16) unsigned NOT NULL AUTO_INCREMENT,
  childcare_limit varchar(50) NOT NULL,
  has_restaurant bool,
  has_snack_bar bool,
  phone_number varchar(20) NOT NULL,
  street_address varchar(250) NOT NULL,
  city_name varchar(250) NOT NULL,
  state varchar(20) NOT NULL,
  PRIMARY KEY (storeID)
);

CREATE TABLE Childcare (
  childcare_limit varchar(50) NOT NULL,
  PRIMARY KEY (childcare_limit)
);

CREATE TABLE City (
  city_name varchar(250) NOT NULL,  
  state varchar(20) NOT NULL,
  population int(16) unsigned NOT NULL,
  PRIMARY KEY (city_name, state)
);

CREATE TABLE Sold (
  PID int(16) unsigned NOT NULL,
  storeID int(16) unsigned NOT NULL,
  date_attr date NOT NULL,
  quantity int(16) unsigned NOT NULL,
  PRIMARY KEY (PID, storeID, date_attr)
);

CREATE TABLE Product (
  PID int(16) unsigned NOT NULL AUTO_INCREMENT,
  product_name varchar(250) NOT NULL,
  retail_price DECIMAL (10, 2) NOT NULL,
  PRIMARY KEY (PID)
);

CREATE TABLE DateYMD (
  date_attr date NOT NULL,
  PRIMARY KEY (date_attr)
);

CREATE TABLE BelongTo (
  PID int(16) unsigned NOT NULL,
  category_name varchar(250) NOT NULL,
  PRIMARY KEY (PID, category_name)
);

CREATE TABLE Category (
  category_name varchar(250) NOT NULL,
  PRIMARY KEY (category_name)
);

CREATE TABLE Discount (
  PID int(16) unsigned NOT NULL,
  date_attr date NOT NULL,
  discount_price DECIMAL (10, 2) NOT NULL,
  PRIMARY KEY (PID, date_attr)
);

CREATE TABLE Holiday (
  holiday_name varchar(250) NOT NULL,
  date_attr date NOT NULL,
  PRIMARY KEY (holiday_name)
);

CREATE TABLE HasAdCamp (
  camp_description varchar(250) NOT NULL,
  date_attr date NOT NULL,
  PRIMARY KEY (camp_description, date_attr)
);

CREATE TABLE AdCamp (
  camp_description varchar(250) NOT NULL,
  PRIMARY KEY (camp_description)
);

-- Constraints   Foreign Keys: FK_ChildTable_childColumn_ParentTable_parentColumn

ALTER TABLE Store
  ADD CONSTRAINT fk_Store_cityname_state_City_cityname_state FOREIGN KEY (city_name, state) REFERENCES City (city_name, state);
  
ALTER TABLE Store
  ADD CONSTRAINT fk_Store_childcare_Childcare_limit FOREIGN KEY (childcare_limit) REFERENCES Childcare (childcare_limit);
 
ALTER TABLE Sold
  ADD CONSTRAINT fk_Sold_pid_Product_pid FOREIGN KEY (PID) REFERENCES Product (PID),
  ADD CONSTRAINT fk_Sold_storeid_Store_storeid FOREIGN KEY (storeID) REFERENCES Store (storeID),
  ADD CONSTRAINT fk_Sold_dateattr_DateYMD_dateattr FOREIGN KEY (date_attr) REFERENCES DateYMD (date_attr);
  
ALTER TABLE BelongTo
  ADD CONSTRAINT fk_BelongTo_pid_Product_pid FOREIGN KEY (PID) REFERENCES Product (PID),
  ADD CONSTRAINT fk_BelongTo_categoryname_Category_categoryname FOREIGN KEY (category_name) REFERENCES Category (category_name);
  
ALTER TABLE Discount
  ADD CONSTRAINT fk_Discount_pid_Product_pid FOREIGN KEY (PID) REFERENCES Product (PID),
  ADD CONSTRAINT fk_Discount_dateattr_DateYMD_dateattr FOREIGN KEY (date_attr) REFERENCES DateYMD (date_attr);
  
ALTER TABLE Holiday
  ADD CONSTRAINT fk_Holiday_dateattr_Dates_dateattr FOREIGN KEY (date_attr) REFERENCES DateYMD (date_attr);

ALTER TABLE HasAdCamp
  ADD CONSTRAINT fk_HasAdCamp_campdescription_AdCamp_campdescription FOREIGN KEY (camp_description) REFERENCES AdCamp (camp_description),
  ADD CONSTRAINT fk_HasAdCamp_dateattr_Dates_dateattr FOREIGN KEY (date_attr) REFERENCES DateYMD (date_attr);  



