pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git 'https://github.com/idoshapi12/jenkins_test2.git'
            }

            post {
                success {
                    echo "build success"
                }
            }
        }        
        stage('Test') {
            steps {
                   bat label: '', script: 'py script1.py'
            }

            post {

                success {
                    echo "test success"
                }
            }
        }
    }
}
