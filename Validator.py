from rdkit import Chem
from rdkit.Chem import Descriptors, QED, rdMolDescriptors

def validate_smiles(smiles: str):
    """Check if a SMILES string is valid."""
    try:
        m = Chem.MolFromSmiles(smiles)
        if m is None:
            return False, None
        Chem.SanitizeMol(m)
        return True, m
    except Exception:
        return False, None


def compute_descriptors(mol):
    """Compute molecular descriptors."""
    desc = {}
    desc['MolWt'] = Descriptors.MolWt(mol)
    desc['LogP'] = Descriptors.MolLogP(mol)
    desc['HBA'] = rdMolDescriptors.CalcNumHBA(mol)
    desc['HBD'] = rdMolDescriptors.CalcNumHBD(mol)
    desc['TPSA'] = rdMolDescriptors.CalcTPSA(mol)
    desc['QED'] = QED.qed(mol)
    desc['NumRotatableBonds'] = Descriptors.NumRotatableBonds(mol)
    return desc
