create table phone_num
(
    c_phone varchar(10) not null
        primary key,
    c_id    int         null,
    constraint phone_num_ibfk_1
        foreign key (c_id) references candidate (c_id)
            on update cascade on delete cascade
);

create index c_id
    on phone_num (c_id);

