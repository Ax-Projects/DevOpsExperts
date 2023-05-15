pipeline {
  agent {
    node {
      label 'laptop'

    }
  environment {
    python = 'C:\\Users\\Orr-Dev\\Documents\\DevOpsExperts\\.venv\\Scripts\\python.exe'
  }

  }
  stages {
    stage('start-backend') {
      parallel {
        stage('start-backend') {
          steps {
            withPythonEnv("C:\\Users\\Orr-Dev\\Documents\\DevOpsExperts\\.venv\\Scripts\\python.exe"){
                bat(script: 'start /min python rest_api.py', returnStdout: true, returnStatus: true)
            }
          }
        }

        stage('start-front') {
          steps {
            withPythonEnv("C:\\Users\\Orr-Dev\\Documents\\DevOpsExperts\\.venv\\Scripts\\python.exe"){
                pybat(script: 'web_app.py', returnStatus: true, returnStdout: true)
            }
          }
        }
      }
    }

    stage('clean-DB') {
      steps {
        bat 'python clean_db.py'
      }
    }

    stage('run-backend-test') {
      steps {
        bat 'python backend_testing.py'
      }
    }

    stage('run-frontend-test') {
      steps {
        bat 'python frontend_testing.py'
      }
    }

    stage('run-combined-tests') {
      steps {
        bat 'python combined_testing.py'
      }
    }

    stage('stop-servers') {
      steps {
        bat 'python clean_environment.py'
      }
    }
  }
}
