-- select a particular guitar, and display the fields on the page from this list
SELECT * FROM GUITAR WHERE ID = /* the ID */;

-- when registering a new user, insert their fields
INSERT INTO USER VALUES (
/* their generated 10-digit id */,
/* their first name */, 
/* their last name */, 
/* their created username (only alphanumeric)*/, 
/* their created password (*/, 
/* their balance starting at $0.00 */);

-- for sorting guitars
SELECT * FROM GUITAR
ORDER BY NAME;

SELECT * FROM GUITAR
ORDER BY PRICE;

SELECT * FROM GUITAR
ORDER BY PRICE DESC;

-- get a company's name from a guitar
SELECT c.Name 
FROM GUITAR g, COMPANY c
WHERE g.ID = /* the guitar's ID */
AND g.Company_ID = c.ID;

-- when a purchase is made, modify the balance then insert the associated fields 
UPDATE USER
SET Balance = Balance - (SELECT Price FROM GUITAR WHERE ID = /* the guitar's 7-digit ID */)
WHERE ID = /* the user's 10-digit ID */;

INSERT INTO PURCHASE VALUES (
/* a generated 15-digit id */, 
/* the user's 10-digit id */, 
/* the user's updated balance (current - price of guitar),
/* the guitar's 7-digit id */, 
GETDATE());

-- change an account's username or password
UPDATE USER
SET Username = /* the new username */
WHERE ID = /* the user's 10-digit ID */;

-- change an account's username or password
UPDATE USER
SET Username = /* the new password */
WHERE ID = /* the user's 10-digit ID */;

-- view a user's purchases (could be done in a specific view)
SELECT p.ID, p.Buy_date, g.Name, g.Price, p.User_balance
FROM PURCHASE p, GUITAR g 
WHERE p.User_ID = /* the user's id */;

-- add a product as a vendor
INSERT INTO GUITAR VALUES (
	/* a generated 7-digit ID */, 
	/* an entered name */,
	/* an entered price */,
	/* the company's 5-digit ID */);