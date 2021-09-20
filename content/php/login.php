<html>
<body>

<?php

$command = escapeshellcmd('content/python/main2.py');
$output = shell_exec($command);
echo $output;

$myfile = fopen('data/dataC.txt', "r") or die("Unable to open file!");
$key = fgets($myfile);
$key = fgets($myfile);
$message = "";

if ($key == 0) {
	$message = "Seccessful!";
	include 'content/html/htmlA.html';
}
else {
	$message = "Fail!";
}

?>

Welcome <?php echo $_POST["name"]; ?><br>
Your email address is: <?php echo $_POST["email"]; ?>

</body>
</html>
