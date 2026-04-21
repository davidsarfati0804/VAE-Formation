#!/usr/bin/env python3
"""
SEO Manager — VAE Formation
Communique avec Google Search Console et Google Analytics 4 via service account.
"""

import os
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest, DateRange, Metric, Dimension
)
from seo_config import EMAIL_FROM, EMAIL_PASSWORD, EMAIL_TO

CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), "potent-terminal-494008-i9-d134e226a2b3.json")
SITE_URL         = "https://vae-formation.com/"
SITEMAP_URL      = "https://vae-formation.com/sitemap.xml"
GA4_PROPERTY_ID  = "properties/533756169"

SCOPES_GSC = ["https://www.googleapis.com/auth/webmasters"]
SCOPES_GA4 = ["https://www.googleapis.com/auth/analytics.readonly"]


def _creds_gsc():
    return service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE, scopes=SCOPES_GSC
    )

def _creds_ga4():
    return service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE, scopes=SCOPES_GA4
    )


def lister_sites():
    """Liste tous les sites accessibles dans Search Console."""
    service = build("searchconsole", "v1", credentials=_creds_gsc())
    res = service.sites().list().execute()
    sites = res.get("siteEntry", [])
    print("\n=== SITES SEARCH CONSOLE ===")
    if not sites:
        print("  ⚠️  Aucun site trouvé — vérifiez que le compte de service a bien été ajouté comme utilisateur dans GSC.")
    for s in sites:
        print(f"  {s['permissionLevel']:20s}  {s['siteUrl']}")
    return sites


def soumettre_sitemap():
    """Soumet sitemap.xml à Google Search Console."""
    service = build("searchconsole", "v1", credentials=_creds_gsc())
    try:
        service.sitemaps().submit(siteUrl=SITE_URL, feedpath=SITEMAP_URL).execute()
        print(f"\n✅ Sitemap soumis : {SITEMAP_URL}")
    except Exception as e:
        print(f"\n❌ Erreur soumission sitemap : {e}")


def statut_sitemap():
    """Vérifie le statut du sitemap soumis."""
    service = build("searchconsole", "v1", credentials=_creds_gsc())
    try:
        res = service.sitemaps().get(siteUrl=SITE_URL, feedpath=SITEMAP_URL).execute()
        print("\n=== STATUT SITEMAP ===")
        print(f"  Dernière soumission : {res.get('lastSubmitted', 'N/A')}")
        print(f"  Dernière téléchargement : {res.get('lastDownloaded', 'N/A')}")
        print(f"  URLs soumises : {res.get('contents', [{}])[0].get('submitted', 'N/A')}")
        print(f"  URLs indexées : {res.get('contents', [{}])[0].get('indexed', 'N/A')}")
    except Exception as e:
        print(f"\n❌ Erreur statut sitemap : {e}")


def performance_gsc(jours=30):
    """Affiche les performances Search Console (clics, impressions, position)."""
    service = build("searchconsole", "v1", credentials=_creds_gsc())
    fin    = date.today() - timedelta(days=3)
    debut  = fin - timedelta(days=jours)

    body = {
        "startDate": str(debut),
        "endDate":   str(fin),
        "dimensions": ["query"],
        "rowLimit": 20,
        "orderBy": [{"fieldName": "clicks", "sortOrder": "DESCENDING"}]
    }

    try:
        res = service.searchanalytics().query(siteUrl=SITE_URL, body=body).execute()
        rows = res.get("rows", [])
        print(f"\n=== TOP MOTS-CLÉS GSC (30 derniers jours) ===")
        print(f"  {'Mot-clé':<45} {'Clics':>6} {'Impr':>7} {'CTR':>6} {'Pos':>6}")
        print("  " + "-"*75)
        for r in rows:
            q   = r["keys"][0][:44]
            clic = r["clicks"]
            imp  = r["impressions"]
            ctr  = f"{r['ctr']*100:.1f}%"
            pos  = f"{r['position']:.1f}"
            print(f"  {q:<45} {clic:>6} {imp:>7} {ctr:>6} {pos:>6}")
        if not rows:
            print("  (Aucune donnée — le site est peut-être trop récent)")
    except Exception as e:
        print(f"\n❌ Erreur GSC performance : {e}")


def performance_pages_gsc(jours=30):
    """Top pages par clics dans GSC."""
    service = build("searchconsole", "v1", credentials=_creds_gsc())
    fin   = date.today() - timedelta(days=3)
    debut = fin - timedelta(days=jours)

    body = {
        "startDate": str(debut),
        "endDate":   str(fin),
        "dimensions": ["page"],
        "rowLimit": 10,
        "orderBy": [{"fieldName": "clicks", "sortOrder": "DESCENDING"}]
    }

    try:
        res = service.searchanalytics().query(siteUrl=SITE_URL, body=body).execute()
        rows = res.get("rows", [])
        print(f"\n=== TOP PAGES GSC ===")
        for r in rows:
            print(f"  {r['keys'][0]:<60} clics:{r['clicks']:>5}  pos:{r['position']:.1f}")
        if not rows:
            print("  (Aucune donnée)")
    except Exception as e:
        print(f"\n❌ Erreur GSC pages : {e}")


