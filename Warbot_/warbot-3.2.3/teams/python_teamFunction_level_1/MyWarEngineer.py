
def actionWarEngineer():

	if(isAbleToCreate(WarAgentType.WarExplorer)):
		setNextAgentToCreate(WarAgentType.WarExplorer);
		return create();

	if (isBlocked()) :
		RandomHeading();
		
	return move();