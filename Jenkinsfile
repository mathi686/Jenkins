pipeline {
    agent any

    stages {
        stage('GIT Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/mathi686/Jenkins.git'
            }
        }

        stage('Terraform Init') {
            steps {
                bat 'terraform init'
            }
        }

        // Add more stages here if needed

    }
}
