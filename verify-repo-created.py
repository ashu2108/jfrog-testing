import os
import sys
out = os.popen('curl -iuadmin:test@1234 -X GET http://13.235.11.202:8081/artifactory/api/repositories -H "Content-type:application/json" | grep -h name | cut -d ":" -f 2 | tr -d \'" ,\' > jfrog-repo.out| comm -1 jfrog-repo.out ansible_repo_created.out' ).read()
print "the repo added in jfrog is " + out
