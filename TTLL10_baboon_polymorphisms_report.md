# TTLL10: baboon cross-species polymorphisms, their human equivalents, and what is known about their function

*Prepared 1 October 2026 for Kasper Munch. Analysis files are listed under "Methods and files" at the end.*

## Summary

- The nine cross-species polymorphic positions (0-based **111, 162, 202, 277, 344, 363, 399, 430, 439**) are positions in the **baboon (*Papio anubis*) reference TTLL10**, RefSeq isoform X1 (XP_031519257.1, 648 aa). Mapped onto human TTLL10 (UniProt Q6ZVT0, 673 aa) they are **E139, Y190, S230, D305, D372, M391, P427, A458 and K467**.
- **No published study has mutated, or reported a phenotype for, any of these positions in any species**, and none has been linked to ATP-grasp loop flexibility. What follows is the known biology of TTLL10 plus a structural and comparative analysis of the positions.
- **Baboon 439 is the site of human K467.** That is one of the two human-specific substitutions that inactivate human TTLL10 ([Rogowski et al., 2009](https://doi.org/10.1016/j.cell.2009.05.020)). The baboon reference has the ancestral T, and the alternative allele is **R**. Like human K, R is a long basic side chain, so **T439R is a strong candidate loss-of-function allele.**
- **Baboon 430 (human A458) is a P→L polymorphism.** It sits 5.8 Å from S448, the other human inactivating site, and changes a proline that is conserved in every primate except the African apes, where it independently became A.
- **Baboon 292 (a within-species polymorphism, not cross-species) maps to human G320**, a backbone-glycine in the **β5–β6 loop, the ATP-grasp loop that closes over the ATP phosphates.** It is the only polymorphic position inside that loop, and AlphaMissense gives it the maximum score (1.00).
- **The notebook's statistics used baboon positions as human positions** (`+1`). With the correct mapping, the enrichment of high AlphaMissense scores among cross-species polymorphisms is **no longer significant** (details below).

## 1. What is known about TTLL10 function

**Enzymology**
- TTLL10 is a member of the TTLL family, a group of ATP-grasp enzymes. It is the **glycine elongase**: it extends glycine side chains on tubulin and other proteins that were first started by the glycine initiases TTLL3 or TTLL8 ([Rogowski et al., 2009](https://doi.org/10.1016/j.cell.2009.05.020); [Ikegami and Setou, 2009](https://doi.org/10.1016/j.febslet.2009.05.003)).
- Mouse Ttll10 also glycylates nucleosome assembly protein 1. Its activity is lost when the active-site glutamate E499 (mouse numbering; human E511) is mutated to V ([Ikegami et al., 2008](https://febs.onlinelibrary.wiley.com/doi/10.1016/j.febslet.2008.02.079)).
- Recombinant *Xenopus* TTLL10 is stimulated by glutamylation of the tubulin tail and inhibited by existing polyglycylation ([Cummings et al., 2025](https://elifesciences.org/reviewed-preprints/98040)). That study tested no point mutants.

**Human TTLL10 is inactive**
- The human and rhesus catalytic domains differ at 11 positions, 7 of which are conserved in other species. [Rogowski et al. (2009)](https://doi.org/10.1016/j.cell.2009.05.020) introduced those 7 human residues into rhesus TTLL10 one at a time. **Two abolished activity: the human residues at 448 (S) and 467 (K).**
- Reverting both in human TTLL10 (**S448N + K467T**) restored polyglycylation. The authors concluded that monoglycylation may be enough in humans.
- *Caveat:* I could not open the full text (it is paywalled), so these details come from the abstract and excerpts. I could not check the figure or whether either reversion was tested alone in the human protein.

**Structure**
- There is no experimental structure of TTLL10. The closest mechanistic reference is mouse TTLL6, solved with ATP and analogs of the reaction intermediates ([Mahalingan et al., 2020](https://www.nature.com/articles/s41594-020-0462-0)).
- In TTLL6, ATP sits between the central and C-terminal domains. Its phosphates are held by the **β5–β6 loop (TTLL6 175–183)**. This loop:
  - is disordered without ligand and becomes ordered when ATP binds;
  - moves inward by up to about 5.7 Å when an intermediate analog binds;
  - contains Q180, which helps decide whether an enzyme initiates or elongates chains. Elongases, TTLL10 included, have Q here; the initiases TTLL3 and TTLL8 have R.
- Key TTLL6 residues whose alanine mutants lose activity: K125 and K174 (phosphate binding), R219 and R241 (which hold the transferred γ-phosphate), N264, and D346 and E359 (Mg²⁺).
- The glycine initiase TTLL3 has two insertion segments that elongases such as TTLL10 lack ([Garnham et al., 2017](https://www.pnas.org/doi/10.1073/pnas.1617286114)).

**Equivalent elements in human TTLL10** (by sequence alignment):
- β5–β6 loop = **314–322 (PTASNQGKG)**. Q319 is the elongase glutamine; G320 matches TTLL6 G181, whose backbone amide binds the β-phosphate.
- K225 ↔ TTLL6 K125, K313 ↔ K174, R379 ↔ R219, **R400 ↔ R241**, N419 ↔ N264, D498 ↔ D346, E511 ↔ E359.
- UniProt also annotates an ATP-binding motif at 362–365 (QRYI) plus 375 and 377, inferred from TTLL7.
- In the AlphaFold model the β5–β6 loop has lower confidence (pLDDT 73–82) than the surrounding core (above 90). That fits a mobile loop, but one static prediction is not a measure of dynamics.

## 2. Mapping between baboon and human TTLL10

**Which baboon reference.** *P. anubis* has six distinct TTLL10 RefSeq proteins (575–648 aa). The polymorphic positions go up to 0-based 636, and only isoform X1 (648 aa; XP_031519257.1, identical to XP_017811592.2 and XP_017811597.2) is that long. *This choice is inferred — please confirm it matches your reference.*

**Mapping rule** (baboon X1 0-based position `p` → human Q6ZVT0 1-based position):

| Baboon X1, 0-based `p` | Human |
|---|---|
| 0–38 | `p + 1` |
| 39–598 | `p + 28` |
| 599–600 (`PT`) | no human counterpart |
| ≥ 601 | `p + 26` |

**Insertions and deletions**
- **Human 40–66 (27 aa, proline-rich) is missing in baboon X1.** The segment is present in chimpanzee, bonobo, gorilla, gibbon, rhesus macaque and gelada. It is absent in orangutan, *M. fascicularis* and *Chlorocebus*. That patchy pattern points to differences in exon annotation (for example an alternative splice acceptor) rather than real deletions. It lies in the disordered N-terminal region and only affects numbering.
- **Baboon `PT` (599–600)** is present in Old World monkeys, marmoset and mouse, so it was lost on the ape lineage.

**Substitutions.** There are 73 between human and baboon. I assigned each to a lineage using great apes and gibbon, four other Old World monkeys (cercopithecids), and marmoset and mouse as outgroups.

| Arose on | Count | Positions (human numbering unless noted) |
|---|---|---|
| Human only | 12 | D2, F22, D94, H183, V371, G414, H435, **S448**, **K467**, R573, W585, L588 |
| Baboon only (differs from all other Old World monkeys) | 3 | T at human I309, C at human F353; L at human R121 (weakly supported) |
| Ape lineage (baboon ancestral) | 13 | |
| Old World monkey lineage (human ancestral) | 15 | |
| Ape vs Old World monkey, not resolvable | 30 | |

Both inactivating substitutions (S448, K467) are human-only; baboon has the ancestral N and T. **Baboon TTLL10 is therefore very likely an active elongase**, so variation in it can have functional consequences.

### All 39 baboon polymorphic positions mapped to human

`*` marks cross-species polymorphic positions. AM is the mean AlphaMissense score over the 19 substitutions of the *human* residue ([Cheng et al., 2023](https://www.science.org/doi/10.1126/science.adg7492)).

| Baboon 0-based | Baboon residue | Human | AM | Note |
|---|---|---|---|---|
| 3 | S | S4 | 0.19 | |
| 15 | T | T16 | 0.18 | |
| 16 | R | R17 | 0.23 | |
| 28 | R | R29 | 0.23 | |
| 46 | M | M74 | 0.32 | |
| 57 | Q | Q85 | 0.18 | |
| 74 | E | E102 | 0.20 | |
| 107 | A | A135 | 0.22 | |
| \*111 | E | E139 | 0.35 | |
| 125 | T | T153 | 0.13 | |
| 153 | R | R181 | 0.65 | |
| 159 | R | R187 | 0.64 | |
| \*162 | Y | Y190 | 0.77 | |
| 168 | E | E196 | 0.94 | |
| \*202 | S | S230 | 0.39 | |
| 213 | K | K241 | 0.30 | |
| 244 | H | Y272 | 0.18 | ape vs monkey difference |
| \*277 | D | D305 | 0.46 | |
| 278 | E | E306 | 0.40 | |
| 292 | G | **G320** | **1.00** | **in the β5–β6 (ATP-grasp) loop** |
| \*344 | D | D372 | 0.49 | |
| 362 | Y | Y390 | 0.67 | |
| \*363 | M | M391 | 0.79 | |
| 384 | D | D412 | 0.49 | |
| \*399 | P | P427 | 0.62 | |
| \*430 | P | **A458** | 0.21 | A in African apes only |
| 431 | K | K459 | 0.36 | |
| 434 | V | V462 | 0.75 | |
| \*439 | T | **K467** | 0.38 | human-only inactivating site |
| 460 | K | K488 | 0.79 | |
| 513 | L | L541 | 0.47 | |
| 519 | S | S547 | 0.50 | |
| 570 | P | P598 | 0.12 | |
| 574 | R | H602 | 0.12 | ape vs monkey difference |
| 582 | R | R610 | 0.20 | |
| 596 | L | P624 | 0.12 | ape vs monkey difference |
| 623 | D | N649 | 0.12 | ape vs monkey difference |
| 633 | G | G659 | 0.17 | |
| 636 | K | K662 | 0.22 | |

## 3. The nine cross-species polymorphic positions

How to read the table:
- **pLDDT, exposure:** from the AlphaFold model of human TTLL10 ([Jumper et al., 2021](https://www.nature.com/articles/s41586-021-03819-2); [Varadi et al., 2024](https://academic.oup.com/nar/article/52/D1/D368/7337620)). Exposure is relative solvent accessibility from DSSP.
- **Distances:** minimum heavy-atom distances in the model.
- **TTLL6:** the aligned residue in mouse TTLL6.

| Baboon 0-based (ref → alt) | Human | pLDDT, exposure | TTLL6 | Context | AM |
|---|---|---|---|---|---|
| 111 E | E139 | 45, 33% | none | just before the TTL domain (155–552); poorly modelled | 0.35 |
| 162 Y | Y190 | 95, 1% (buried strand) | W90 | N-domain core, 23 Å or more from the active site; Y in all TTLL10 orthologs | 0.77 |
| 202 S | S230 | 96, 31% (helix) | none (segment 229–235) | **5.1 Å from K225** (≙ TTLL6 K125, phosphate binding, essential); **8.4 Å from the β5–β6 loop** | 0.39 |
| 277 D | D305 | 92, 42% | R166 | a few residues before the β5–β6 loop in sequence; **5.5 Å from ATP-motif R363** | 0.46 |
| 344 D | D372 | 94, 50% (turn) | D212 | 6.7 Å from ATP-site residue 375; next to human-only V371 (baboon L) | 0.49 |
| 363 M | M391 | 98, 0% (buried strand) | R231 | central core, 17 Å from the catalytic residues | 0.79 |
| 399 P | P427 | 93, 94% (exposed turn) | S272 | surface; P in all TTLL10 orthologs | 0.62 |
| **430 P → L** | **A458** | 92, 33% (loop) | E301 | 5.8 Å from S448; contacts W452, T464, T465 | 0.21 (A458L: 0.15) |
| **439 T → R** | **K467** | 98, 28% (helix) | none (segment 463–468) | the human inactivating site; side chain packs against **F394 and H396 on the β-strand carrying catalytic R400**, plus V462–T465, R469–Q471, V563 | 0.38 (K467R: 0.09; K467T: 0.04) |

### The two alternative alleles you have

**439 T → R (human K467).**
- In rhesus, putting K at this position appears to be enough to abolish activity ([Rogowski et al., 2009](https://doi.org/10.1016/j.cell.2009.05.020)).
- R is not K, but both are long, positively charged side chains, so a similar effect is plausible.
- In the model, the 467 side chain packs against F394 and H396. Those residues sit on the same β-strand as R400, the arginine that holds the transferred γ-phosphate (TTLL6 R241; R241A drops activity to background; [Mahalingan et al., 2020](https://www.nature.com/articles/s41594-020-0462-0)). That gives one plausible structural route from this site to the active site. It is a hypothesis drawn from a static apo model, not evidence.

**430 P → L (human A458).**
- The proline is ancestral: it is present in orangutan, gibbon, Old World monkeys, marmoset and mouse. The human, chimpanzee, bonobo and gorilla lineage replaced it with A.
- So two primate lineages changed the same residue independently, 10 residues from K467 and 6 Å from S448. Both 430 and 439 contact T464/T465.
- Losing a proline in a loop usually makes the loop more flexible. Any functional effect is unknown.

**The pattern.** Two alleles shared across baboon species sit in the small region where human TTLL10 became inactive. One of them is a basic residue at the exact inactivating position. That fits the idea that **losing TTLL10 elongase activity is tolerated, and may even be favoured, in primates.**

### ATP-grasp loop flexibility

- **None of the nine cross-species positions is in the β5–β6 loop (human 314–322).** The closest are:
  - S230, 8.4 Å from the loop and next to the phosphate-binding K225;
  - D305 and D372, each about 6 Å from the ATP-binding motif;
  - indirectly, K467 (baboon 439), through its packing against the R400 strand.
- **One within-species polymorphism, baboon 292 = human G320, is in the loop itself.** G320 matches TTLL6 G181, whose backbone amide holds the β-phosphate. A loop glycine is typically needed for the backbone flexibility that lets the loop close over ATP, so almost any substitution there could change loop dynamics and ATP binding (AM 1.00). The alternative allele at 292 is not known to me.
- **No study has measured loop dynamics in TTLL10 or tested variants there.** Testable approaches: AlphaFold 3 models with ATP and Mg²⁺ for wild-type versus variant baboon TTLL10; short molecular dynamics simulations of loop ordering; or a direct activity assay (below).

## 4. Consequences for the notebook analysis

**`+1` is not a valid mapping.** The notebook converts baboon positions with `+ 1` and then looks them up in human AlphaMissense scores. The proper mapping (section 2) gives different human residues for every site after baboon position 38. I reproduced the notebook's printed p-values exactly with the `+1` mapping, which confirms that this is what it does.

| Comparison | Notebook (`+1`) | Corrected mapping |
|---|---|---|
| Mean AM: cross-species / other polymorphic / all positions | 0.60 / 0.35 / 0.43 | 0.50 / 0.37 / 0.43 |
| Mann–Whitney, cross-species > all polymorphic | p = 0.035 | p = 0.083 |
| Mann–Whitney, cross-species > all positions | p = 0.038 | p = 0.10 |
| Mann–Whitney, other polymorphic < all positions | p = 0.081 | p = 0.30 |
| Fisher, AM > 0.75, against all positions | p = 0.041 | p = 0.68 |
| Fisher, AM > 0.75, within polymorphic positions | p = 0.018 | p = 0.43 |
| High-AM cross-species positions (human numbering) | 163, 203, 364, 400, 440 | 190, 391 |
| High-AM other polymorphic positions (human numbering) | 160, 214, 385, 461 | 196, 320, 462, 488 |

So **"cross-species polymorphisms are more pathogenic" is not supported once positions are mapped correctly.** The trend is in the same direction but small and not significant with nine sites.

**Interpretation caveat.** AlphaMissense scores human sequences only, and here it is being applied to a protein that is inactive in humans. Its scores reflect constraint on the TTL fold across species. They are not predictions of the effect in baboons. At A458 and K467 the human residue is not even the baboon residue. The tool also rates the activating reversion K467T as benign (0.04). For these two sites a low score says nothing about whether the baboon alleles are harmless.

**Other notebook issues**
- The `seq` string in the notebook (`MAGGRPHPEP…`, headed as Q6ZVT0) is **not TTLL10**: it matches Q6ZVT0 at 55 of 671 positions, which is chance level. It looks like a wrong-frame translation. The `human_nucl_polymorphic` output built from it is therefore wrong.
- The project folder `/Users/kmt/py3Dmol` disappeared during this session, so the notebook has not been changed.

## 5. Suggested next steps

1. Confirm that the baboon reference is *P. anubis* RefSeq isoform X1 (XP_031519257.1), and get the alternative alleles at the remaining positions, especially 292 (human G320).
2. Re-run the notebook's statistics with the baboon-to-human mapping, and replace `seq` with the Q6ZVT0 sequence.
3. Functional test, following the Rogowski et al. (2009) assay: baboon TTLL10, wild-type versus T439R, P430L and the double mutant, plus the variant at 292, co-expressed with TTLL3 or TTLL8 in cells, reading out polyglycylation.
4. Structural follow-up: AlphaFold 3 models of baboon TTLL10 with ATP and Mg²⁺ for each variant, focusing on the β5–β6 loop and the R400 strand.

## Methods and files

**Sequences**
- Human TTLL10: UniProt Q6ZVT0.
- Baboon: *P. anubis* RefSeq, all TTLL10 isoforms.
- Other primates: longest RefSeq TTLL10 protein for *Pan troglodytes*, *P. paniscus*, *Gorilla gorilla*, *Pongo abelii*, *Nomascus leucogenys*, *Macaca mulatta*, *M. fascicularis*, *Chlorocebus sabaeus*, *Theropithecus gelada* and *Callithrix jacchus* (whose RefSeq model is flagged "LOW QUALITY").
- Mouse Ttll10: UniProt A4Q9F3.
- Paralogs: mouse TTLL6 (A4Q9E8), human TTLL7 (Q6ZT98), human TTLL3 (Q9Y4R7), *Xenopus tropicalis* TTLL10.

**Alignments.** MAFFT L-INS-i ([Katoh and Standley, 2013](https://doi.org/10.1093/molbev/mst010)), one alignment of primates plus mouse and one of TTLL10 with its paralogs.
- Equivalences between paralogs are by sequence, not structural superposition. They are reliable in the conserved core (the QRYI motif and the R400 strand align exactly) and weaker inside the TTLL10-specific segments.
- Lineage assignments use outgroup parsimony and depend on the RefSeq gene models.

**Structure.** AlphaFold DB model AF-Q6ZVT0-F1 v6: an apo prediction with no ATP. Secondary structure and exposure from DSSP ([Kabsch and Sander, 1983](https://doi.org/10.1002/bip.360221211)); distances computed with Biopython.

**AlphaMissense.** The AF-Q6ZVT0-F1 substitution table. "AM" is the mean over the 19 substitutions at a residue.

**Files** (in the session scratchpad, `/private/tmp/claude-501/-Users-kmt-py3Dmol/da3e864d-0d81-4fba-97e2-63c63668658c/scratchpad/`):

| File | Contents |
|---|---|
| `pri_aln.fa` | primate + mouse alignment |
| `aln.fa` | paralog alignment |
| `bmap.py`, `pol.py` | position mapping and lineage assignment |
| `geo.py` | structural measurements |
| `stats.py` | notebook statistics, original and corrected |
| `baboon.fa`, `prim.fa`, `seqs.fa` | input sequences |
| `ttll10.pdb`, `am.csv` | AlphaFold model and AlphaMissense table |

## References

- Cheng J, et al. (2023). Accurate proteome-wide missense variant effect prediction with AlphaMissense. *Science* 381: eadg7492. [(Cheng et al., 2023)](https://www.science.org/doi/10.1126/science.adg7492)
- Cummings SW, et al. (2025). The TTLL10 polyglycylase is stimulated by tubulin glutamylation and inhibited by polyglycylation. *eLife* reviewed preprint 98040. [(Cummings et al., 2025)](https://elifesciences.org/reviewed-preprints/98040)
- Garnham CP, et al. (2017). Crystal structure of tubulin tyrosine ligase-like 3 reveals essential architectural elements unique to tubulin monoglycylases. *PNAS* 114: 6545–6550. [(Garnham et al., 2017)](https://www.pnas.org/doi/10.1073/pnas.1617286114)
- Ikegami K, et al. (2008). TTLL10 is a protein polyglycylase that can modify nucleosome assembly protein 1. *FEBS Letters* 582: 1129–1134. [(Ikegami et al., 2008)](https://febs.onlinelibrary.wiley.com/doi/10.1016/j.febslet.2008.02.079)
- Ikegami K, Setou M (2009). TTLL10 can perform tubulin glycylation when co-expressed with TTLL8. *FEBS Letters* 583: 1957–1963. [(Ikegami and Setou, 2009)](https://doi.org/10.1016/j.febslet.2009.05.003)
- Jumper J, et al. (2021). Highly accurate protein structure prediction with AlphaFold. *Nature* 596: 583–589. [(Jumper et al., 2021)](https://www.nature.com/articles/s41586-021-03819-2)
- Kabsch W, Sander C (1983). Dictionary of protein secondary structure. *Biopolymers* 22: 2577–2637. [(Kabsch and Sander, 1983)](https://doi.org/10.1002/bip.360221211)
- Katoh K, Standley DM (2013). MAFFT multiple sequence alignment software version 7. *Mol Biol Evol* 30: 772–780. [(Katoh and Standley, 2013)](https://doi.org/10.1093/molbev/mst010)
- Mahalingan KK, et al. (2020). Structural basis for polyglutamate chain initiation and elongation by TTLL family enzymes. *Nat Struct Mol Biol* 27: 802–813. [(Mahalingan et al., 2020)](https://www.nature.com/articles/s41594-020-0462-0)
- Rogowski K, et al. (2009). Evolutionary divergence of enzymatic mechanisms for posttranslational polyglycylation. *Cell* 137: 1076–1087. [(Rogowski et al., 2009)](https://doi.org/10.1016/j.cell.2009.05.020)
- Varadi M, et al. (2024). AlphaFold Protein Structure Database in 2024. *Nucleic Acids Res* 52: D368–D375. [(Varadi et al., 2024)](https://academic.oup.com/nar/article/52/D1/D368/7337620)
