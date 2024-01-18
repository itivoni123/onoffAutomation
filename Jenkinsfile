pipeline {
    agent any

    stages {
        stage('Chekcout') {
            steps {
                checkout scmGit(branches: [[name: '*/move-conftest']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/itivoni123/onoffAutomation.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'move-conftest', url: 'https://github.com/itivoni123/onoffAutomation.git'
            }
        }
        stage('Tests') {
            steps {
                sh 'pytest -v -s -k test_numbers'
                sh 'pytest -v -s -k test_status_code --url=https://todo.pixegami.io'
            }
        }
    }
}