def trafic_ga4(jours=30):
    """Affiche les métriques GA4 : sessions, utilisateurs, taux d'engagement."""
    if "YOUR_GA4" in GA4_PROPERTY_ID:
        print("\n⚠️  GA4 : Remplacez YOUR_GA4_PROPERTY_ID dans seo_manager.py par votre vrai ID de propriété GA4.")
        return

    creds  = _creds_ga4()
    client = BetaAnalyticsDataClient(credentials=creds)

    fin   = date.today() - timedelta(days=1)
    debut = fin - timedelta(days=jours)

    request = RunReportRequest(
        property=GA4_PROPERTY_ID,
        date_ranges=[DateRange(start_date=str(debut), end_date=str(fin))],
        metrics=[
            Metric(name="sessions"),
            Metric(name="activeUsers"),
            Metric(name="engagementRate"),
            Metric(name="conversions"),
        ],
        dimensions=[Dimension(name="date")],
        order_bys=[{"dimension": {"dimension_name": "date"}}],
        limit=jours,
    )

    try:
        response = client.run_report(request)
        total_sessions = total_users = total_conv = 0
        print(f"\n=== TRAFIC GA4 ({jours} derniers jours) ===")
        for row in response.rows:
            d    = row.dimension_values[0].value
            sess = int(row.metric_values[0].value)
            usr  = int(row.metric_values[1].value)
            eng  = float(row.metric_values[2].value)
            conv = int(row.metric_values[3].value)
            total_sessions += sess
            total_users    += usr
            total_conv     += conv

        print(f"  Sessions totales    : {total_sessions}")
        print(f"  Utilisateurs actifs : {total_users}")
        print(f"  Conversions         : {total_conv}")
    except Exception as e:
        print(f"\n❌ Erreur GA4 : {e}")


def envoyer_rapport_email(contenu_texte):
    """Envoie le rapport SEO par email en HTML."""
    lignes = contenu_texte.strip().split("\n")
    html_lignes = []
    for ligne in lignes:
        if ligne.startswith("===") or ligne.startswith("==="):
            html_lignes.append(f"<h3 style='color:#0B1F3A;margin-top:24px'>{ligne.replace('=','').strip()}</h3>")
        elif ligne.startswith("✅"):
            html_lignes.append(f"<p style='color:#00B8A0'>{ligne}</p>")
        elif ligne.startswith("❌"):
            html_lignes.append(f"<p style='color:#e74c3c'>{ligne}</p>")
        elif ligne.startswith("⚠️"):
            html_lignes.append(f"<p style='color:#f39c12'>{ligne}</p>")
        elif ligne.startswith("  "):
            html_lignes.append(f"<p style='font-family:monospace;margin:2px 0;font-size:13px'>{ligne}</p>")
        elif ligne == "" or ligne.startswith("--") or ligne.startswith("=="):
            html_lignes.append("<hr style='border:none;border-top:1px solid #eee;margin:8px 0'>")
        else:
            html_lignes.append(f"<p>{ligne}</p>")

    html = f"""
    <div style="font-family:'DM Sans',Arial,sans-serif;max-width:680px;margin:0 auto;background:#f7f4ef;padding:32px;border-radius:12px">
      <div style="background:#0B1F3A;border-radius:10px;padding:24px 32px;margin-bottom:24px">
        <h1 style="color:#fff;margin:0;font-size:22px">📊 Rapport SEO — VAE Formation</h1>
        <p style="color:rgba(255,255,255,.6);margin:6px 0 0;font-size:14px">{date.today().strftime('%d/%m/%Y')}</p>
      </div>
      <div style="background:#fff;border-radius:10px;padding:24px 32px">
        {''.join(html_lignes)}
      </div>
      <p style="font-size:11px;color:#999;text-align:center;margin-top:16px">
        Rapport généré automatiquement · VAE Formation SEO Manager
      </p>
    </div>
    """

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"📊 Rapport SEO VAE Formation — {date.today().strftime('%d/%m/%Y')}"
    msg["From"]    = EMAIL_FROM
    msg["To"]      = EMAIL_TO
    msg.attach(MIMEText(contenu_texte, "plain"))
    msg.attach(MIMEText(html, "html"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_FROM, EMAIL_PASSWORD)
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        print(f"\n✅ Rapport envoyé à {EMAIL_TO}")
    except Exception as e:
        print(f"\n❌ Erreur envoi email : {e}")


def rapport_complet():
    """Lance un rapport complet GSC + GA4."""
    print("\n" + "="*60)
    print("   RAPPORT SEO — VAE FORMATION")
    print(f"   {date.today().strftime('%d/%m/%Y')}")
    print("="*60)
    lister_sites()
    statut_sitemap()
    performance_gsc()
    performance_pages_gsc()
    trafic_ga4()
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    import io, sys
    buf = io.StringIO()
    sys.stdout = buf
    rapport_complet()
    sys.stdout = sys.__stdout__
    contenu = buf.getvalue()
    print(contenu)
    envoyer_rapport_email(contenu)
