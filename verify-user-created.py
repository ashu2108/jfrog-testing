import os
import sys
out = os.popen('curl -iuadmin:test@1234 -X GET http://13.235.11.202:8081/artifactory/api/security/users -H "Content-type:application/json"| grep -h name | cut -d ":" -f 2 | tr -d \'" ,\' > jfrog-user.out| comm -1 jfrog-user.out ansible_user_created.out' ).read()
print "the user added in jfrog is"+out
