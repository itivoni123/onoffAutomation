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
        stage('Install Apps') {
            steps {
                sh 'sleep 5'
                sh 'pwd'
                sh 'cd /var/jenkins_home/workspace/run-bash'
                sh 'sudo apt-get update'
                sh 'sudo apt-get install python3'
            }
        }
        stage('Tests') {
            steps {
                sh 'pytest -v -s -k test_create_task --url=https://todo.pixegami.io/'
                sh 'pytest -v -s -k test_update_task --url=https://todo.pixegami.io/'
                sh 'pytest -v -s -k test_delete_task --url=https://todo.pixegami.io/'
                sh 'pytest -v -s -k test_list_tasks --url=https://todo.pixegami.io/'
                sh 'pytest -v -s -k test_get_data --url=https://todo.pixegami.io/'
            }
        }
    }
}
