create table selected_candidatesR2
(
    c_id int not null
        primary key,
    constraint selected_candidatesR2_ibfk_1
        foreign key (c_id) references selected_candidatesR1 (c_id)
            on update cascade on delete cascade
);

