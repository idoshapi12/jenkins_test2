pipeline {
    agent any

    options {
    	retry (3)
    }
    parametrs {
    	choise{name: 'a', chices {'1', '2', '3'}, description: 'one to three'}
    	choise{name: 'b', chices {'1', '2', '3'}, description: 'one to three'}
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
            		echo "ready to start test"
                   	bat label: '', script: 'py test.py ${a} ${b} test_inputs'
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
