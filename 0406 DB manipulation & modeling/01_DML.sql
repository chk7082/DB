-- users table 생성
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

SELECT COUNT(*) FROM users;

SELECT avg(balance) FROM users;

SELECT DISTINCT country FROM users;

SELECT country, avg(balance) FROM users WHERE country="전라북도";

SELECT country, avg(balance) FROM users GROUP BY country;

SELECT country, avg(balance) FROM users 
GROUP BY country ORDER BY avg(balance) DESC;

SELECT AVG(age) FROM users WHERE age >= 30;

SELECT country, COUNT(*) FROM users GROUP BY country;
SELECT country, COUNT(*) AS number_of_residents FROM users GROUP BY country;

SELECT country, AVG(age) AS average_age FROM users GROUP BY country;

SELECT last_name, COUNT(*) FROM users GROUP BY last_name;

CREATE TABLE classmates (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);

INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 23, '서울');

INSERT INTO classmates
VALUES ('홍길동', 23, '서울');

INSERT INTO classmates
VALUES
  ('김철수', 30, '경기'),
  ('이영미', 31, '강원'),
  ('박진성', 26, '전라'),
  ('최지수', 12, '충청'),
  ('정요한', 28, '경상');

UPDATE classmates
SET name = '김철수한무두루미',
 address = '제주도'
WHERE rowid = 2;

DELETE FROM classmates
WHERE rowid=6;

SELECT rowid, * FROM classmates;

DELETE FROM classmates WHERE name LIKE '%영%';

-- DELETE FROM classmates;


CREATE TABLE articles (
  id INTEGER NOT NULL,
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  userID INTEGER NOT NULL
);

CREATE TABLE article_users (
  id INTEGER NOT NULL,
  name TEXT NOT NULL,
  roleID INTEGER NOT NULL
);

INSERT INTO articles (id, title, content, userID)
VALUES
  (1, '제목1', '내용1', 1),
  (2, '제목2', '내용2', 2),
  (3, '제목3', '내용3', 3),
  (5, '제목5', '내용5', 5),
  (9, '제목9', '내용9', 9),
  (10, '제목10', '내용10', 10);

INSERT INTO article_users (id, name, roleID)
VALUES
  (1, 'aiden', 1),
  (2, 'ken', 3),
  (3, 'lynda', 3),
  (4, 'sophia', 2),
  (5, 'beemo', 1),
  (6, 'feel', 3),
  (7, 'coco', 2);


SELECT * FROM articles, article_users;

SELECT * FROM articles, article_users WHERE articles.userID = article_users.id;

SELECT * FROM articles, article_users WHERE userID=article_users.rowid;

SELECT * FROM articles INNER JOIN article_users ON articles.userID = article_users.id;

-- 저렇게 그냥 합치면, id col이 여러개라 id 호출할때 ambiguous col이라고 에러 나옴
-- 주의하자
SELECT * FROM articles LEFT JOIN article_users ON articles.userID = article_users.id;

SELECT * FROM articles RIGHT JOIN article_users ON articles.userID = article_users.id;

SELECT * FROM articles FULL OUTER JOIN article_users ON articles.userID = article_users.id;



-- DELETE FROM articles;
-- DELETE FROM article_users;

-- DROP TABLE articles;
-- DROP TABLE article_users;

-- INSERT INTO articles (id, title, content, userID)
-- VALUES
--   (1, '제목1', '내용1', 1),
--   (2, '제목2', '내용2', 2),
--   (3, '제목3', '내용3', 3);

-- INSERT INTO article_users (id, name, roleID)
-- VALUES
--   (1, 'aiden', 1),
--   (2, 'ken', 3),
--   (3, 'lynda', 3);

-- SELECT * FROM articles INNER JOIN article_users ON articles.userID = article_users.id;