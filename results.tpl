<html>
	<head>
		<title>ArticleSense</title>
		<style type="text/css">
			p { padding:0px 0px; }
			button { background-color: Transparent;
					 padding: 0px 
					 height: 25 }
		</style>
	</head>

	<body>
		<br>
		<br>
		<table border="0" align="center">
			<tr>
				<td width=10%></td>
				<td width="100">		
					<div id="header" align="center">
						<a href="/upload"><img src="/static/as_logo_banner.gif" /></a>
						<form action="/upload" method="post"> 
							<input name="my_url" type="text" size="65"/> 
							<input type="submit" name="submit" value="Enter URL" />
						</form>
					</div>
				</td>
			</tr>
			<tr>
				<td width=10%></td>
				<td width="100">
					<div id="data">
						<p>{{!data}}</p>
					</div>
				</td>
			</tr>
		</table> 


	</body>
</html>