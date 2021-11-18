pipeline {
  agent any

  stages {
stage('PR ONLY - Install App Dependencies') {
      when {
        not {
          anyOf{
            branch 'master'
          }
        }
      }
      steps {
        _sh """
        echo 'installing app build requirements'
        cd yason
        pip install virtualenv
        virtualenv victor
        ls
        source victor/bin/activate
        pip install -r ../requirements.txt
        """
      }
    }

    stage('PR ONLY - test') {
      when {
        not {
          anyOf{
            branch 'master'
          }
        }
      }
      steps {
        sh 'echo "testing the code"'
        sh 'python yason/manage.py test'
      }  
    }

    stage('PR ONLY - Build Image') {
      when {
        not {
          anyOf{
            branch 'master'
          }
        }
      }
      steps {
        sh 'echo "docker build phase"'
        sh 'docker build  -f ./Dockerfile -t sysadminexe/yason:V${BUILD_NUMBER} .'
        sh 'docker rmi sysadminexe/yason:V${BUILD_NUMBER}'
      }
    }

    stage('Install App Dependencies') {
        when {
          anyOf {
            branch 'master'
          }
        }
        steps {
          _sh """
          echo 'installing app build requirements'
          cd yason
          pip install virtualenv
          virtualenv victor
          ls
          source victor/bin/activate
          pip install -r ../requirements.txt
          """
        }
      }

    stage('test') {
      when {
        anyOf {
          branch 'master'
        }
      }
      steps {
        sh 'echo "testing the code"'
        sh 'python yason/manage.py test'
      }  
    }

    stage('Build Image') {
      when {
        anyOf {
          branch 'master'
        }
      }
      steps {
        sh 'echo "docker build phase"'
        sh 'docker build  -f ./Dockerfile -t sysadminexe/yason:V${BUILD_NUMBER} .'
      }
    }

    stage('Push Image') {
      when {
        anyOf {
          branch 'master'
        }
      }
      steps{
        sh 'echo "Pushing Image to Docker Hub"'
        sh 'docker push sysadminexe/yason:V${BUILD_NUMBER} '
        sh 'docker rmi sysadminexe/yason:V${BUILD_NUMBER} '
      }
    } 

    stage('Deploy to server') {
      when {
        anyOf {
          branch 'master'
        }
      }
      steps{
        //script to deploy the docker image goes here
        echo "this little light of mine"
      }
    }  
  }
}

def _sh (shell_command) {
  sh """
  #!/bin/bash -e
  $shell_command
  """
}