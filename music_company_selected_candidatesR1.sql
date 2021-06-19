create table selected_candidatesR1
(
    c_id int not null
        primary key,
    constraint selected_candidatesR1_ibfk_1
        foreign key (c_id) references candidate_submission (c_id)
            on update cascade on delete cascade
);

