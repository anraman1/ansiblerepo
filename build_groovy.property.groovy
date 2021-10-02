properties([parameters([string(defaultValue: '', description: 'interger', name: 'inter', trim: false)])])

 String string=params.inter;
 int loopint = Integer.parseInt(string);
 
timeout(unit: 'SECONDS', time: 500) {
    stage("One"){
        node {
            sleep 2
            echo params.inter
            for (int i = 0; i<loopint; i++){
                   echo "Hello"
            }
            
    }
}
}
