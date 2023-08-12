create table SAMPLE
(
    id   serial
        primary key,
    name varchar(10),
    ts   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

create or replace function log_update_some_table() returns trigger as
$$
begin
    NEW.ts := CURRENT_TIMESTAMP;
    return NEW;
end;
$$ language plpgsql;

create or replace trigger log_update_some_table_trigger
    before update
    on SAMPLE
    for each row
execute procedure log_update_some_table();