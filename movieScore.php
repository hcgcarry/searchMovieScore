<?php 

//error_reporting(0); //關掉php的詭異報錯題示
$movieName=$_GET['q']; $web=$_GET['web'];

switch($web){
	case 'meta':
		$saveMovieName=$movieName;
		$movieName=str_replace(" ","-",$movieName);
		$command="/usr/bin/python3 srcScore.py ".$movieName." meta";
		$movieScore_json=exec($command);
		$movieScore=json_decode($movieScore_json,true);
		echo "<h3>meta</h3>";
		echo "<a target='_blank' href='https://www.metacritic.com/movie/$movieName'>visit metacritic $saveMovieName</a><br>";
		echo "meta_pro_score:".$movieScore["meta_pro_score"]."<br>";
		echo "meta_pro_count:".$movieScore["meta_pro_count"]."<br>";
		echo "meta_user_score:".$movieScore["meta_user_score"]."<br>";
		echo "meta_user_count:".$movieScore["meta_user_count"]."<br>";
		break;

	case 'rotten':
		$saveMovieName=$movieName;
		$movieName=str_replace(" ","_",$movieName);
		$command="/usr/bin/python3 srcScore.py ".$movieName." rotten";
		$movieScore_json=exec($command);
		$movieScore=json_decode($movieScore_json,true);
		echo "<span style='float:left;'>";
		printf("<img src='%s' alt='movie img not found'>",$movieScore['rotten_img']);
		echo "</span>";
		//rotten score span
		echo "<span style='margin-left:30px;float:left;'>";
		
		echo "<h3>rotten</h3>";
		echo "<a target='_blank' href='https://www.rottentomatoes.com/m/$movieName'>visit rottentomatoes $saveMovieName</a><br>";
		echo "rotten_pro_score:".$movieScore["rotten_pro_score"]."<br>";
		echo "rotten_pro_count:".$movieScore["rotten_pro_count"]."<br>";
		echo "rotten_user_score:".$movieScore["rotten_user_score"]."<br>";
		echo "rotten_user_count:".$movieScore["rotten_user_count"]."<br>";
		echo "</span>";
	
		break;


	case 'imdb':
		$saveMovieName=$movieName;
		$movieName=str_replace(" ","+",$movieName);
		$command="/usr/bin/python3 srcScore.py ".$movieName." imdb";
		$movieScore_json=exec($command);
		$movieScore=json_decode($movieScore_json,true);
		echo "<h3>imdb</h3>";
		printf("<a href='%s' target='_blank'>visit imdb %s</a><br>",$movieScore['imdb_url'],$saveMovieName);
		printf("imdb_count:%s <br>",$movieScore['imdb_score']);
		printf("imdb_score:%s <br>",$movieScore['imdb_count']);

		
		break;
}

	
		

?>
