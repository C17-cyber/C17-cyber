# C17 CYBER — PERSONALIZE THIS PROFILE

This repository is designed to be the `C17-cyber/C17-cyber` GitHub profile repository.

## How to install

1. Create a **public** GitHub repository named `C17-cyber` under your `C17-cyber` account.
2. Copy `README.md`, `assets/` and `.github/` from this package into the repository root.
3. Commit and push. Your profile will immediately display the graphics.
4. Open **Actions** → **C17 contributions animation** → **Run workflow**. This replaces the placeholder activity graph with the real animated contribution snake.
5. In **Settings** → **Actions** → **General**, ensure workflow token permissions permit repository contents to be written if the workflow cannot commit.

## Easy edits

- Top links: `tools/build.py` → `LINKS`.
- Projects/sites: `tools/build.py` → `PROJECTS`.
- Skill cards: `CAPABILITIES`.
- Labs and work: `WORK`.
- CTF / diploma / credentials: `MILESTONES`.
- Theme: `DARK` and `LIGHT`.
- Run `python tools/build.py` to recreate the graphics and README.

**Current links to review:** `imortel.fr` portfolio and `linkedin.com/in/imortel` were previously associated with your online profile. Update them if they no longer represent your new C17 identity.

**Accuracy:** Hackerverse ranking is a user-reported result, not independently verified by this generator. The BTS SIO SISR is a diploma, not an industry cybersecurity certification. Research topics are interests, not proof of completed cryptography implementations. C17Chat / UberBoxing are marked in development, not as publicly shipped products.

**Technical note:** GitHub README pages support images, SVG and animated SVG, but not arbitrary React, JavaScript or Three.js execution. Assets are self-contained and require no external image service. Only the scheduled snake uses a GitHub Action and a third-party open-source generator.

**Design:** layout closely follows the reference's overall section arrangement: hero → links → current status → 3-column projects → offerings/focus → selected work → toolbox → contribution snake → CTA. Artwork and editorial text are original to C17 Cyber.
