--User table
create table person(person_id serial primary key, first_name varchar(10), last_name varchar(10),
email varchar(30), phone varchar(10), password varchar(10), username varchar(10));

--Group Chat  & Chat Member tables
create table group_chat(gchat_id serial primary key, gchat_name varchar(20),
 person_id int references person(person_id));

create table chat_members(member_id serial primary key,
 gchat_id int references group_chat(gchat_id), person_id int references person(person_id));

--Contact List & Contacts tables
create table contact_list(clist_id serial primary key,
 person_id int references person(person_id));

create table contacts(contact_id serial primary key, clist_id int references
 contact_list(clist_id), person_id int references person(person_id));

--Hashtag table
create table Hashtag(hash_id serial primary key, hash_text varchar, msg_id int references message(msg_id));

--Message & Reply tables
create table message(msg_id serial primary key, text varchar, likes int, dislikes int, date date,
 time time, person_id int references person(person_id),gchat_id int references group_chat(gchat_id), username varchar(10));

create table reply(repy_id serial primary key, original_id int references message(msg_id),
 msg_id int references message(msg_id));

--Reaction (like/dislike) table
create table react(react_id serial primary key, likes boolean, dislikes boolean,
 person_id int references person(person_id), msg_id int references message(msg_id));