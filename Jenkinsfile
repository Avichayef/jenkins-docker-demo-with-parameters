pipeline {
    agent any
    
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
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        ANSIBLE_SUDO_PASS = credentials('ansible_sudo_pass')  // Changed from 'ansible-sudo-password'
        SERVICE_PATH = "./docker/${params.SERVICE_NAME}"
    }

    stages {
        stage('Deploy with Ansible') {
            steps {
                script {
                    sh """
                        ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook ansible/deploy-playbook.yml \
                        -i ansible/inventory.ini \
                        -e "service_name=${params.SERVICE_NAME}" \
                        -e "docker_tag=${params.DOCKER_TAG}" \
                        -e "dockerhub_username=${params.DOCKERHUB_USERNAME}" \
                        -e "ansible_become_password=${ANSIBLE_SUDO_PASS}"
                    """
                }
            }
        }
    }

    post {
        always {
            node('any') {
                sh 'docker logout'
            }
        }
    }
}