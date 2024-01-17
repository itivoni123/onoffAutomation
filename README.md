# onoffAutomation

### onoffAutomation is a test environment to check the amazing website musicOnOff 
###The infrastructure includes:
- #### Client test
- #### Backend test

#### Relevant references
- Docker Selenium Grid: https://www.youtube.com/watch?v=jZEFp7-VhmM&list=PLlc_LrU50tliN8PZ7Xk41NwrnelPHchSk
- How to unsinstall Jenkins: https://www.youtube.com/watch?v=TV1hD7Y5iGk
- Jenkins Workspace: /Users/itaytivony/.jenkins/workspace/ 



#### How To Run The Tests
- Validate that you on the right path. For example: /Users/{computer-name}/Desktop/onoffAutomation/automation/e2e
- Run the docker container. For example: docker compose -f docker-compose.yml up -d
- To see the Selenium Grid Instances: http://localhost:4444/ui- 


#### How To Run The Jenkins in Docker
- To create one from scratch run the following command: "docker run -p 8080:8080 -p 5000:5000 -d -v jenkis_home:/var/jenkins_home jenkins/jenkins:lts"
- Then run "docker ps -a" and then run: "docker logs {container_id}" then the password will be shown.
- 