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

-- when a purchase is made, modify the balance then insert the associated fields 
UPDATE BALANCE
INSERT INTO PURCHASE VALUES (
/* the generated 15-digit id */, 
/* the user's 10-digit id */, 
/* the user's updated balance (current - price of guitar),
/* the guitar's 7-digit id */, 
/* the current date and time [use datetime()] */);

-- change an account's username or password

-- view a user's purchases (could be done in a specific view)
SELECT p.ID, p.Buy_date, g.Name, g.Price, p.User_balance
FROM PURCHASE p, GUITAR g 
WHERE p.User_ID = /* the user's id */;

-- add a product as a vendor