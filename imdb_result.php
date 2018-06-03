<?php
$q=$_GET['q'];
echo $q;
$startTime=time();
$command="/usr/bin/python3 imdb_src.py ".$q;

$movieScore_json=exec($command);

echo $movieScore_json;
$endTime=time();
echo ($startTime - $endTime);

?>
