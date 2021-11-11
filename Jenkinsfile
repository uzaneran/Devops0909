properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/uzaneran/Devops0909.git"
    }
    stage("show files"){
        sh "ls -l"
    }
}
