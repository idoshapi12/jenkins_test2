pipeline {
    agent any

    options {
    	retry (3)
    }
    parameters {
    	choice(name: 'A', choices: ['1', '2', '3'], description: 'one to three')
    	choice(name: 'B', choices: ['1', '2', '3'], description: 'one to three')
    }
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
            		echo "${params.A} ${params.B} ready to start test"

                   	bat label: '', script: 'py test.py 3 3 test_inputs'
            } 

            post {
            	always {
            		echo "test finished"
            	}
                success {
                    echo "test success"
                }
                failure {
                	echo "test failed"
                }
            }
        }
    }
}
