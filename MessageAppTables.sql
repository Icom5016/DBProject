CREATE TABLE dashboard (
    dash_id int serial primary key, --dashboard id
  date date, --dashboard date
  total_messages int, --total messages in day
  total_replies int, --total replies in day
  total_likes int, --total likes in day
  total_dislikes int, --total dislikes in day
  total_active_users int); --total active users in day

CREATE TABLE hashtag(
	hash_id int serial primary key, --hashtag id
	text string, --hashtag text
	frequency int); --hashtag frequency

insert into hashtag(hash_id, text, frequency) VALUES (1, '#DontTellToby', 5)
insert into hashtag(hash_id, text, frequency) VALUES (2, '#DwightRegionalManager', 1)
insert into hashtag(hash_id, text, frequency) VALUES (3, '#GoingToSandalsJamaica', 2)
insert into hashtag(hash_id, text, frequency) VALUES (6, '#Angela&Dwight', 5)
insert into hashtag(hash_id, text, frequency) VALUES (7, '#AssistantTOTHERegionalManager', 4)
insert into hashtag(hash_id, text, frequency) VALUES (8, '#MichealComeBack', 6)

CREATE TABLE message(
	msg_id int serial primary key, --message id
	text string, --message text
	likes int, --message likes
	dislikes int, --message dislikes
	date date, --message date
	time time, --message time
	person_id int references person(person_id), --user that sent the message
	gchat_id int references group_chat(gcid)); --group chat where it was sent

insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES ()

CREATE TABLE group_chat(
	gchat_id int serial primary key, --group chat id
	gchat_name varchar(12), --group chat name
	person_id int references person(person_id)); --owner of group chat

insert into group_chat(gchat_name, person_id) VALUES ('DinnerParty', 1);
insert into group_chat(gchat_name, person_id) VALUES ('PartyPlanning', 5);
insert into group_chat(gchat_name, person_id) VALUES ('NOOO', 6);
insert into group_chat(gchat_name, person_id) VALUES ('P&J', 3);
insert into group_chat(gchat_name, person_id) VALUES ('PostMichael', 4);
insert into group_chat(gchat_name, person_id) VALUES ('LoveMe', 8);


CREATE TABLE person(
	person_id int serial primary key, --user id
	first_name varchar(50), --user first name
	last_name varchar(50), --user last name
	email unique string, --user email
	phone unique char(10), --user phone
	password varchar(50)); --user password

insert into person(first_name, last_name, email, phone, password) VALUES ('Michael', 'Scott', 'scott@dunder.com', '7871234567', 'boobz');
insert into person(first_name, last_name, email, phone, password) VALUES ('Jim', 'Halpert', 'halpert@dunder.com', '7870987654', 'cece');
insert into person(first_name, last_name, email, phone, password) VALUES ('Pam', 'Beesly', 'beesly@dunder.com', '7874563728', 'art');
insert into person(first_name, last_name, email, phone, password) VALUES ('Dwight', 'Schrute', 'schrute@dunder.com', '7870000123', 'beets');
insert into person(first_name, last_name, email, phone, password) VALUES ('Angela', 'Martin', 'martin@dunder.com', '7877777777', 'cats');
insert into person(first_name, last_name, email, phone, password) VALUES ('Toby', 'Flenderson', 'loser@dunder.com', '7876668909', 'strangle');
insert into person(first_name, last_name, email, phone, password) VALUES ('Kevin', 'Malone', 'malone@dunder.com', '7870696969', 'ashton');
insert into person(first_name, last_name, email, phone, password) VALUES ('Kelly', 'Kapoor', 'kapoor@dunder.com', '7873436574', 'ryan');
insert into person(first_name, last_name, email, phone, password) VALUES ('Ryan', 'Howard', 'howard@dunder.com', '7870908787', 'fraud');
insert into person(first_name, last_name, email, phone, password) VALUES ('Phyllis', 'Vance', 'vance@dunder.com', '7874541212', 'rainyday');


CREATE TABLE contact_list(
	clist_id int serial primary key, --contact list id
	user_id int references User(uid), --contact list owner id
	contact int references User(uid)); --contact id

CREATE TABLE trending (
	dash_id int references dashboard(dash_id), --dashboard id
	hash_id int references hashtag(hash_id), --hashtag id
	primary key (dash_id, hash_id));

CREATE TABLE chat_members(
    member_id serial primary key, --track how many members of chats
	gchat_id int references group_chat(gchat_id), --group chat id
	person_id int references person(person_id), --user id that belongs in group chat
	primary key(gchat_id, person_id));

insert into chat_members(gchat_id, person_id) VALUES (1, 1);
insert into chat_members(gchat_id, person_id) VALUES (1, 2);
insert into chat_members(gchat_id, person_id) VALUES (1, 3);
insert into chat_members(gchat_id, person_id) VALUES (1, 4);
insert into chat_members(gchat_id, person_id) VALUES (1, 5);
insert into chat_members(gchat_id, person_id) VALUES (1, 7);
insert into chat_members(gchat_id, person_id) VALUES (2, 3);
insert into chat_members(gchat_id, person_id) VALUES (2, 5);
insert into chat_members(gchat_id, person_id) VALUES (2, 8);
insert into chat_members(gchat_id, person_id) VALUES (2, 10);
insert into chat_members(gchat_id, person_id) VALUES (3, 1);
insert into chat_members(gchat_id, person_id) VALUES (3, 6);
insert into chat_members(gchat_id, person_id) VALUES (4, 2);
insert into chat_members(gchat_id, person_id) VALUES (4, 3);
insert into chat_members(gchat_id, person_id) VALUES (5, 2);
insert into chat_members(gchat_id, person_id) VALUES (5, 3);
insert into chat_members(gchat_id, person_id) VALUES (5, 4);
insert into chat_members(gchat_id, person_id) VALUES (5, 5);
insert into chat_members(gchat_id, person_id) VALUES (6, 8);
insert into chat_members(gchat_id, person_id) VALUES (6, 9);

CREATE TABLE contains_hashtag(
	hash_id int references hashtag(hash_id), --hashtag id
	mid int references message(msg_id), --message id
	primary key(hash_id, msg_id));

CREATE TABLE likes (
  msg_id int references message(msg_id), --message id
  person_id int references person(person_id), --user id
  primary key(msg_id, person_id));

CREATE TABLE dislikes (
  msg_id int references message(msg_id), --message id
  person_id int references person(person_id), --user id
  primary key(msg_id, person_id));
