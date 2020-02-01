#This File contains helper functions that are needed by TFIDF
############################  SPELL CORRECTION ###################

def ascii(letter):
	if ord(letter) in range(48,58)+range(65,91)+range(97,123)+[35,36,37,38,64]:
		return True
	else:
		return False

##### CLEANING THE STRINGS #################################################
def clean(strn):
	out=''
	for i in strn:
		if ascii(i):
			out+=i
		else:
			out+=' '
	return out


Stopwords=['all','just','less','being','indeed','over','move','anyway','four','not','own','through','using','fifty','where','mill',
'only','find','before','one','whose','how','somewhere','much','thick','show','had','enough','should','to','must','whom','seeming','yourselves',
'under','ours','two','has','might','thereafter','latterly','do','them','his','around','than','get','very','de','none','cannot','every','un',
'they','front','during','thus','now','him','nor','name','regarding','several','hereafter','did','always','who','didn','whither','this','someone',
'either','each','become','thereupon','sometime','side','towards','therein','twelve','because','often','ten','our','doing','km','eg','some','back',
'used','up','go','namely','computer','are','further','beyond','ourselves','yet','out','even','will','what','still','for','bottom','mine','since',
'please','forty','per','its','everything','behind','does','various','above','between','it','neither','seemed','ever','across','she','somehow','be',
'we','full','never','sixty','however','here','otherwise','were','whereupon','nowhere','although','found','alone','re','along','quite','fifteen','by',
'both','about','last','would','anything','via','many','could','thence','put','against','keep','etc','amount','became','hence','onto','or','con',
'among','already','co','afterwards','formerly','within','seems','into','others','while','whatever','except','down','hers','everyone','done','least',
'another','whoever','moreover','couldnt','throughout','anyhow','yourself','three','from','her','few','together','top','there','due','been','next',
'anyone','eleven','call','therefore','then','thru','themselves','hundred','really','sincere','empty','more','himself','elsewhere','mostly','on','am',
'becoming','hereby','amongst','else','everywhere','too','herself','former','those','he','me','myself','made','twenty','these','was','cant','us',
'until','besides','nevertheless','below','anywhere','nine','can','whether','of','your','toward','my','say','something','and','whereafter',
'whenever','give','almost','wherever','is','describe','beforehand','herein','doesn','an','as','itself','at','have','in','seem','whence','ie','any',
'again','hasnt','thereby','no','perhaps','latter','meanwhile','when','detail','same','wherein','beside','also','that','other','take',
'which','becomes','you','if','nobody','unless','whereas','see','though','may','after','upon','most','hereupon','but','serious','nothing',
'such','why','off','a','whereby',
'third','i','whole','noone','sometimes','amongst','yours','their','rather','without','so','five','the','with','once','']

def remove_stopwords(tokens):
	out=[]
	for token in tokens:
		if token not in Stopwords:
			out+=[token]
	return out
