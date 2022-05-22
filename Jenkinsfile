pipeline{

    agent any
    stages
    {
        stage('Clone Repo'){
            steps{
                script{
                    if(fileExists('/home/jenkins/.jenkins/workspace/Project2-Pipeline')){
                        sh 'cd Project2-Pipeline && git pull'
                    }
                    else{
                        sh 'git clone https://github.com/BrightBee22/qa-project2.git'
                    }
                }
            }
        }
        stage('Install Requirements for APIs'){
            steps{
                sh 'Project2-Pipeline && pip3 install -r api1/application/requirements.txt'
                sh 'Project2-Pipeline && pip3 install -r api2/application/requirements.txt'
                sh 'Project2-Pipeline && pip3 install -r api3/application/requirements.txt'
                sh 'Project2-Pipeline && pip3 install -r api4/application/requirements.txt'
            }
        }
        stage('Testing'){
            steps{
                sh 'cd Project2-Pipeline/api1 && python3 -m pytest --cov=application'
                sh 'cd Project2-Pipeline/api2 && python3 -m pytest --cov=application'
                sh 'cd Project2-Pipeline/api3 && python3 -m pytest --cov=application'
                sh 'cd Project2-Pipeline/api4 && python3 -m pytest --cov=application'
            }
        }
        stage('Build and Push Images'){
            steps{
                sh 'cd Project2-Pipeline && docker-compose build'
                sh 'cd Project2-Pipeline && docker-compose push'
            }
        }
        stage('App Deployment'){
            steps{
                sh 'cd Project2-Pipeline && docker-compose up -d'
            }
        }
    }
}

