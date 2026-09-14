# Jeux de Chiffres 🎮 (V1.0)

Bienvenue sur **Jeux de Chiffres**, un jeu de devinette classique développé en Python. Le principe est simple : le programme choisit un nombre aléatoire, et c'est à vous de le deviner en un nombre limité de tentatives !

---

## 📌 Fonctionnalités
- Génération aléatoire d'un nombre secret compris entre 1 et 100.
- Indices textuels dynamiques (**"C'est plus !"** ou **"C'est moins !"**).
- Suivi en temps réel du nombre de tentatives.
- Gestion des erreurs (entrées invalides ou hors limites).
- Limite de 5 tentatives pour pimenter la partie.

---

## 📋 Règles du Jeu
1. Le jeu sélectionne secrètement un nombre entre **1 et 100**.
2. Vous devez proposer une valeur.
3. Le programme vous guide :
   - Si votre proposition est trop petite, il affiche **"C'est plus !"**.
   - Si elle est trop grande, il affiche **"C'est moins !"**.
4. Vous disposez d'un maximum de **5 tentatives** pour trouver la bonne réponse.

---

## ⚙️ Prérequis
Pour exécuter ce script, vous devez avoir installé sur votre machine :
- **Python 3.x** (Aucune bibliothèque externe n'est requise, le jeu utilise uniquement le module natif `random`).

---

## 🚀 Installation et Utilisation

1. **Cloner ou télécharger le dépôt** sur votre machine locale :
   ```bash
   git clone https://github.com/yahiagaied/jeux_chiffres.git
   ```

2. **Se placer dans le dossier du projet** :
   ```bash
   cd jeux_chiffres
   ```

3. **Lancer le jeu** avec Python :
   ```bash
   python main.py
   ```

## 🖼️ Aperçu

![Interface principale](screenshot.png)


## 📝 Licence
Ce projet est open source et disponible sous licence [MIT](LICENSE).