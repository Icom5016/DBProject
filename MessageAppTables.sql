CREATE TABLE Dashboard (
	sid int serial primary key,
    date date, 
    total_messages int, 
    total_replies int, 
    total_likes int, 
    total_dislikes int, 
    total_active_users int);

CREATE TABLE Hashtag(
	hid int serial primary key, 
	text string, 
	frequency int);

CREATE TABLE Message(
	mid int serial primary key, 
	text string, 
	likes int, 
	dislikes int, 
	sentby int references User(uid), 
	cgid int references Group_Chat(gcid),
	date string);

CREATE TABLE Group_Chat(
	gcid int serial primary key, 
	gcname varchar(12), 
	gcownerid int references User(uid));

CREATE TABLE User(
	uid int serial primary key, 
	firstname varchar(10), 
	lastname varchar(10), 
	email string, 
	phone varchar(10));

CREATE TABLE Contact_List(
	clid int serial primary key, 
	uid int references User(uid), 
	contact int, 
	primary key(uid, contact));

CREATE TABLE Replies (
	original int references Message(mid), 
	reply int references Message(mid), 
	primary key(mid, rid));

CREATE TABLE Trending (
	sid int references Dashboard(sid), 
	hid int references Hashtag(hid), 
	primary key (sid, hid));

CREATE TABLE Has_User(
	gcid int references Group_Chat(gcid), 
	uid int references User(uid), 
	primary key(gcid, uid));

CREATE TABLE Has_Hashtag(
	hid int references Hashtag(hid), 
	mid int references Message(mid), 
	primary key(hid, mid));
