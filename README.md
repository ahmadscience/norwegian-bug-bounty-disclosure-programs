# Norske bug bounty- og responsible disclosure-program 🇳🇴 / Norwegian Bug Bounty & Coordinated Disclosure Programs

En oversikt over norske, eller Norge-baserte, virksomheter med et bug bounty-program, sårbarhetsrapporteringsprogram (VDP), ansvarlig rapporteringspolicy (RDP), eller som minst tar imot rapporter via en `security.txt`.

A curated list of Norwegian, or Norway-based, organizations with a bug bounty program, vulnerability disclosure program (VDP), responsible disclosure policy (RDP), or that at minimum accept reports via a `security.txt`.

Vet du om et program som mangler? Se [Bidra](#bidra--contributing) under, eller rediger [`programs.yaml`](programs.yaml) direkte og send en pull request.

Know of a program that's missing? See [Contributing](#bidra--contributing) below, or edit [`programs.yaml`](programs.yaml) directly and send a pull request.

> ⚠️ **En `security.txt` er ikke en invitasjon til å teste.** Den er en kontaktkanal for å rapportere sårbarheter du har funnet gjennom normal bruk, ikke tillatelse til å skanne, angripe eller aktivt lete etter svakheter. De fleste `security.txt`-oppføringene under (kategorien "kun security.txt / kontakt") har **ingen** formell policy, scope eller trygg-havn-klausul. Har du ikke en publisert bug bounty- eller VDP-avtale som sier at aktiv testing er tillatt, kan uautorisert testing være ulovlig etter straffeloven § 204 og du kan komme i ansvar selv om du rapporterer funnet i god tro.
>
> ⚠️ **A `security.txt` is not an invitation to test.** It is a contact channel for reporting vulnerabilities you found through normal use, not permission to scan, attack, or actively probe for weaknesses. Most `security.txt` entries below (the "security.txt / contact only" category) have **no** formal policy, scope, or safe harbor language. Without a published bug bounty or VDP agreement that explicitly authorizes active testing, unauthorized testing can be illegal and you may face liability even if you report the finding in good faith.

<!-- programs:start -->
**85 aktive program / active programs · 9 offentlige bug bounty-program med pengedusør / public bug bounty programs with a cash reward · sist oppdatert / last updated 2026-10-05**

### 💰 Offentlige bug bounty-program / Public bug bounty programs

|Firma / Company|Plattform / program / Platform / program|Dusør / Reward|security.txt|Kommentar / Comment|Lansert / Launched|Kilde / Source|
|---|---|---|---|---|---|---|
|[DN](https://www.dn.no)|[Eget program / Self-hosted](https://www.dn.no/kundeservice/faq/vilkar-og-personvern/bug-bounty)|<span title="Penger / Money">💰</span>|-|Dagens Næringsliv. Dusør etter alvorlighetsgrad, rapporter til sikkerhet@dn.no. / Dagens Næringsliv. Reward based on severity, report to sikkerhet@dn.no.|?|-|
|[Dune Analytics](https://dune.com)|[Eget program / Self-hosted](https://docs.dune.com/web-app/bug-bounty)|<span title="Penger / Money">💰</span>|-|Norsk-grunnlagt, nå internasjonalt selskap. / Norwegian-founded, now an international company.|?|-|
|[Kantega](https://www.kantega.no) - Kantega SSO|[Bugcrowd](https://bugcrowd.com/engagements/kantega)|<span title="Penger / Money">💰</span>|[security.txt](https://www.kantega.no/.well-known/security.txt)|Dekker SSO-produktet, ikke nødvendigvis hele kantega.no. / Covers the SSO product, not necessarily all of kantega.no.|?|-|
|[Klarna](https://www.klarna.com)|[HackerOne](https://hackerone.com/klarna/policy_scopes)|<span title="Penger / Money">💰</span>|-|Nordisk fintech med virksomhet i Norge. / Nordic fintech with operations in Norway.|?|-|
|[Morgenbladet](https://morgenbladet.no) <span title="Usikker status / Unknown status">⚠️</span>|[Eget program / Self-hosted](https://www.morgenbladet.no/kontakt-oss)|<span title="Penger / Money">💰</span>|-|Fant ingen egen policyside, lenken går til kontaktsiden. Bekreft før du tester. / No dedicated policy page found, link goes to the contact page. Verify before testing.|?|-|
|[NBX](https://nbx.com)|[Open Bug Bounty](https://openbugbounty.org/bugbounty/nbxsec/)|<span title="Penger / Money">💰</span> <span title="Hall of Fame">🏆</span>|[security.txt](https://app.nbx.com/.well-known/security.txt)|-|?|[NBX](https://nbx.com/en/security)|
|[Opera Software](https://www.opera.com)|[Bugcrowd](https://bugcrowd.com/opera)|<span title="Penger / Money">💰</span>|[security.txt](https://opera.com/.well-known/security.txt)|-|<= 2018|[Opera](https://security.opera.com/en/bug-bounty/)|
|[Tidal](https://tidal.com)|[Bugcrowd](https://bugcrowd.com/engagements/tidal-bugbounty)|<span title="Penger / Money">💰</span>|[security.txt](https://tidal.com/.well-known/security.txt)|-|?|-|
|[Visma](https://visma.no)|[Intigriti](https://app.intigriti.com/researcher/programs/visma/visma)|<span title="Penger / Money">💰</span>|-|Startet som privat program, offentlig siden januar 2021. / Started as a private program, public since January 2021.|Jan. 2021|[Intigriti](https://www.intigriti.com/blog/customer-stories/vismas-bug-bounty-program-manager-speaks-to-intigriti-about-the-practice-of-running-a-successful-program)|

### 🔒 Private bug bounty-program / Private bug bounty programs

Private program krever invitasjon fra plattformen eller selskapet, men det er offentlig kjent at de finnes. / Private programs require an invite from the platform or company, but are publicly known to exist.

|Firma / Company|Plattform / program / Platform / program|Dusør / Reward|security.txt|Kommentar / Comment|Lansert / Launched|Kilde / Source|
|---|---|---|---|---|---|---|
|[Ardoq](https://ardoq.com)|HackerOne|<span title="Penger / Money">💰</span>|-|-|<= 2022|[Ardoq](https://www.ardoq.com/blog/bug-bounty-hackerone)|
|[Firi](https://firi.com)|[HackerOne](https://hackerone.com/firi_as)|<span title="Penger / Money">💰</span>|[security.txt](https://firi.com/.well-known/security.txt)|-|Okt. 2024|[security.txt](https://firi.com/.well-known/security.txt)|
|[Kahoot](https://kahoot.com)|Intigriti|<span title="Penger / Money">💰</span>|[security.txt](https://kahoot.com/.well-known/security.txt)|Kilden er Intigritis generelle kundeliste, ikke en programside. / Source is Intigriti's general customer list, not a program page.|?|[Intigriti](https://intigriti.com/companies)|
|[Kahoot](https://kahoot.com) - [Motimate](https://motimateapp.com)|Intigriti|<span title="Penger / Money">💰</span>|[security.txt](https://motimateapp.com/.well-known/security.txt)|-|?|[Facebook](https://business.facebook.com/motimateapp/photos/a.1702293843419477/3049907031991478/)|
|[Nordic Semiconductor](https://www.nordicsemi.com)|YesWeHack|<span title="Penger / Money">💰</span>|-|Startet på HackerOne i 2021, nå på YesWeHack. Kontakt YesWeHack for invitasjon. / Started on HackerOne in 2021, now on YesWeHack. Contact YesWeHack for an invite.|Jan. 2021|[Nordic Semiconductor](https://www.nordicsemi.com/Products/Technologies/Security/Vulnerability-Disclosure)|
|[Northern.tech](https://northern.tech)|[HackerOne](https://hackerone.com/northerntechhq)|<span title="Penger / Money">💰</span>|[security.txt](https://northern.tech/security.txt)|-|2021|[Northern.tech](https://northern.tech/blog/)|
|[Oda](https://oda.com)|YesWeHack|<span title="Penger / Money">💰</span>|[security.txt](https://oda.com/.well-known/security.txt)|-|Apr. 2022|[security.txt](https://oda.com/.well-known/security.txt)|
|[Promon](https://promon.io)|[Eget program / Self-hosted](https://trust.promon.io/)|<span title="Penger / Money">💰</span> <span title="Hall of Fame">🏆</span>|[security.txt](https://promon.io/.well-known/security.txt)|Belønningsvilkår ikke offentlige. / Reward terms not public.|?|-|
|[Schibsted](https://schibsted.com)|Bugcrowd|<span title="Penger / Money">💰</span>|[security.txt](https://schibsted.com/.well-known/security.txt)|Dekker flere Schibsted-merkevarer, bl.a. Aftenposten og VG. / Covers several Schibsted brands, incl. Aftenposten and VG.|?|[security.txt](https://vg.no/.well-known/security.txt)|
|[Signicat](https://www.signicat.com)|Intigriti|<span title="Penger / Money">💰</span>|[security.txt](https://www.signicat.com/.well-known/security.txt)|-|?|[Intigriti](https://app.intigriti.com/programs/signicat/signicatresponsibledisclosure/detail)|
|[Sparebank 1](https://www.sparebank1.no)|Intigriti|<span title="Penger / Money">💰</span>|[security.txt](https://www.sparebank1.no/.well-known/security.txt)|-|Nov. 2021|[kode24](https://www.kode24.no/artikkel/slik-blir-du-dusorjeger-for-sparebank-1/76160552)|
|[Storebrand](https://www.storebrand.no)|Intigriti|<span title="Penger / Money">💰</span>|[security.txt](https://www.storebrand.no/.well-known/security.txt)|-|Feb. 2025|[BankShift](https://www.bankshift.no/teknologi/storebrand-apne-om-angrep-i-egne-systemer-noen-hadde-tatt-over-koden-som-andre-hadde-laget/457471)|
|[Vend](https://vend.com) - [FINN.no](https://finn.no)|HackerOne|<span title="Penger / Money">💰</span>|[security.txt](https://finn.no/.well-known/security.txt)|Tidligere del av Schibsted/Adevinta, nå eget selskap. / Formerly part of Schibsted/Adevinta, now a separate company.|Sep. 2019|[Medium](https://medium.com/finn-no/one-year-with-a-private-bug-bounty-program-f928a57ad026)|

**I tillegg kjenner man til minst 3 norske private programmer hvor selskapet ikke kan oppgis. / In addition, at least 3 private Norwegian programs are known to exist where the company cannot be named.**

### 📨 Responsible disclosure / VDP

|Firma / Company|Plattform / program / Platform / program|Dusør / Reward|security.txt|Kommentar / Comment|Lansert / Launched|Kilde / Source|
|---|---|---|---|---|---|---|
|[AutoStore](https://www.autostoresystem.com)|[Eget program / Self-hosted](https://www.autostoresystem.com/legal/vulnerability-disclosure-policy-responsible-research-guidelines)|<span title="Hall of Fame">🏆</span>|-|Ingen dusør. Produktene styrer fysiske roboter, test forsiktig. / No bounty. Products control physical robots, test with care.|?|-|
|[Bergen kommune](https://www.bergen.kommune.no)|Eget program / Self-hosted|-|[security.txt](https://www.bergen.kommune.no/.well-known/security.txt)|Kontakt: itsikkerhet@bergen.kommune.no. Ber om varsel før aktiv testing. / Contact: itsikkerhet@bergen.kommune.no. Asks for advance notice before active testing.|?|-|
|[Cognite](https://www.cognite.com)|[Eget program / Self-hosted](https://docs.cognite.com/cdf/trust/vulnerability-disclosure-policy)|-|[security.txt](https://www.cognite.com/.well-known/security.txt)|-|?|-|
|[Dagbladet](https://www.dagbladet.no)|[HackerOne](https://hackerone.com/dagbladet)|-|-|Generisk HackerOne-oppføring, scope og vilkår er uklare. / Generic HackerOne listing, scope and terms are unclear.|?|-|
|[Danske Bank](https://danskebank.com)|[Eget program / Self-hosted](https://danskebank.com/responsible-disclosure)|-|-|Nordisk konsern, dekker Danske Bank Norge. / Nordic group, covers Danske Bank Norge.|?|-|
|[Digdir](https://www.digdir.no)|[Eget program / Self-hosted](https://www.digdir.no/digdir/responsible-disclosure-policy/6386)|<span title="Hall of Fame">🏆</span>|[security.txt](https://www.digdir.no/.well-known/security.txt)|-|?|-|
|[Equinor](https://www.equinor.com)|[Eget program / Self-hosted](https://www.equinor.com/about-us/csirt)|-|[security.txt](https://www.equinor.com/.well-known/security.txt)|-|?|-|
|[Euronext Securities Oslo](https://www.euronext.com)|[Eget program / Self-hosted](https://www.euronext.com/en/post-trade/euronext-securities/oslo/about-us/vulnerability-reporting)|-|-|Tidligere Verdipapirsentralen, forkortet VPS. / Formerly Verdipapirsentralen, abbreviated VPS.|?|-|
|[Gjensidige](https://www.gjensidige.no)|[HackerOne](https://hackerone.com/gjensidige)|<span title="Hall of Fame">🏆</span>|[security.txt](https://www.gjensidige.no/.well-known/security.txt)|-|?|-|
|[Handelsbanken](https://www.handelsbanken.no)|[HackerOne](https://hackerone.com/handelsbanken)|-|-|Nordisk konsern, dekker Handelsbanken Norge. / Nordic group, covers Handelsbanken Norge.|?|-|
|[Horde](https://horde.no)|[Eget program / Self-hosted](https://horde.no/responsible-disclosure/)|<span title="Hall of Fame">🏆</span>|[security.txt](https://horde.no/.well-known/security.txt)|-|?|-|
|[Infront](https://oslomarketsolutions.no) - Oslo Market Solutions <span title="Usikker status / Unknown status">⚠️</span>|[Eget program / Self-hosted](https://oslomarketsolutions.no/en/responsibledisclosure/)|-|-|Nettstedet har utløpt TLS-sertifikat per oktober 2026. / The site has an expired TLS certificate as of October 2026.|?|-|
|[Jobreg](https://jobreg.no)|[Eget program / Self-hosted](https://www.jobreg.no/security.php)|<span title="Hall of Fame">🏆</span>|-|-|?|-|
|[JustisCERT](https://www.justiscert.no)|[Eget program / Self-hosted](https://www.justiscert.no/rapportering-av-sarbarheter)|-|[security.txt](https://www.justiscert.no/.well-known/security.txt)|CERT for justissektoren, bl.a. politiet og domstolene. / CERT for the justice sector, incl. police and courts.|?|-|
|[Kahoot](https://kahoot.com)|[Eget program / Self-hosted](https://kahoot.com/disclosure-policy.txt)|-|[security.txt](https://kahoot.com/.well-known/security.txt)|-|?|-|
|[Kartverket](https://www.kartverket.no)|[Eget program / Self-hosted](https://vdp.kartverket.no/responsible-disclosure-policy.txt)|<span title="Hall of Fame">🏆</span>|-|Dekker alle underdomener av kartverket.no og geonorge.no. / Covers all subdomains of kartverket.no and geonorge.no.|?|-|
|[KLP](https://www.klp.no)|[Eget program / Self-hosted](https://www.klp.no/om-klp/personvern/slik-sikrer-vi-din-informasjon)|-|[security.txt](https://www.klp.no/.well-known/security.txt)|Kontakt: sikkerhet@klp.no, PGP foretrekkes. / Contact: sikkerhet@klp.no, PGP preferred.|?|-|
|[NBIM](https://www.nbim.no)|[Eget program / Self-hosted](https://www.nbim.no/en/responsible-disclosure-policy/)|<span title="Hall of Fame">🏆</span>|[security.txt](https://www.nbim.no/.well-known/security.txt)|Forvalter Statens pensjonsfond utland, kjent som Oljefondet. / Manages the Government Pension Fund Global, known as the Oil Fund.|?|-|
|[Nettavisen](https://www.nettavisen.no) - Nettavisen Sport|[HackerOne](https://hackerone.com/nettavisen_sport)|-|-|Dekker trolig kun Sport-seksjonen. / Likely covers only the Sport section.|?|-|
|[Nordea](https://www.nordea.com)|[HackerOne](https://hackerone.com/nordea)|<span title="Hall of Fame">🏆</span>|-|Nordisk konsern, dekker også norsk virksomhet. / Nordic group, also covers Norwegian operations.|?|-|
|[Nordic Semiconductor](https://www.nordicsemi.com)|[Eget program / Self-hosted](https://www.nordicsemi.com/Products/Technologies/Security/Vulnerability-Disclosure)|-|-|-|?|-|
|[Nordnet](https://www.nordnet.no)|[Eget program / Self-hosted](https://www.nordnet.se/security-disclosure)|-|[security.txt](https://www.nordnet.no/.well-known/security.txt)|Nordisk plattform, ikke bekreftet Norge-spesifikk side. / Nordic platform, no Norway-specific page confirmed.|?|-|
|[NorgesGruppen](https://www.norgesgruppen.no)|[Eget program / Self-hosted](https://www.norgesgruppen.no/cybersikkerhet/)|-|-|-|?|-|
|[Norsk Helsenett](https://www.nhn.no) - [Helsenorge](https://www.helsenorge.no)|[Eget program / Self-hosted](https://www.nhn.no/.well-known/vulnerability-disclosure.html)|<span title="Hall of Fame">🏆</span>|[security.txt](https://www.nhn.no/.well-known/security.txt)|-|?|-|
|[Norsk Hydro](https://www.hydro.com)|[HackerOne](https://hackerone.com/norskhydroasa)|<span title="Hall of Fame">🏆</span>|-|-|?|-|
|[NRK](https://nrk.no)|[Eget program / Self-hosted](https://info.nrk.no/responsible-disclosure-policy/)|<span title="Hall of Fame">🏆</span>|[security.txt](https://nrk.no/.well-known/security.txt)|-|?|-|
|[PostNord](https://www.postnord.com) - [Bring](https://www.bring.no)|[Eget program / Self-hosted](https://vdp.postnord.com/)|<span title="Hall of Fame">🏆</span>|[security.txt](https://www.postnord.com/.well-known/security.txt)|-|?|-|
|[reMarkable](https://remarkable.com)|[Eget program / Self-hosted](https://support.remarkable.com/hc/en-us/articles/5068888862621-Vulnerability-Disclosure-Policy)|<span title="Hall of Fame">🏆</span>|[security.txt](https://remarkable.com/.well-known/security.txt)|Oslo-basert nettbrettprodusent. / Oslo-based tablet maker.|?|-|
|[SAS](https://www.flysas.com)|[HackerOne](https://hackerone.com/sas_legacy)|<span title="Hall of Fame">🏆</span>|-|Scandinavian Airlines, skandinavisk flyselskap med stor virksomhet i Norge. / Scandinavian Airlines, a Scandinavian airline with major operations in Norway.|?|-|
|[Signicat](https://www.signicat.com)|[Intigriti](https://app.intigriti.com/programs/signicat/signicatresponsibledisclosure/detail)|<span title="Hall of Fame">🏆</span>|[security.txt](https://www.signicat.com/.well-known/security.txt)|-|?|-|
|[Storebrand](https://www.storebrand.no)|[Intigriti](https://app.intigriti.com/programs/spp-storebrand/storebrand-rd/detail)|-|[security.txt](https://www.storebrand.no/.well-known/security.txt)|-|Jan. 2026|-|
|[Sykehuspartner](https://www.sykehuspartner.no) <span title="Usikker status / Unknown status">⚠️</span>|Eget program / Self-hosted|-|[security.txt](https://www.sykehuspartner.no/.well-known/security.txt)|Felles helse-IT-drift for Helse Sør-Øst. Policysiden er borte, security.txt virker fortsatt. / Shared health-IT operations for Helse Sør-Øst. The policy page is gone, security.txt still works.|?|-|
|[Telenor](https://www.telenor.com)|[HackerOne](https://hackerone.com/telenor_group)|<span title="Hall of Fame">🏆</span>|-|-|?|-|
|[Telia](https://www.telia.no)|[HackerOne](https://hackerone.com/teliasoneraab)|-|-|Nordisk konsern, ikke bekreftet Norge-spesifikk scope. / Nordic group, no Norway-specific scope confirmed.|?|-|
|[Tryg Forsikring](https://www.tryg.no)|[Eget program / Self-hosted](https://tryg.com/en/responsible-disclosure)|-|[security.txt](https://tryg.dk/.well-known/security.txt)|Nordisk konsern, dekker Tryg Norge. / Nordic group, covers Tryg Norge.|?|-|
|[TV 2](https://www.tv2.no)|[Eget program / Self-hosted](https://info.tv2.no/info/artikkel/responsible-disclosure-policy)|<span title="Hall of Fame">🏆</span>|[security.txt](https://www.tv2.no/.well-known/security.txt)|-|?|-|
|[Universitetet i Oslo](https://www.uio.no)|[Eget program / Self-hosted](https://www.uio.no/english/services/it/security/cert/vulnerability-disclosure-policy.html)|-|[security.txt](https://www.uio.no/.well-known/security.txt)|Drives av UiO-CERT. / Run by UiO-CERT.|?|-|
|[Vipps](https://vipps.no)|[Eget program / Self-hosted](https://vipps.no/sikkerhet/responsible-disclosure-policy/)|<span title="Hall of Fame">🏆</span>|[security.txt](https://vipps.no/.well-known/security.txt)|-|?|-|
|[Visma](https://visma.no)|[Intigriti](https://app.intigriti.com/researcher/programs/visma/VismaResponsibleDisclosure)|<span title="Swag">👕</span> <span title="Hall of Fame">🏆</span>|-|-|?|[Visma](https://www.visma.com/trust-centre/responsible-disclosure)|
|[Vy](https://www.vy.no)|[Eget program / Self-hosted](https://www.vy.no/en/conditions-and-privacy/vulnerability-disclosure-policy)|-|[security.txt](https://www.vy.no/.well-known/security.txt)|Tidligere NSB. / Formerly NSB.|?|-|
|[Yara](https://www.yara.com) <span title="Usikker status / Unknown status">⚠️</span>|[Eget program / Self-hosted](https://vdp.yara.com/)|<span title="Hall of Fame">🏆</span>|-|VDP-siden svarer med feil TLS-sertifikat per oktober 2026. / The VDP site serves a mismatched TLS certificate as of October 2026.|?|-|

### 📇 Kun security.txt / kontakt, uten egen policyside / security.txt or contact only, no dedicated policy page

Ingen bug bounty eller formell policyside, men det finnes en kjent kanal for å rapportere sårbarheter. / No bug bounty or formal policy page, but there is a known channel for reporting vulnerabilities.

|Firma / Company|Plattform / program / Platform / program|Dusør / Reward|security.txt|Kommentar / Comment|Lansert / Launched|
|---|---|---|---|---|---|
|[Bane NOR](https://www.banenor.no)|Eget program / Self-hosted|-|[security.txt](https://www.banenor.no/.well-known/security.txt)|-|?|
|[BankID Norge](https://www.bankid.no)|Eget program / Self-hosted|<span title="Hall of Fame">🏆</span>|[security.txt](https://bankid.no/.well-known/security.txt)|Ingen egen policyside funnet, bare security.txt. / No dedicated policy page found, only security.txt.|?|
|[Forsvaret](https://www.forsvaret.no)|Eget program / Self-hosted|-|[security.txt](https://www.forsvaret.no/.well-known/security.txt)|-|?|
|[Gelato](https://www.gelato.com)|Eget program / Self-hosted|-|[security.txt](https://www.gelato.com/.well-known/security.txt)|Oslo-grunnlagt print-on-demand-selskap. / Oslo-founded print-on-demand company.|?|
|[Helse Sør-Øst](https://helse-sorost.no)|Eget program / Self-hosted|-|[security.txt](https://helse-sorost.no/.well-known/security.txt)|Håndteres av Sykehuspartner. / Handled by Sykehuspartner.|?|
|[Holtålen kommune](https://holtalen.kommune.no)|Eget program / Self-hosted|-|[security.txt](https://holtalen.kommune.no/.well-known/security.txt)|-|?|
|[Kongsberg Gruppen](https://www.kongsberg.com)|Eget program / Self-hosted|-|[security.txt](https://www.kongsberg.com/.well-known/security.txt)|-|?|
|[NAV](https://www.nav.no)|Eget program / Self-hosted|-|[security.txt](https://nav.no/.well-known/security.txt)|Kontakt: soc@nav.no. / Contact: soc@nav.no.|?|
|[Norkart](https://www.norkart.no)|Eget program / Self-hosted|-|[security.txt](https://norkart.no/.well-known/security.txt)|-|?|
|[Oslo kommune](https://www.oslo.kommune.no)|Eget program / Self-hosted|-|[security.txt](https://www.oslo.kommune.no/.well-known/security.txt)|-|?|
|[Ringerike kommune](https://www.ringerike.kommune.no)|Eget program / Self-hosted|-|[security.txt](https://www.ringerike.kommune.no/.well-known/security.txt)|-|?|
|[Sbanken](https://www.sbanken.no)|Eget program / Self-hosted|-|[security.txt](https://sbanken.no/.well-known/security.txt)|Del av DNB, kontakt irt@dnb.no. / Part of DNB, contact irt@dnb.no.|?|
|[Skatteetaten](https://www.skatteetaten.no)|Eget program / Self-hosted|-|[security.txt](https://www.skatteetaten.no/.well-known/security.txt)|Kontakt: csirt@skatteetaten.no. / Contact: csirt@skatteetaten.no.|?|
|[Stange kommune](https://www.stange.kommune.no)|Eget program / Self-hosted|-|[security.txt](https://www.stange.kommune.no/.well-known/security.txt)|-|?|
|[Statens vegvesen](https://www.vegvesen.no)|Eget program / Self-hosted|-|[security.txt](https://www.vegvesen.no/.well-known/security.txt)|-|?|
|[Statkraft](https://www.statkraft.com)|[Eget program / Self-hosted](https://www.statkraft.com/about-statkraft/irt/)|-|[security.txt](https://www.statkraft.com/.well-known/security.txt)|IRT-kontakt: csirt@statkraft.com, ingen egen policyside. / IRT contact: csirt@statkraft.com, no dedicated policy page.|?|
|[Søndre Land kommune](https://www.sondre-land.kommune.no)|Eget program / Self-hosted|-|[security.txt](https://www.sondre-land.kommune.no/.well-known/security.txt)|-|?|
|[Telenor](https://www.telenor.no) - Telenor Norge|Eget program / Self-hosted|-|[security.txt](https://www.telenor.no/.well-known/security.txt)|-|?|
|[Valgdirektoratet](https://www.valg.no)|Eget program / Self-hosted|-|[security.txt](https://www.valg.no/.well-known/security.txt)|Kontakt: sikkerhet@valg.no. / Contact: sikkerhet@valg.no.|?|

Dusør / Reward: 💰 penger / money · 🏆 hall of fame · 👕 swag. ⚠️ = usikker status / unknown status · 🔴 = stengt / closed.
<!-- programs:end -->

Vil du legge til eller endre noe? Rediger [`programs.yaml`](programs.yaml) - tabellene over genereres automatisk fra den filen når du sender en pull request. Se [CONTRIBUTING.md](CONTRIBUTING.md).

Want to add or change something? Edit [`programs.yaml`](programs.yaml) - the tables above are generated automatically from that file when you send a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Hall of Fame

Program som offentlig krediterer forskere (🏆 i tabellene), nyttig om du vil ha anerkjennelse i tillegg til, eller i stedet for, penger. Listen genereres fra `programs.yaml`.

Programs that publicly credit researchers (🏆 in the tables), useful if you want recognition in addition to, or instead of, cash. The list is generated from `programs.yaml`.

<!-- halloffame:start -->
- [AutoStore](https://www.autostoresystem.com/legal/vulnerability-disclosure-policy-responsible-research-guidelines)
- [BankID Norge](https://bankid.no/.well-known/security.txt)
- [Digdir](https://www.digdir.no/digdir/responsible-disclosure-policy/6386)
- [Gjensidige](https://hackerone.com/gjensidige)
- [Horde](https://horde.no/responsible-disclosure/)
- [Jobreg](https://www.jobreg.no/security.php)
- [Kartverket](https://vdp.kartverket.no/responsible-disclosure-policy.txt)
- [NBIM](https://www.nbim.no/en/responsible-disclosure-policy/)
- [NBX](https://openbugbounty.org/bugbounty/nbxsec/)
- [Nordea](https://hackerone.com/nordea)
- [Norsk Helsenett / Helsenorge](https://www.nhn.no/.well-known/vulnerability-disclosure.html)
- [Norsk Hydro](https://hackerone.com/norskhydroasa)
- [NRK](https://info.nrk.no/responsible-disclosure-policy/)
- [PostNord / Bring](https://vdp.postnord.com/)
- [Promon](https://trust.promon.io/)
- [reMarkable](https://support.remarkable.com/hc/en-us/articles/5068888862621-Vulnerability-Disclosure-Policy)
- [SAS](https://hackerone.com/sas_legacy)
- [Signicat](https://app.intigriti.com/programs/signicat/signicatresponsibledisclosure/detail)
- [Telenor](https://hackerone.com/telenor_group)
- [TV 2](https://info.tv2.no/info/artikkel/responsible-disclosure-policy)
- [Vipps](https://vipps.no/sikkerhet/responsible-disclosure-policy/)
- [Visma](https://app.intigriti.com/researcher/programs/visma/VismaResponsibleDisclosure)
- [Yara](https://vdp.yara.com/)
<!-- halloffame:end -->

## Bidra / Contributing

Denne listen driftes av fellesskapet. Slik hjelper du til:

This list is community-maintained. Here's how to help:

1. Rediger [`programs.yaml`](programs.yaml). **Ikke** rediger tabellene i `README.md` direkte - de genereres automatisk når endringen havner på `main`.
   Edit [`programs.yaml`](programs.yaml). **Do not** edit the tables in `README.md` directly - they are generated automatically once the change lands on `main`.
2. Send en pull request. Feltbeskrivelser står øverst i `programs.yaml`, og en fyldigere guide finnes i [CONTRIBUTING.md](CONTRIBUTING.md).
   Send a pull request. Field descriptions are at the top of `programs.yaml`, and a fuller guide is in [CONTRIBUTING.md](CONTRIBUTING.md).
3. En sjekk kjører automatisk på pull requesten og sier fra hvis noe mangler eller har feil verdi.
   A check runs automatically on the pull request and flags anything missing or invalid.

Har du ikke lyst til å lage en pull request selv? [Opprett et issue](../../issues/new) med en lenke til programmet, så tar noen seg av resten.

Don't want to open a pull request yourself? [Open an issue](../../issues/new) with a link to the program, and someone will take it from there.

Hva hører hjemme i listen: programmer hos norske selskap eller norske datterselskap/merkevarer av utenlandske selskap; både betalte bug bounty-program og gratis responsible/vulnerability disclosure-program; private program bare når eksistensen er offentlig kjent og du kan oppgi en kilde (er programmet hemmelig, utelat `name` og sett `visibility: undisclosed`); og virksomheter som i det minste svarer på rapporter via en publisert `security.txt`.

What belongs in the list: programs run by Norwegian companies, or by Norwegian subsidiaries/brands of foreign companies; both paid bug bounty programs and free responsible/vulnerability disclosure programs; private programs only when their existence is publicly known and you can cite a source (if the program is secret, omit `name` and set `visibility: undisclosed`); and organizations that at least respond to reports via a published `security.txt`.

Kjenner du en norsk virksomhet som burde hatt et program, men ikke har det? Ikke legg dem til her - oppfordre dem heller til å publisere en `security.txt` etter [RFC 9116](https://datatracker.ietf.org/doc/html/rfc9116), det er det enkleste stedet å starte.

Know a Norwegian organization that should have a program but doesn't? Don't add them here - encourage them to publish a `security.txt` per [RFC 9116](https://datatracker.ietf.org/doc/html/rfc9116) instead, it's the easiest place to start.

## Ressurser / Resources

- **[securitytxt.no](https://web.archive.org/web/20260517123123/https://securitytxt.no/)** (arkivert / archived) - Tidligere oversikt over `security.txt`-bruk i norsk offentlig sektor. Siden er nå nede, lenken går til siste kjente arkiverte versjon. Sjekk gjerne selv om en virksomhet har lagt til en `security.txt` senere.
  Former adoption tracker for `security.txt` in Norwegian public sector. The site is now down, the link goes to the last known archived version. It's worth checking directly whether an organization has added a `security.txt` since.
- **[kode24 - Dusørjegerne](https://www.kode24.no/tag/dus%C3%B8rjegerne)** - Intervjuserie med norske dusørjegere. / Interview series with Norwegian bug bounty hunters.
- **[RFC 9116](https://datatracker.ietf.org/doc/html/rfc9116)** - Standarden for `security.txt`. / The `security.txt` standard.
- **[disclose.io](https://disclose.io/)** - Åpent prosjekt om trygg-havn-klausuler og VDP-praksis. / Open project on safe harbor language and VDP best practice.
- **[NSM](https://nsm.no/)** - Nasjonal sikkerhetsmyndighet. / The Norwegian National Security Authority.

---

*Se [`programs.yaml`](programs.yaml) for kilde-dataen og [CONTRIBUTING.md](CONTRIBUTING.md) for en fullstendig bidragsguide. / See [`programs.yaml`](programs.yaml) for the source data and [CONTRIBUTING.md](CONTRIBUTING.md) for a full contribution guide.*
