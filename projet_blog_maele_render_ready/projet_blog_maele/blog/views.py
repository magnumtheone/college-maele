from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import register
from .models import Article

@register.filter
def split(value, arg=","):
    """
    Divise une chaîne en liste selon le séparateur donné
    Usage: {{ value|split:"," }}
    """
    return [x.strip() for x in value.split(arg) if x.strip()]

def professeurs(request):
    """
    Page listant les professeurs avec photo, matière principale et courte description.
    La liste est construite ici comme exemple. Idéalement ces données viendraient d'un modèle Professeur.
    """
    profs = []
    # Liste fournie par l'utilisateur (42 professeurs)
    noms_matieres = [
        ("Trésor KISONDOKOLO", "Technologie de science physique"),
        ("Germaine HAWA SUNGA", "Éducation à la vie"),
        ("Sœur YUMA SAFINIA", "Catéchèse"),
        ("Hubert KATAPULU", "Chimie"),
        ("Jean de la Croix KATSUVA", "Anglais"),
        ("Diaz MATIKALI", "Français"),
        ("Cédric KAHEMBE", "Mathématique et sciences physique et technologie"),
        ("Yvon TSHITENDA", "Dessin scientifique, physique et mathématiques"),
        ("Scolastique AMISI", "TIC"),
        ("Jephté MUMBERE", "Latin et français"),
        ("Luc BOBANGA", "Éducation à la vie"),
        ("Alain OTEPA", "Français"),
        ("Grâce AMBWA", "Anglais"),
        ("Peter KAKEYI", "SVT"),
        ("Faustin LINGOMBO MONDENGA", "Français"),
        ("Michel KILYOBO KIMWANGA", "SVT et Chimie"),
        ("Floribert ILONGA BIKI", "Mathématiques"),
        ("Paulin KASONGO NSENGA", "Anglais"),
        ("John KAMANGO", "SVT"),
        ("Edo KAPITA", "Mathématiques"),
        ("Justin NGONGO KIBONDO", "Mathématiques"),
        ("Alfonse IGWANGOZI BUMBA", "Français"),
        ("Gérard BASILA LABAMA", "Éducation Physique"),
        ("Joseph LITETE BOBINA", "SVT"),
        ("Lucien RAMAZANI MUNGANGA", "Géographie"),
        ("Donat MWAMBA WETU TSHIALU", "Français"),
        ("Édouard LOBOLO AMURI", "Anglais"),
        ("Alain AMSINI", "Français"),
        ("Georges LIKENGE LOTIKA", "Mathématiques"),
        ("Marie BOYOMA MATOLO", "Dessin"),
        ("Martin MUHINDO BUSANGI", "Mathématiques"),
        ("José MAKANGA", "Bibliothécaire"),
        ("Jean Floribert Mondondo Mongita", "Histoire"),
        ("Evariste LITHO LOULA", "Français"),
        ("Père Joseph-Prince EKAGNY", "Religion"),
        ("Rachel SOMANA", "Dessin"),
        ("François KOSHI KILOLO", "Géographie"),
        ("Franck YANYONGO MAINGOLO", "TIC"),
        ("Franck MUMBERE", "Latin"),
        ("Albert BUKASA", "Histoire"),
        ("Dieu-Merci BOLONGE", "Physique"),
        ("Emmanuel AMURI", "Professeur et Surveillant")
    ]

    # Map explicite (nom -> fichier) pour tous les professeurs.
    # Utilise '5png.png' pour l'entrée 5 et applique les overrides demandés.
    explicit_photos = {
        'Trésor KISONDOKOLO': '1.png',
        'Germaine HAWA SUNGA': '2.png',
        'Sœur YUMA SAFINIA': '3.png',
        'Hubert KATAPULU': '4.png',
        'Jean de la Croix KATSUVA': '5png.png',
        'Diaz MATIKALI': '6.png',
        'Cédric KAHEMBE': '7.png',
        'Yvon TSHITENDA': '8.png',
        'Scolastique AMISI': '9.png',
        'Jephté MUMBERE': '12.png',
        'Luc BOBANGA': '10.png',
        'Alain OTEPA': '11.png',
        'Grâce AMBWA': '13.png',
        'Peter KAKEYI': '14.png',
        'Faustin LINGOMBO MONDENGA': '15.png',
        'Michel KILYOBO KIMWANGA': '16.png',
        'Floribert ILONGA BIKI': '17.png',
        'Paulin KASONGO NSENGA': '18.png',
        'John KAMANGO': '19.png',
        'Edo KAPITA': '20.png',
        'Justin NGONGO KIBONDO': '21.png',
        'Alfonse IGWANGOZI BUMBA': '22.png',
        'Gérard BASILA LABAMA': '23.png',
        'Joseph LITETE BOBINA': '24.png',
        'Lucien RAMAZANI MUNGANGA': '25.png',
        'Donat MWAMBA WETU TSHIALU': '26.png',
        'Édouard LOBOLO AMURI': '27.png',
        'Alain AMSINI': '28.png',
        'Georges LIKENGE LOTIKA': '29.png',
        'Marie BOYOMA MATOLO': '30.png',
        'Martin MUHINDO BUSANGI': '31.png',
        'José MAKANGA': '32.png',
        'Jean Floribert Mondondo Mongita': '33.png',
        'Evariste LITHO LOULA': '34.png',
        'Père Joseph-Prince EKAGNY': '35.png',
        'Rachel SOMANA': '36.png',
        'François KOSHI KILOLO': '37.png',
        'Franck YANYONGO MAINGOLO': '38.png',
        'Franck MUMBERE': '39.png',
        'Albert BUKASA': '40.png',
        'Dieu-Merci BOLONGE': '41.png',
        'Emmanuel AMURI': '42.png',
    }
    for i, (name, subject) in enumerate(noms_matieres, start=1):
        bio = f"{name} enseigne {subject} au Collège Maele."
        if name in explicit_photos:
            filename = explicit_photos[name]
        else:
            # Hypothèse : les photos sont nommées 1.png, 2.png, ... ; garder la prise en charge spéciale existante pour le fichier '5png.png' si nécessaire
            filename = '5png.png' if i == 5 else f'{i}.png'
        photo = f"blog/images/Professeurs/{filename}"
        profs.append({'name': name, 'subject': subject, 'bio': bio, 'photo': photo})

    return render(request, 'blog/professeurs.html', {'professeurs': profs})

