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

insert into hashtag(hash_id, text, frequency) VALUES (1, '#DontTellToby', 5) --done
insert into hashtag(hash_id, text, frequency) VALUES (2, '#DwightRegionalManager', 1) --done
insert into hashtag(hash_id, text, frequency) VALUES (3, '#GoingToSandalsJamaica', 1) --done
insert into hashtag(hash_id, text, frequency) VALUES (7, '#AssistantTOTHERegionalManager', 4) --done
insert into hashtag(hash_id, text, frequency) VALUES (8, '#MichealComeBack', 2) --done

CREATE TABLE message(
	msg_id serial primary key, --message id
	text varchar, --message text
	likes int, --message likes
	dislikes int, --message dislikes
	date date, --message date
	time time, --message time
	person_id int references person(person_id), --user that sent the message
	gchat_id int references group_chat(gchat_id)); --group chat where it was sent

insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (1, 'Hey guys!', 2, 0, '2018-03-01', '07:30:13', 1, 1);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (2, '#DontTellToby', 1, 5, '2018-03-01', '07:30:40', 1, 1);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (3, 'Lets throw a dinner party!. Also Im #GoingToSandalsJamaica in summer with my boss thats also my girlfriend', 0, 0, '2018-03-01', '07:31:02', 1, 1);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (4, 'Wow... #DontTellToby seriously Micheal?', 3, 0, '2018-03-01', '07:31:10', 2, 1);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (5, 'Yeah I think thats a bit too much... #DontTellToby ???', 0, 0, '2018-03-01', '07:31:20', 3, 1);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (6, 'You shouldnt be so harsh on him' , 0, 1, '2018-03-01', '07:31:30', 3, 1);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (7, 'Yeah well whatever... he sucks', 0, 2, '2018-03-01', '07:31:50', 1, 1);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (8, 'HAHAH MICHEAL COMEDIC GENIUS! #DontTellToby hahaahahah', 1, 0, '2018-03-01', '07:32:00', 4, 1);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (9, 'Ill bring Mose #DontTellToby', 0, 5, '2018-03-01', '07:32:13', 4, 1);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (10, 'NO dwight... no', 5, 0, '2018-03-01', '07:32:20', 1, 1);

insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (11, 'So what are we bringing for the party?', 1, 0, '2018-03-01', '09:17:00', 5, 2);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (12, 'Cake?', 3, 1, '2018-03-01', '09:17:30', 3, 2);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (13, 'EW NO!', 0, 0, '2018-03-01', '09:18:00', 5, 2);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (14, 'We should ask Ryan', 0, 4, '2018-03-01', '09:18:30', 8, 2);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (15, 'Hes not in the party planning comittee Kelly', 2, 0, '2018-03-01', '09:19:00', 10, 2);

insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (16, ' Hi Micheal, I was thinking about #DwightRegionalManager... what do you', 0, 1, '2018-03-01', '09:18:30', 6, 3);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (17, 'SHUTUP TOBY. DONT TYPE ANYMORE', 0, 0, '2018-03-01', '09:18:35', 1, 3);

insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (18, 'I love you!', 1, 0, '2018-03-01', '09:18:35', 2, 4);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (19, 'Me too <3', 1, 0, '2018-03-01', '09:18:55', 3, 4);

insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (20, 'I miss Micheal. #MichealComeBack', 2, 0, '2018-03-01', '12:30:00', 2, 5);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (21, 'Me too T.T #MichealComeBack', 1, 0, '2018-03-01', '12:31:00', 4, 5);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (22, 'What does T.T mean Dwight...', 0, 1, '2018-03-01', '12:32:00', 3, 5);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (23, 'Its a crying face, Koreans used it in the ancient wars agaisnt the japanese', 0, 0, '2018-03-01', '12:33:00', 4, 5);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (24, 'What do you guys think of me being the Regional Manager?', 0, 0, '2018-03-01', '12:34:00', 4, 5);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (25, 'Youll forever remain #AssistantTOTHERegionalManager', 0, 1, '2018-03-01', '12:35:00', 2, 5);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (26, 'Yup... #AssistantTOTHERegionalManager (:', 0, 1, '2018-03-01', '12:36:00', 3, 5);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (27, 'How dare yee create such defamatory hashtag... #AssistantTOTHERegionalManager ... Ill get you fired JIM', 1, 0, '2018-03-01', '12:37:00', 4, 5);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (28, 'I kinda like it actually... #AssistantTOTHERegionalManager', 1, 1, '2018-03-01', '12:38:00', 5, 5);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (29, 'Now that you say it... Me too HAha', 1, 0, '2018-03-01', '12:39:00', 4, 5);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (30, 'jesus...', 0, 1, '2018-03-01', '12:40:00', 2, 5);

insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (31, 'Love me Ryan! I prefer to die if youre not with me...', 0, 0, '2018-03-01', '12:34:00', 8, 6);
insert into message(msg_id, text, likes, dislikes, date, time, person_id, gchat_id) VALUES (32, 'No Kelly this is not meant to be', 0, 1, '2018-03-01', '12:35:00', 9, 6);




CREATE TABLE group_chat(
	gchat_id int serial primary key, --group chat id
	gchat_name varchar(12), --group chat name
	person_id int references person(person_id)); --owner of group chat

insert into group_chat(gchat_name, person_id) VALUES ('DinnerParty', 1); --1
insert into group_chat(gchat_name, person_id) VALUES ('PartyPlanning', 5); --2
insert into group_chat(gchat_name, person_id) VALUES ('NOOO', 6); --3
insert into group_chat(gchat_name, person_id) VALUES ('P&J', 3); --4
insert into group_chat(gchat_name, person_id) VALUES ('PostMichael', 4); --5
insert into group_chat(gchat_name, person_id) VALUES ('LoveMe', 8); --6


CREATE TABLE person(
	person_id int serial primary key, --user id
	first_name varchar(50), --user first name
	last_name varchar(50), --user last name
	email unique string, --user email
	phone unique char(10), --user phone
	password varchar(50)); --user password

insert into person(first_name, last_name, email, phone, password) VALUES ('Michael', 'Scott', 'scott@dunder.com', '7871234567', 'boobz');  --1
insert into person(first_name, last_name, email, phone, password) VALUES ('Jim', 'Halpert', 'halpert@dunder.com', '7870987654', 'cece'); --2
insert into person(first_name, last_name, email, phone, password) VALUES ('Pam', 'Beesly', 'beesly@dunder.com', '7874563728', 'art'); --3
insert into person(first_name, last_name, email, phone, password) VALUES ('Dwight', 'Schrute', 'schrute@dunder.com', '7870000123', 'beets'); --4
insert into person(first_name, last_name, email, phone, password) VALUES ('Angela', 'Martin', 'martin@dunder.com', '7877777777', 'cats'); --5
insert into person(first_name, last_name, email, phone, password) VALUES ('Toby', 'Flenderson', 'loser@dunder.com', '7876668909', 'strangle'); --6
insert into person(first_name, last_name, email, phone, password) VALUES ('Kevin', 'Malone', 'malone@dunder.com', '7870696969', 'ashton'); --7
insert into person(first_name, last_name, email, phone, password) VALUES ('Kelly', 'Kapoor', 'kapoor@dunder.com', '7873436574', 'ryan'); --8
insert into person(first_name, last_name, email, phone, password) VALUES ('Ryan', 'Howard', 'howard@dunder.com', '7870908787', 'fraud'); --9
insert into person(first_name, last_name, email, phone, password) VALUES ('Phyllis', 'Vance', 'vance@dunder.com', '7874541212', 'rainyday'); --10


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
