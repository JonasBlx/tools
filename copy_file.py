import shutil

# Chemin de l'image originale
original = r"\Users\jonax\DocumentsPC\Code\Projets\Australie\Intelligence artificielle\projets_ia\cs50\course6\attention\athlete_he\Attention_Layer6_Head6.png"

# Nouveau chemin où vous voulez copier l'image
target = r"\Users\jonax\DocumentsPC\Code\Projets\Australie\Intelligence artificielle\projets_ia\cs50\course6\attention\images_analyzed\reference.png"

# Copier l'image
shutil.copyfile(original, target)
