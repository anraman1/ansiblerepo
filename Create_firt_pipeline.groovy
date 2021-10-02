pipeline {
	agent any 
	stages{
		stage("First"){
			steps{
				echo "first_stage"
			}
		}
        stage("Two"){
        	steps{
        		echo "second_stage"
        	}
        }
       stage("Three"){
       	  steps{
       	  	echo "Third_stage"
       	  }
       }

	}
}
