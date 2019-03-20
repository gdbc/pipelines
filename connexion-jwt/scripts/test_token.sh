TOKEN="YWRtaW46c2VjcmV0"
USER='graeme'
JWT=$(curl -X GET "http://localhost:8080/getjwt" -H "accept: text/plain" -H "Authorization: Basic $TOKEN")
echo ""

echo "JWT is $JWT"

echo ""

curl -X GET "http://dhost:8080/createdb" -H "accept: text/plain" -H "Authorization: Bearer $JWT"
echo ""

curl -X GET "http://dhost:8080/get_user_envs/$USER" -H "accept: text/plain" -H "Authorization: Bearer $JWT"
echo ""

curl -X GET "http://dhost:8080/get_jwt_user" -H "accept: text/plain" -H "Authorization: Bearer $JWT"

