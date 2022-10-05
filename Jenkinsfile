pipeline {
    agent any
    stages {
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
