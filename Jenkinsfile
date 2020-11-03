pipeline { 
    environment { 
        registry = "flask-jenkins-docker-cicd" 
        registryCredential = 'dockerhub_id' 
        dockerImage = '' 
    }
    agent any 
    stages { 
        stage('Cloning our Git') { 
            steps { 
                git 'https://github.com/himanshunikhare/flask-docker-jenkins-connectivity.git' 
                echo "Cloned"

            }
        } 
        stage('Building our image') { 
            steps { 
                script { 
                    dockerImage = docker.build registry + ":$BUILD_NUMBER" 
                }
                echo "Image Build"
            } 
        }
        stage('Deploy our image') { 
            steps { 
                script { 
                    withDockerRegistry([ credentialsId: registryCredential, url: "" ])
                    docker.withRegistry( '', registryCredential ) { 
                        dockerImage.push() 
                    }
                echo "Image Deployed"
                } 
            }
        } 
        
        stage('Cleaning up') { 
            steps { 
                sh "docker rmi $registry:$BUILD_NUMBER" 
                echo "Cleanup complete"
            }
        } 
        
    }
}
