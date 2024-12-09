create table feedback
(
    id                          uuid      default uuid_generate_v4() not null,
    timestamp                   timestamp default now()              not null,
    phone                       varchar                              not null,
    email                       varchar,
    message                     text                                 not null,
    name                        varchar                              not null,
    status_publish_msg_in_redis boolean                              not null
);

alter table feedback
    owner to db_admin;

create index feedback_phone_index
    on feedback (phone);


create table sign_form
(
    id                       uuid      default uuid_generate_v4() not null
        constraint sign_form_pk
            primary key,
    timestamp                timestamp default now()              not null,
    name                     varchar                              not null,
    phone                    varchar                              not null,
    status_publish_msg_redis boolean                              not null
);

alter table sign_form
    owner to db_admin;

create index sign_form_phone_index
    on sign_form (phone);

