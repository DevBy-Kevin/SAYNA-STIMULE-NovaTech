#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Générateur de mots de passe sécurisés pour NovaTech
Ce script génère des mots de passe forts avec différents niveaux de complexité
Dernière mise à jour : 15/06/2023
"""

import random
import string
import secrets
import argparse
import sys

def generer_mot_de_passe(longueur=12, majuscules=True, chiffres=True, symboles=True):
    """
    Génère un mot de passe sécurisé avec les critères spécifiés
    
    Args:
        longueur (int): Longueur du mot de passe (8-64)
        majuscules (bool): Inclure des lettres majuscules
        chiffres (bool): Inclure des chiffres
        symboles (bool): Inclure des symboles
    
    Returns:
        str: Mot de passe généré
    """
    # Caractères de base (minuscules)
    caracteres = string.ascii_lowercase
    
    # Ajout des majuscules si demandé
    if majuscules:
        caracteres += string.ascii_uppercase
    
    # Ajout des chiffres si demandé
    if chiffres:
        caracteres += string.digits
    
    # Ajout des symboles si demandé
    if symboles:
        caracteres += string.punctuation
    
    # Vérification de la longueur minimale
    if longueur < 8:
        print("⚠️  Attention : Un mot de passe de moins de 8 caractères n'est pas sécurisé !")
        print("   La longueur a été automatiquement ajustée à 8 caractères.")
        longueur = 8
    
    # Vérification de la longueur maximale
    if longueur > 64:
        print("⚠️  Attention : La longueur maximale recommandée est de 64 caractères.")
        print("   La longueur a été automatiquement ajustée à 64 caractères.")
        longueur = 64
    
    # Génération du mot de passe avec le module secrets (plus sécurisé que random)
    mot_de_passe = ''.join(secrets.choice(caracteres) for _ in range(longueur))
    
    return mot_de_passe

def evaluer_force(mot_de_passe):
    """
    Évalue la force d'un mot de passe selon plusieurs critères
    
    Args:
        mot_de_passe (str): Mot de passe à évaluer
    
    Returns:
        dict: Résultats de l'évaluation avec score et recommandations
    """
    score = 0
    recommendations = []
    
    # Longueur
    if len(mot_de_passe) >= 16:
        score += 3
    elif len(mot_de_passe) >= 12:
        score += 2
    elif len(mot_de_passe) >= 8:
        score += 1
    else:
        recommendations.append("Le mot de passe est trop court (minimum 8 caractères recommandés)")
    
    # Diversité des caractères
    has_upper = any(c in string.ascii_uppercase for c in mot_de_passe)
    has_lower = any(c in string.ascii_lowercase for c in mot_de_passe)
    has_digit = any(c in string.digits for c in mot_de_passe)
    has_symbol = any(c in string.punctuation for c in mot_de_passe)
    
    if has_upper:
        score += 1
    else:
        recommendations.append("Ajoutez des lettres majuscules")
    
    if has_lower:
        score += 1
    else:
        recommendations.append("Ajoutez des lettres minuscules")
    
    if has_digit:
        score += 1
    else:
        recommendations.append("Ajoutez des chiffres")
    
    if has_symbol:
        score += 1
    else:
        recommendations.append("Ajoutez des symboles")
    
    # Détermination du niveau de force
    if score >= 7:
        force = "Très fort"
        couleur = "🟢"
    elif score >= 5:
        force = "Fort"
        couleur = "🟡"
    elif score >= 3:
        force = "Moyen"
        couleur = "🟠"
    else:
        force = "Faible"
        couleur = "🔴"
    
    return {
        "score": score,
        "force": force,
        "couleur": couleur,
        "recommendations": recommendations,
        "longueur": len(mot_de_passe),
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_symbol": has_symbol
    }

def afficher_resultat(mot_de_passe, evaluation):
    """
    Affiche le mot de passe et son évaluation de manière formatée
    
    Args:
        mot_de_passe (str): Mot de passe généré
        evaluation (dict): Résultats de l'évaluation
    """
    print("\n" + "="*50)
    print("GÉNÉRATEUR DE MOTS DE PASSE NOVATECH".center(50))
    print("="*50)
    print(f"Mot de passe généré: {mot_de_passe}")
    print(f"Longueur: {evaluation['longueur']} caractères")
    print(f"Force: {evaluation['couleur']} {evaluation['force']} (Score: {evaluation['score']}/7)")
    print("-"*50)
    
    # Détails de composition
    print("Composition:")
    print(f"  - Lettres majuscules: {'✅' if evaluation['has_upper'] else '❌'}")
    print(f"  - Lettres minuscules: {'✅' if evaluation['has_lower'] else '❌'}")
    print(f"  - Chiffres: {'✅' if evaluation['has_digit'] else '❌'}")
    print(f"  - Symboles: {'✅' if evaluation['has_symbol'] else '❌'}")
    
    # Recommandations
    if evaluation['recommendations']:
        print("\nRecommandations:")
        for rec in evaluation['recommendations']:
            print(f"  - {rec}")
    
    print("="*50)

def generer_plusieurs_mots_de_passe(nombre, longueur=12, majuscules=True, chiffres=True, symboles=True):
    """
    Génère plusieurs mots de passe avec les mêmes critères
    
    Args:
        nombre (int): Nombre de mots de passe à générer
        longueur (int): Longueur de chaque mot de passe
        majuscules (bool): Inclure des majuscules
        chiffres (bool): Inclure des chiffres
        symboles (bool): Inclure des symboles
    
    Returns:
        list: Liste des mots de passe générés
    """
    mots_de_passe = []
    for _ in range(nombre):
        mot_de_passe = generer_mot_de_passe(longueur, majuscules, chiffres, symboles)
        mots_de_passe.append(mot_de_passe)
    
    return mots_de_passe

def interface_utilisateur():
    """
    Interface utilisateur en ligne de commande
    """
    print("=== GÉNÉRATEUR DE MOTS DE PASSE SÉCURISÉS NOVATECH ===")
    print("Ce générateur crée des mots de passe forts pour sécuriser vos comptes\n")
    
    # Saisie des paramètres
    try:
        longueur = int(input("Longueur du mot de passe (8-64, défaut: 12): ") or "12")
        if longueur < 8 or longueur > 64:
            print("Longueur invalide, utilisation de la valeur par défaut (12)")
            longueur = 12
    except ValueError:
        print("Valeur incorrecte, utilisation de la valeur par défaut (12)")
        longueur = 12
    
    majuscules = input("Inclure des majuscules (O/n): ").lower() != 'n'
    chiffres = input("Inclure des chiffres (O/n): ").lower() != 'n'
    symboles = input("Inclure des symboles (O/n): ").lower() != 'n'
    
    try:
        nombre = int(input("Nombre de mots de passe à générer (défaut: 1): ") or "1")
        if nombre < 1:
            nombre = 1
    except ValueError:
        nombre = 1
    
    # Génération des mots de passe
    mots_de_passe = generer_plusieurs_mots_de_passe(nombre, longueur, majuscules, chiffres, symboles)
    
    # Affichage des résultats
    if nombre == 1:
        evaluation = evaluer_force(mots_de_passe[0])
        afficher_resultat(mots_de_passe[0], evaluation)
    else:
        print(f"\nGénération de {nombre} mots de passe:")
        print("-" * 50)
        for i, mdp in enumerate(mots_de_passe, 1):
            evaluation = evaluer_force(mdp)
            print(f"{i:2d}. {mdp} ({evaluation['couleur']} {evaluation['force']})")
        
        # Afficher une évaluation détaillée pour le premier mot de passe
        print("\n" + "="*50)
        print("ÉVALUATION DÉTAILLÉE DU PREMIER MOT DE PASSE".center(50))
        print("="*50)
        evaluation = evaluer_force(mots_de_passe[0])
        afficher_resultat(mots_de_passe[0], evaluation)

def interface_arguments():
    """
    Interface en ligne de commande avec arguments
    """
    parser = argparse.ArgumentParser(description="Générateur de mots de passe sécurisés NovaTech")
    parser.add_argument("-l", "--longueur", type=int, default=12, help="Longueur du mot de passe (8-64)")
    parser.add_argument("-n", "--nombre", type=int, default=1, help="Nombre de mots de passe à générer")
    parser.add_argument("-u", "--majuscules", action="store_false", help="Exclure les majuscules")
    parser.add_argument("-c", "--chiffres", action="store_false", help="Exclure les chiffres")
    parser.add_argument("-s", "--symboles", action="store_false", help="Exclure les symboles")
    parser.add_argument("-q", "--quiet", action="store_true", help="Mode silencieux (affiche seulement les mots de passe)")
    
    args = parser.parse_args()
    
    # Validation des arguments
    if args.longueur < 8 or args.longueur > 64:
        print("Erreur : La longueur doit être entre 8 et 64 caractères")
        sys.exit(1)
    
    if args.nombre < 1:
        print("Erreur : Le nombre doit être au moins 1")
        sys.exit(1)
    
    # Génération des mots de passe
    mots_de_passe = generer_plusieurs_mots_de_passe(
        args.nombre, 
        args.longueur, 
        args.majuscules, 
        args.chiffres, 
        args.symboles
    )
    
    # Affichage des résultats
    if args.quiet:
        for mdp in mots_de_passe:
            print(mdp)
    else:
        if args.nombre == 1:
            evaluation = evaluer_force(mots_de_passe[0])
            afficher_resultat(mots_de_passe[0], evaluation)
        else:
            print(f"Génération de {args.nombre} mots de passe:")
            for i, mdp in enumerate(mots_de_passe, 1):
                evaluation = evaluer_force(mdp)
                print(f"{i:2d}. {mdp} ({evaluation['couleur']} {evaluation['force']})")

if __name__ == '__main__':
    # Vérifier si des arguments ont été passés
    if len(sys.argv) > 1:
        interface_arguments()
    else:
        interface_utilisateur()