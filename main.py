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
options_debug_satement=False
options_player_color_1="#ff0000"
options_player_color_2="#0000ff"

#--- data get ---



given_state=datas.getvalue("send_state")

given_matches_max=datas.getvalue("send_matches_max")
given_playername_1=datas.getvalue("send_playername_1")
given_playername_2=datas.getvalue("send_playername_2")


#true = player 1
#false = player 2
given_player=datas.getvalue("send_player")
given_round=datas.getvalue("send_round")
given_matches_total=datas.getvalue("send_matches_total")
given_matches_removed=datas.getvalue("send_matches_removed")

#--- state ---

#[game_state] :
# 1 = game's menu. select your names and other things.
# 2 = gameplay. just, playing.
# 3 = end. who wins ? me
game_state=-1
cheater=False


def check(f_value, f_intcheck=True):
	if (f_value==None):
		return True
	if (f_intcheck):
		try:
			int(f_value)
		#except ValueError:
		#this execept any error.  but not cool for dbuging !
		except:
			return True
	return False
	#isinstance(f_value, f_type)


def hash1(f_int1, f_int2, f_int3, f_int4, f_bool1):
	return 0
	



if (check(given_state) or (given_state=="0")):
	#reseting... [->1]
	game_state=1
	if (options_debug_satement): print("<p>DBUG : action/menu</p>")
	given_state="0"
	if (given_matches_max == None):
		given_matches_max="21"
	given_matches_total=given_matches_max
	if (given_playername_1 == None):
		given_playername_1="unknow1"
	if (given_playername_2 == None):
		given_playername_2="unknow2"
	#!
	given_round="0"
	given_player=f"{(rickroll(0,1)==1)}"
	given_matches_removed="0"





given_state=int(given_state)

#here you must have menu information.
if (check(given_player,False) or check(given_playername_1,False) or check(given_playername_2,False) or check(given_matches_max)):
	#no ? ur cheater. [->0]
	cheater=True
	#1/0
	
else:

	given_player=(given_player=="True")
	given_matches_max=int(given_matches_max)


	if (given_state==1):
		#starting... [->2]
		game_state=2
		if (options_debug_satement): print("<p>DBUG : action/start</p>")
	
		given_round="0"
		given_matches_total=given_matches_max
		given_matches_removed="0"

	#here, you must have round informations.
	if (check(given_matches_total) or check(given_matches_removed)):
		if (options_debug_satement): print(f"<p>{check(given_matches_total)} or {check(given_matches_removed)}</p>")
		#no ? ur cheater. [->0]
		cheater=True
		#1/0

	else:
		given_round=int(given_round)
		given_matches_total=int(given_matches_total)
		given_matches_removed=int(given_matches_removed)

		if (given_state==2):
			#checks
			if (given_matches_total>given_matches_max or given_matches_total<0 or given_matches_max<0 ):
				cheater=True
			if (given_matches_removed>3 or given_matches_removed<0):
			# or given_matches_total+given_matches_removed>given_matches_max or given_matches_total-given_matches_removed<0#noo !!
				cheater=True

			#continuing... [->2]
			game_state=2


		if (given_state==3):
			#check
			if (given_matches_total!=0):
				cheater=True


			#restarting... [->2]
			game_state=2
			#given_round=0#!
			given_matches_total=given_matches_max
			given_matches_removed=0
			#given_player=(rickroll(0,1)==1)#!



#here, you must have a state.
if (game_state==-1):
	#no ? ur cheater. [->0]
	cheater=True
	#1/0



if (cheater):
	game_state=0
	#avoid errors
	given_player=False


if (given_player):
	game_player_color=options_player_color_1
	game_player_play=given_playername_1
	game_player_other=given_playername_2
else:
	game_player_color=options_player_color_2
	game_player_play=given_playername_2
	game_player_other=given_playername_1





#--- matches ---

if (game_state==0):
	page_matches=f"""<section><img src="images/allumette6.png"></section>"""

else:
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
		if (given_matches_total-i <= 3 and game_state==2):
			page_matches+=f"""<section><label for="matches_{given_matches_total-i}" class="link_label"><img src="images/allumette4.png" class="flammable"><footer>⮝</footer></label></section>"""
		else:
			page_matches+=f"""<section><img src="images/allumette1.png"></section>"""
	for i in range (given_matches_removed):
		page_matches+=f"""<section><img src="images/allumette2.png"></section>"""
	for i in range (given_matches_max-given_matches_total-given_matches_removed):
		page_matches+=f"""<section><img src="images/allumette3.png"></section>"""
	# height="{25}%" width="{3}%"



