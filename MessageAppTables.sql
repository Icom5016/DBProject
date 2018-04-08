CREATE TABLE Dashboard (
	dash_id int serial primary key, --dashboard id
  date date, --dashboard date
  total_messages int, --total messages in day
  total_replies int, --total replies in day
  total_likes int, --total likes in day
  total_dislikes int, --total dislikes in day
  total_active_users int); --total active users in day

CREATE TABLE Hashtag(
	hash_id int serial primary key, --hashtag id
	text string, --hashtag text
	frequency int); --hashtag frequency

CREATE TABLE Message(
	msgid int serial primary key, --message id
	text string, --message text
	likes int, --message likes
	dislikes int, --message dislikes
	date date, --message date
	time time, --message time
	user_id int references User(uid), --user that sent the message
	gchat_id int references Group_Chat(gcid)); --group chat where it was sent

CREATE TABLE Group_Chat(
	gchat_id int serial primary key, --group chat id
	gchat_name varchar(12), --group chat name
	user_id int references User(uid)); --owner of group chat

CREATE TABLE User(
	user_id int serial primary key, --user id
	first_name varchar(50), --user first name
	last_name varchar(50), --user last name
	email unique string, --user email
	phone unique char(10), --user phone
	username unique varchar(15), --user username
	password varchar(50)); --user password

CREATE TABLE Contact_List(
	clist_id int serial primary key, --contact list id
	user_id int references User(uid), --contact list owner id
	contact int references User(uid)); --contact id

CREATE TABLE Replies (
	original int references Message(mid), --original message
	reply int references Message(mid), --reply message
	primary key(mid, rid));

CREATE TABLE Trending (
	dashid int references Dashboard(sid), --dashboard id
	hashid int references Hashtag(hid), --hashtag id
	primary key (sid, hid));

CREATE TABLE IsAMember(
	gcid int references Group_Chat(gcid), --group chat id
	uid int references User(uid), --user id that belongs in group chat
	primary key(gcid, uid));

CREATE TABLE ContainsHashtag(
	hid int references Hashtag(hid), --hashtag id
	mid int references Message(mid), --message id
	primary key(hid, mid));

CREATE TABLE Likes (
  msgid int references Message(msgid), --message id
  uid int references User(uid), --user id
  primary key(msgid, uid));

CREATE TABLE Dislikes (
  msgid int references Message(msgid), --message id
  uid int references User(uid), --user id
  primary key(msgid, uid));
