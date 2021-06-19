create table audio
(
    m_id              int                       not null
        primary key,
    length            int                       not null,
    audio_file_format varchar(30) default 'mp3' not null,
    constraint audio_ibfk_1
        foreign key (m_id) references album_media_type (m_id)
            on update cascade on delete cascade
);

