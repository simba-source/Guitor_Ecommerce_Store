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
SET Password = /* the new password */
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

-- create a cart for a user (should be done upon account creation maybe)
INSERT INTO CART VALUES (
/* a generated ID (9-digits) */,
/* the user's ID */,
GETDATE()
);

-- add an item to the cart
INSERT INTO CART_ITEM VALUES (
/* a generated ID (8-digits) */,
/* the guitar's ID */,
/* the quantity */,
GETDATE(),
/* the cart's ID */
);

-- delete an item from the cart
DELETE FROM CART_ITEM
WHERE ID = /* the item's ID (NOT THE GUITAR'S) */;

-- view the cart (fetches quantity, name, and price of item)
SELECT i.Quantity, g.Name, g.Price
FROM CART_ITEM AS i, GUITAR AS g, CART AS c
WHERE i.Cart_ID = c.ID
AND i.Item_ID = g.ID
AND c.User_ID = /* the user's ID */;

-- everything from cart_item
SELECT i.ID, i.Item_ID, i.Quantity, i.Date_made, i.Cart_ID
FROM CART_ITEM AS i, CART AS c
WHERE i.Cart_ID = c.ID
AND c.User_ID = /* the user's ID */;
