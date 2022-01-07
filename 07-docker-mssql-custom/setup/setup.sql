CREATE DATABASE ProductCatalog
GO

USE ProductCatalog
CREATE TABLE Products (id INT, name NVARCHAR(50), gross_price DECIMAL)
INSERT INTO Products VALUES (1, 'smartphone', 799.99); 
INSERT INTO Products VALUES (2, 'tablet', 1099.99);
GO

SELECT * FROM Products WHERE gross_price > 500.0;
GO