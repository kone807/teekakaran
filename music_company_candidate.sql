create table candidate
(
    c_id        int auto_increment
        primary key,
    c_name      varchar(30)   not null,
    c_dob       date          not null,
    c_city      varchar(30)   not null,
    c_email     varchar(30)   null,
    c_exp_years int default 2 not null,
    c_adv_seen  varchar(20)   not null
);

