pipeline {
    agent { label 'windows_clients' }

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

        stage('plan') {
            steps {
                bat 'terraform plan -out=tfplan'
            }
        }
        stage('Terraform apply or destroy ') {
            steps {
                bat 'terraform ${action} tfplan --auto-approve'
            }
        }

        // Add more stages here if needed

    }
}
