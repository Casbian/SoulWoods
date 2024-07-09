//Package
package soulWoods;
//Imported Classes
import java.util.Scanner;
//Game Root Class
class Root {
//Game Logic 
public static void main(String[] args) {
Game g = new Game();
Player y = new Player();
Scanner z = new Scanner(System.in);
Encounter e = new Encounter();	
CMDColors c = new CMDColors();
	
System.out.println(g.welcomeArt);
System.out.println(g.welcomeText);

boolean gameLoop = false;
while (gameLoop==false) {
++e.roundCounter;
Monster x = new Monster();
x.monsterLevel = e.roundCounter;
x.monsterHealth = (int)(Math.random() * 100)+x.monsterLevel;
x.monsterSpeed = (int)(Math.random() * 30)+x.monsterLevel;
x.monsterDamage = (int)(Math.random() * 10)+x.monsterLevel;
y.playerLevel = e.roundCounter;
Upgrades u = new Upgrades();
System.out.println("Du betrittst eine Lichtung im Wald.");
System.out.println("Ein Monster erscheint !!!");
System.out.println(c.CYAN+"Willst du KÄMPFEN (1) oder FLÜCHTEN (0) ?!");
System.out.println("Round: "+e.roundCounter+c.RESET);
System.out.println(e.formatencounterFrame(e.encounterFrame,y,x));
System.out.print("Input : ");
int inputInt = z.nextInt();
if (inputInt==1) {
int fightResult = e.fight(y, x);
y.playerHealth = fightResult;
if (y.playerHealth<=0) {
System.out.println(c.RED+"YOU DIED\nRound "+e.roundCounter+c.RESET);
System.exit(0);
}
else {
}
}
else {
int fleeresult = e.flee(y);
y.playerFleeCounter = fleeresult;
if (y.playerFleeCounter<0) {
System.out.println(c.RED+"YOU DIED FROM EXHAUSTION\nRound "+e.roundCounter+c.RESET);
System.exit(0);
}
else {
}
}
if (e.roundCounter%5==0) {
String item = u.randomItem(u.itemsBuff, u.itemsDebuff);
System.out.println(c.PURPLE+"\nItem found !!!");
System.out.println("Item : "+item+c.RESET);
switch (item) {
case "EnergieGetraenk":
System.out.println(c.GREEN+"NICE");
System.out.println("-- +10 Speed --"+c.RESET);
y.playerSpeed = u.energieGetraenk(y);
break;
case "Kippe":
System.out.println(c.GREEN+"NICE");
System.out.println("-- +10 Damage --"+c.RESET);
y.playerSpeed = u.kippe(y);
break;
case "Admin Passwort":
System.out.println(c.GREEN+"RLY NICE");
System.out.println("-- +50 Health --"+c.RESET);
y.playerSpeed = u.adminPasswort(y);
break;
case "Beschwerde":
System.out.println(c.GREEN+"RLY NICE");
System.out.println("-- +30 Damage --"+c.RESET);
y.playerSpeed = u.beschwerde(y);
break;
case "Hodenhalter":
System.out.println(c.RED+"MEINE EIER");
System.out.println("-- -10 Speed --"+c.RESET);
y.playerSpeed = u.hodenhalter(y);
break;
case "SUS Pössel":
System.out.println(c.RED+"PARANOIA");
System.out.println("-- -20 Damage --"+c.RESET);
y.playerSpeed = u.sUSPössel(y);
break;
case "The Man Himself":
System.out.println(c.RED+"OHH NEEE");
System.out.println("-- -30 Health --"+c.RESET);
y.playerSpeed = u.theManHimself(y);
break;
case "Alter Mann":
System.out.println(c.RED+"BRUH FAHR JETZT");
System.out.println("-- -25 Speed --"+c.RESET);
y.playerSpeed = u.alterMann(y);
break;
}
}
else {
}
System.out.println(u.formatupgradesFrame(u.upgradesFrame,y));
System.out.print("Input : ");
inputInt = z.nextInt();
switch (inputInt){
case 1:
int healResult = u.chooseHeal(y);
y.playerHealth = healResult;
break;
case 2:
int speedResult = u.chooseSpeed(y);
y.playerSpeed = speedResult;
break;
case 3:
int damageResult = u.chooseDamage(y);
y.playerDamage = damageResult;
break;
}
}
z.close();
}
}