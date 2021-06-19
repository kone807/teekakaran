create table candidate_submission
(
    s_id               int auto_increment
        primary key,
    s_name             varchar(30)  not null,
    s_file_length_sec  int          not null,
    s_file_size        float(10, 2) not null,
    s_type             varchar(30)  not null,
    s_file_upload_path varchar(50)  not null,
    s_submission_date  date         not null,
    c_id               int          null,
    p_id               int          null,
    constraint candidate_submission_ibfk_1
        foreign key (c_id) references candidate (c_id)
            on update cascade on delete cascade,
    constraint candidate_submission_ibfk_2
        foreign key (p_id) references panelist (p_id)
            on update cascade on delete cascade
);

create index c_id
    on candidate_submission (c_id);

create index p_id
    on candidate_submission (p_id);

