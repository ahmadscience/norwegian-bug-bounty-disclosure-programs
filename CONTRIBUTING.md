# Bidra / Contributing

Vet du om et norsk bug bounty-, VDP- eller responsible disclosure-program som mangler, eller er noe i listen feil? Flott!

Know of a Norwegian bug bounty, VDP or responsible disclosure program that's missing, or something in the list that's wrong? Great!

## Slik gjør du det / How to do it

1. Rediger [`programs.yaml`](programs.yaml). **Ikke** rediger tabellene eller Hall of Fame-listen i `README.md` direkte, de genereres automatisk når endringen er inne på `main`.
   Edit [`programs.yaml`](programs.yaml). **Do not** edit the tables or the Hall of Fame list in `README.md` directly, they are generated automatically once the change lands on `main`.
2. Send en pull request. Beskrivelsen av feltene står øverst i `programs.yaml`.
   Send a pull request. Field descriptions are at the top of `programs.yaml`.
3. En sjekk kjører på pull requesten og sier fra hvis noe mangler eller har feil verdi.
   A check runs on the pull request and flags anything missing or invalid.

Eksempel på en oppføring / Example entry:

```yaml
- name: Oda
  url: https://oda.com
  platform: intigriti
  visibility: public
  type: bug-bounty
  program_url: https://app.intigriti.com/researcher/programs/oda/oda
  rewards: [money]
  launched: 2022-04
  source: https://medium.com/oda-product-tech/oda-is-launching-our-bug-bounty-program-8e356d5ac0d3
  source_name: Medium
  comment: Valgfritt fritekstnotat, f.eks. et forbehold. / Optional free-text note, e.g. a caveat.
```

Er et program stengt? Sett `status: closed` i stedet for å fjerne oppføringen.

Is a program closed? Set `status: closed` instead of removing the entry.

Har du ikke lyst til å lage en pull request? [Opprett et issue](../../issues/new/choose) med lenke til programmet, så tar noen seg av resten.

Don't want to open a pull request? [Open an issue](../../issues/new/choose) with a link to the program, and someone will take it from there.

## Hva hører hjemme i listen? / What belongs in the list?

- Program hos norske selskap, eller norske datterselskap/merkevarer av utenlandske selskap, oppgi da eier som `name` og merkevaren som `unit`.
  Programs run by Norwegian companies, or by Norwegian subsidiaries/brands of foreign companies, list the owner as `name` and the brand as `unit`.
- Både betalte bug bounty-program og responsible/vulnerability disclosure-program uten dusør (`type: rdp` eller `type: vdp`).
  Both paid bug bounty programs and free responsible/vulnerability disclosure programs (`type: rdp` or `type: vdp`).
- Virksomheter uten formell policyside, men som i det minste tar imot rapporter via en publisert `security.txt` eller en oppgitt sikkerhetskontakt (`type: contact-only`).
  Organizations with no formal policy page, but that at least accept reports via a published `security.txt` or a stated security contact (`type: contact-only`).
- Private program bare hvis eksistensen er offentlig kjent (`visibility: private-known`) og du kan oppgi en kilde. Er programmet hemmelig, utelat `name` og sett `visibility: undisclosed`.
  Private programs only if their existence is publicly known (`visibility: private-known`) and you can cite a source. If the program is secret, omit `name` and set `visibility: undisclosed`.
- Ikke legg til en virksomhet bare fordi du synes de *burde* hatt et program. De må faktisk ha en publisert kanal for rapportering.
  Don't add an organization just because you think they *should* have a program. They need an actual published reporting channel.

## Forhåndsvise lokalt / Preview locally

```sh
pip install pyyaml
python3 scripts/render.py
```

Kjør `python3 scripts/render.py --check` for å se om `README.md` er i sync med `programs.yaml` uten å skrive noe.

Run `python3 scripts/render.py --check` to see whether `README.md` is in sync with `programs.yaml` without writing anything.

`python3 scripts/check_links.py` sjekker at alle lenker i `programs.yaml` fungerer. Den kjører også automatisk hver uke.

`python3 scripts/check_links.py` checks that every link in `programs.yaml` works. It also runs automatically every week.

## Lisens / License

Ved å bidra godtar du at bidraget ditt publiseres under [CC0 1.0](LICENSE) (fritt for alle formål).

By contributing you agree that your contribution is published under [CC0 1.0](LICENSE) (free for any purpose).
