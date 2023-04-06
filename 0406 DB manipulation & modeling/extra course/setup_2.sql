INSERT INTO articles
VALUES
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 5),
  ('제목6', '내용6', 6),
  ('제목7', '내용7', 7),
  ('제목8', '내용8', 8),
  ('제목9', '내용9', 9),
  ('제목10', '내용10', 10);

INSERT INTO users
VALUES
  ('sophia', 2),
  ('beemo', 1),
  ('feel', 3),
  ('coco', 2);

SELECT u.name, r.role FROM users AS u INNER JOIN roles AS r where u.role_id = r.rowId;


-- 논리 연산자

-- 키가 175이거나, 185이면서 몸무게가 80인 사람
WHERE height = 175 OR height = 185 and weight = 80

-- 키가 175이거나 185인 사람 중에서 몸무게가 80인 사람
WHERE (height = 175 OR height = 185) and weight = 80