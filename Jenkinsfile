pipeline {
    agent any

    stages {
        stage('Chekcout') {
            steps {
                checkout scmGit(branches: [[name: '*/backend-tests']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/itivoni123/onoffAutomation.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'backend-tests', url: 'https://github.com/itivoni123/onoffAutomation.git'
            }
        }
        stage('Tests') {
            steps {
                sh 'pytest -v -s -k test_numbers'
                sh 'pytest -v -s -k test_update_task --url=https://todo.pixegami.io/'
            }
        }
    }
}
