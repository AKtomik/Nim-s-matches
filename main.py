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



given_state=datas.getvalue("state")
given_element_1=datas.getvalue("element_1")
given_element_2=datas.getvalue("element_2")

given_matches_burnable=datas.getvalue("matches_burnable")
given_matches_max=datas.getvalue("matches_max")
given_playername_1=datas.getvalue("playername_1")
given_playername_2=datas.getvalue("playername_2")
given_score_1=datas.getvalue("score_1")
given_score_2=datas.getvalue("score_2")


#true = player 1
#false = player 2
given_player=datas.getvalue("player")
given_round=datas.getvalue("round")
given_matches_total=datas.getvalue("matches_total")
given_matches_removed=datas.getvalue("matches_removed")

#--- state ---

#[game_state] :
# 1 = game's menu. select your names and other things.
# 2 = gameplay. just, playing.
# 3 = end. who wins ? me
game_state=-1
cheater=False
skip_check=False
fail_message=""


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


#hash value
#hash1(given_matches_total, given_matches_max, given_matches_burnable, given_score_1, given_score_2, given_round, given_element_2, given_player)
def hash1(f_int_m1, f_int_m2, f_int_m3, f_int_i1, f_int_i2, f_int_r2, f_int_r1, f_bool1):
	return (f_int_m1+1)*(f_int_r1+1) +(f_int_m2+1)**3 +(f_int_m3+1)**5  +(f_int_i1+1)*(f_int_i2+1)  +f_int_r2  +(round(1/f_int_r1*100))  -f_bool1
	



#special case :
if ((given_state=="1") and (check(given_playername_1,False) or check(given_playername_2,False) or check(given_matches_max) or check(given_matches_burnable))):
	given_state="0"
	fail_message="remplis intégralement les options !"


if (check(given_state) or (given_state=="0")):
	#reseting... [->1]
	game_state=1
	if (options_debug_satement): print("<p>DBUG : action/menu</p>")
	given_state="0"
	if (check(given_matches_max)):
		given_matches_max="21"
	if (check(given_matches_burnable)):
		given_matches_burnable="3"
	given_matches_total=given_matches_max
	if (check(given_playername_1, False)):
		given_playername_1="unknow1"
	if (check(given_playername_2, False)):
		given_playername_2="unknow2"
	given_score_1="0"
	given_score_2="0"
	given_player=f"{(rickroll(0,1)==1)}"
	#!
	given_round="0"
	given_element_1="-1"
	given_element_2="-1"
	skip_check=True
	given_matches_removed="0"





given_state=int(given_state)#only this value can be here


#here you must have menu information.
if (check(given_player,False) or check(given_playername_1,False) or check(given_playername_2,False) or check(given_score_1,False) or check(given_score_2,False) or check(given_matches_max) or check(given_matches_burnable)):
	#no ? ur cheater. [->0]
	cheater=True
	fail_message=f"(manque)"
	#1/0
	
