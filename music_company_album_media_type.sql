create table album_media_type
(
    m_id int not null
        primary key,
    constraint album_media_type_ibfk_1
        foreign key (m_id) references music_album (m_id)
            on update cascade on delete cascade
);

