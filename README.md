# 🌐 NovaTech - Site Web Officiel

Site web professionnel pour **NovaTech**, startup innovante spécialisée dans les solutions digitales, développement web, applications mobiles et solutions cloud.

## 📋 Table des matières
- [Pages disponibles](#-pages-disponibles)
- [Déploiement sur GitHub Pages](#-déploiement-sur-github-pages)
- [Scripts Python](#-scripts-python)
- [Structure du projet](#-structure-du-projet)
- [Contributions](#-contributions)
- [Licence](#-licence)

## 📄 Pages disponibles

| Page | Description |
|------|-------------|
| **index.html** | Page d'accueil avec présentation et services principaux |
| **services.html** | Détails des services avec grille tarifaire |
| **calculator.html** | Calculateur interactif de devis |
| **blog.html** | Articles et actualités avec système de filtrage |
| **about.html** | À propos de l'entreprise et équipe |
| **contact.html** | Formulaire de contact et coordonnées |
| **legal.html** | Mentions légales et politique de confidentialité |

## 🚀 Déploiement sur GitHub Pages

### Prérequis
- Compte GitHub
- Git installé localement
- Navigateur web moderne

### Étapes de déploiement
1. **Cloner le repository**
   ```bash
   git clone https://github.com/votre-username/novatech-website.git
   cd novatech-website
   ```

2. **Ajouter les fichiers**
   - Copier tous les fichiers HTML, CSS, JS et assets dans le dossier cloné

3. **Configurer GitHub Pages**
   - Aller dans Settings → Pages
   - Sélectionner "Deploy from a branch"
   - Choisir la branche main et le dossier /root
   - Sauvegarder

4. **Accéder au site**
   - Votre site sera disponible à l'adresse :
   ```
   https://votre-username.github.io/novatech-website/
   ```
   - Le déploiement est généralement actif sous 1-2 minutes

## 🐍 Scripts Python

### Prérequis
- Python 3.8+
- Accès terminal

### 📊 Calculateur de Devis
**Fichier :** `scripts/calculateur_novatech.py`

**Utilisation :**
```bash
cd scripts
python calculateur_novatech.py
```

**Fonctionnalités :**
- Calcul automatique des coûts de projet
- Prise en compte de multiples paramètres :
  - Type de projet
  - Nombre de pages
  - Niveau de design
  - Fonctionnalités supplémentaires
  - Options SEO
- Application automatique de remises

**Exemple de sortie :**
```
==================================================
                DEVIS NOVATECH                
==================================================
Type de projet:        Site Web Vitrine
Nombre de pages:       5
Niveau de design:      Personnalisé
Fonctionnalités:       2 option(s)
Option SEO:            300€
--------------------------------------------------
TOTAL:                 3100€
==================================================
```

### 🔐 Générateur de Mots de Passe
**Fichier :** `scripts/generateur_mdp.py`

**Utilisation de base :**
```bash
python generateur_mdp.py
```

**Options avancées :**
```bash
# Générer un mot de passe de 16 caractères
python generateur_mdp.py -l 16

# Générer 3 mots de passe sans symboles
python generateur_mdp.py -n 3 -s

# Mode silencieux (affichage minimal)
python generateur_mdp.py -q

# Aide complète
python generateur_mdp.py --help
```

**Options disponibles :**
| Option | Description |
|--------|-------------|
| `-l N` | Longueur du mot de passe (8-64) |
| `-n N` | Nombre de mots de passe à générer |
| `-s` | Exclure les symboles spéciaux |
| `-q` | Mode silencieux |
| `--help` | Afficher l'aide complète |

## 📁 Structure du projet
```
novatech-website/
├── index.html
├── services.html
├── calculator.html
├── blog.html
├── about.html
├── contact.html
├── legal.html
├── css/
│   └── style.css
├── js/
│   └── script.js
├── images/
│   └── logo.png
├── scripts/
│   ├── calculateur_novatech.py
│   └── generateur_mdp.py
└── README.md
```

## 🤝 Contributions
Les contributions sont les bienvenues ! Pour contribuer :
1. Forker le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Committer les changements (`git commit -m 'Add AmazingFeature'`)
4. Pusher la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📜 Licence
Distribué sous licence MIT. Voir le fichier `LICENSE` pour plus d'informations.

---

**Note :** Remplacez `votre-username` par votre nom d'utilisateur GitHub réel dans les liens et instructions.