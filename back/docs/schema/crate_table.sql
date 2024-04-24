CREATE TABLE user (
    id             int          auto_increment primary key,
    user_id        varchar(11)  not null,
    password       varchar(100) not null,
    privacy_policy varchar(1)	default 'N',
    nickname	   varchar(30)	not null,
    created_at	   datetime		default CURRENT_TIMESTAMP,
    stat           varchar(1)   default 'A'
);