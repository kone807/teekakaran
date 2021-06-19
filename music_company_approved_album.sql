create table approved_album
(
    m_id            int  not null
        primary key,
    m_approval_date date not null,
    constraint approved_album_ibfk_1
        foreign key (m_id) references music_album (m_id)
            on update cascade on delete cascade
);

