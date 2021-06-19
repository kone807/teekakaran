create table downloads
(
    d_incoming_url  varchar(50) not null,
    m_id            int         not null,
    do_request_date date        not null,
    do_status       varchar(4)  not null,
    primary key (d_incoming_url, m_id),
    constraint downloads_ibfk_1
        foreign key (m_id) references sells_album (m_id)
            on update cascade on delete cascade,
    constraint downloads_ibfk_2
        foreign key (d_incoming_url) references sells_album (d_incoming_url)
            on update cascade on delete cascade
);

create index m_id
    on downloads (m_id);

