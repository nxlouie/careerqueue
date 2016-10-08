#!/bin/bash
#FILE: reset_sql.sh

DB_NAME=cq_db

SQL_DB=../sql/db_init.sql
SQL_CREATE=../sql/tbl_create.sql
SQL_LOAD=../sql/load_data.sql


echo "Resetting SQL database..."
SQL_QUERY="source $SQL_DB; use $DB_NAME; source $SQL_CREATE; source $SQL_LOAD;"
mysql -u root -p -e "$SQL_QUERY"
echo "Done."
