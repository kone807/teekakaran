create table video
(
    m_id       int         not null
        primary key,
    length     int         not null,
    resolution varchar(20) not null,
    constraint video_ibfk_1
        foreign key (m_id) references album_media_type (m_id)
            on update cascade on delete cascade
);

