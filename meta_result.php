<?php $movieName=$_GET['q']; $web=$_GET['web'];
echo $movieName;
echo $web;

$startTime=time();
switch($web){
	case 'meta':
		$command="/usr/bin/python3 meta_src.py ".$movieName;
		$movieScore_json=exec($command);
		echo $movieScore_json;
		echo "fuck1";
	case 'rotten':
		$command="/usr/bin/python3 rotten_src.py ".$movieName;
		$movieScore_json=exec($command);
		echo $movieScore_json;
		echo "fuck2";

	case 'imdb':
		$command="/usr/bin/python3 imdb_src.py ".$movieName;
		$movieScore_json=exec($command);
		echo $movieScore_json;
		echo "fuck3";
}

$endTime=time();
$costTime=$endTime-$startTime;
echo "it cost $costTime sec";
?>
