create table review
(
    o_id    int          null,
    m_id    int          null,
    comment varchar(200) null,
    likes   varchar(1)   not null,
    constraint review_ibfk_1
        foreign key (o_id) references outsiders (o_id)
            on update cascade on delete cascade,
    constraint review_ibfk_2
        foreign key (m_id) references trailer (m_id)
            on update cascade on delete cascade
);

create index m_id
    on review (m_id);

create index o_id
    on review (o_id);

