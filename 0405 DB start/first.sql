CREATE TABLE contacts (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  email TEXT NOT NULL UNIQUE
);


-- 1. Rename a table
ALTER TABLE contacts RENAME TO new_contacts;

-- 2. Rename a column
ALTER TABLE new_contacts RENAME COLUMN age TO my_age;

-- 3. Add a new column to a table
ALTER TABLE new_contacts ADD COLUMN message TEXT NOT NULL DEFAULT 'no message';

-- 4. Delete a column
ALTER TABLE new_contacts DROP COLUMN message;


-- DROP TABLE new_contacts;