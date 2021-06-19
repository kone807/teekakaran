create table music_album
(
    m_id            int auto_increment
        primary key,
    m_name          varchar(30)  not null,
    m_type          varchar(30)  not null,
    m_creation_date date         not null,
    m_description   varchar(200) null
);

