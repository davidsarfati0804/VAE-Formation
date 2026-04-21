# Guide Google SEO / SEA — VAE Formation
## Fascicule pratique étape par étape

---

# PARTIE 1 — GOOGLE SEARCH CONSOLE
### Ce que c'est
Google Search Console (GSC) est l'outil gratuit de Google qui vous dit :
- Si Google a bien trouvé et indexé votre site
- Sur quels mots-clés vous apparaissez dans les résultats
- S'il y a des erreurs techniques sur votre site
- Combien de clics vous recevez chaque jour

**C'est obligatoire. C'est gratuit. C'est la base de tout.**

---

## Étape 1 — Créer un compte Google dédié au site

1. Allez sur **gmail.com**
2. Créez un compte Google avec l'adresse : `contact@vae-formation.com`
   (ou utilisez un compte Google existant professionnel)
3. Gardez l'adresse et le mot de passe dans un endroit sûr

---

## Étape 2 — Accéder à Google Search Console

1. Allez sur : **search.google.com/search-console**
2. Connectez-vous avec votre compte Google
3. Cliquez sur **"Commencer"**

---

## Étape 3 — Ajouter votre site

1. Cliquez sur **"Ajouter une propriété"** (en haut à gauche)
2. Choisissez **"Préfixe d'URL"** (le panneau de droite)
3. Entrez : `https://vae-formation.com/`
4. Cliquez sur **"Continuer"**

---

## Étape 4 — Vérifier que vous êtes bien le propriétaire du site

Google doit s'assurer que c'est bien vous. Plusieurs méthodes sont proposées :

### Méthode recommandée : Balise HTML
1. Google vous donne un code qui ressemble à :
   `<meta name="google-site-verification" content="XXXXXXXXXXXXXXXX">`
2. Copiez ce code
3. Ouvrez le fichier `index.html` de votre site
4. Collez-le juste après la ligne `<meta name="robots" content="index, follow">`
5. Sauvegardez et déployez le site sur Netlify
6. Revenez sur Search Console et cliquez **"Vérifier"**

---

## Étape 5 — Soumettre votre sitemap

Le sitemap dit à Google quelles pages existent sur votre site.

1. Dans le menu gauche de Search Console, cliquez **"Sitemaps"**
2. Dans le champ, entrez : `sitemap.xml`
3. Cliquez **"Envoyer"**
4. Google devrait afficher **"Succès"** sous 24h

---

## Étape 6 — Ce que vous allez surveiller chaque semaine

Dans le menu gauche, regardez :
- **"Résultats de recherche"** → vos clics, impressions, position moyenne
- **"Couverture"** → pages indexées / erreurs
- **"Core Web Vitals"** → vitesse de votre site

> Comptez 2 à 4 semaines avant que les premières données apparaissent.

---
---

# PARTIE 2 — GOOGLE ANALYTICS 4
### Ce que c'est
Google Analytics (GA4) vous dit ce que font les visiteurs sur votre site :
- Combien de personnes visitent le site chaque jour
- D'où viennent-ils (Google, réseaux sociaux, email…)
- Quelles pages ils regardent, combien de temps
- Combien remplissent le formulaire de contact

**C'est gratuit. Indispensable pour mesurer vos campagnes Google Ads.**

---

## Étape 1 — Créer votre propriété GA4

1. Allez sur : **analytics.google.com**
2. Connectez-vous avec le même compte Google que Search Console
3. Cliquez **"Commencer la mesure"**
4. **Nom du compte** : `VAE Formation`
5. Cliquez **"Suivant"**
6. **Nom de la propriété** : `vae-formation.com`
7. **Fuseau horaire** : France
8. **Devise** : Euro (€)
9. Cliquez **"Suivant"** puis **"Créer"**

---

## Étape 2 — Configurer le flux de données

