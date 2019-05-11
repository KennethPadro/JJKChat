-- Last modification date: 2019-04-05 18:08:03.977

-- tables

-- Table: users
CREATE TABLE users (
    user_id serial PRIMARY KEY,
    first_name varchar(50),
    last_name varchar(50),
    email varchar(50),
    phone varchar(50),
    password varchar(200),
    username varchar(50) UNIQUE
);

-- Table: chat_groups
CREATE TABLE chat_groups (
    chat_group_id serial PRIMARY KEY,
    chat_name varchar(50),
    user_id int REFERENCES users (user_id)
);

-- Table: post
CREATE TABLE post (
    post_id serial PRIMARY KEY,
    media varchar(200),
    message varchar(255)  NULL,
    post_date date,
    chat_group_id int REFERENCES chat_groups (chat_group_id),
    user_id int REFERENCES users (user_id)
);

-- Table: chat_group_members
CREATE TABLE chat_group_members (
    user_id int REFERENCES users (user_id),
    chat_group_id int REFERENCES chat_groups (chat_group_id),
    PRIMARY KEY (user_id,chat_group_id)
);

-- Table: contact
CREATE TABLE contact (
    user_id int REFERENCES users (user_id),
    contact_user_id int REFERENCES users (user_id) ,
    PRIMARY KEY (user_id,contact_user_id)
);

-- Table: hashtags
CREATE TABLE hashtags (
    hashtag_id serial PRIMARY KEY,
    hashtag varchar(50),
    post_id int REFERENCES post (post_id)
);

-- Table: reactions
CREATE TABLE reactions (
    reaction varchar(10),
    user_id int REFERENCES users (user_id),
    post_id int REFERENCES post (post_id),
    reaction_date date,
    PRIMARY KEY (user_id,post_id)
);

-- Table: reply
CREATE TABLE reply (
    reply_id serial PRIMARY KEY,
    reply_date date,
    reply_message varchar(255),
    post_id int REFERENCES post (post_id),
    user_id int REFERENCES users (user_id)
);


INSERT INTO users (first_name, last_name, email, phone, password, username) VALUES('Kenneth', 'Padro', 'Kenneth.padro@upr.edu', '7876083112', 'noteimporta', 'kpadro');
INSERT INTO users (first_name, last_name, email, phone, password, username) VALUES('Joshua', 'Bonilla', 'joshua.bonilla@upr.edu', '7876083112', 'noteimporta', 'jbonilla');
INSERT INTO users (first_name, last_name, email, phone, password, username) VALUES('Jesiniel', 'Nieves', 'jesiniel.nieves@upr.edu', '7876083112', 'noteimporta', 'jnieves');

INSERT INTO chat_groups (chat_name, user_id) VALUES('Admin Chat', 1);
INSERT INTO chat_groups (chat_name, user_id) VALUES('Los bananeros', 2);
INSERT INTO chat_groups (chat_name, user_id) VALUES('Avengers', 1);

INSERT INTO chat_group_members (user_id, chat_group_id) VALUES (1, 1);
INSERT INTO chat_group_members (user_id, chat_group_id) VALUES (1, 3);
INSERT INTO chat_group_members (user_id, chat_group_id) VALUES (2, 3);

INSERT INTO post (media, message, post_date, chat_group_id, user_id) VALUES('/testimage.png','Esto esta crapiau #acho', NOW(), 1, 1);
INSERT INTO post (media, message, post_date, chat_group_id, user_id) VALUES('/test2image.png','Que cool funciona!', now(), 1, 2);
INSERT INTO post (media, message, post_date, chat_group_id, user_id) VALUES('/test3image.png','haciendo la diferencia', '03/03/2019', 3, 3);

INSERT INTO contact (user_id, contact_user_id) VALUES(1, 2);
INSERT INTO contact (user_id, contact_user_id) VALUES(2, 1);

INSERT INTO hashtags (hashtag, post_id) VALUES('#acho', 1);

INSERT INTO reactions (reaction, user_id, post_id, reaction_date) VALUES('like', 2, 1, now());

INSERT INTO reply (reply_date, reply_message, post_id, user_id) VALUES(now(), 'Saludos a todos los presentes en esta noche tan majestuosa', 1, 2)
