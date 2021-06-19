create table panelist
(
    p_id                int auto_increment
        primary key,
    p_name              varchar(30)   not null,
    p_dob               date          not null,
    p_email             varchar(30)   not null,
    p_association_start date          not null,
    p_exp               int default 5 null
);

