#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('data.db')

print "Opened database successfully";

conn.execute('''CREATE TABLE WALL
       (ID	INTEGER	PRIMARY KEY	AUTOINCREMENT,
       NAME	TEXT	NOT NULL
	   );''')
	   
conn.execute('''CREATE TABLE SCENARIO
       (ID	INTEGER	PRIMARY KEY	AUTOINCREMENT,
	   WALL_ID	INTEGER	NOT NULL,	
       NAME	TEXT	NOT NULL,
	   FOREIGN KEY(WALL_ID) REFERENCES WALL(ID)
	   );''')

conn.execute('''CREATE TABLE SCREEN 
       (ID	INTEGER	PRIMARY KEY	AUTOINCREMENT,
       DISPLAYED_SIZE	TEXT	NOT NULL,
	   HEIGHT	TEXT	NOT NULL,
	   WIDTH	TEXT	NOT NULL
	   );''')	   
	   
conn.execute('''CREATE TABLE USER
       (ID	INTEGER	PRIMARY KEY	AUTOINCREMENT,
       NAME	TEXT	NOT NULL,
	   PASSWORD	TEXT	NOT NULL
	   );''')

conn.execute('''CREATE TABLE USER_HAS_WALL
       (USER_ID	INTEGER	NOT NULL,	
       WALL_ID	INTEGER	NOT NULL,
	   PRIMARY KEY ( USER_ID, WALL_ID),
	   FOREIGN KEY(USER_ID) REFERENCES USER(ID),
	   FOREIGN KEY(WALL_ID) REFERENCES WALL(ID)
	   );''')
	  
conn.execute('''CREATE TABLE USER_HAS_SCENARIO
       (USER_ID	INTEGER	NOT NULL,
       SCENARIO_ID	INTEGER	NOT NULL,
	   PRIMARY KEY ( USER_ID, SCENARIO_ID),
	   FOREIGN KEY(USER_ID) REFERENCES USER(ID),
	   FOREIGN KEY(SCENARIO_ID) REFERENCES SCENARIO(ID)
	   );''')

conn.execute('''CREATE TABLE WALL_HAS_SCREEN
       (ID	INTEGER	PRIMARY KEY	AUTOINCREMENT,
	   SCREEN_ID	INTEGER	NOT NULL,	
       WALL_ID	INTEGER	NOT NULL,
	   POSITION	INTEGER	NOT NULL,
	   FOREIGN KEY(SCREEN_ID) REFERENCES SCREEN(ID),
	   FOREIGN KEY(WALL_ID) REFERENCES WALL(ID)
	   );''')
	   
conn.execute('''CREATE TABLE SCENARIO_HAS_WALL_HAS_SCREEN
       (WALL_HAS_SCREEN_ID	INTEGER	NOT NULL,	
       SCENARIO_ID	INTEGER	NOT NULL,
	   MEDIA_PATH	TEXT	NOT NULL,
	   AREA_COLOR	TEXT	NOT NULL,
	   IS_MASTER	INTEGER	NOT NULL,
	   PRIMARY KEY ( WALL_HAS_SCREEN_ID, SCENARIO_ID),
	   FOREIGN KEY(WALL_HAS_SCREEN_ID) REFERENCES WALL_HAS_SCREEN(ID),
	   FOREIGN KEY(SCENARIO_ID) REFERENCES SCENARIO(ID)
	   );''')

	   
print "Opened database successfully";

conn.close()