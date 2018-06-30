<?php
$msg="";
if (empty($_REQUEST["Name"])){
	$msg="暱稱必須填寫";
}
else if(empty($_REQUEST["ID"])){
	$msg="帳號必須填寫";

}
else if(empty($_REQUEST["Password"])){
	$msg="密碼必須填寫";

}
else if(empty($_REQUEST["Email"])){
	$msg="email必須填寫";
}

else{
	$Name = $_REQUEST["Name"];
	$Email = $_REQUEST["Email"];
	$ID = $_REQUEST["ID"];
	$Password = $_REQUEST["Password"];


	$dbconn=mysqli_connect("127.0.0.1","root","toor","members");
	if(!$dbconn){
		die("connect faild:".mysqli_connect_error());
	}


	//mysql_query("set character set utf8mb4_gernal_ci");

	$sql="Select ID From users Where ID='".$ID."'";

	$result=$dbconn->query($sql);

	if($result->num_rows==0){
		$sql="Insert Into users (ID,Password,Name,Email) Value ('".$ID."','".$Password."','".$Name."','".$Email."')";
		$dbconn->query($sql);
		echomsg("會員註冊成功!!!");
		
	}
	else{
		echomsg("您註冊的帳號已經有人使用");
	}
}
?>
<?php
function echomsg($info) {
?>
<HTML>
<head>
<title>加入會員狀況</title>
</head>
<BODY>
<CENTER>
	<h2><?php echo $info;?></h2>
<FORM>
	<INPUT Type=Button Value="上一頁" OnClick="history.back();">
</FORM>
</CENTER>
</BODY>
</HTML>
<?php
exit();    
} 
?>


<html>
	<head>
		<meta charset='UTF-8'>
		<link rel='stylesheet' type='text/css' href='style.css'>
		<title>dio的電影院</title>
		<style>
			body{
				position:relative;
			}
			div{
				margin-top:100px;
				position:absolute;
				left:40%;
			} 
			div h2{
			text-align:center;
			}

			#submit{
				border-radius:6px;
				width:70px;
				margin-left:70px;	
			}
			span{
				position:absolute;
				left:50px;
				color:green;
			}
			
		</style>
	</head>
	<body>
		<div>
			<h2>carrydio的註冊網站</h2>
			<form method='post'action='signup.php'>
				暱稱 <input type='text' size='20' name='Name'><br>
				帳號 <input type='text' size='20' name='ID'><br>
				密碼 <input type='text' size='20' name='Password'><br>
				email <input type='text' size='30' name='Email'><br>
				<input id='submit' type='submit' value='提交'>
			</form>
			<span><?php echo $msg ?></span>
			
		</div>
	</body>
	
</html>