else:

	given_player=(given_player=="True")
	given_matches_max=int(given_matches_max)
	given_matches_burnable=int(given_matches_burnable)
	given_score_1=int(given_score_1)
	given_score_2=int(given_score_2)


	if (given_state==1):
		#check
			
		#starting... [->2]
		game_state=2
		if (options_debug_satement): print("<p>DBUG : action/start</p>")
	
		given_round="0"
		given_matches_total=given_matches_max
		given_matches_removed="0"

		given_element_1="-1"
		given_element_2="-1"
		skip_check=True
	

	#here, you must have round informations.
	if (check(given_matches_total) or check(given_matches_removed) or check(given_round) or check(given_element_2) or check(given_element_1)):
		if (options_debug_satement): print(f"<p>({check(given_matches_total)} or {check(given_matches_removed)} or {check(given_round)} or {check(given_element_2)} or {check(given_element_1)})</p>")
		#no ? ur cheater. [->0]
		cheater=True
		fail_message=f"(manque)"
		#1/0

	else:
		given_matches_total=int(given_matches_total)
		given_matches_removed=int(given_matches_removed)
		given_round=int(given_round)
		given_element_2=int(given_element_2)
		given_element_1=int(given_element_1)



		#ultimate check
		if (options_debug_satement): print(f"hash ; {given_element_1}=={hash1(given_matches_total, given_matches_max, given_matches_burnable, given_score_1, given_score_2, given_round, given_element_2, given_player)}  (skip:{skip_check})")
		if (not ((skip_check) or (given_element_1==hash1(given_matches_total, given_matches_max, given_matches_burnable, given_score_1, given_score_2, given_round, given_element_2, given_player)))):
			cheater=True
			fail_message=f"(hash)"
			#fail_message=f"{given_element_1}!={hash1(given_matches_total, given_matches_max, given_matches_burnable, given_score_1, given_score_2, given_round, given_element_2, given_player)}  ({skip_check})"


		

		if (given_state==2):
			#checks
			if (given_matches_total>given_matches_max or given_matches_total<0 or given_matches_max<0 ):
				cheater=True
				fail_message=f"(incohérence)"
			if (given_matches_removed>3 or given_matches_removed<0):
			# or given_matches_total+given_matches_removed>given_matches_max or given_matches_total-given_matches_removed<0#noo !!
				cheater=True
				fail_message=f"(incohérence)"
			if (given_round<0 or given_round>given_matches_max):
				cheater=True
				fail_message=f"(incohérence)"
				

			#continuing... [->2]
			game_state=2


		if (given_state==3):
			#check
			if (given_matches_total!=0 or given_matches_removed!=0):
				cheater=True
				fail_message=f"(incohérence)"


			#restarting... [->2]
			game_state=2
			given_round=0#!
			given_matches_total=given_matches_max
			given_matches_removed=0
			#given_player=(rickroll(0,1)==1)#!



#here, you must have a state.
if (game_state==-1):
	#no ? ur cheater. [->0]
	cheater=True
	fail_message=f"(fail)"
	#1/0



if (cheater):
	game_state=0
	#avoid errors
	given_player=False
else:
	#anti-cheat
	given_element_2=rickroll(254,2047)


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
			page_matches+=f"""<section><label for="matches_{given_matches_total-i}" id="flame_frame_{given_matches_total-i}" class="link_label flame_frame"><img src="images/allumette4.png" class="flammable"><footer>⮝</footer></label></section>"""
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
page_root=""#not often used

