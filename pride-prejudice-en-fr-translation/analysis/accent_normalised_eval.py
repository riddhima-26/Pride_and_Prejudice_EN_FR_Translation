"""Accent-insensitive re-scoring of the test translations.

The French side of the OPUS Books edition of Pride and Prejudice has lost several characters
(e.g. "à" -> "a", "è"/"ê" -> "e", "œ" -> "o", so "sœur" appears as "sour"), while "é" is kept.
Systems that write correct French are therefore penalised. This script strips diacritics and maps
œ/æ -> o/a on BOTH hypotheses and references, then recomputes BLEU and chrF.

Usage (from the repository root):  python analysis/accent_normalised_eval.py
"""
import re, unicodedata
import pandas as pd, sacrebleu

def norm(s):
    s = str(s).replace("œ", "o").replace("Œ", "O").replace("æ", "a").replace("Æ", "A")
    s = s.replace("’", "'").replace("‘", "'")
    s = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", s).strip()

t = pd.read_csv("results/test_translations.csv", keep_default_na=False)
refs = [norm(r) for r in t.reference]
raw = pd.read_csv("results/metrics.csv").set_index("system")
rows = []
for system in t.columns[2:]:
    hyps = [norm(h) for h in t[system]]
    rows.append({"system": system,
                 "BLEU (original)": raw.loc[system, "BLEU"], "chrF (original)": raw.loc[system, "chrF"],
                 "BLEU (accent-insensitive)": round(sacrebleu.corpus_bleu(hyps, [refs]).score, 2),
                 "chrF (accent-insensitive)": round(sacrebleu.corpus_chrf(hyps, [refs]).score, 2)})
out = pd.DataFrame(rows).set_index("system")
out.to_csv("results/accent_normalised_scores.csv")
print(out.to_string())
