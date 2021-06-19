create table creates_album
(
    m_id int         not null,
    c_id int         not null,
    g_id int         not null,
    role varchar(30) not null,
    primary key (m_id, c_id, g_id),
    constraint creates_album_ibfk_1
        foreign key (m_id) references music_album (m_id)
            on update cascade on delete cascade,
    constraint creates_album_ibfk_2
        foreign key (c_id) references group_members (c_id)
            on update cascade on delete cascade,
    constraint creates_album_ibfk_3
        foreign key (g_id) references group_members (g_id)
            on update cascade on delete cascade
);

create index c_id
    on creates_album (c_id);

create index g_id
    on creates_album (g_id);

