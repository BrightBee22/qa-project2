pipeline{

    agent any
    stages
    {
        stage('Clone Repo'){
            steps{
                script{
                    if(fileExists('/home/jenkins/.jenkins/workspace/qa-project2')){
                        sh 'cd QA-practical-assessment && git pull'
                    }
                    else{
                        sh 'git clone git@github.com:BrightBee22/qa-project2.git '
                    }
                }
            }
        }
        stage('Install Requirements for APIs'){
            steps{
                sh 'qa-project2 && pip3 install -r api1/application/requirements.txt'
                sh 'qa-project2 && pip3 install -r api2/application/requirements.txt'
                sh 'qa-project2 && pip3 install -r api3/application/requirements.txt'
                sh 'qa-project2 && pip3 install -r api4/application/requirements.txt'
            }
        }
        stage('Testing'){
            steps{
                sh 'cd qa-project2/api1 && python3 -m pytest --cov=application'
                sh 'cd qa-project2/api2 && python3 -m pytest --cov=application'
                sh 'cd qa-project2/api3 && python3 -m pytest --cov=application'
                sh 'cd qa-project2/api4 && python3 -m pytest --cov=application'
            }
        }
        stage('Build and Push Images'){
            steps{
                sh 'cd qa-project2 && docker-compose build'
                sh 'cd qa-project2 && docker-compose push'
            }
        }
        stage('App Deployment'){
            steps{
                sh 'cd qa-project2 && docker-compose up -d'
            }