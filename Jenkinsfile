#!/bin/bash
pipeline{

    agent any
    stages
    {
        stage('Clone Repo'){
            steps{
                script{
                    if(fileExists('/home/jenkins/.jenkins/workspace/qa-project2')){
                        dir('qa-project2'){ sh 'git pull https://github.com/BrightBee22/qa-project2.git main'}
                    }
                    else{
                        sh 'git clone https://github.com/BrightBee22/qa-project2.git'
                    }
                }
            }
        }
        stage('Install Requirements for APIs'){
            steps{
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Testing'){
            steps{
                sh 'cd api1 && python3 -m pytest --cov=application'
                sh 'cd api2 && python3 -m pytest --cov=application'
                sh 'cd api3 && python3 -m pytest --cov=application'
                sh 'cd api4 && python3 -m pytest --cov=application'
            }
        }
        stage('Build and Push Images'){
            steps{
                sh 'docker-compose build'
                sh 'docker-compose push'
            }
        }
        stage('App Deployment'){
            steps{
                sh 'docker-compose up -d'
            }
        }
    }
}

