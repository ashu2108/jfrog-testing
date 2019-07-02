import os
import sys
out = os.popen('curl -iuadmin:test@1234 -X GET http://13.235.11.202:8081/artifactory/api/security/groups -H "Content-type:application/json" | grep -h name | cut -d ":" -f 2 | tr -d \'" ,\' > jfrog-group.out| comm -1 jfrog-user.out ansible_group_created.out' ).read()
print "the group added in jfrog is " + out
