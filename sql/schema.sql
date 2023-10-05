CREATE TABLE "stats" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL UNIQUE,
	"amount"	INTEGER NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
PRAGMA database_list;
SELECT type,name,sql,tbl_name FROM "main".sqlite_master;
PRAGMA collation_list;
SAVEPOINT "db4s_edittable_1696488260483746";
CREATE TABLE "users" (
	"discord_id"	TEXT NOT NULL UNIQUE,
	"username"	TEXT NOT NULL UNIQUE,
	"points"	INTEGER NOT NULL DEFAULT 0 UNIQUE,
	PRIMARY KEY("discord_id")
);
PRAGMA database_list;
SELECT type,name,sql,tbl_name FROM "main".sqlite_master;