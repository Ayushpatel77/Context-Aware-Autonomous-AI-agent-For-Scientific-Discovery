from rdkit import Chem
import random

def mutate_smiles(smiles: str, n_mutations: int = 5):
    """Naively mutate SMILES by replacing random atoms."""
    muts = set()
    atoms = ['C', 'N', 'O', 'F', 'Cl', 'Br', 'S']
    for _ in range(n_mutations * 3):
        s = list(smiles)
        if not s:
            continue
        idx = random.randrange(len(s))
        s[idx] = random.choice(atoms)
        cand = ''.join(s)
        try:
            m = Chem.MolFromSmiles(cand)
            if m:
                smi = Chem.MolToSmiles(m)
                muts.add(smi)
        except Exception:
            continue
        if len(muts) >= n_mutations:
            break
    return list(muts)


def generate_from_scaffold(scaffold_smiles: str, n=5):
    """Generate molecules by mutating the given scaffold."""
    return mutate_smiles(scaffold_smiles, n_mutations=n)


def random_small_molecule(n=5):
    """Generate a few simple random molecules."""
    fragments = ['CCO', 'c1ccccc1', 'CCN', 'C(=O)O', 'C1CCCCC1', 'CN(C)C']
    generated = set()
    while len(generated) < n:
        a = random.choice(fragments)
        b = random.choice(fragments)
        smi = a + '.' + b
        try:
            m = Chem.MolFromSmiles(smi)
            if m:
                generated.add(Chem.MolToSmiles(m))
        except Exception:
            continue
    return list(generated)
