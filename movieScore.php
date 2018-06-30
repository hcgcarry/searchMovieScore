<?php 

//error_reporting(0); //關掉php的詭異報錯題示
$movieName=$_GET['q']; $web=$_GET['web'];
$saveMovieName=$movieName;
$movieName=json_encode($movieName);



switch($web){
	case 'meta':
		$movieName=str_replace(" ","-",$movieName);
		$command="/usr/bin/python3 srcScore.py ".$movieName." meta";
		$movieScore_json=exec($command);
		$movieScore=json_decode($movieScore_json,true);
		$url=$movieScore['meta_url'];
		echo "<h3>metacritic</h3>";
		echo "<a target='_blank' href=$url>visit metacritic $saveMovieName</a><br>";
		echo "專業評價:".$movieScore["meta_pro_score"]."<br>";
		echo "專業評分人數:".$movieScore["meta_pro_count"]."<br>";
		echo "<br><br>";
		echo "觀眾評價:".$movieScore["meta_user_score"]."<br>";
		echo "觀眾評分人數:".$movieScore["meta_user_count"]."<br>";
		break;

	case 'rotten':
		$movieName=str_replace(" ","_",$movieName);
		$command="/usr/bin/python3 srcScore.py ".$movieName." rotten";
		$movieScore_json=exec($command,$output,$return);
		$movieScore=json_decode($movieScore_json,true);
		$url=$movieScore['rotten_url'];
		//print_r($output);
		//print_r($return);
		//rotten image
		echo "<span style='float:left;'>";
		printf("<img src='%s' alt='movie img not found'>",$movieScore['rotten_img']);
		echo "</span>";

		echo "<span style='margin-left:30px;float:left;'>";
		
		echo "<h3>爛番茄</h3>";
		echo "<a target='_blank' href=$url>visit rottentomatoes $saveMovieName</a><br>";
		echo "專業評價:".$movieScore["rotten_pro_score"]."<br>";
		echo "專業評分人數:".$movieScore["rotten_pro_count"]."<br>";
		echo "<br><br>";
		echo "觀眾評價:".$movieScore["rotten_user_score"]."<br>";
		echo "觀眾評分人數:".$movieScore["rotten_user_count"]."<br>";
		echo "</span>";
	
		break;


	case 'imdb':
		$movieName=str_replace(" ","+",$movieName);
		$command="/usr/bin/python3 srcScore.py ".$movieName." imdb";
		$movieScore_json=exec($command);
		$movieScore=json_decode($movieScore_json,true);
		echo "<h3>imdb</h3>";
		printf("<a href='%s' target='_blank'>visit imdb %s</a><br>",$movieScore['imdb_url'],$saveMovieName);
		printf("評分:%s <br>",$movieScore['imdb_score']);
		printf("評分人數:%s <br>",$movieScore['imdb_count']);

		
		break;
} 
	
		

?>
