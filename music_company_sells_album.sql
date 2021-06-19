create table sells_album
(
    m_id           int                         not null,
    d_incoming_url varchar(50)                 not null,
    d_price        float(10, 2) default 350.50 not null,
    primary key (m_id, d_incoming_url),
    constraint sells_album_ibfk_1
        foreign key (m_id) references for_sale_album (m_id)
            on update cascade on delete cascade,
    constraint sells_album_ibfk_2
        foreign key (d_incoming_url) references distributor (d_incoming_url)
            on update cascade on delete cascade
);

create index d_incoming_url
    on sells_album (d_incoming_url);

