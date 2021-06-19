create table trailer
(
    m_id               int         not null
        primary key,
    t_visits           int         not null,
    t_url              varchar(50) not null,
    t_release_date     date        not null,
    t_terminating_date date        not null,
    constraint trailer_ibfk_1
        foreign key (m_id) references approved_album (m_id)
            on update cascade on delete cascade
);

