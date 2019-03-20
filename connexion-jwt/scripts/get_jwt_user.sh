TOKEN="YWRtaW46c2VjcmV0"
USER='graeme'
JWT=$(curl -s -X GET "http://localhost:8080/getjwt" -H "accept: text/plain" -H "Authorization: Basic $TOKEN")

JWTUSER=$(curl -s -X GET "http://dhost:8080/get_jwt_user" -H "accept: text/plain" -H "Authorization: Bearer $JWT")

echo $JWTUSER
