pipeline {
    agent any
    stages {
        // stage('preparation') {
        //     sh 'git clone git@github.com:daovietduy99/sandbox.git'
        // }
        stage('init') {
            steps {
                sh 'terraform init'
            }
        }
        stage('validate') {
            steps {
                sh 'terraform validate'
            }
        }
        stage('plan') {
            steps {
                sh 'terraform plan'
            }
        }
    }
}
