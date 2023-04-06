CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);

BEGIN;
  DELETE FROM zoo
  WHERE weight < 100;
ROLLBACK;
BEGIN;
  DELETE FROM zoo
  WHERE eat = 'omnivore';
COMMIT;

SELECT COUNT(*)
FROM zoo;

-- BEGIN으로 트랜잭션을 시작해서, weight가 100 이하인 아래 3개를 버렸지만
-- 아직까지 COMMIT을 적용하진 않았으므로 DB에 반영되지는 않은 상태이다
-- 여기서 ROLLBACK으로 BEGIN 이후에 수행한 모든 연산을 되돌리게 되면
-- 다시 처음 상태로 돌아와서 6개의 데이터가 다 들어 있게 되고
-- 여기서 eat이 omnivore인 데이터를 모두 지워서 나머지 3개만 남게된 상태에서
-- commit이 이루어졌으므로 3개가 남게되는 것이다
