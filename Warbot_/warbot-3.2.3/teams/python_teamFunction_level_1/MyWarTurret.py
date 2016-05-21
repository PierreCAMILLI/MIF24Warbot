
def actionWarTurret():
	
	percepts = getPercepts();
	
	for percept in percepts:
		if(isEnemy(percept)):
			setDebugString("Ennemi repéré");
			setHeading(percept.angle);
			
			if(isReloaded()):
				setDebugString("FIRE!");
				return fire();
			else:
				return reloadWeapon();
		else:
			setDebugString("Aucun ennemi en vue");
	
	return idle();