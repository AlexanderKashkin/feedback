-- create table feedback
-- depends: 

create table feedback
(
    id                          uuid      default uuid_generate_v4() not null,
    timestamp                   timestamp default now() not null,
    phone                       varchar not null,
    email                       varchar,
    message                     text not null,
    name                        varchar not null,
    status_publish_msg_in_redis boolean not null
);
