pipeline {
    agent any
    stages {
        stage('preparation') {
            sh 'git clone git@github.com:daovietduy99/sandbox.git'
        }
        stage('validate') {
            steps {
                sh 'terraform validate'
            }
        }
        stage('init') {
            steps {
                sh 'terraform init'
            }
        }
        stage('plan') {
            steps {
                sh 'terraform plan'
            }
        }
    }
}
