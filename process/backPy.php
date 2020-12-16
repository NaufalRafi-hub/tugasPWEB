<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        h1 {
            text-align: center;
		    font-family: helvetica;
		    font-style: italic;
            font-size: 200px;
            margin-right: auto;
            margin-left: auto;
            margin-top: 100px;
        }
    </style>
</head>
<body>
    <h1>
    <?php 
        $file = "../uploads/".$_GET["message"];
        // echo $file;
        $test = passthru("python ./face_detection.py -i $file");
        
        // TODO: Tambahin front end buat bagusin echo test
        echo $test;
    ?>
    </h1>
</body>
</html>
