<?php
error_reporting(0);
session_start();
//color
$ress="\033[0;32m";
$res="\033[0;33m";
$red="\033[0;31m";
$green="\033[0;37m";
$yellow="\033[0;33m";
$white= "\033[0;33m";  
$xnhac= "\033[1;96m";
$den="\033[1;90m";
$do="\033[1;91m";
$luc="\033[1;92m";
$vang="\033[1;93m";
$xduong="\033[1;94m";
$hong="\033[1;95m";
$trang="\033[1;97m";
#time
date_default_timezone_set("Asia/Ho_Chi_Minh");
//config
{echo $vang. "Vui Lòng Nhập API Key :$luc";
$key = trim(fgets(STDIN));
if ($key == "leminh"){
echo $luc."Bạn Đã Nhập Key Đúng\n\n";} else {
sleep(1);
exit("Bạn Đã Nhập Sai Key");}
sleep(1);
$listnv = [];
echo"Đang Loading Dữ Liệu...\n\n";
sleep(2);
echo $vang."[✓] TÀI KHOẢN TDS: $xnhac";
$_SESSION["username"]=trim(fgets(STDIN));
echo $vang."[✓] MẬT KHẨU TDS: $xnhac";
$_SESSION['password']=trim(fgets(STDIN));
echo $vang."[✓] COOKIE FB: $xnhac";
$cookie=trim(fgets(STDIN));
echo"$res\n";
$ch = curl_init();
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_URL, 'https://traodoisub.com/scr/login.php');
curl_setopt($ch, CURLOPT_COOKIEJAR, "minh.txt");
curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Linux; Android 10; RMX1925) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36');
$login =array('username' => $_SESSION['username'],'password' => $_SESSION['password'],'submit' => ' Đăng Nhập');
curl_setopt($ch, CURLOPT_POST,count($login));
curl_setopt($ch, CURLOPT_POSTFIELDS,$login);
curl_setopt($ch, CURLOPT_COOKIEFILE, "minh.txt");
$source=curl_exec($ch);
curl_close($ch);
if ($source != 1 && $source != ''){
  @system('clear');
	echo $vang."Đăng nhập thành công!\n\n";
	$user = $_SESSION["username"];
	$xu = file_get_contents('https://traodoisub.com/scr/test3.php?user='.$user);
		echo $do."[".$vang."✓".$do."]".$white." => ".$luc."Nhập [1] Chế độ Auto Follow \n";
		echo $do."[".$vang."✓".$do."]".$white." => ".$luc."Nhập [2] Chế độ Auto Like \n";
		echo $do."[".$vang."✓".$do."]".$white." => ".$luc."Nhập [3] Chế độ Auto Page \n";
        echo $do."[".$vang."✓".$do."]".$white." => ".$luc."Nhập [4] Chế độ Auto Comment \n";
        echo $do."[".$vang."✓".$do."]".$white." => ".$luc."Nhập [5] Chế độ Auto Cảm xúc \n";
        echo $do."[".$vang."✓".$do."]".$white." => ".$luc."Nhập [6] Chế độ Auto Comment Like \n";
        echo $do."[".$vang."✓".$do."]".$white." => ".$luc."Nhập [7] Chế độ Auto Follow Page \n";
        echo $xnhac."Nhập số :  ";
		$nv = trim(fgets(STDIN));
		if($nv =='1'){
		  array_push($listnv,'sub');
		}
		elseif($nv=='2'){
		  array_push($listnv,'like');
		}
		elseif($nv =='3'){
		  array_push($listnv,'page');
		}
       elseif($nv =='4'){
		  array_push($listnv,'cmt');
		}
       elseif($nv =='5'){
		  array_push($listnv,'cx');
		}
       elseif($nv =='6'){
		  array_push($listnv,'cmt','like');
		}
       elseif($nv =='7'){
		  array_push($listnv,'sub','page');
		}
        else{exit("Bạn nhập sai!");}
		echo $vang."Nhập delay:  $xnhac";
		$_SESSION['delay']=trim(fgets(STDIN));
	echo $vang."Nhập chống block: $xnhac";
	$_SESSION['block']=trim(fgets(STDIN));
	
	echo $vang."Nhập thời gian chống block: $xnhac";
	$_SESSION['j']=trim(fgets(STDIN));
	if($_SESSION['j'] < 10)
	{exit($vang."Tối thiểu 10 giây: \n\n");}
}else{
	exit($red."Tài khoản hoặc mật khẩu sai, kiểm tra lại");
}
@system('clear');
echo "\n";
$ch=curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed');
$head[] = "Connection: keep-alive";
$head[] = "Keep-Alive: 300";
$head[] = "authority: m.facebook.com";
$head[] = "ccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7";
$head[] = "accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5";
$head[] = "cache-control: max-age=0";
$head[] = "upgrade-insecure-requests: 1";
$head[] = "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9";
$head[] = "sec-fetch-site: none";
$head[] = "sec-fetch-mode: navigate";
$head[] = "sec-fetch-user: ?1";
$head[] = "sec-fetch-dest: document";
curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Linux; Android 10; RMX1925) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36');
curl_setopt($ch, CURLOPT_ENCODING, '');
curl_setopt($ch, CURLOPT_COOKIE, $cookie);
curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
curl_setopt($ch, CURLOPT_TIMEOUT, 60);
curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect:'));
$access = curl_exec($ch);
curl_close($ch);
if (explode('\",\"useLocalFilePreview',explode('accessToken\":\"', $access)[1])[0]){
$access_token = explode('\",\"useLocalFilePreview',explode('accessToken\":\"', $access)[1])[0];
if(json_decode(file_get_contents('https://graph.facebook.com/me/?access_token='.$access_token))->{'id'}){
	$idfb = json_decode(file_get_contents('https://graph.facebook.com/me/?access_token='.$access_token))->{'id'};	
}else{
	exit($red."Cookie die!!");
}
sleep(2);
function follow($access_token,$id,$cookie){
	$ch=curl_init();
	curl_setopt($ch, CURLOPT_URL, 'https://graph.facebook.com/'.$id.'/subscribers');
	$head[] = "Connection: keep-alive";
	$head[] = "Keep-Alive: 300";
	$head[] = "authority: m.facebook.com";
	$head[] = "ccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7";
	$head[] = "accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5";
	$head[] = "cache-control: max-age=0";
	$head[] = "upgrade-insecure-requests: 1";
	$head[] = "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9";
	$head[] = "sec-fetch-site: none";
	$head[] = "sec-fetch-mode: navigate";
	$head[] = "sec-fetch-user: ?1";
	$head[] = "sec-fetch-dest: document";
	curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Linux; Android 10; RMX1925) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36');
	curl_setopt($ch, CURLOPT_ENCODING, '');
	curl_setopt($ch, CURLOPT_COOKIE, $cookie);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
	curl_setopt($ch, CURLOPT_TIMEOUT, 60);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
	curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect:'));
	$data = array('access_token' => $access_token);
	curl_setopt($ch, CURLOPT_POST,count($data));
	curl_setopt($ch, CURLOPT_POSTFIELDS,$data);
	$access = curl_exec($ch);
	curl_close($ch);
	return json_decode($access);
}
function like($access_token,$id,$cookie){
	$ch=curl_init();
	curl_setopt($ch, CURLOPT_URL, 'https://graph.facebook.com/'.$id.'/likes');
	$head[] = "Connection: keep-alive";
	$head[] = "Keep-Alive: 300";
	$head[] = "authority: m.facebook.com";
	$head[] = "ccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7";
	$head[] = "accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5";
	$head[] = "cache-control: max-age=0";
	$head[] = "upgrade-insecure-requests: 1";
	$head[] = "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9";
	$head[] = "sec-fetch-site: none";
	$head[] = "sec-fetch-mode: navigate";
	$head[] = "sec-fetch-user: ?1";
	$head[] = "sec-fetch-dest: document";
	curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Linux; Android 10; RMX1925) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36');
	curl_setopt($ch, CURLOPT_ENCODING, '');
	curl_setopt($ch, CURLOPT_COOKIE, $cookie);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
	curl_setopt($ch, CURLOPT_TIMEOUT, 60);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
	curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect:'));
	$data = array('access_token' => $access_token);
	curl_setopt($ch, CURLOPT_POST,count($data));
	curl_setopt($ch, CURLOPT_POSTFIELDS,$data);
	$access = curl_exec($ch);
	curl_close($ch);
	return json_decode($access);
}
function page($id,$cookie){
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, 'https://mbasic.facebook.com/'.$id);
	$head[] = "Connection: keep-alive";
	$head[] = "Keep-Alive: 300";
	$head[] = "Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7";
	$head[] = "Accept-Language: en-us,en;q=0.5";
	curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Linux; Android 10; RMX1925) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.81 Mobile Safari/537.36');
	curl_setopt($ch, CURLOPT_ENCODING, '');
	curl_setopt($ch, CURLOPT_COOKIE, $cookie);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, FALSE);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
	curl_setopt($ch, CURLOPT_TIMEOUT, 60);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
	curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect
	:'));
	$page = curl_exec($ch);
	if (explode('&amp;refid=',explode('pageSuggestionsOnLiking=1&amp;gfid=',$page)[1])[0]){
		$get = explode('&amp;refid=',explode('pageSuggestionsOnLiking=1&amp;gfid=',$page)[1])[0];
		$link = 'https://mbasic.facebook.com/a/profile.php?fan&id='.$id.'&origin=page_profile&pageSuggestionsOnLiking=1&gfid='.$get.'&refid=17';
		curl_setopt($ch, CURLOPT_URL, $link);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
		curl_exec($ch);
	}	
	curl_close($ch);

}
function cmt($access_token,$id,$cookie,$msg){
	$ch=curl_init();
	curl_setopt($ch, CURLOPT_URL, 'https://graph.facebook.com/'.$id.'/comments');
	$head[] = "Connection: keep-alive";
	$head[] = "Keep-Alive: 300";
	$head[] = "authority: m.facebook.com";
	$head[] = "ccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7";
	$head[] = "accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5";
	$head[] = "cache-control: max-age=0";
	$head[] = "upgrade-insecure-requests: 1";
	$head[] = "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9";
	$head[] = "sec-fetch-site: none";
	$head[] = "sec-fetch-mode: navigate";
	$head[] = "sec-fetch-user: ?1";
	$head[] = "sec-fetch-dest: document";
	curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Linux; Android 10; RMX1925) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.81 Mobile Safari/537.36');
	curl_setopt($ch, CURLOPT_ENCODING, '');
	curl_setopt($ch, CURLOPT_COOKIE, $cookie);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
	curl_setopt($ch, CURLOPT_TIMEOUT, 60);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
	curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect:'));
	$data = array('message' => $msg,'access_token' => $access_token);
	curl_setopt($ch, CURLOPT_POST,count($data));
	curl_setopt($ch, CURLOPT_POSTFIELDS,$data);
	$access = curl_exec($ch);
	curl_close($ch);
	return json_decode($access);

}
function camxuc($id,$type,$cookie){
	$ch = curl_init();
	if(strpos($id,'_')){
		$uid = explode('_',$id, 2);
		$id2 = 'story.php?story_fbid='.$uid[1].'&id='.$uid[0];
	}else{
		$id2 = $id;
	}
	curl_setopt($ch, CURLOPT_URL, 'https://mbasic.facebook.com/'.$id2);
	$head[] = "Connection: keep-alive";
	$head[] = "Keep-Alive: 300";
	$head[] = "Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7";
	$head[] = "Accept-Language: en-us,en;q=0.5";
	curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Linux; Android 10; RMX1925) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.81 Mobile Safari/537.36');
	curl_setopt($ch, CURLOPT_ENCODING, '');
	curl_setopt($ch, CURLOPT_COOKIE, $cookie);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, FALSE);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
	curl_setopt($ch, CURLOPT_TIMEOUT, 60);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
	curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect
	:'));
	$page = curl_exec($ch);
	if ($id2 != $id && explode('&amp;origin_uri=',explode('amp;ft_id=',$page,2)[1],2)[0]){
		$get = explode('&amp;origin_uri=',explode('amp;ft_id=',$page,2)[1],2)[0];
	}else{
		$get = $id2;
	}
	$link = 'https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id='.$get;
	curl_setopt($ch, CURLOPT_URL, $link);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	$cx = curl_exec($ch);
	$haha = explode('<a href="',$cx);
	if ($type == 'LOVE'){
		$haha2 = explode('" style="display:block"',$haha[2])[0];
	}else if ($type == 'WOW'){
		$haha2 = explode('" style="display:block"',$haha[5])[0];
	}else if ($type == 'HAHA'){
		$haha2 = explode('" style="display:block"',$haha[4])[0];
	}else if ($type == 'SAD'){
		$haha2 = explode('" style="display:block"',$haha[6])[0];
	}else{
		$haha2 = explode('" style="display:block"',$haha[7])[0];
	}
	$link2 = html_entity_decode($haha2);	

	curl_setopt($ch, CURLOPT_URL, 'https://mbasic.facebook.com'.$link2);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_exec($ch);
	curl_close($ch);
}
echo("\n\n\033[91m ════════════════════════════════════════════════\n");
echo "\033[1;91m    _       //\    __  __ _____ _   _ _    _\n";
#sleep(1);
echo "\033[1;97m   | |     |/ \|  |  \/  |_   _| \ | | |  | |\n";
sleep(1);
echo "\033[1;92m   | |    | ____| | \  / | | | |  \| | |__| |\n";
#sleep(1);
echo "\033[1;97m   | |    |  _|   | |\/| | | | | . ` |  __  |\n";
sleep(1);
echo "\033[1;93m   | |____| |___  | |  | |_| |_| |\  | |  | |\n";
#sleep(1);
echo "\033[1;97m   |______|_____| |_|  |_|_____|_| \_|_|  |_|\n";
sleep(1);
echo("\n\033[91m ════════════════════════════════════════════════\n");
echo $vang."Creator: ";
echo $luc."[ Lê Minh ] ";
echo $do."[✓] ".$vang."TOOLS FREE";
echo $do."\n\n[".$vang."✓".$do."]".$trang." => ".$xnhac."Tool Auto Traodoisub Cookie Facebook\n";
echo $do."[".$vang."✓".$do."]".$trang." => ".$luc."Bản quyền: ".$vang."Lê Minh\n";
echo $do."[".$vang."✓".$do."]".$trang." => ".$luc."Facebook : ".$vang."Facebook.com/Dangvanleminh\n";
echo $do."[".$vang."✓".$do."]".$trang." => ".$luc."Zalo     : ".$vang."0795322271";

