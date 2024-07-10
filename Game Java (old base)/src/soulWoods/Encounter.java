//Package
package soulWoods;
//Enocunter Class
class Encounter {
//Format Object
CMDColors c = new CMDColors();
//Variables or Attributes in use
String encounterFrame = ""
+"                                                   oo`'._..---.___..-"
+"\n ~O                                              (_,-.        ,..'`"
+"\n /()'-{---                                            `'.    ;"
+"\n  /)                                                      : :`"
+"\n ~ ~                                                     _;_;"
+"\n"
+"\nPlayer Stats                                        Monster Stats"
+"\n -- HP -<     %d                                   -- HP -<      %d"
+"\n -- Speed -<  %d                                    -- Speed -<   %d"
+"\n -- Damage -< %d                                    -- Damage -<  %d"
+"\n -- Level -<  %d                                     --  Level -<  %d";
int roundCounter = 0;
String deathfromflee = "YOU DIED FROM EXHAUSTION\nRound "+roundCounter;
//Methods
String formatencounterFrame(String Frame,Player y,Monster x) {
String resultFrame = String.format(Frame,y.playerHealth,x.monsterHealth,y.playerSpeed,x.monsterSpeed,y.playerDamage,x.monsterDamage,y.playerLevel,x.monsterLevel);
return resultFrame;
}
int fight(Player y,Monster x) {
boolean deathLoop = false;
if (y.playerSpeed>=x.monsterHealth) {	
while (deathLoop==false) {
x.monsterHealth = x.monsterHealth-y.playerDamage;
y.playerHealth = y.playerHealth-x.monsterDamage;
if (y.playerHealth<=0 || x.monsterHealth<=0) {
deathLoop = true;
}
else {
deathLoop = false;
}
}
}
else {
while (deathLoop==false) {
y.playerHealth = y.playerHealth-x.monsterDamage;
x.monsterHealth = x.monsterHealth-y.playerDamage;
if (y.playerHealth<=0 || x.monsterHealth<=0) {
deathLoop = true;
}
else {
deathLoop = false;
}
}
}
return y.playerHealth;
}
int flee(Player y) {
y.playerFleeCounter = y.playerFleeCounter-1;
return y.playerFleeCounter;
}	
}