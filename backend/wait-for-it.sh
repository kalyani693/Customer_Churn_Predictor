#!/user/bin/env bash 
hostport=$1
shift
cmd="$@"

host=$(echo $hostport | cut -d:-f1)
port=$(echo $hostport | cut -d:-f2)
until nc -z $host $port;do
 echo "waiting for database..."
 sleep 2
done

echo "Database is up!"
exec $cmd