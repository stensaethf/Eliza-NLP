'''
eliza.py
Frederik Roenn Stensaeth & Phineas Callahan, 09.20.2015

A simply Python implementation of the famous Eliza program from 1966.
Users can talk to Eliza and have Eliza respond. Eliza is only able to respond
to certian things defined by the structure of the sentence.

Additional responses added by authors:
Q: you are <tag>. (optional period)
A: Why do you think I am <tag>?

Q: i <tag1> out <tag2>. (optional period)
A: How did you <tag1> out <tag2>?

Q: do you like <tag>? (optional question mark)
A: I do not have a strong opinion about <tag>.

Q: have you ever seen <tag>? (optional question mark)
A: No, I have not seen <tag>. I do not get out often.
'''

import sys
import re

def startEliza():
	"""
	startEliza() starts up Eliza and prompts the user to tell her about
	his/hers problems. The respond depends upon what the user has said. 

	@param: n/a
	@return: n/a
	"""

	print("Hello. Please tell me about your problems.")
	
	while True:
		user = input().lower()

		response = re.sub('^goodbye$', 'Goodbye!', user)
		if response != user:
			print(response)
			return

		response = re.sub('^yes$', 'I see.', response)
		response = re.sub('^no$', 'Why not?', response)
		response = re.sub('^(([a-z\' ]+ you)|you)$', 
						  "Let's not talk about me.", response)
		response = re.sub('^what is ([a-z\' ]+)\?$', 
						  r'Why do you ask about \1?', response)
		response = re.sub('^i am ([a-z\' ]+)$', 
						  r'Do you enjoy being \1?', response)
		response = re.sub('^why is ([a-z\' ]+)\?$', 
						  r'Why do you think \1?', response)
		response = re.sub('^my ([a-z\' ]+)$', r'Your \1.', response)

		# Responses that the author added in addition to the ones given in the
		# assignment.
		response = re.sub('^you are ([a-z\'\- ]+)\.?$', 
						  r'What makes you think I am \1?', response)
		response = re.sub('^i ([a-z]+) out ([a-z\'\- ]+)\.?$',
						  r'How did you \1 out \2?', response)
		response = re.sub('^do you like ([a-z\'\- ]+)\??$', 
						  r'I do not have a strong opinion about \1.', 
						  response)
		response = re.sub('have you ever seen ([a-z\'\- ]+)\??', 
						  r'No, I have not seen \1. I do not get out often.', 
						  response)

		# If the response the user gave and our response are still the same,
		# this means that none of the other re.sub's matched.
		if response == user:
			response = re.sub('.*', 'Please go on.', response)

		print(response)

def main():
	if len(sys.argv) != 1:
		print("Error. This program does not take any arguments.")
		sys.exit()
	startEliza()


if __name__ == '__main__':
	main()