#--- form ---


def plurial(f_number):
	if abs(f_number>1):
		return "s"
	else:
		return ""


match game_state:

	case 0:
		page_text=f"""
		<h1>
		tricheur !!
		</h1>
		<p>
			oui, tu as bidouillé l'URL, et je le sais.
		</p>
		"""


		page_form_inside=f"""
		<form method ="GET" action ="main.py">
		<ul>
			<input type ="hidden" name ="send_state" value="0"/>

			<li>
				<label>retourne jouer <b>normalement</b> :</label>
			</li>
			<li>
				<input type ="submit" value ="OK" class="button">
			</li>
		</ul>
		</form>
		"""

	case 1:
		page_text=f"""
		<h1>
		bienvenue
		</h1>
		<p>
			saisisez vos informations pour jouer !
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
			<input type ="hidden" name ="send_state" value="1"/>


			<li>
				<label for ="name1" class="for_player_1">joueur 1 :</label>
				<input type ="text" id="name1" name ="send_playername_1" value="{given_playername_1}"/>
			</li>
			<li>
				<label for ="name2" class="for_player_2">joueur 2 :</label>
				<input type ="text" id="name2" name ="send_playername_2" value="{given_playername_2}"/>
			</li>
			<li>
				<label for ="matches_max">alumettes :</label>
				<input type ="text" id="matches_max" name ="send_matches_max" value="{given_matches_max}"/>
			</li>
			<li>
				<input type ="submit" value ="OK" class="button">
			</li>

			<input type ="hidden" name ="send_player" value="{given_player}"/>
		</ul>
		</form>
		"""
	case 2:

		if (given_matches_removed==0):
			page_text_line2=""
		#elif (given_matches_removed<=1):
		else:
			page_text_line2=f"<b>{given_matches_removed}</b> brûlé{plurial(given_matches_removed)} le dernier tour"
		page_text=f"""
		<h1 class="for_player">
		c'est à <b>{game_player_play}</b>
		</h1>
		<p>
		il reste <b>{given_matches_total}</b> alumette{plurial(given_matches_total)}<br>
		{page_text_line2}
		</p>
		"""
		if (options_debug_satement): 
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


		check_numbers_texts_old=["Un","Deux","Trois"]
		check_numbers_texts=["une","deux","trois"]

		
		if (given_matches_removed <= 0):
			here_tocheck=1
		elif (given_matches_removed>given_matches_total):
			here_tocheck=given_matches_total
		else:
			here_tocheck=given_matches_removed

		i=0
		page_form_check=""
		while (i<3 and i<given_matches_total):
			if (here_tocheck==(i+1)):
				here_checked=" checked"
			else:
				here_checked=""
			page_form_check+=f"""
			<input type ="radio" class="matche" id="matches_{i+1}" name="send_matches_removed" value="{i+1}"{here_checked}>
			<label for ="matches_{i+1}">{check_numbers_texts_old[i]}</label>
			"""
			#"""+page_form_check
			i+=1


		i=0
		page_form_sentances=""
		while (i<3 and i<given_matches_total):
			page_form_sentances+=f"""
			<label class="sentance" id="sentance_{i+1}">brûler <b>{check_numbers_texts[i]}</b> alumette{plurial(i+1)}</label>
			"""
			i+=1

		given_round=given_round+1
		given_player=not given_player
		page_form_inside=f"""

			<input type ="hidden" name ="send_state" value="2"/>

			<input type ="hidden" name ="send_playername_1" value="{given_playername_1}"/>
			<input type ="hidden" name ="send_playername_2" value="{given_playername_2}"/>
			<input type ="hidden" name ="send_round" value="{given_round}"/>
			
			<input type ="hidden" name ="send_player" value="{given_player}"/>
			<input type ="hidden" name ="send_matches_total" value="{given_matches_total}"/>
			<input type ="hidden" name ="send_matches_max" value="{given_matches_max}"/>


			<ul>
				<!--
				<li>
					<b>
						<label for ="matches">Nombre d'alumettes prises</label><br>
					</b>
				</li>
				-->
				<li>
				</li>
				
				<li>
					<div class="sentances">
					{page_form_check}
					{page_form_sentances}
					</div>
				</li>
				<li>
					<input type ="submit" value ="OK" class="button">
				</li>
			<ul>
		"""

	case 3:
		page_text=f"""
		<h1 class="for_player">
			GG
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
				
				<input type ="hidden" name ="send_state" value="3"/>
				
				<input type ="hidden" name ="send_playername_1" value="{given_playername_1}"/>
				<input type ="hidden" name ="send_playername_2" value="{given_playername_2}"/>
				<input type ="hidden" name ="send_round" value="{given_round}"/>

				<input type ="hidden" name ="send_player" value="{given_player}"/>
				<input type ="hidden" name ="send_matches_total" value="{given_matches_total}"/><!-- is 0 at this point -->
				<input type ="hidden" name ="send_matches_max" value="{given_matches_max}"/>
				<input type ="hidden" name ="send_matches_removed" value="0"/><!-- must be send -->

				
				<input type ="submit" value ="recomencer" class="button">
				</form>
			</li>
			<li>
				<form method ="GET" action ="main.py">
					<input type ="hidden" name ="send_state" value="0"/>
					<!--it make it like a list, so except an error, so reset-->

					<input type ="hidden" name ="send_playername_1" value="{given_playername_1}"/>
					<input type ="hidden" name ="send_playername_2" value="{given_playername_2}"/>
					<input type ="hidden" name ="send_matches_max" value="{given_matches_max}"/>
					
					<input type ="submit" value ="quitter" class="button">
			</li>
		</ul>
		"""

