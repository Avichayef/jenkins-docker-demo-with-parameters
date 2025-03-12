pipeline {
    agent any
    
    // Define parameters that will be shown in Jenkins UI
    parameters {
        choice(
            name: 'SERVICE_NAME',
            choices: ['service1', 'service2'],
            description: 'Select the service to deploy'
        )
        string(
            name: 'DOCKER_TAG',
            defaultValue: 'latest',
            description: 'Tag for the Docker image'
        )
        string(
            name: 'DOCKERHUB_USERNAME',
            defaultValue: 'avichaye',
            description: 'DockerHub Username'
        )
    }

    environment {
        // Define environment variables
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        SERVICE_PATH = "./docker/${params.SERVICE_NAME}"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh """
                        docker build -t ${params.DOCKERHUB_USERNAME}/${params.SERVICE_NAME}:${params.DOCKER_TAG} \
                        -f ${SERVICE_PATH}/dockerfile .
                    """
                }
            }
        }

        stage('Login to DockerHub') {
            steps {
                script {
                    // Login to DockerHub
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    // Push the image to DockerHub
                    sh """
                        docker push ${params.DOCKERHUB_USERNAME}/${params.SERVICE_NAME}:${params.DOCKER_TAG}
                    """
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                script {
                    // Run Ansible playbook
                    sh """
                        ansible-playbook ansible/deploy-playbook.yml \
                        -e "service_name=${params.SERVICE_NAME}" \
                        -e "docker_tag=${params.DOCKER_TAG}" \
                        -e "dockerhub_username=${params.DOCKERHUB_USERNAME}"
                    """
                }
            }
        }
    }

    post {
        always {
            // Always logout from DockerHub
            sh 'docker logout'
        }
    }
}