<?php $movieName=$_GET['q']; $web=$_GET['web'];
echo date('l dS \of F Y h:i:s A');
echo "<br>";
echo $movieName;
echo $web;
$startTime=time();

switch($web){
	case 'meta':
		$command="/usr/bin/python3 srcScore.py ".$movieName." meta";
		$movieScore_json=exec($command);
		echo $movieScore_json;
		break;

	case 'rotten':
		$command="/usr/bin/python3 srcScore.py ".$movieName." rotten";
		$movieScore_json=exec($command);
		echo $movieScore_json;
		break;


	case 'imdb':
		$command="/usr/bin/python3 srcScore.py ".$movieName." imdb";
		$movieScore_json=exec($command);
		echo $movieScore_json;
		break;
}
$endTime=time();
$costTime=$endTime-$startTime;
echo "<br> it cost $costTime sec";

?>
