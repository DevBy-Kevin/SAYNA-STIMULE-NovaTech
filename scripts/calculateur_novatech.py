#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Calculateur de devis pour NovaTech
Ce script calcule le prix d'un projet digital en fonction de ses caractéristiques
Dernière mise à jour : 15/06/2023
"""

def calculer_prix_projet(type_projet, nb_pages, design, fonctionnalites, seo):
    """
    Calcule le prix total d'un projet digital
    
    Args:
        type_projet (str): Type de projet (website, ecommerce, webapp, mobile, desktop)
        nb_pages (int): Nombre de pages du site/application
        design (float): Niveau de design (1.0 = basique, 1.5 = personnalisé, 2.0 = premium)
        fonctionnalites (list): Liste des fonctionnalités supplémentaires
        seo (int): Option SEO choisie (0, 300, 800, 1500)
    
    Returns:
        float: Prix total du projet
    """
    # Prix de base selon le type de projet
    prix_base = {
        'website': 1500,
        'ecommerce': 3500,
        'webapp': 5000,
        'mobile': 8500,
        'desktop': 7000
    }
    
    # Vérification du type de projet
    if type_projet not in prix_base:
        raise ValueError("Type de projet non reconnu. Choisissez parmi: website, ecommerce, webapp, mobile, desktop")
    
    # Calcul du prix total
    total = prix_base.get(type_projet, 0)
    total += nb_pages * 100  # 100€ par page
    total += (design - 1) * 500  # Supplément design
    total += sum(fonctionnalites)  # Fonctionnalités supplémentaires
    total += seo  # Option SEO
    
    # Application des remises pour les gros projets
    if total > 10000:
        total *= 0.9  # 10% de remise
    elif total > 5000:
        total *= 0.95  # 5% de remise
    
    return round(total, 2)

def afficher_devis(type_projet, nb_pages, design, fonctionnalites, seo, total):
    """
    Affiche un devis formaté
    
    Args:
        type_projet (str): Type de projet
        nb_pages (int): Nombre de pages
        design (float): Niveau de design
        fonctionnalites (list): Liste des fonctionnalités
        seo (int): Option SEO
        total (float): Prix total
    """
    # Traduction des types de projet
    types_traduits = {
        'website': 'Site Web Vitrine',
        'ecommerce': 'Site E-commerce',
        'webapp': 'Application Web',
        'mobile': 'Application Mobile',
        'desktop': 'Application Desktop'
    }
    
    # Traduction des niveaux de design
    design_traduit = {
        1.0: 'Basique',
        1.5: 'Personnalisé',
        2.0: 'Premium'
    }
    
    print("\n" + "="*50)
    print("DEVIS NOVATECH".center(50))
    print("="*50)
    print(f"{'Type de projet:':<20} {types_traduits.get(type_projet, type_projet)}")
    print(f"{'Nombre de pages:':<20} {nb_pages}")
    print(f"{'Niveau de design:':<20} {design_traduit.get(design, design)}")
    print(f"{'Fonctionnalités:':<20} {len(fonctionnalites)} option(s)")
    print(f"{'Option SEO:':<20} {seo}€")
    print("-"*50)
    print(f"{'TOTAL:':<20} {total}€")
    print("="*50)
    print("\n")

def obtenir_choix_utilisateur():
    """
    Demande à l'utilisateur de saisir les paramètres du projet
    
    Returns:
        tuple: (type_projet, nb_pages, design, fonctionnalites, seo)
    """
    print("=== CALCULATEUR DE DEVIS NOVATECH ===")
    print("Ce calculateur vous permet d'estimer le coût de votre projet digital\n")
    
    # Choix du type de projet
    print("Types de projet disponibles:")
    print("1. Site Web Vitrine (1500€)")
    print("2. Site E-commerce (3500€)")
    print("3. Application Web (5000€)")
    print("4. Application Mobile (8500€)")
    print("5. Application Desktop (7000€)")
    
    choix_type = input("\nChoisissez le type de projet (1-5): ")
    types_map = {
        '1': 'website',
        '2': 'ecommerce',
        '3': 'webapp',
        '4': 'mobile',
        '5': 'desktop'
    }
    
    type_projet = types_map.get(choix_type, 'website')
    
    # Nombre de pages
    try:
        nb_pages = int(input("Nombre de pages: "))
        if nb_pages < 1:
            print("Nombre de pages incorrect, valeur par défaut (5) utilisée")
            nb_pages = 5
    except ValueError:
        print("Valeur incorrecte, nombre de pages par défaut (5) utilisé")
        nb_pages = 5
    
    # Niveau de design
    print("\nNiveaux de design disponibles:")
    print("1. Design Basique (+0€)")
    print("2. Design Personnalisé (+500€)")
    print("3. Design Premium (+1000€)")
    
    choix_design = input("Choisissez le niveau de design (1-3): ")
    design_map = {
        '1': 1.0,
        '2': 1.5,
        '3': 2.0
    }
    
    design = design_map.get(choix_design, 1.0)
    
    # Fonctionnalités supplémentaires
    print("\nFonctionnalités supplémentaires disponibles:")
    print("1. Formulaire de contact (+500€)")
    print("2. Espace membre (+800€)")
    print("3. Paiement en ligne (+1200€)")
    print("4. Blog/Actualités (+700€)")
    print("5. Multilingue (+1000€)")
    print("6. Réseaux sociaux (+600€)")
    print("7. Aucune fonctionnalité supplémentaire")
    
    fonctionnalites_choisies = input("Choisissez les fonctionnalités (séparées par des virgules, ex: 1,3,5): ")
    fonctionnalites_map = {
        '1': 500,
        '2': 800,
        '3': 1200,
        '4': 700,
        '5': 1000,
        '6': 600
    }
    
    fonctionnalites = []
    if fonctionnalites_choisies != '7':
        for choix in fonctionnalites_choisies.split(','):
            choix = choix.strip()
            if choix in fonctionnalites_map:
                fonctionnalites.append(fonctionnalites_map[choix])
    
    # Option SEO
    print("\nOptions SEO disponibles:")
    print("1. Aucun SEO (+0€)")
    print("2. SEO Basique (+300€)")
    print("3. SEO Avancé (+800€)")
    print("4. SEO Premium (+1500€)")
    
    choix_seo = input("Choisissez l'option SEO (1-4): ")
    seo_map = {
        '1': 0,
        '2': 300,
        '3': 800,
        '4': 1500
    }
    
    seo = seo_map.get(choix_seo, 0)
    
    return type_projet, nb_pages, design, fonctionnalites, seo

def exemple_utilisation():
    """
    Exemple d'utilisation du calculateur
    """
    print("Exemple d'utilisation du calculateur:\n")
    
    # Configuration d'un projet exemple
    type_projet = 'website'
    nb_pages = 5
    design = 1.5  # Design personnalisé
    fonctionnalites = [500, 800]  # Formulaire + Espace membre
    seo = 300  # SEO Basique
    
    total = calculer_prix_projet(type_projet, nb_pages, design, fonctionnalites, seo)
    afficher_devis(type_projet, nb_pages, design, fonctionnalites, seo, total)

if __name__ == '__main__':
    # Exemple d'utilisation
    exemple_utilisation()
    
    # Demander à l'utilisateur s'il veut faire son propre calcul
    reponse = input("\nVoulez-vous créer votre propre devis? (o/n): ")
    
    if reponse.lower() in ['o', 'oui', 'y', 'yes']:
        try:
            type_projet, nb_pages, design, fonctionnalites, seo = obtenir_choix_utilisateur()
            total = calculer_prix_projet(type_projet, nb_pages, design, fonctionnalites, seo)
            afficher_devis(type_projet, nb_pages, design, fonctionnalites, seo, total)
        except Exception as e:
            print(f"Une erreur s'est produite: {e}")
    else:
        print("Au revoir! N'hésitez pas à revenir pour estimer votre projet.")