page_css=f"""
@import 'https://fonts.googleapis.com/css?family=Open+Sans';
body {{

	.link_label {{
		cursor: pointer;
	}}


	aside {{/*images*/
		display: flex;
		text-align: justify;
		justify-content: center;
		section {{
			text-align: center;
			img {{
				width:100%;
				height:90%;
			}}
			.flammable {{
				width:100%;
				height:90%;
			}}

			footer {{
				width:100%;
				height:0%;/*!no matter*/
			}}
		}}
	}}

	.for_player {{
		color: {game_player_color};
	}}
	.for_player_1 {{
		color: {options_player_color_1};
	}}
	.for_player_2 {{
		color: {options_player_color_2};
	}}

	section {{/*text+form*/
		font-family: 'Open Sans', sans-serif;
		header {{/*the text decription*/
			margin: 5px;
			text-align: center;
			
			h1 {{/*title*/
				font-weight: 500;
			}}
			p {{/*paragraph*/
			}}
			b {{/*bold*/
				font-weight: 900;
			}}
		}}

		article {{/*the form*/
			margin: 5px;
			li {{/*each element*/
				display: flex;
				justify-content: center;
			}}
			label {{
				margin: 0px 5px 0px 5px;
			}}
			b {{/*bold*/
				font-weight: 900;
			}}

			input[type='radio'] {{
			    accent-color: {game_player_color};
			}}
			
			

			.sentances {{/* for all sentances */
			
				display: flex;
				justify-content: center;
				margin-bottom: 30px;/*!*/

				/* class for each frame and checker. used to hide :*/
				.matche {{ 
					opacity: 1;
					z-align:1;
				}}
				/* using id bcs it must be unic, and for for= */
				.sentance {{/*for each of them*/
					margin-top: 30px;/*!*/
					opacity: 0;
					position: absolute;
					text-align: center;
					text-intend: 0px;
					z-align:0;
				}}
				#matches_1:checked ~ #sentance_1 {{
					opacity: 1;
				}}
				#matches_2:checked ~ #sentance_2 {{
					opacity: 1;
				}}
				#matches_3:checked ~ #sentance_3 {{
					opacity: 1;
				}}
			}}

			
			.button {{/*the button*/
				background-color: #cccccc;
				padding: 5px;
				margin: 5px;
				color: #330033;
				text-align: center;
				font-size: 100%;
			}}
		}}
	}}
}}
"""



page_form=f"""
{page_form_inside}
"""

#--- assembly ---

print(f"""
<!doctype html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
	<style type="text/css">{page_css}</style>
	<title>{page_title}</title>
</head>
<body>


<!-- the form is this big to be able having form element at differents places -->
<form method ="GET" action ="main.py">
	<aside>
	{page_matches}
	</aside>
	<section>
		<header>
			{page_text}
		</header>
		<article>
			{page_form}
		</article>
	</section>
</form>


</body>
</html>
""")