match game_state:

	#cheater page
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
		<ul>
			<input type ="hidden" name ="state" value="0"/>

			<li>
				<!--<label>tien, retourne au <b>menu</b> :</label>-->
				<label>retourne jouer <b>normalement</b> :</label>
			</li>
			<li>
				<input type ="submit" value ="OK..." class="button">
				</form>
			</li>
			<!--
			<li>
				<form method ="GET" action ="main.py">
				<input type ="submit" value ="mais j'aime tricher" class="button">
			</li>
			-->
		</ul>
		"""

	#menu
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
			<input type ="hidden" name ="state" value="1"/>
			<input type ="hidden" name ="element_1" value="-2"/>
			<input type ="hidden" name ="element_2" value="{given_element_2}"/>


			<li>
				<label for ="name1" class="for_player_1">joueur 1 :</label>
				<input type ="text" id="name1" name ="playername_1" value="{given_playername_1}"/>
			</li>
			<li>
				<label for ="name2" class="for_player_2">joueur 2 :</label>
				<input type ="text" id="name2" name ="playername_2" value="{given_playername_2}"/>
			</li>
			<li>
				<label for ="matches_max">alumettes :</label>
				<input type ="text" id="matches_max" name ="matches_max" value="{given_matches_max}"/>
			</li>
			<li>
				<label for ="matches_burnable">brûlables :</label>
				<input type ="text" id="matches_burnable" name ="matches_burnable" value="{given_matches_burnable}"/>
			</li>
			<li>
				<input type ="submit" value ="OK" class="button">
			</li>

			<input type ="hidden" name ="player" value="{given_player}"/>
			<input type ="hidden" name ="score_1" value="{given_score_1}"/>
			<input type ="hidden" name ="score_2" value="{given_score_2}"/>
		"""
	
	#in game
	case 2:

		if (given_matches_removed <= 0):
			here_tocheck=1
		elif (given_matches_removed>given_matches_total):
			here_tocheck=given_matches_total
		else:
			here_tocheck=given_matches_removed
		i=0
		page_root_check=""
		while (i<3 and i<given_matches_total):
			if (here_tocheck==(i+1)):
				here_checked=" checked"
			else:
				here_checked=""
			page_root_check=f"""
			<input type ="radio" class="matche" id="matches_{i+1}" name="matches_removed" value="{i+1}"{here_checked}>
			"""+page_root_check
			i+=1
		
		page_root=f"{page_root_check}"





		page_text_line1=f"il reste <b>{given_matches_total}</b> alumette{plurial(given_matches_total)}<br>"
		if (given_matches_removed==0):
			page_text_line2=""
		#elif (given_matches_removed<=1):
		else:
			page_text_line2=f"<b>{given_matches_removed}</b> brûlé{plurial(given_matches_removed)} le dernier tour"
			
		page_text=f"""
		<!--
		<details>
		<summary></summary>
		<p>
		{page_text_line1}
		{page_text_line2}
		</p>
		</details>
		-->
		<h1 class="for_player">
		c'est à <b>{game_player_play}</b> {given_matches_burnable}
		</h1>
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

		


		i=0
		page_form_sentances=""
		while (i<3 and i<given_matches_total):
			page_form_sentances+=f"""
			<label class="flame_sentance" id="flame_sentance_{i+1}">brûler <b>{check_numbers_texts[i]}</b> alumette{plurial(i+1)}</label>
			"""
			i+=1

		given_round=given_round+1
		given_player=not given_player
		page_form_inside=f"""

			<input type ="hidden" name ="state" value="2"/>
			<input type ="hidden" name ="element_1" value="{hash1(given_matches_total, given_matches_max, given_matches_burnable, given_score_1, given_score_2, given_round, given_element_2, given_player)}"/>
			<input type ="hidden" name ="element_2" value="{given_element_2}"/>

			<input type ="hidden" name ="playername_1" value="{given_playername_1}"/>
			<input type ="hidden" name ="playername_2" value="{given_playername_2}"/>
			<input type ="hidden" name ="round" value="{given_round}"/>
			<input type ="hidden" name ="score_1" value="{given_score_1}"/>
			<input type ="hidden" name ="score_2" value="{given_score_2}"/>
			

			<input type ="hidden" name ="player" value="{given_player}"/>
			<input type ="hidden" name ="matches_total" value="{given_matches_total}"/>
			<input type ="hidden" name ="matches_max" value="{given_matches_max}"/>
			<input type ="hidden" name ="matches_burnable" value="{given_matches_burnable}"/>

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
					<div class="flame_sentances">
					<p></p>
					{page_form_sentances}
					</div>
				</li>
				<li>
					<input type ="submit" value ="OK" class="button">
				</li>
		"""

	#end
	case 3:
		if (given_player):
			given_score_1+=1
		else:
			given_score_2+=1

		page_text=f"""
		<h1 class="for_player">
			GG
		</h1>
		<p>
			<b>{game_player_play}</b> a gagné
		</p>
		<p>
			<section> </section>  <section class="for_player_1">{given_playername_1}  <b>{given_score_1}</b></section> - <section class="for_player_2"><b>{given_score_2}</b>  {given_playername_2}</section>
		</p>
		"""
		#<input type ="hidden" name ="playername_1" value="{given_playername_1}"/>
		#<input type ="hidden" name ="playername_2" value="{given_playername_2}"/>
		page_form_inside=f"""
			<li>
				
				<input type ="hidden" name ="state" value="3"/>
				<input type ="hidden" name ="element_1" value="{hash1(given_matches_total, given_matches_max, given_matches_burnable, given_score_1, given_score_2, given_round, given_element_2, given_player)}"/>
				<input type ="hidden" name ="element_2" value="{given_element_2}"/>
				
				<input type ="hidden" name ="playername_1" value="{given_playername_1}"/>
				<input type ="hidden" name ="playername_2" value="{given_playername_2}"/>
				<input type ="hidden" name ="round" value="{given_round}"/>
				<input type ="hidden" name ="score_1" value="{given_score_1}"/>
				<input type ="hidden" name ="score_2" value="{given_score_2}"/>

				<input type ="hidden" name ="player" value="{given_player}"/>
				<input type ="hidden" name ="matches_total" value="{given_matches_total}"/><!-- is 0 at this point -->
				<input type ="hidden" name ="matches_max" value="{given_matches_max}"/>
				<input type ="hidden" name ="matches_burnable" value="{given_matches_burnable}"/>
				<input type ="hidden" name ="matches_removed" value="0"/><!-- must be send -->

				
				<input type ="submit" value ="recomencer" class="button">
				</form>
			</li>
			<li>
				<form method ="GET" action ="main.py">
					<input type ="hidden" name ="state" value="0"/>
					<!--it make it like a list, so except an error, so reset-->

					<input type ="hidden" name ="playername_1" value="{given_playername_1}"/>
					<input type ="hidden" name ="playername_2" value="{given_playername_2}"/>
					<input type ="hidden" name ="matches_max" value="{given_matches_max}"/>
					<input type ="hidden" name ="matches_burnable" value="{given_matches_burnable}"/>
					
					<input type ="submit" value ="quitter" class="button">
			</li>
		"""
	


css_flamed_frame=f"""
footer {{
	color: {game_player_color};
	opacity: 1;
}}
img {{
	content: url("images/allumette5.png");
}}
"""
css_flamed_sentance=f"""
opacity: 1;
"""

page_css=f"""
@import 'https://fonts.googleapis.com/css?family=Open+Sans';
body {{

	.link_label {{
		cursor: pointer;
	}}


	/*dynamic parth. is to root to be able to make tow cousin dynamic*/
	/*radio input*/
		.matche {{
			
			/*
		    accent-color: {game_player_color};
			display: flex;
			justify-content: center;
			*/
			position: absolute;
			opacity: 0;
			z-align: 1;
		}}

	/*image dynamic parth*/
		#matches_1:checked ~ aside>section{{
			#flame_frame_1 {{ {css_flamed_frame} }}
		}}
		#matches_2:checked ~ aside>section{{
			#flame_frame_1 {{ {css_flamed_frame} }}
			#flame_frame_2 {{ {css_flamed_frame} }}
		}}
		#matches_3:checked ~ aside>section{{
			#flame_frame_1 {{ {css_flamed_frame} }}
			#flame_frame_2 {{ {css_flamed_frame} }}
			#flame_frame_3 {{ {css_flamed_frame} }}
		}}
	/*text dynamic parth*/
		#matches_1:checked ~ section>article>ul>li>.flame_sentances>.flame_sentance#flame_sentance_1 {{{css_flamed_sentance}}}
		#matches_2:checked ~ section>article>ul>li>.flame_sentances>.flame_sentance#flame_sentance_2 {{{css_flamed_sentance}}}
		#matches_3:checked ~ section>article>ul>li>.flame_sentances>.flame_sentance#flame_sentance_3 {{{css_flamed_sentance}}}



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
				height:91%;
			}}

			footer {{
				
				/* radio and parth to display is mooved to ROOT */
				color:#550000;

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
			section {{
				display: inline-block;
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
			.fail {{
				font-weight: 900;
				color: #ff5500;
				/*
				border-style:solid;
				border-width: 3px;
				border-color: rgb(255,0,30);
				*/
			}}
			label {{
				margin: 0px 5px 0px 5px;
			}}
			b {{/*bold*/
				font-weight: 900;
			}}

			
			

			.flame_sentances {{/* for all sentances */
			
				display: flex;
				justify-content: center;
				/*margin-bottom: 30px;!*/

				/* radio and parth to display is mooved to ROOT */

				.flame_sentance {{/*hide and style*/
					/*margin-top: 30px;!*/
					opacity: 0;
					position: absolute;
					text-align: center;
					text-intend: 0px;
					z-align:0;
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


if (fail_message==""):
	form_fail=""
else:
	form_fail=f"""
<li class="fail">
	<p>
		{fail_message}
	</p>
</li>
"""

page_form=f"""
<ul>
{page_form_inside}
{form_fail}
</ul>
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
	{page_root}
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