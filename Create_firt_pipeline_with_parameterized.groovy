properties([parameters([string(defaultValue: '', description: 'First_stage message', name: 'First_stage', trim: false), string(defaultValue: '', description: 'Second stage message', name: 'Second_stage', trim: false), choice(choices: ['First', 'Second', 'third'], description: 'Third stage message ', name: 'third_stage')])])
pipeline {
	agent any 
	stages{
		stage("First"){
			steps{
				echo "${first_stage}"
			}
		}
        stage("Two"){
        	steps{
        		echo "${second_stage}"
        	}
        }
       stage("Three"){
       	  steps{
       	  	echo "${Third_stage}"
       	  }
       }

	}
}
