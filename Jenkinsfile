pipeline {
    agent any

    options {
    	retry (3)
    }
    parameters {
    	choice(name: 'A', choices: ['1', '2', '3'], description: 'one to three')
    	choice(name: 'B', choices: ['1', '2', '3'], description: 'one to three')
    }
    triggers{
        pollSCM('H/2 * * * *')
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
        stage ('tests') {
            parallel {
                stage('Test a') {

                    steps {
                    		echo "${params.B} ready to start test"

                           	bat label: '', script: 'py test.py 3 3 test_inputs'
                    } 

                    post {
                    	always {
                    		echo "test a finished!"
                    	}
                        success {
                            echo "test success!"
                        }
                        failure {
                        	echo "test failed"
                        }
                    }
                }

                stage('Test b') {
                    steps {
                            echo "${params.B} ready to start test"

                            bat label: '', script: 'py test.py 1 3 test_inputs'
                    } 

                    post {
                        always {
                            echo "test b finished!"
                        }
                        success {
                            echo "test success!"
                        }
                        failure {
                            echo "test failed"
                        }
                    }
                }
            }
        }
    }
}

