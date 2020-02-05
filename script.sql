-- SQLite
CREATE TABLE user(
  id    INTEGER PRIMARY KEY, 
  name  TEXT
);
CREATE TABLE file(
  id    INTEGER PRIMARY KEY, 
  file_name  TEXT,
  creation_date  TEXT,
  modification_date  TEXT
);
CREATE TABLE file_control(
  user_id INTEGER,
  file_id INTEGER
);
