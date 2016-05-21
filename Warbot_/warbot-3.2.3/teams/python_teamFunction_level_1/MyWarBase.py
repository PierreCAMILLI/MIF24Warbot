
def actionWarBase():

	if((getHealth/getEnergy) > 2):
		if(not isMyBagEmpty()):
			setDebugString("Miam ! Miam ! Miam !");
			return eat();
	
	messages = getMessages();

	for message in messages:
		if(message.getMessage() == "whereAreYou"):
			setDebugString("I'm here base PY");
			sendMessage(message.getSenderID(), "here", "");


	return idle();
