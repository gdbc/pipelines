TOKEN="YWRtaW46c2VjcmV0"
JWT=$(curl -s -X GET "http://localhost:8080/getjwt" -H "accept: text/plain" -H "Authorization: Basic $TOKEN")

ENVS=$(curl -s -X GET "http://localhost:8080/get_apps" -H "accept: text/plain" -H "Authorization: Bearer $JWT") 

echo $ENVS
