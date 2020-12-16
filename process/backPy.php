<?php 
    $file = "../uploads/".$_GET["message"];
    // echo $file;
    $test = passthru("python ./face_detection.py -i $file");
    
    // TODO: Tambahin front end buat bagusin echo test
    echo $test;
?>