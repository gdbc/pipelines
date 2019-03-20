TOKEN="YWRtaW46c2VjcmV0"
USER=$1
JWT=$(curl -s -X GET "http://localhost:8080/getjwt" -H "accept: text/plain" -H "Authorization: Basic $TOKEN")

APPS=$(curl -s -X GET "http://dhost:8080/get_user_app/$USER" -H "accept: text/plain" -H "Authorization: Bearer $JWT") 

echo $APPS
