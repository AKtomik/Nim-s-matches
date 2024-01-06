#!"C:\rootapp\Python312\python.exe"
import cgitb
cgitb.enable()
print()
#your title
page_title="match's game"
import cgi
datas=cgi.FieldStorage()
#now you can begin :



from random import randint as rickroll
debug_satement=False

#--- data get ---



given_matches_total=datas.getvalue("send_matches_total")
given_matches_max=datas.getvalue("send_matches_max")
given_matches_removed=datas.getvalue("send_matches_removed")
given_player=datas.getvalue("send_player")
#true = player 1
#false = player 2
given_playername_1=datas.getvalue("send_playername_1")
given_playername_2=datas.getvalue("send_playername_2")


#--- state ---

#[game_state] :
# 1 = game's menu. select your names and other things.
# 2 = gameplay. just, playing.
# 3 = end. who wins ? me

game_state=2

#is round informations missing ?
if ((given_matches_total==None) or (given_player==None)):
	#yes ? restart the game.
	if (debug_satement): print("<p>DBUG : action/restart</p>")
	if (given_matches_max!= None): given_matches_total=int(given_matches_max)
	given_matches_removed=0
	given_player=(rickroll(0,1)==1)
else:
	#no ? cool.
	given_matches_total=int(given_matches_total)
	given_matches_removed=int(given_matches_removed)
	given_player=(given_player=="True")

#is menu informations missing ?
if ((given_playername_1==None) or (given_playername_2==None) or (given_matches_max==None)):
	#yes ? goto menu.
	if (debug_satement): print("<p>DBUG : action/menu</p>")
	game_state=1
	if (given_matches_max == None):
		given_matches_max=21
		given_matches_total=21
	else:
		given_matches_max=int(given_matches_max)
		given_matches_total=int(given_matches_max)
	given_playername_1="unknow1"
	given_playername_2="unknow2"
else:
	given_matches_max=int(given_matches_max)



if (given_player):
	game_player_play=given_playername_1
	game_player_other=given_playername_2
else:
	game_player_play=given_playername_2
	game_player_other=given_playername_1





#--- matches ---


#is no matches ?
given_matches_total-=given_matches_removed
if (given_matches_total<=0):
	#yes ? finish the game.
	game_state=3


page_text=""
page_form=""
page_matches=""
if (given_matches_total < 0):
	given_matches_total=0
for i in range (given_matches_total):
	page_matches+=f"""<img src="images/allumette1.png" height="{25}%" width="{3}%">"""
for i in range (given_matches_removed):
	page_matches+=f"""<img src="images/allumette2.png" height="{25}%" width="{3}%">"""
for i in range (given_matches_max-given_matches_total-given_matches_removed):
	page_matches+=f"""<img src="images/allumette3.png" height="{25}%" width="{3}%">"""



#--- form ---


match game_state:
	case 1:
		page_text=f"""
		<h1>
		bienvenue
		</h1>
		<p>
			c'est le lancement
		</p>
		"""
		form_default_playername_1=given_playername_1
		if (given_playername_1=="unknow1"):
			given_playername_1=""
			
	
		form_default_playername_2=given_playername_2
		if (given_playername_2=="unknow2"):
			given_playername_2=""
			

		page_form_inside=f"""
		<form method ="GET" action ="main.py">
		<ul>
			<input type ="hidden" name ="send_matches_removed" value="{given_matches_removed}"/>


			<li>
				<label for ="name1">Nom du joueur 1 :</label>
				<input type ="text" id="name1" name ="send_playername_1" value="{given_playername_1}"/>
			</li>
			<li>
				<label for ="name2">Nom du joueur 2 :</label>
				<input type ="text" id="name2" name ="send_playername_2" value="{given_playername_2}"/>
			</li>
			<li>
				<label for ="matches_max">alumettes</label>
				<input type ="text" id="matches_max" name ="send_matches_max" value="{given_matches_max}"/>
			</li>
			<li>
				<input type ="submit" value ="OK">
			</li>
		</ul>
		</form>
		"""
	case 2:
		page_text=f"""
		<p>
		c'est à <b>{game_player_play}</b></br>
		il reste <b>{given_matches_total}</b> alumettes
		et <b>{given_matches_removed}</b> en ont été enlevés
		</p>
		"""
		if (debug_satement): 
			page_text+=f"""
			<p>
			DBUG :</br>
			given_player={given_player}!={not given_player}</br>
			given_matches_total={given_matches_total}</br>
			given_matches_removed={given_matches_removed}</br>
			given_playername_1={given_playername_1}</br>
			given_playername_2={given_playername_2}</br>
			</p>
			"""

		page_form_inside=f"""
		<ul>
			<input type ="hidden" name ="send_playername_1" value="{given_playername_1}"/>
			<input type ="hidden" name ="send_playername_2" value="{given_playername_2}"/>
			<input type ="hidden" name ="send_player" value="{not given_player}"/>
			
			<input type ="hidden" name ="send_matches_total" value="{given_matches_total}"/>
			<input type ="hidden" name ="send_matches_max" value="{given_matches_max}"/>


                <div class="tbouton">
				<label for ="matches">Nombre d'alumettes prises</label><br>
                </div>
                <div class="bouton">
				<input type ="radio" id="matches_1" name="send_matches_removed" value="1" checked>
				<label for ="matches_1">Un</label>
				<input type ="radio" id="matches_2" name="send_matches_removed" value="2">
				<label for ="matches_2">Deux</label>
				<input type ="radio" id="matches_3" name="send_matches_removed" value="3">
				<label for ="matches_3">Trois</label>
                </div>
                
                <div class ="ok">
				<input type ="submit" value ="OK">
                </div>
			</li>


		</ul>
		"""
	case 3:
		page_text=f"""
		<h1>
			win
		</h1>
		<p>
			<b>{game_player_play}</b> a gagné
		</p>
		"""
		#<input type ="hidden" name ="send_playername_1" value="{given_playername_1}"/>
		#<input type ="hidden" name ="send_playername_2" value="{given_playername_2}"/>
		page_form_inside=f"""
		<ul>
			<li>
				<input type ="hidden" name ="send_matches_max" value="{given_matches_max}"/>
				<input type ="submit" value ="RECOMMENCER">
			</li>
		</ul>
		"""

page_css="""
@import 'https://fonts.googleapis.com/css?family=Open+Sans';
.matches_images {
	display: flex;
	justify-content: center;   
}
.tbouton {
    display: flex;
	justify-content: center;
	font-family: 'Open Sans', sans-serif;
    font-weight: 900;
}
.bouton {
    display: flex;
	justify-content: center;
	font-family: 'Open Sans', sans-serif;
}
.ok {
    display: flex;
	justify-content: center;
}
"""



page_form=f"""
<form method ="GET" action ="main.py">
{page_form_inside}
</form>
"""

#--- assembly ---

print(f"""
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
	<style type="text/css">{page_css}</style>
	<title>{page_title}</title>
<head>
<body>



<div class="matches_images">
{page_matches}
</div>
{page_text}
{page_form}


</body>
</html>
""")