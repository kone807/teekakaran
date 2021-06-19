create table group_members
(
    g_id int not null,
    c_id int not null,
    primary key (g_id, c_id),
    constraint group_members_ibfk_1
        foreign key (c_id) references selected_candidatesR2 (c_id)
            on update cascade on delete cascade,
    constraint group_members_ibfk_2
        foreign key (g_id) references music_group (g_id)
            on update cascade on delete cascade
);

create index c_id
    on group_members (c_id);

