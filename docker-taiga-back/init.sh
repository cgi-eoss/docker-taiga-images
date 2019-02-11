#!/bin/bash

set -x

TAIGA_BACK_ROOT="/taiga/taiga-back"

cd ${TAIGA_BACK_ROOT} && source /taiga/virtualenv/bin/activate

# Setup database automatically if needed
echo "Running database check"
python /taiga/checkdb.py
DB_CHECK_STATUS=$?

if [ $DB_CHECK_STATUS -eq 1 ]; then
    echo "Failed to connect to database server or database does not exist."
    exit 1
elif [ $DB_CHECK_STATUS -eq 2 ]; then
    echo "Configuring initial database"
    python manage.py migrate --noinput
    python manage.py loaddata initial_user
    python manage.py loaddata initial_project_templates
    python manage.py collectstatic --noinput
    python manage.py compilemessages
else
    echo "Database already configured"
fi