def galerie(request):
    """
    Page galerie : fournit la liste d'images pour la galerie.
    Les images sont référencées via le dossier static `blog/Images/`.
    """
    images = [
        {'file': 'blog/Images/campus.jpg', 'caption': 'Cour principale'},
        {'file': 'blog/Images/point.jpg', 'caption': "Point d'honneur"},
        {'file': 'blog/Images/grotte.jpg', 'caption': 'Activité de découverte'},
        {'file': 'blog/Images/facade.jpg', 'caption': 'Façade historique'},
        {'file': 'blog/Images/primaire.jpg', 'caption': 'Pôle primaire'},
        {'file': 'blog/Images/cours.jpg', 'caption': 'Cours en plein air'},
        {'file': 'blog/Images/cinquantenaire.jpg', 'caption': 'Célébration'},
        {'file': 'blog/Images/drapeau.jpg', 'caption': 'Cérémonie'},
        {'file': 'blog/Images/bbio.jpg', 'caption': 'Laboratoire de biologie'}
    ]
    return render(request, 'blog/galerie.html', {'images': images})

def home(request):
    """
    Page d'accueil publique (front statique + petits extraits du blog).
    Affiche les 4 derniers articles pour la section blog du front.
    """
    articles = Article.objects.order_by('-date_publication')[:3]
    return render(request, 'blog/index.html', {'articles': articles})

def accueil(request):
    """
    Page listant tous les articles (utilisée pour la page 'Articles').
    """
    articles = Article.objects.order_by('-date_publication')
    return render(request, 'blog/accueil.html', {'articles': articles})

def detail_article(request, id_article):
    """
    Cette vue affiche un article détaillé en fonction de son ID.
    """
    # Récupérer l'article spécifique par son ID
    article = get_object_or_404(Article, id=id_article)
    return render(request, 'blog/detail.html', {'article': article})


def contact_submit(request):
    """
    Handle contact form submissions locally and render a thank-you page.
    For now this view only renders a confirmation page with the sender's name.
    You can later extend it to send emails (send_mail) or persist messages in the DB.
    """
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('message', '').strip()

        # Minimal server-side validation (keep it simple)
        context = {
            'name': name or None,
            'email': email,
            'phone': phone,
            'message': message,
        }

        # TODO: send an email or save the message to the database
        return render(request, 'blog/merci.html', context)

    # If not POST, redirect to home
    return redirect('home')

