DROP TABLE IF EXISTS SAMPLE;

create table SAMPLE
(
    id   int auto_increment
        primary key,
    name varchar(10),
    ts   TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
