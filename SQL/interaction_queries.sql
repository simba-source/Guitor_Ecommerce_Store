-- select a particular guitar, and display the fields on the page from this list
SELECT * FROM GUITAR WHERE ID = /* the ID */;

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

-- add a product as a vendor
INSERT INTO GUITAR VALUES (
	/* a generated 7-digit ID */, 
	/* an entered name */,
	/* an entered price */,
	/* the company's 5-digit ID */);