CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 
-- 자동 변환되어 정의한 것에 맞게 잘 들어감
INSERT INTO zoo VALUES 
(5, 180, 210, 'gorilla', 'omnivore');

-- 2)
-- INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
-- (10,'dolphin', 'carnivore', 210, 3),
-- (10, 'alligator', 'carnivore', 250, 50);

-- rowid는 기본적으로 pk값으로 쓰이기 위해서 UNIQUE가 설정되어 있는데
-- 저렇게 같은 값으로 두개를 넣어준다면 에러가 발생한다
-- 하나를 다음처럼 바꿔주면 된다
INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
(10,'dolphin', 'carnivore', 210, 3),
(11, 'alligator', 'carnivore', 250, 50);

-- 3)
-- INSERT INTO zoo (name, eat, age) VALUES
-- ('dolphin', 'carnivore', 3);

-- weight는 NOT NULL 속성과 함께 정의되어, 값을 넣어줘야 하는데
-- 따로 넣어주지 않았기 때문이다. 
-- weight col도 넣을것이라고 명시하고 weight 값을 같이 넣어주면 해결된다
INSERT INTO zoo (name, eat, weight, age) VALUES
('dolphin', 'carnivore', 200, 3);

-- SELECT rowid, * FROM zoo;