<?php 

//error_reporting(0); //關掉php的詭異報錯題示
$movieName=$_GET['q']; $web=$_GET['web'];


switch($web){
	case 'meta':
		$command="/usr/bin/python3 srcScore.py ".$movieName." meta";
		$movieScore_json=exec($command);
		$movieScore=json_decode($movieScore_json,true);
		echo "<h3>meta</h3>";
		echo "<a href='https://www.metacritic.com/movie/$movieName'>visit metacritic</a><br>";
		echo "meta_pro_score:".$movieScore["meta_pro_score"]."<br>";
		echo "meta_pro_count:".$movieScore["meta_pro_count"]."<br>";
		echo "meta_user_score:".$movieScore["meta_user_score"]."<br>";
		echo "meta_user_count:".$movieScore["meta_user_count"]."<br>";
		break;

	case 'rotten':
		$command="/usr/bin/python3 srcScore.py ".$movieName." rotten";
		$movieScore_json=exec($command);
		$movieScore=json_decode($movieScore_json,true);
		echo "<span style='float:left;'>";
		printf("<img src='%s' alt='movie img not found'>",$movieScore['rotten_img']);
		echo "</span>";
		//rotten score span
		echo "<span style='margin-left:30px;float:left;'>";
		
		echo "<h3>rotten</h3>";
		echo "<a href='https://www.rottentomatoes.com/m/$movieName'>visit rottentomatoes</a><br>";
		echo "rotten_pro_score:".$movieScore["rotten_pro_score"]."<br>";
		echo "rotten_pro_count:".$movieScore["rotten_pro_count"]."<br>";
		echo "rotten_user_score:".$movieScore["rotten_user_score"]."<br>";
		echo "rotten_user_count:".$movieScore["rotten_user_count"]."<br>";
		echo "</span>";
	
		break;


	case 'imdb':
		$command="/usr/bin/python3 srcScore.py ".$movieName." imdb";
		$movieScore_json=exec($command);
		echo $movieScore_json;
		
		break;
}

	
		

?>
