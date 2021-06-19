create table for_sale_album
(
    m_id           int         not null
        primary key,
    m_release_date date        not null,
    m_url          varchar(50) not null,
    constraint for_sale_album_ibfk_1
        foreign key (m_id) references approved_album (m_id)
            on update cascade on delete cascade
);

