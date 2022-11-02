-- create companies (5-digit id)
INSERT INTO COMPANY VALUES (47350, 'Gibson');
INSERT INTO COMPANY VALUES (36613, 'Fender');
INSERT INTO COMPANY VALUES (90346, 'Taylor');
INSERT INTO COMPANY VALUES (80816, 'Martin');
INSERT INTO COMPANY VALUES (81080, 'Paul Reed Smith');
INSERT INTO COMPANY VALUES (96852, 'Mitchell');

-- create guitars (7-digit id)
INSERT INTO GUITAR VALUES (2099551, 'Gibson SG Standard Electric Guitar', 1799.99, 47350);
INSERT INTO GUITAR VALUES (5495151, 'Gibson Les Paul Standard \'60s Electric Guitar', 2799.99, 47350);
INSERT INTO GUITAR VALUES (9498421, 'Gibson ES-335 Semi-Hollow Electric Guitar', 3499.99, 47350);
INSERT INTO GUITAR VALUES (3836594, 'Gibson F-25 Folksinger 1965 Acoustic Guitar', 2699.99, 47350);
INSERT INTO GUITAR VALUES (4946939, 'Fender Player Series Stratocaster Maple Fingerboard Electric Guitar', 849.99, 36613);
INSERT INTO GUITAR VALUES (7873513, 'Fender Player Series Telecaster Maple Fingerboard Electric Guitar', 849.99, 36613);
INSERT INTO GUITAR VALUES (3724920, 'PRS SE Standard 24 Electric Guitar', 649.99, 81080);
INSERT INTO GUITAR VALUES (7329790, 'Taylor 322e V-Class Grand Concert Acoustic-Electric Guitar', 2299.99, 90346);
INSERT INTO GUITAR VALUES (8184316, 'Martin Standard Series 000-18 Auditorium Acoustic Guitar', 2799.99, 80816);
INSERT INTO GUITAR VALUES (0146632, 'Mitchell MM100 Mini Double-Cutaway Electric Guitar', 99.99, 96852);