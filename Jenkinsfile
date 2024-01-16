pipeline {
    agent {
        docker {
            image 'docker:dind'
            privileged true
        }
    stages {
        stage("verify tooling") {
            steps {
                sh '''
                  docker version
                  docker info
                '''
            }
        }
    }
}