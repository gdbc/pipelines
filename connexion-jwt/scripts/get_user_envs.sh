TOKEN="YWRtaW46c2VjcmV0"
USER=$1
JWT=$(curl -s -X GET "http://localhost:8080/getjwt" -H "accept: text/plain" -H "Authorization: Basic $TOKEN")

ENVS=$(curl -s -X GET "http://dhost:8080/get_user_envs/$USER" -H "accept: text/plain" -H "Authorization: Bearer $JWT") 

echo $ENVS
