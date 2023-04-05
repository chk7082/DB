-- 문제1. 아래 제시된 스키마 정보를 토대로 users 테이블을 생성하는 쿼리문을 작성하시오.
CREATE TABLE users (
  name TEXT NOT NULL,
  phoneNumber TEXT NOT NULL,
  balance TEXT NOT NULL,
  age INTEGER,
  gender TEXT
);

-- 문제2. sqlite3 명령어를 이용하여 제공된 users.csv 파일의 데이터를 users 테이블에 가져오시오.

-- $ sqlite3 hw_db.sqlite3
-- sqlite> .mode csv
-- sqlite> .import users.csv users



-- 문제3. users 테이블에서 이름, 나이, 계좌 잔고를 나이가 어린순으로, 만약 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회하는 쿼리문 작성하시오.
SELECT name, age, balance FROM users ORDER BY age, balance DESC;