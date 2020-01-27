def most_frequent(text):
	text= "".join(text.split())
	d={}
	for letter in text:
		d[letter]=d.get(letter,0)+1
	for value in d.values.sort(reverse=True):
		for key in d:
			if d[key]==value:
				ptint(key,value)







if __name_ == "__main__"
	text_english= """GitHub Packages is a package hosting service, 
	fully integrated with GitHub. 
	GitHub Packages combines your source code and packages in one place to provide integrated permissions management and billing, so you can centralize your software development on GitHub.
	You can publish packages in a public repository (public packages) 
	to share with all of GitHub, or in a private repository
	 (private packages) to share with collaborators or an organization. 
	 You can use GitHub roles and teams to limit who can install or 
	 publish each package, as packages inherit the permissions of 
	 the repository. Anyone with read permissions for a repository 
	 can install a package as a dependency in a project, and anyone 
	 with write permissions can publish a new package version.
	You can host multiple packages in one repository and see more 
	information about each package by viewing the package's README, 
	download statistics, version history, and more.
	You can integrate GitHub Packages with GitHub APIs, 
	GitHub Actions, and webhooks to create an end-to-end 
	DevOps workflow that includes your code, CI, and 
	deployment solutions."""

	print("The most frequent letters in English Language are\n ")
	most_frequent(english_text)

	malaylam_text=""" മുതിര്‍ന്ന പൗരന്‍മാരുടെ രചനകള്‍ കോര്‍ത്തിണക്കി 
	കൊച്ചിയിലൊരു ചിത്രപ്രദര്‍ശനം . 
	കൊച്ചി പത്തടിപ്പാലത്തെ കേരള 
	ചരിത്രമ്യൂസിയത്തില്‍ സംഘടിപ്പിച്ചിരിക്കുന്ന പ്രദര്‍ശനത്തിന് 
	മികച്ച പ്രതികരണമാണ് കലാസ്വാദകരില്‍ നിന്ന് കിട്ടുന്നത്. 

	പതിനഞ്ച് ചിത്രകാരന്‍മാരുടെ മിഴിവുളള രചനകളാണ് ചുവരു നിറയെ . 
	ചിത്രങ്ങള്‍ വരച്ചൊരുക്കിയിരിക്കുന്നത് അമ്പത്തിയഞ്ച് വയസിനു 
	മുകളില്‍ പ്രായമുളള ചിത്രകാരന്‍മാര്‍. നാടറിയുന്ന പ്രൊഫഷണല്‍ ചിത്രകാരന്‍മാര്‍ 
	മുതല്‍  കാലങ്ങളുടെ ഇടവേളയ്ക്കു ശേഷം പെയിന്‍റിങ് ബ്രഷ് കയ്യിലെടുത്തവരുടെ 
	വരെ വരകളുണ്ട്  ഇക്കൂട്ടത്തില്‍.

	ആലുവ ചെമ്പറക്കിയിലെ ബ്ലസ് റിട്ടയര്‍മെന്‍റ് 
	ലിവിങ്ങിലെ  അന്തേവാസികളായ മുതിര്‍ന്ന പൗരന്‍മാരുടെ സൃഷ്ടികളും പ്രദര്‍ശനത്തിലുണ്ട്.  കളിമണ്ണില്‍ തീര്‍ത്ത കലാസൃഷ്ടികളും പ്രദര്‍ശനത്തിന്‍റെ മറ്റൊരാകര്‍ഷണം. നാലുമണിപൂക്കള്‍ എന്നു പേരിട്ട പ്രദര്‍ശനം ഞായറാഴ്ച വരെ നീളും.
	"""
	print("The most frequent letters in Malayalam Language are\n")

	most_frequent(malaylam_text)

	Hindi_text="""
	कहानी
	पीके एक राजनीतिक व्यंग्य है, जो कि समाज में फैले भ्रष्टाचार को उजागर करता है। 
	निर्देशक राजकुमार हिरानी के मुताबिक फिल्म भगवान और उसके भक्तों पर व्यंग्य करती है।

	कथानक

	एक एलियन (आमिर खान) बिना किसी चीज के पृथ्वी पर आता है, 
	उसके पास कपड़े तक नहीं है सिवाय उसके लाॅकेट के जो कि उसका 
	रिमोट है और उसी के सहारे अंतरिक्ष यान को बुलाकर वह अपने ग्रह 
	पर वापस जा सकता है लेकिन कुछ समय के भीतर ही उस एलियन यानी 
	आमिर खान से लाॅकेट लूट लिया जाता है। वह उसे वापस पाने का प्रयास 
	करता है मगर असफल रहता है। वह ऐसी धरती पर आ गया है जो कि उसके 
	घर से बिल्कुल अलग है। यहां वह धीरे धीरे पैसों और कपड़ों का मतलब समझता है।

	एक बार, जब वह अपने जीवन के लिए चल रहा होता है, भैरो सिंह (संजय दत्त) 
	की गाड़ी से लड़ जाता है। उसे लगता है कि इस एलियन की याददाश्त जा चुकी है 
	और वह किसी को पहचान नहीं पा रहा है। वह उस एलियन को अपने साथ ले जाता 
	है और धरती के रीति रिवाजों को समझाने में उसकी मदद करता है। वह पृथ्वी पर कोई 
	भी भाषा समझ नहीं पाता है और वह महिला के हाथों से उसकी भाषा को अपने अंदर लेने 
	की कोशिश करता रहता है। भैरों को लगता है कि एलियन औरतों की तरफ ज्यादा प्रभावित है 
	इसलिए वह उसे नाइट क्लब में लेकर जाता है जहां वह हाथ पकड़ने के लिए अब स्वतंत्र था। 
	सीख जाता है।"""

	print("The most frequent letters in Hindi lanuage are\n")
	most_frequent(Hindi_text)