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
        ANSIBLE_SUDO_PASS = credentials('ansible_sudo_pass')
        SERVICE_PATH = "./docker/${params.SERVICE_NAME}"
    }

    stages {
        stage('Deploy with Ansible') {
            steps {
                sh '''
                    ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook ansible/deploy-playbook.yml \
                    -i ansible/inventory.ini \
                    -e "service_name=${SERVICE_NAME}" \
                    -e "docker_tag=${DOCKER_TAG}" \
                    -e "dockerhub_username=${DOCKERHUB_USERNAME}" \
                    -e "dockerhub_password=${DOCKERHUB_CREDENTIALS_PSW}" \
                    -e "ansible_become_password=${ANSIBLE_SUDO_PASS}"
                '''
            }
        }
    }

    post {
        always {
            sh 'docker logout'
        }
    }
}