create table bot_users
(
  user_id        int              not null,
  first_name     varchar (30),
  last_name      varchar (30),
  username       varchar  (50),
  phone          varchar(11),
  registered     timestamp        default current_timestamp,
  primary key (user_id)
);