echo $trang."\n------------------------------------------------------\n";
echo $xduong."                 THÔNG TIN TÀI KHOẢN\n   ";
sleep(2);
echo $do."\n[".$vang."✓".$do."]".$trang." => ".$xnhac."Tên tài khoản: ".$vang.$_SESSION['username'];
sleep(1);
echo $do."\n[".$vang."✓".$do."]".$trang." => ".$xnhac."Xu hiện có   : ".$vang.$xu;
sleep(1);
echo $do."\n[".$vang."✓".$do."]".$trang." => ".$xnhac."ID tool      : ".$vang.$idfb;
sleep(3);
echo $trang."\n------------------------------------------------------\n";
sleep(2);
$h = datnick($user,$idfb);
$dem = 1;
$tangblock = 1;
if ($h == '1') {
  $i=1;
  while($i<99999999999999999999999999999){
    foreach($listnv as $loai){
if($loai == 'sub'){
      $list = getnv('follow',$user);
      $check =count($list);
      if($check == 0){$i++;continue;}
        
        foreach ($list  as $id) {
        $g = follow($access_token,$id,$cookie);
        if ($g->{'error'}->{'code'} == 368){
						exit($red."Đã bị block!");
					}
        $s = nhantien('sub',$id);
        if ($s == 2){$xu = $xu + 600;
        $congxu= $do."[".$luc."+600 Xu".$do."] ● [".$trang.$xu." Xu".$do."]\n";
        $kl = $do."[".$trang.$dem.$do."]●".$do."[".$vang.date("H:i").$do."]●".$do."[".$luc."FOLLOW".$do."]●".$do."|".$luc."ID:".$trang.$id.$luc." ● ";
        echo $kl;sleep(2);echo $congxu;
        for($countdown = 0;$countdown<($_SESSION['delay']+1);$countdown++){echo $vang."    ● nữa sẽ làm nhiệm vụ mới ●\r".($_SESSION['delay']-$countdown);
         sleep(1);
         echo "\r";
        }
          $dem++;
       if($dem > $_SESSION['block']){
           for($x = 0;$x<($_SESSION['j']+1);$x++){
             echo $do."   \r".($_SESSION['j']-$x)." giây chống block";
             sleep(1);
             echo "                           \r";}
        $tangblock++;
        $_SESSION['block']=$tangblock*$_SESSION['block'];
           }
          }
        else {echo "                                                                    \r";
          echo $do."[".$dem.$do."]●".$do."[".date("H:i").$do."]●".$do." ["."FOLLOW".$do."]●".$luc."|"."ID:".$id." ● ";
          sleep(2);
          echo "                      \r";
        
          continue;}
          
        }
      
    }
    elseif($loai == 'like'){
      $list = getnv('like',$user);
      $check = count($list);
      if($check == 0){$i++;continue;}
      foreach ($list  as $id) {
        $g = like($access_token,$id,$cookie);
        if ($g->{'error'}->{'code'} == 368){
						exit($red."Đã bị block!");
					}
        $s = nhantien('like',$id);
        if ($s == 2){$xu = $xu + 200;
        $congxu= $do."[".$luc."+200 Xu".$do."] ● [".$trang.$xu." Xu".$do."]\n";
        $kl = $do."[".$trang.$dem.$do."]●".$do."[".$vang.date("H:i").$do."]".$do."●[".$luc." LIKE ".$do."]●".$do."|".$luc."ID:".$trang.$id.$vang." ● ";
        echo $kl;sleep(2);echo $congxu;
         for($countdown = 0;$countdown<($_SESSION['delay']+1);$countdown++){echo $vang."    ● nữa sẽ làm nhiệm vụ mới ● \r".($_SESSION['delay']-$countdown);
         sleep(1);
           echo "\r";
         }
         $dem++;
         if($dem > $_SESSION['block']){
           for($x = 0;$x<($_SESSION['j']+1);$x++){
             echo $do."   \r".($_SESSION['j']-$x)." giây chống block";
             sleep(1);
             echo "                           \r";}
        $tangblock++;
        $_SESSION['block']=$tangblock*$_SESSION['block'];
        }
        }
        else {echo "                                                                     \r";
          echo $do."[".$dem.$do."]●".$do."[".date("H:i").$do."]●".$do." ["."LIKE".$do."]●".$do."|"."ID:".$id." ● ";
          sleep(2);
          echo "                      \r";
        
          continue;}
        
      }
    }
    }
if($loai == 'page'){
      $list = getnv('likepage',$user);
      $check =count($list);
      if($check == 0){$i++;continue;}
        
        foreach ($list  as $id) {
        $g = page($id,$cookie);
        if ($g->{'error'}->{'code'} == 368){
						exit($red."Đã bị block!");
					}
        $s = nhantien('page',$id);
        if ($s == 2){$xu = $xu + 600;
        $congxu= $do."[".$luc."+600 Xu".$do."] ● [".$trang.$xu." Xu".$do."]\n";
        $kl = $do."[".$trang.$dem.$do."]●".$do."[".$vang.date("H:i").$do."]●".$do."[".$luc."PAGE".$do."]●".$do."|".$luc."ID:".$trang.$id.$xduong." ● ";
        echo $kl;sleep(2);echo $congxu;
        for($countdown = 0;$countdown<($_SESSION['delay']+1);$countdown++){echo $vang."    ● nữa sẽ làm nhiệm vụ mới ●\r".($_SESSION['delay']-$countdown);
         sleep(1);
         echo "\r";
        }
          $dem++;
       if($dem > $_SESSION['block']){
           for($x = 0;$x<($_SESSION['j']+1);$x++){
             echo $do."   \r".($_SESSION['j']-$x)." giây chống block";
             sleep(1);
             echo "                           \r";}
        $tangblock++;
        $_SESSION['block']=$tangblock*$_SESSION['block'];
           }
          }
        else {echo "                                                                    \r";
          echo $do."[".$dem.$do."]●".$do."[".date("H:i").$do."]●".$do." ["."PAGE".$do."]●".$do."|"."ID:".$id." ● ";
          sleep(2);
          echo "                      \r";
        
          continue;}
          
        }
      
    }
if($loai == 'cmt'){
      $list = getnv('cmt',$user);
      $check =count($list);
      if($check == 0){$i++;continue;}
        
        foreach ($list  as $id => $key) {
        $id = $key->{'id'};
		$type = $key->{'type'};
        $g = cmt($access_token,$id,$cookie,$msg);
        if ($g->{'error'}->{'code'} == 368){
						exit($red."Đã bị block!");
					}
        $s = nhantien('cmt',$id);
        if ($s == 2){$xu = $xu + 600;
        $congxu= $do."[".$luc."+600 Xu".$do."] ● [".$trang.$xu." Xu".$do."]\n";
        $kl = $do."[".$trang.$dem.$do."]●".$do."[".$vang.date("H:i").$do."]●".$do."[".$luc."CMT".$do."]●".$do."|".$luc."ID:".$trang.$id.$hong." ● ";
        echo $kl;sleep(2);echo $congxu;
        for($countdown = 0;$countdown<($_SESSION['delay']+1);$countdown++){echo $vang."    ● nữa sẽ làm nhiệm vụ mới ●\r".($_SESSION['delay']-$countdown);
         sleep(1);
         echo "\r";
        }
          $dem++;
       if($dem > $_SESSION['block']){
           for($x = 0;$x<($_SESSION['j']+1);$x++){
             echo $do."   \r".($_SESSION['j']-$x)." giây chống block";
             sleep(1);
             echo "                           \r";}
        $tangblock++;
        $_SESSION['block']=$tangblock*$_SESSION['block'];
           }
          }
        else {echo "                                                                    \r";
          echo $do."[".$dem.$do."]●".$do."[".date("H:i").$do."]●".$do." ["."CMT".$do."]●".$do."|"."ID:".$id." ● ";
          sleep(2);
          echo "                      \r";
        
          continue;}
          
        }
      
    }
   if($loai == 'cx'){
      $list = getnv('camxuc',$user);
      $check =count($list);
      if($check == 0){$i++;continue;}
        
        foreach ($list  as $id => $key) {
        $id = $key->{'id'};
		$type = $key->{'type'};
        camxuc($id,$type,$cookie);
        $s = nhantien('$type',$id);
        if ($s == 2){$xu = $xu + 400;
        $congxu= $do."[".$luc."+400 Xu".$do."] ● [".$trang.$xu." Xu".$do."]\n";
        $kl = $do."[".$trang.$dem.$do."]●".$do."[".$vang.date("H:i").$do."]●".$do."[".$luc."$type".$do."]●".$do."|".$luc."ID:".$trang.$id.$xnhac." ● ";
        echo $kl;sleep(2);echo $congxu;
        for($countdown = 0;$countdown<($_SESSION['delay']+1);$countdown++){echo $vang."    ● nữa sẽ làm nhiệm vụ mới ●\r".($_SESSION['delay']-$countdown);
         sleep(1);
         echo "\r";
        }
          $dem++;
       if($dem > $_SESSION['block']){
           for($x = 0;$x<($_SESSION['j']+1);$x++){
             echo $do."   \r".($_SESSION['j']-$x)." giây chống block";
             sleep(1);
             echo "                           \r";}
        $tangblock++;
        $_SESSION['block']=$tangblock*$_SESSION['block'];
           }
          }
        else {echo "                                                                    \r";
          echo $do."[".$dem.$do."]●".$do."[".date("H:i").$do."]●".$do." ["."$type".$do."]●".$do."|"."ID:".$id." ● ";
          sleep(2);
          echo "                      \r";
        
          continue;}
          
        }
      
    }
    $i++;}
}else{exit($red."Cấu hình thất bại, vui lòng thêm id: $id vào cấu hình");}
}else{exit($red."Cookie die!!");}
}
function getnv($loai,$user){
	$list = file_get_contents('https://traodoisub.com/scr/api_job.php?chucnang='.$loai.'&user='.$user);
	return json_decode($list);
}
function datnick($user,$id){
	$xxx = file_get_contents('https://traodoisub.com/scr/api_dat.php?user='.$user.'&idfb='.$id);
	return $xxx;
}
function nhantien($loai,$id){
	$ch=curl_init();
	curl_setopt($ch, CURLOPT_URL, 'https://traodoisub.com/scr/nhantien'.$loai.'.php');
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	$tdsxu=array('id' => $id);
	curl_setopt($ch, CURLOPT_POST,count($tdsxu));
	curl_setopt($ch, CURLOPT_POSTFIELDS,$tdsxu);
	curl_setopt($ch, CURLOPT_COOKIEFILE, "minh.txt");
	$xu=curl_exec($ch);
	curl_close($ch);
	return $xu;
}
function nhantiencx($loai,$id){
	$ch=curl_init();
	curl_setopt($ch, CURLOPT_URL, 'https://traodoisub.com/scr/nhantiencx.php');
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	$tdsxu=array('id' => $id, 'loaicx' => $loai);
	curl_setopt($ch, CURLOPT_POST,count($tdsxu));
	curl_setopt($ch, CURLOPT_POSTFIELDS,$tdsxu);
	curl_setopt($ch, CURLOPT_COOKIEFILE, "minh.txt");
	$xu=curl_exec($ch);
	curl_close($ch);
	return $xu;
}
?>
