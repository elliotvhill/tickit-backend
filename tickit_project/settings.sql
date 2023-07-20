-- settings.sql
CREATE DATABASE tickit;
CREATE USER tickitruser WITH PASSWORD 'tickit';
GRANT ALL PRIVILEGES ON DATABASE tickit TO tickitruser;