pipeline {
    agent any

    stages {
        stage('GIT') {
            steps {
                git branch: 'main', url: 'https://github.com/mathi686/Jenkins.git'
            }
        }
        stages {
        stage('init') {
            steps {
                bat 'terraform init'
            }
        }
//         stages {
//         stage('GIT') {
//             steps {
//                 git branch: 'main', url: 'https://github.com/mathi686/Jenkins.git'
//             }
//         }
//         stages {
//         stage('GIT') {
//             steps {
//                 git branch: 'main', url: 'https://github.com/mathi686/Jenkins.git'
//             }
//         }
    }
}
}