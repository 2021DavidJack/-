SET character_set_client = utf8;
CREATE TABLE `user`(
    `uid` int(10) NOT NULL AUTO_INCREMENT,
    `username` varchar(20) NOT NULL,
    `groupid` tinyint(2) NOT NULL default 2,
    `password` varchar(50) NOT NULL,
    `cookie_token` varchar (50),
    `avatar` varchar(200)  default NULL,
    `avatar_small` varchar(200) default NULL,
    `email` varchar(50) NOT NULL,
    `name` varchar(15) default NULL,
    `reg_time` int(11) NOT NULL default 0,
    `last_login_time` int(11) NOT NULL default 0
)ENGINE = InnoDB DEFAULT CHARSET = utf8 COLLATE = utf8_general_ci;
