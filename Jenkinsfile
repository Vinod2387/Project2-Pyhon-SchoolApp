pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'git-cred', url: 'https://github.com/Vinod2387/Project2-Pyhon-SchoolApp.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --break-system-packages -r requirements.txt
                '''
            }
        }

        // stage('Lint') {
        //     steps {
        //         sh '''
        //             source venv/bin/activate
        //             flake8 . --exclude=venv
        //         '''
        //     }
        // }

        stage('Unit Tests') {
           steps {
             sh '''
                . venv/bin/activate
                export DJANGO_SETTINGS_MODULE=schoolapp.settings
                pytest
             '''
            }
        } 

        stage('Build Package') {
            steps {
                sh 'source venv/bin/activate && python setup.py sdist bdist_wheel'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution complete.'
        }
    }
}
