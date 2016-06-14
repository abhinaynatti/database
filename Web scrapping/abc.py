import urllib2
from bs4 import BeautifulSoup
page='''

<html>
	<head>

		<title>Romit | Student Search</title>
		<meta name='author' content='Romit Choudhary'>
		<meta http-equiv='cache-control' content='public'>
		<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
		<meta http-equiv='content-language' content='en-US'>
		<meta name='copyright' content='&copy; 2014 Romit Choudhary'>
		<meta name='description' content='A search engine for campus students to search for anyone in the campus.'>
		<meta name='keywords' content='student search iitk, student search, search iitk, search, romit iitk, romit choudhary iitk, romit, choudhary, web developer, coder, search engine'>
		<meta name='robots' content='index,follow'>
		<meta property='og:title' content='Student Search'>
		<meta property='og:type' content='website'>
		<meta property='og:site_name' content='Student Search'>
		<meta property='fb:admins' content='100002095998425'>		
		<script>
		function result(search)
{
	if(search.value=='')
	{
		document.getElementById('info').innerHTML = ''
		return
	}
	else if(search.value.length==1)
	{
		document.getElementById('info').innerHTML = ''
		return
	}
	
	params = "search="+search.value
	request = new ajaxRequest()
	request.open("POST","search.php",true)
	
	 request.setRequestHeader("Content-type", "application/x-www-form-urlencoded")    
	 request.setRequestHeader("Content-length", params.length)    
	 request.setRequestHeader("Connection", "close")
	 
	 request.onreadystatechange = function()
	 {
		if(this.readyState == 4)
		{
			if(this.status ==200)
			{
				if(this.responseText != null)
				{
					document.getElementById('info').innerHTML = this.responseText;
				}
				else alert("AJAX Error : No data received")
			}
			else alert("AJAX Error: "+this.statusText)
		}}
		request.send(params)
	 }	 
	 
	 
	 function ajaxRequest() {
			try    { 
					var request = new XMLHttpRequest()    
					}    
			catch(e1)    {        
			try        {            
					request = new ActiveXObject("Msxml2.XMLHTTP")        
					}      
			catch(e2)        {            
			try            {                
					request = new ActiveXObject("Microsoft.XMLHTTP")            }            
			catch(e3)  {                
					request = false            
						}        
						}    }    
						
				return request } 		</script>
		<link rel='stylesheet' type='text/css' href='main.css'>
		<script type="text/javascript">
		 function focusOnInput()
			{
		 		document.getElementById("sname").focus();
		 	}
 </script>	
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-43364785-4', 'auto');
  ga('send', 'pageview');

</script>

</head>
<body onload="focusOnInput()">
	<div id="searchform"  align="center" style='height:110px;margin-top:0px;padding-top:20px;background:white;position:fixed;z-index:100;left:0px;right:0px;'>

				
				<form align="center" method="post" action="searchres.php" style='background:white;'>
			<input type="text" name="sname" id="name" placeholder="Name of student" autofocus autocomplete='off' onKeyUp="result(this)" style="width:12%;">
				<input type="text" name="roll" id="roll" placeholder="Roll No" style="width:8%;">
				<input type="text" name="city" id="city" placeholder="City" style="width:10%;">
				<input type='text' name='email' id="email" placeholder='Email' style="width:10%;" >					
					<select name="gender" id="gender">
						<option value="">Gender</option>
						<option value="M">Male</option>
						<option value="F">Female</option>
					</select>
					<select name="batch" id="batch">
					<option value="">Batch</option>
						<option value="y15">Y15</option>
						<option value="y14">Y14</option>
						<option value="y13">Y13</option>
						<option value="y12">Y12</option>
						<option value="y11">Y11</option>
						<option value="y10">Y10</option>
					</select>
					<select name="program" id="program">
						<option value="">Program</option>
						<option value='BTech'>BTech</option>
						<option value='MTech'>MTech</option>
						<option value='BS'>BS</option>
						<option value='MSc(2 yr)'>MSc(2 yr)</option>
						<option value='PhD'>PhD</option>
						<option value='PhD(Dual)'>PhD(Dual)</option>
						<option value='Ms-research'>MS-Research</option>
					</select>
					<select name="dept" id="dept">
						<option value="">Dept</option>
						<option value="AE">AE</option>
						<option value="EE">EE</option>
						<option value="CSE">CSE</option>
						<option value="MSE">MSE</option>
						<option value="BSBE">BSBE</option>
						<option value="ME">ME</option>
						<option value="CE">CE</option>
						<option value="CHE">CHE</option>
						<option value="MTH">MTH</option>
						<option value="CHM">CHM</option>
						<option value="ECO">ECO</option>
						<option value="PHY">PHY</option>
 						<option value="HSS">HSS</option>
						<option value="STATS">STATS</option>
						<option value="ES">ES</option>
						<option value="NETP">NETP</option>
						<option value="LT">LT</option>
						<option value="MSP">MSP</option>
						<option value="IME">IME</option>
						<option value="DES">DES</option>
						<option value="EEM">EEM</option>
					</select>
					<select name="hall" id="hall">
						<option value="">Hall</option>
						<option value="Hall 1">Hall 1</option>
						<option value="Hall 2">Hall 2</option>
						<option value="Hall 3">Hall 3</option>
						<option value="Hall 4">Hall 4</option>
						<option value="Hall 5">Hall 5</option>
						<option value="Hall 6">Hall 6</option>
						<option value="Hall 7">Hall 7</option>
						<option value="Hall 8">Hall 8</option>
						<option value="Hall 9">Hall 9</option>
						<option value="Hall 10">Hall 10</option>
						<option value="Hall 11">Hall 11</option>
						<option value="Gh">GH</option>
					</select>
					<select name="blood" id="blood">
						<option value="">Blood Group</option>
						<option value="A&#43;">A+</option>
						<option value="A&#45;">A-</option>
						<option value="B&#43;">B+</option>
						<option value="B&#45;">B-</option>
						<option value="AB&#43;">AB+</option>
						<option value="AB&#45;">AB-</option>
						<option value="O&#43;">O+</option>
						<option value="O&#45;">O-</option>
					</select>
					
					<br><br>
				<a href="index.php" style="text-decoration:none;background:#8C8C8C;color:white;cursor:pointer;margin-top:20px;box-shadow:0px 0px 1px rgb(216, 216, 216);font-size:16px;padding:5px;font-weight:bold;padding-left:20px;padding-right:20px;">Home</a>
			<input type="submit" name="submitforface" value="Find Faces" style="font-size:16px;background:#8C8C8C;padding:5px;color:white;cursor:pointer;box-shadow:none;font-weight:bold;width:140px;">
				</form>
			<br>
			</div>

			<table>
				<tr>
					<p style='background:white;box-shadow:0px 0px 1px rgb(216, 216, 216);padding:10px;text-align:center;margin-top:80px;font-weight:bold;position:fixed;bottom:0px;left:0px;right:0px;' >Designed and Developed By <a href="http://www.facebook.com/choudharyromit" target='_blank' style='text-decoration:underline;background:white;'>Romit Choudhary</a></p>
				</tr>
			</table>

		
		<!-- headergoeshere -->
<div id='info' align="center" style='margin-top:10%;position:absolute;z-index:1;background:#EEEEEE;box-shadow:0px 0px 5px black;min-width:100%;'></div>

	<div id='studimages'  style='margin-top:170px;margin-left:80px;margin-right:80px;'><table align=center style='margin:10px auto;margin-bottom:0px;' cellspacing='1'>		
									<tr align=center><a href='http://home.iitk.ac.in/~kaul' target='_blank'>
											<td id='imagebox' style='background:white;box-shadow:0px 0px 1px grey ;min-width:150px;margin-left:5px;'>
												<img src='http://oa.cc.iitk.ac.in:8181/Oa/Jsp/Photo/150003_0.jpg' width='200px' height='245px'>
											<p id='imagelayer'>Aakash Kaul<br>150003</p>
							
											</td></a><td style='padding:20px;padding-left:20px;width:400px;min-width:300px;text-align:left;background:white;box-shadow:0px 0px 1px grey ;margin:5px;font-family:Lato;'><div id='variables' style=''>
										<li>Name</li><hr>
										<li>Roll No</li><hr>
										<li>Batch</li><hr>
										<li>Gender</li><hr>
										<li>Program</li><hr>
										<li>Department</li><hr>
										<li>IITK Address</li><hr>
										<li>Hometown</li><hr>
										<li>Email</li><hr>
										<li>Blood Group</li><hr>
									  </div><div id='values'>
										<li>Aakash Kaul</li><hr>
										<li>150003</li><hr>
										<li>y15</li><hr>
										<li>M</li><hr>
										<li>Btech</li><hr>
										<li>CHE</li><hr>
										<li>Hall 10,  a-339</li><hr>
										<li>Chandigarh</li><hr>
										<li><a href='mailto:kaul@iitk.ac.in' style='font-size:17px;text-decoration:none;background:white;'>kaul@iitk.ac.in</li></a><hr>
										<li>Ab+</li><hr>
									  </div></td><td style='background:white;box-shadow:0px 0px 1px grey;padding:10px;min-width:260px;width:280px;'><a href='http://home.iitk.ac.in/~kaul' target='_blank' style='text-decoration:none;color:white;font-size:18px;'><div style='padding:6px;background:#381811;margin:4px;margin-left:40px;margin-right:40px;box-shadow:inset 0px 0px 10px black;font:bold 24px calibri;opacity:0.8;padding-left:10px;padding-right:10px;'>Homepage
							 </div></a><a href='https://www.facebook.com/search/results.php?q=Aakash Kaul&type=users&ed=iit kanpur' target='_blank' style='text-decoration:none;color:white;font-size:18px;'><div style='padding:6px;background:#003399;margin:4px;margin-left:40px;margin-right:40px;box-shadow:inset 0px 0px 10px black;font:bold 24px calibri;opacity:0.8;padding-left:10px;padding-right:10px;'>facebook
							 </div></a>
							 <a href='https://plus.google.com/s/Aakash Kaul/people' target='_blank' style='text-decoration:none;color:white;font-size:18px;'><div style='padding:6px;background:red;opacity:0.8;padding-left:10px;margin:4px;margin-left:40px;margin-right:40px;box-shadow:inset 0px 0px 10px black;font:bold 24px calibri;padding-right:10px;'>
								google+
							 </div></a>
							 <a href='https://twitter.com/search?q=Aakash Kaul&mode=users' target='_blank' style='text-decoration:none;color:white;font-size:18px;'>
							 <div style='padding:6px;margin:4px;margin-left:40px;margin-right:40px;box-shadow:inset 0px 0px 10px black;font:bold 24px calibri;background:#2daebf;opacity:0.8;padding-left:10px;padding-right:10px;'>
								twitter
							 </div></a>
							 <a href='http://www.linkedin.com/vsearch/p?keywords=Aakash Kaul' target='_blank' style='text-decoration:none;color:white;font-size:18px;'>
							 <div style='padding:6px;margin:4px;margin-left:40px;margin-right:40px;box-shadow:inset 0px 0px 10px black;font:bold 24px calibri;background:#007d9a;opacity:0.8;padding-left:10px;padding-right:10px;'>
								linkedin
							 </div></a>
							 </td></tr></table>	<br><h3 style='font:bold 24px franklin gothic book;font-variant:small-caps;'>Other related searches</h3><br><hr><br><div id='othersearches' style='display:inline-block;margin:7px;'>	<a href='groups.php?type=hometown&value=Chandigarh' style='color:blue;' >Find other people from <b style='font:bold 18px arial;background:#00000000;'>Chandigarh</b></a></div><div id='othersearches' style='display:inline-block;margin:7px;'>	<a href='groups.php?type=department&value=CHE' style='color:blue;' >Find  people from <b style='font:bold 18px arial;background:#00000000;'>CHE</b></a></div><div id='othersearches' style='display:inline-block;margin:7px;'>	<a href='groups.php?type=hall&value=Hall 10' style='color:blue;' >Find other people from <b style='font:bold 18px arial;background:#00000000;'>Hall 10</b></a></div><div id='othersearches' style='display:inline-block;margin:7px;'>	<a href='groups.php?type=batch&value=y15' style='color:blue;' >Find other people from <b style='font:bold 18px arial;background:#00000000;'>y15</b></a></div>			
		</div>			
	</body>
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-43364785-4', 'auto');
  ga('send', 'pageview');

</script>
</html>


'''
f= open('a.txt','w')
for i in range(150002,150003):

	soup=BeautifulSoup(page,'html.parser')
	div1=soup.find_all("div",{"id":"values"})
	img=soup.find_all("img")
	for element in img:
		imgsrc=element.get("src")

	for elements in div1:
		div2=elements.text
		
	x=div2.split('\n')
	f.write(x[1]+'\t'+x[2]+'\t'+imgsrc)
		
	'''for element in div1:
		div2=div1
		with open('data.csv','w') as csvfile:
			writer=csv.writer(csvfile)
			[writer.writerow(r) for r in div2]'''
