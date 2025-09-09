#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Analyseur de sentiments pour NovaTech
Ce script analyse les témoignages clients pour déterminer leur sentiment (positif, négatif, neutre)
Dernière mise à jour : 15/06/2023
"""

import re
import argparse
import sys
from collections import defaultdict
import math

class AnalyseurSentiments:
    def __init__(self):
        """
        Initialise l'analyseur avec des dictionnaires de mots positifs et négatifs
        """
        # Mots-clés positifs avec pondération (1-3)
        self.mots_positifs = {
            'excellent': 3, 'super': 3, 'génial': 3, 'parfait': 3, 'exceptionnel': 3,
            'bon': 2, 'agréable': 2, 'satisfait': 2, 'rapide': 2, 'efficace': 2,
            'professionnel': 2, 'qualité': 2, 'recommande': 3, 'merci': 1, 'bravo': 2,
            'content': 2, 'heureux': 2, 'impressionnant': 3, 'fantastique': 3,
            'remarquable': 2, 'parfaitement': 2, 'idéal': 2, 'optimiste': 1,
            'félicitations': 2, 'extra': 2, 'formidable': 3, 'top': 2, 'meilleur': 3
        }
        
        # Mots-clés négatifs avec pondération (1-3)
        self.mots_negatifs = {
            'mauvais': 3, 'horrible': 3, 'nul': 3, 'déçu': 3, 'décevant': 3,
            'lent': 2, 'cher': 2, 'compliqué': 2, 'problème': 2, 'bug': 2,
            'erreur': 2, 'insatisfait': 3, 'déception': 3, 'pénible': 2,
            'catastrophe': 3, 'inefficace': 2, 'médiocre': 2, 'insuffisant': 2,
            'inacceptable': 3, 'désagréable': 2, 'frustrant': 2, 'honteux': 3,
            'critique': 2, 'lamentable': 3, 'désastre': 3, 'piètre': 2,
            'insupportable': 3, 'défectueux': 2, 'incomplet': 2, 'inadapté': 2
        }
        
        # Négations qui inversent le sentiment
        self.negations = {'pas', 'non', 'ne', 'ni', 'aucun', 'aucune', 'jamais', 'sans'}
        
        # Termes d'intensité qui amplifient le sentiment
        self.intensificateurs = {
            'très': 1.5, 'vraiment': 1.5, 'extrêmement': 2.0, 'totalement': 1.7,
            'absolument': 1.8, 'complètement': 1.6, 'particulièrement': 1.4,
            'fortement': 1.5, 'tellement': 1.5, 'exceptionnellement': 1.8
        }

    def preprocess_texte(self, texte):
        """
        Nettoie et prépare le texte pour l'analyse
        
        Args:
            texte (str): Texte à analyser
        
        Returns:
            list: Liste des mots nettoyés avec leurs positions
        """
        # Conversion en minuscules
        texte = texte.lower()
        
        # Suppression de la ponctuation mais conservation des négations
        texte = re.sub(r'[^\w\s]', ' ', texte)
        
        # Tokenization
        mots = texte.split()
        
        # Conservation des mots avec leur position pour l'analyse contextuelle
        mots_avec_position = []
        for i, mot in enumerate(mots):
            mots_avec_position.append({
                'mot': mot,
                'position': i,
                'negation': False,
                'intensificateur': False
            })
        
        return mots_avec_position

    def analyser_contexte(self, mots):
        """
        Analyse le contexte des mots (négations et intensificateurs)
        
        Args:
            mots (list): Liste des mots avec leurs métadonnées
        
        Returns:
            list: Liste des mots avec contexte analysé
        """
        for i, mot_data in enumerate(mots):
            mot = mot_data['mot']
            
            # Vérification des négations (regarde les 2 mots précédents)
            for j in range(max(0, i-2), i):
                if mots[j]['mot'] in self.negations:
                    mot_data['negation'] = True
                    break
            
            # Vérification des intensificateurs (regarde le mot précédent)
            if i > 0 and mots[i-1]['mot'] in self.intensificateurs:
                mot_data['intensificateur'] = True
                mot_data['facteur_intensite'] = self.intensificateurs[mots[i-1]['mot']]
        
        return mots

    def analyser_texte(self, texte):
        """
        Analyse le sentiment d'un texte
        
        Args:
            texte (str): Texte à analyser
        
        Returns:
            dict: Résultats de l'analyse avec scores détaillés
        """
        # Prétraitement du texte
        mots = self.preprocess_texte(texte)
        
        # Analyse du contexte
        mots = self.analyser_contexte(mots)
        
        # Calcul des scores
        score_positif = 0
        score_negatif = 0
        mots_positifs_trouves = []
        mots_negatifs_trouves = []
        
        for mot_data in mots:
            mot = mot_data['mot']
            poids = 1
            
            # Vérification des mots positifs
            if mot in self.mots_positifs:
                poids = self.mots_positifs[mot]
                if mot_data['intensificateur']:
                    poids *= mot_data['facteur_intensite']
                
                if mot_data['negation']:
                    score_negatif += poids
                    mots_negatifs_trouves.append({
                        'mot': mot,
                        'poids': poids,
                        'negation': True,
                        'intensificateur': mot_data['intensificateur']
                    })
                else:
                    score_positif += poids
                    mots_positifs_trouves.append({
                        'mot': mot,
                        'poids': poids,
                        'negation': False,
                        'intensificateur': mot_data['intensificateur']
                    })
            
            # Vérification des mots négatifs
            elif mot in self.mots_negatifs:
                poids = self.mots_negatifs[mot]
                if mot_data['intensificateur']:
                    poids *= mot_data['facteur_intensite']
                
                if mot_data['negation']:
                    score_positif += poids
                    mots_positifs_trouves.append({
                        'mot': mot,
                        'poids': poids,
                        'negation': True,
                        'intensificateur': mot_data['intensificateur']
                    })
                else:
                    score_negatif += poids
                    mots_negatifs_trouves.append({
                        'mot': mot,
                        'poids': poids,
                        'negation': False,
                        'intensificateur': mot_data['intensificateur']
                    })
        
        # Calcul du score total et détermination du sentiment
        score_total = score_positif + score_negatif
        
        if score_total == 0:
            sentiment = "neutre"
            confiance = 0
        else:
            ratio = score_positif / score_total
            
            if ratio > 0.7:
                sentiment = "positif"
            elif ratio < 0.3:
                sentiment = "négatif"
            else:
                sentiment = "neutre"
            
            # Calcul de la confiance basée sur l'écart des scores
            confiance = min(100, abs(score_positif - score_negatif) * 10)
        
        return {
            "sentiment": sentiment,
            "confiance": round(confiance, 1),
            "score_positif": round(score_positif, 2),
            "score_negatif": round(score_negatif, 2),
            "score_total": round(score_total, 2),
            "mots_positifs": mots_positifs_trouves,
            "mots_negatifs": mots_negatifs_trouves,
            "texte_original": texte
        }

    def analyser_fichier(self, chemin_fichier):
        """
        Analyse les sentiments d'un fichier texte
        
        Args:
            chemin_fichier (str): Chemin vers le fichier à analyser
        
        Returns:
            list: Liste des résultats d'analyse pour chaque ligne
        """
        resultats = []
        
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                for ligne in fichier:
                    ligne = ligne.strip()
                    if ligne:  # Ignorer les lignes vides
                        resultat = self.analyser_texte(ligne)
                        resultats.append(resultat)
        except FileNotFoundError:
            print(f"Erreur : Le fichier '{chein_fichier}' n'a pas été trouvé.")
            return []
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier : {e}")
            return []
        
        return resultats

def afficher_resultat(resultat, verbose=False):
    """
    Affiche les résultats de l'analyse de manière formatée
    
    Args:
        resultat (dict): Résultat de l'analyse
        verbose (bool): Mode détaillé
    """
    # Détermination de l'emoji en fonction du sentiment
    emojis = {
        "positif": "😊",
        "négatif": "😠",
        "neutre": "😐"
    }
    
    emoji = emojis.get(resultat["sentiment"], "❓")
    
    print("\n" + "="*60)
    print("ANALYSE DE SENTIMENT NOVATECH".center(60))
    print("="*60)
    print(f"Texte: \"{resultat['texte_original']}\"")
    print(f"Sentiment: {emoji} {resultat['sentiment'].upper()}")
    print(f"Confiance: {resultat['confiance']}%")
    print(f"Score positif: {resultat['score_positif']}")
    print(f"Score négatif: {resultat['score_negatif']}")
    print(f"Score total: {resultat['score_total']}")
    
    if verbose:
        # Afficher les mots détectés
        if resultat['mots_positifs']:
            print("\nMots positifs détectés:")
            for mot in resultat['mots_positifs']:
                negation = "(négation) " if mot['negation'] else ""
                intensificateur = f"(intensifié x{mot['intensificateur']}) " if mot['intensificateur'] else ""
                print(f"  - {negation}{intensificateur}{mot['mot']}: {mot['poids']}")
        
        if resultat['mots_negatifs']:
            print("\nMots négatifs détectés:")
            for mot in resultat['mots_negatifs']:
                negation = "(négation) " if mot['negation'] else ""
                intensificateur = f"(intensifié x{mot['intensificateur']}) " if mot['intensificateur'] else ""
                print(f"  - {negation}{intensificateur}{mot['mot']}: {mot['poids']}")
    
    print("="*60)

def afficher_statistiques(resultats):
    """
    Affiche des statistiques sur plusieurs analyses
    
    Args:
        resultats (list): Liste des résultats d'analyse
    """
    if not resultats:
        return
    
    # Calcul des statistiques
    total = len(resultats)
    sentiments = [r['sentiment'] for r in resultats]
    positifs = sentiments.count('positif')
    negatifs = sentiments.count('négatif')
    neutres = sentiments.count('neutre')
    
    confiance_moyenne = sum(r['confiance'] for r in resultats) / total
    
    print("\n" + "="*60)
    print("STATISTIQUES GLOBALES".center(60))
    print("="*60)
    print(f"Total d'analyses: {total}")
    print(f"Sentiments positifs: {positifs} ({positifs/total*100:.1f}%)")
    print(f"Sentiments négatifs: {negatifs} ({negatifs/total*100:.1f}%)")
    print(f"Sentiments neutres: {neutres} ({neutres/total*100:.1f}%)")
    print(f"Confiance moyenne: {confiance_moyenne:.1f}%")
    print("="*60)

def interface_utilisateur():
    """
    Interface utilisateur en ligne de commande
    """
    print("=== ANALYSEUR DE SENTIMENTS NOVATECH ===")
    print("Cet outil analyse le sentiment des textes (positif, négatif, neutre)\n")
    
    analyseur = AnalyseurSentiments()
    
    while True:
        print("\nOptions disponibles:")
        print("1. Analyser un texte")
        print("2. Analyser un fichier")
        print("3. Quitter")
        
        choix = input("\nChoisissez une option (1-3): ")
        
        if choix == '1':
            texte = input("Entrez le texte à analyser: ")
            if texte.strip():
                resultat = analyseur.analyser_texte(texte)
                afficher_resultat(resultat, verbose=True)
            else:
                print("Le texte ne peut pas être vide.")
        
        elif choix == '2':
            chemin = input("Entrez le chemin du fichier à analyser: ")
            if chemin.strip():
                resultats = analyseur.analyser_fichier(chemin)
                if resultats:
                    for i, resultat in enumerate(resultats, 1):
                        print(f"\n--- Analyse {i} ---")
                        afficher_resultat(resultat)
                    afficher_statistiques(resultats)
                else:
                    print("Aucun résultat à afficher.")
            else:
                print("Le chemin du fichier ne peut pas être vide.")
        
        elif choix == '3':
            print("Au revoir!")
            break
        
        else:
            print("Option non valide. Veuillez choisir 1, 2 ou 3.")

def interface_arguments():
    """
    Interface en ligne de commande avec arguments
    """
    parser = argparse.ArgumentParser(description="Analyseur de sentiments NovaTech")
    parser.add_argument("texte", nargs="?", help="Texte à analyser")
    parser.add_argument("-f", "--fichier", help="Chemin vers un fichier à analyser")
    parser.add_argument("-v", "--verbose", action="store_true", help="Mode verbeux")
    parser.add_argument("-s", "--stats", action="store_true", help="Afficher les statistiques")
    
    args = parser.parse_args()
    
    analyseur = AnalyseurSentiments()
    
    if args.fichier:
        # Analyser un fichier
        resultats = analyseur.analyser_fichier(args.fichier)
        if resultats:
            for i, resultat in enumerate(resultats, 1):
                print(f"\n--- Analyse {i} ---")
                afficher_resultat(resultat, args.verbose)
            
            if args.stats:
                afficher_statistiques(resultats)
        else:
            print("Aucun résultat à afficher.")
    
    elif args.texte:
        # Analyser un texte
        resultat = analyseur.analyser_texte(args.texte)
        afficher_resultat(resultat, args.verbose)
    
    else:
        # Mode interactif
        interface_utilisateur()

if __name__ == '__main__':
    # Vérifier si des arguments ont été passés
    if len(sys.argv) > 1:
        interface_arguments()
    else:
        interface_utilisateur()