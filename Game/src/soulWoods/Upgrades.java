//Package
package soulWoods;
//Upgrades Class
class Upgrades {
//Format Object
CMDColors c = new CMDColors();
//Variables or Attributes in use
int heilung = (int)(Math.random() * 10)+1;
int damageBuff = (int)(Math.random() * 20)+1;
int speedBuff = (int)(Math.random() * 2)+1;
String upgradesFrame = ""
+"\nLevel UP"
+"\nCurrent Stats"
+"\n -- HP -<            %d"
+"\n -- Speed -<         %d"
+"\n -- Damage -<        %d"
+"\n -- Flee Counter -<  %d"
+"\nCHOOSE"
+c.GREEN+"\n-- Heal   --  %d"+c.RESET
+c.CYAN+"\n-- Speed  --  %d"+c.RESET
+c.RED+"\n-- Damage --  %d"+c.RESET;
String[] itemsBuff = {"EnergieGetraenk", "Kippe", "Admin Passwort", "Beschwerde"};
String[] itemsDebuff = {"Hodenhalter","SUS Pössel","The Man Himself","Alter Mann"};
//Methods
String formatupgradesFrame(String Frame,Player y) {
String resultFrame = String.format(Frame,y.playerHealth,y.playerSpeed,y.playerDamage,y.playerFleeCounter,heilung,speedBuff,damageBuff);
return resultFrame;
}
int chooseHeal(Player y) {
y.playerHealth = y.playerHealth+heilung;
return y.playerHealth;
}
int chooseSpeed(Player y) {
y.playerSpeed = y.playerSpeed+speedBuff;
return y.playerSpeed;
}
int chooseDamage(Player y) {
y.playerDamage = y.playerDamage+damageBuff;	
return y.playerDamage;
}
String randomItem(String[] itemDebuff,String[] itemBuff) {
int randomNumber1 = (int)(Math.random() * 2);
String result = null;
switch (randomNumber1) {
case 0:
int randomNumber2 = (int)(Math.random() * itemBuff.length);
result = itemBuff[randomNumber2];
break;
case 1:
randomNumber2 = (int)(Math.random() * itemDebuff.length);
result = itemDebuff[randomNumber2];
break;
}
return result;
}
int energieGetraenk(Player y) {
y.playerSpeed = y.playerSpeed+10;
return y.playerSpeed;
}
int kippe(Player y) {
y.playerDamage = y.playerDamage+10;
return y.playerDamage;
}
int adminPasswort(Player y) {
y.playerHealth = y.playerHealth+50;
return y.playerHealth;
}
int beschwerde(Player y) {
y.playerDamage = y.playerDamage+30;
return y.playerDamage;
}
int hodenhalter(Player y) {
y.playerSpeed = y.playerSpeed-10;
return y.playerSpeed;
}
int sUSPössel(Player y) {
y.playerDamage = y.playerDamage-20;
return y.playerDamage;
}
int theManHimself(Player y) {
y.playerHealth = y.playerHealth-30;
return y.playerHealth;
}
int alterMann(Player y) {
y.playerSpeed = y.playerSpeed-25;
return y.playerSpeed;
}
}