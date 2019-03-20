TOKEN="YWRtaW46c2VjcmV0"
USER='admin'
JWT=$(curl -X GET "http://localhost:8080/getjwt" -H "accept: text/plain" -H "Authorization: Basic $TOKEN")
echo ""

echo "JWT is $JWT"
