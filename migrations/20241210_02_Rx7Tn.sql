-- 
-- depends: 20241210_01_elYEA

create table sign_form
(
    id                       uuid      default uuid_generate_v4() not null,
    timestamp                timestamp default now() not null,
    name                     varchar not null,
    phone                    varchar not null,
    status_publish_msg_redis boolean not null
);