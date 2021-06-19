create table music_group
(
    g_id        int auto_increment
        primary key,
    g_type      varchar(30) not null,
    director_id int         null,
    constraint music_group_ibfk_1
        foreign key (director_id) references selected_candidatesR2 (c_id)
            on update cascade on delete cascade
);

create index director_id
    on music_group (director_id);

