# 📤 GUIDE UPLOAD COMPLET GITHUB

**Objectif** : Uploader les 27 fichiers du dossier `saviesa-framework-github/` vers GitHub

---

## 🎯 MÉTHODE RECOMMANDÉE : Git Command Line

### **Étape 1 : Initialiser Git dans le dossier (2 min)**

Ouvrir PowerShell dans le dossier `saviesa-framework-github/` :

```powershell
cd "d:\Data_OBs\SCIENCE_DE_LINTENTION\00_META\01_FORMATION\FORMATION_HERITIER\CONTEXTE_HISTORIQUE\PHILOSOPHIE\ARTICLES\saviesa-framework-github"

# Initialiser Git
git init

# Configurer remote (remplacer par votre URL)
git remote add origin https://github.com/jcbogui/saviesa-framework.git
```

---

### **Étape 2 : Ajouter tous les fichiers (1 min)**

```powershell
# Ajouter tous les fichiers
git add .

# Vérifier les fichiers ajoutés
git status
```

**Résultat attendu** : ~27 fichiers en vert (new file)

---

### **Étape 3 : Commit (1 min)**

```powershell
git commit -m "feat: Add complete Saviesa Framework implementation

- Add 4 validation scripts (COVID, Education, Diagnostic, LOOCV)
- Add 4 utility modules (models, metrics, visualization)
- Add 2 Jupyter notebooks (interactive examples)
- Add 22 unit tests (pytest)
- Add COVID dataset (n=65) and 3 figures
- Add complete documentation (guides, API reference)
- Add requirements.txt and configuration files"
```

---

### **Étape 4 : Push vers GitHub (2 min)**

```powershell
# Pull d'abord (pour récupérer README, LICENSE, .gitignore créés sur GitHub)
git pull origin main --allow-unrelated-histories

# Résoudre conflits si nécessaire (garder version locale pour README)

# Push
git branch -M main
git push -u origin main
```

---

## ⚠️ SI ERREUR "UNRELATED HISTORIES"

Si erreur lors du pull :

```powershell
# Option 1 : Force push (ATTENTION : écrase README GitHub)
git push -f origin main

# Option 2 : Merge manuel
git pull origin main --allow-unrelated-histories --no-edit
git push origin main
```

**Recommandation** : Option 2 (merge) pour conserver historique

---

## 🔄 ALTERNATIVE : GitHub Desktop (plus simple)

### **Étape 1 : Installer GitHub Desktop**

Télécharger : https://desktop.github.com/

### **Étape 2 : Cloner le dépôt**

1. Ouvrir GitHub Desktop
2. File → Clone repository
3. Sélectionner `jcbogui/saviesa-framework`
4. Choisir destination locale

### **Étape 3 : Copier fichiers**

1. Copier TOUT le contenu de `saviesa-framework-github/` 
2. Coller dans le dossier cloné (écraser README, LICENSE, .gitignore)

### **Étape 4 : Commit et Push**

1. GitHub Desktop détecte automatiquement les changements
2. Écrire message commit (voir ci-dessus)
3. Cliquer "Commit to main"
4. Cliquer "Push origin"

---

## ✅ VÉRIFICATION FINALE

Après upload, vérifier sur https://github.com/jcbogui/saviesa-framework :

- [ ] 27 fichiers présents
- [ ] Structure dossiers visible (data/, scripts/, figures/, docs/, examples/, tests/)
- [ ] README.md s'affiche avec badges
- [ ] Figures PNG visibles dans figures/
- [ ] LICENSE MIT visible

---

## 🎯 COMMANDES RAPIDES (COPIER-COLLER)

```powershell
# Tout en une fois
cd "d:\Data_OBs\SCIENCE_DE_LINTENTION\00_META\01_FORMATION\FORMATION_HERITIER\CONTEXTE_HISTORIQUE\PHILOSOPHIE\ARTICLES\saviesa-framework-github"
git init
git remote add origin https://github.com/jcbogui/saviesa-framework.git
git add .
git commit -m "feat: Add complete Saviesa Framework implementation"
git pull origin main --allow-unrelated-histories --no-edit
git push -u origin main
```

---

## 📧 BESOIN D'AIDE ?

Si problème, me fournir :
1. Message d'erreur complet
2. Résultat de `git status`
3. Résultat de `git remote -v`

---

**Temps total estimé** : 5-10 minutes

**Prochaine étape** : Configuration dépôt (description, topics, release)