1. Choisissez **"Web"**
2. **URL** : `https://vae-formation.com`
3. **Nom du flux** : `Site VAE Formation`
4. Cliquez **"Créer un flux"**
5. Google vous donne un **ID de mesure** qui ressemble à : `G-XXXXXXXXXX`
   → **Copiez-le, vous en aurez besoin**

---

## Étape 3 — Installer le code sur votre site

1. Google vous propose un bloc de code JavaScript
2. Copiez tout le bloc (commence par `<!-- Google tag (gtag.js) -->`)
3. Ouvrez `index.html`
4. Collez-le juste avant la balise `</head>`
5. Sauvegardez et déployez
6. Pour vérifier : dans GA4, allez dans **"Temps réel"** et visitez votre site
   → Vous devriez vous voir apparaître en "utilisateur actif"

---
---

# PARTIE 3 — GOOGLE BUSINESS PROFILE
### Ce que c'est
La fiche Google Business est la fiche qui apparaît à droite des résultats Google quand quelqu'un cherche "VAE Formation" ou votre entreprise.
Elle affiche : votre nom, téléphone, site, horaires, avis clients.

**C'est gratuit. Ça booste massivement la visibilité locale.**

---

## Étape 1 — Créer votre fiche

1. Allez sur : **business.google.com**
2. Connectez-vous avec votre compte Google
3. Cliquez **"Gérer maintenant"**
4. Entrez : `VAE Formation`
5. **Catégorie** : `École de formation professionnelle`
6. Choisissez **"Je propose des services dans ma zone"**
   (car vous êtes 100% distanciel — pas besoin d'adresse physique publique)
7. **Zone de service** : France entière (ou sélectionnez les régions cibles)

---

## Étape 2 — Remplir la fiche complètement

Complétez absolument tous les champs :

| Champ | Valeur |
|---|---|
| Nom | VAE Formation |
| Téléphone | 06 68 26 62 26 |
| Site web | https://vae-formation.com |
| Catégorie principale | École de formation professionnelle |
| Description | Centre spécialisé VAE CQP Assistant Médical (RNCP 40913). Accompagnement 100% distanciel, toute la France. Financement CPF & OPCO EP à 100%. 95% de réussite au jury. |
| Horaires | Lundi–Vendredi 9h–18h (ou vos horaires réels) |

---

## Étape 3 — Vérifier votre fiche

Google doit vérifier que l'entreprise existe.
- **Par appel téléphonique** : Google appelle le 06 68 26 62 26, vous donnez le code
- **Par e-mail** : Google envoie un code à votre adresse
- **Par vidéo** : Vous filmez une courte vidéo de votre activité

---

## Étape 4 — Collecter des avis clients

Les avis Google sont un facteur de référencement majeur.
- Dès que vous avez vos premiers candidats diplômés → demandez-leur un avis Google
- Google vous fournit un lien direct à envoyer par SMS ou email
- Objectif : **10 avis minimum à 4-5 étoiles** dans les 3 premiers mois

---
---

# PARTIE 4 — GOOGLE ADS (SEA)
### Ce que c'est
Google Ads vous permet d'apparaître **en premier** dans Google, au-dessus des résultats naturels, sur les mots-clés que vous choisissez. Vous payez uniquement quand quelqu'un clique (CPC — Coût Par Clic).

**Pour VAE Formation : budget recommandé = 300 à 600 €/mois pour commencer.**

---

## Étape 1 — Créer votre compte Google Ads

1. Allez sur : **ads.google.com**
2. Connectez-vous avec le même compte Google
3. Cliquez **"Commencer"**
4. **Sélectionnez votre objectif** : "Obtenir plus d'appels téléphoniques ou visites sur le site"
5. Entrez `https://vae-formation.com`

---

## Étape 2 — Créer votre première campagne

### Paramètres de campagne

| Paramètre | Valeur recommandée |
|---|---|
| Type | Réseau de Recherche (Search) |
| Objectif | Prospects / Formulaires |
| Zone géographique | France entière |
| Langue | Français |
| Budget journalier | 10 à 20 €/jour pour commencer |
| Stratégie d'enchères | Maximiser les conversions |

---

## Étape 3 — Mots-clés à cibler (liste prête à l'emploi)

### Groupe 1 — Intention forte (conversion directe)
```
"VAE assistant médical"
"CQP assistant médical VAE"
"obtenir CQP assistant médical"
"VAE secrétaire médicale diplôme"
"accompagnement VAE assistant médical"
```

### Groupe 2 — Financement (forte intention)
```
"financement VAE CPF assistant médical"
"OPCO EP VAE assistant médical"
"VAE gratuite assistant médical"
"financer VAE secrétaire médicale"
```

### Groupe 3 — Informationnels (sensibilisation)
```
"comment devenir assistant médical sans diplôme"
"RNCP 40913 assistant médical"
"éligibilité VAE 1 an expérience"
"délai VAE assistant médical"
```

### Mots-clés à exclure (négatifs — pour ne pas gaspiller le budget)
```
-formation initiale
-emploi assistant médical
-offre emploi
-recrutement
-salaire
-poste
```

---

## Étape 4 — Rédiger vos annonces

Chaque annonce comporte 3 titres (30 caractères max) + 2 descriptions (90 caractères max).

### Annonce 1 — Conversion directe
- **Titre 1** : VAE Assistant Médical
- **Titre 2** : CQP RNCP 40913 en 9 Mois
- **Titre 3** : Financement CPF à 100%
- **Description 1** : Obtenez le CQP Assistant Médical par la VAE. 95% de réussite. 100% distanciel France entière.
- **Description 2** : Financement via CPF, OPCO EP ou employeur. Diagnostic gratuit. Répondez en 48h.

### Annonce 2 — Financement mis en avant
- **Titre 1** : VAE Assistante Médicale
- **Titre 2** : 0€ Avancé — OPCO EP 100%
- **Titre 3** : Diagnostic Gratuit Sans Engagement
- **Description 1** : Salariée en cabinet médical ? L'OPCO EP finance votre VAE à 100%. Aucune avance.
- **Description 2** : Accompagnement individuel par un expert CQP. Résultat en 9 à 12 mois.

---

## Étape 5 — Configurer le suivi des conversions

Sans suivi des conversions, vous ne savez pas quelles annonces fonctionnent.

1. Dans Google Ads → **Outils → Mesure → Conversions**
2. Cliquez **"Nouvelle action de conversion"**
3. Choisissez **"Site web"**
4. **Nom** : `Formulaire contact envoyé`
5. **Catégorie** : Prospect
6. **Valeur** : 50 € (valeur estimée d'un lead)
7. Google vous génère un code → à installer sur la page de confirmation après soumission du formulaire

---
---

# RÉCAPITULATIF — Ordre de mise en place recommandé

| Priorité | Action | Durée estimée | Coût |
|---|---|---|---|
| 1 | Google Search Console + sitemap | 30 min | Gratuit |
| 2 | Google Analytics 4 | 30 min | Gratuit |
| 3 | Google Business Profile | 1h + vérification (1-3 jours) | Gratuit |
| 4 | Créer l'image OG (1200×630px) | 20 min (Canva) | Gratuit |
| 5 | Google Ads — première campagne | 2h | 300-600 €/mois |
| 6 | Collecter 10 avis Google clients | 1 mois | Gratuit |

---

# OUTILS COMPLÉMENTAIRES GRATUITS

| Outil | Utilité | Lien |
|---|---|---|
| **PageSpeed Insights** | Tester la vitesse du site | pagespeed.web.dev |
| **Rich Results Test** | Vérifier les rich snippets JSON-LD | search.google.com/test/rich-results |
| **Schema Markup Validator** | Valider le JSON-LD | validator.schema.org |
| **Canva** | Créer l'image OG 1200×630 | canva.com |
| **Ubersuggest** | Idées de mots-clés gratuits | neilpatel.com/ubersuggest |

---

*Document créé le 20/04/2026 — VAE Formation*
