import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from ingest.semantic_scholar import fetch_research_papers
from rag.llm import summarize
from chem.Generator import random_small_molecule, generate_from_scaffold
from chem.validator import validate_smiles, compute_descriptors
from rdkit.Chem import Draw
import pandas as pd

st.set_page_config(layout='wide', page_title='Context-Aware AI Agent')
st.title('🧠 Context-Aware Autonomous AI Agent for Scientific Discovery')

with st.sidebar:
    st.header('🔍 Research Query')
    topic = st.text_input('Enter a scientific topic:', value="Alzheimer's disease")
    num_papers = st.slider('Number of papers to fetch', 1, 10, 5)
    gen_mode = st.selectbox('Molecule generation mode', ['random', 'scaffold'])
    scaffold = st.text_input('Scaffold SMILES :', value='CCO')
    num_mols = st.slider('Number of molecules to generate', 1, 10, 5)
    run_btn = st.button('🚀 Run Agent')

if run_btn:
    # Fetch research papers
    with st.spinner('Fetching research papers...'):
        try:
            papers = fetch_research_papers(topic, limit=num_papers)
            # Keep only valid dict entries
            papers = [p for p in papers if isinstance(p, dict)]
        except Exception as e:
            st.error(f'Error fetching papers: {e}')
            st.stop()

    if not papers:
        st.warning("❌ No valid papers found for this topic.")
    else:
        # Summarize papers
        with st.spinner('Summarizing findings...'):
            summary_text = summarize(papers, topic)
        st.subheader('🧩 AI-Generated Summary')
        st.write(summary_text)

        # Display fetched papers
        st.subheader('📚 Fetched Research Papers')
        for i, p in enumerate(papers, 1):
            title = p.get('title') or 'No title'
            abstract = p.get('abstract') or 'No abstract available'

            authors_list = p.get('authors', [])
            authors = [
                a.get('name', str(a)) if isinstance(a, dict) else str(a)
                for a in authors_list
            ]

            year = p.get('year', '?')

            st.markdown(f"**{i}. {title}**")
            st.write(abstract)
            st.write(f"📅 Year: {year} | 👩‍🔬 Authors: {authors}")
            st.markdown('---')


        # 🧪 Molecule generation
        st.subheader('🧪 Molecule Generation')
        if gen_mode == 'random':
            candidates = random_small_molecule(n=num_mols)
        else:
            candidates = generate_from_scaffold(scaffold, n=num_mols)

        records = []
        cols = st.columns(2)
        for idx, smi in enumerate(candidates):
            ok, mol = validate_smiles(smi)
            if not ok:
                continue
            desc = compute_descriptors(mol)
            desc['SMILES'] = smi
            records.append(desc)
            img = Draw.MolToImage(mol, size=(150, 150))
            with cols[idx % 2]:
                st.image(img)
                st.write(f"**SMILES:** `{smi}`")
                st.write(pd.DataFrame([desc]).T)

        if records:
            df = pd.DataFrame(records)
            st.download_button('📥 Download Molecules (CSV)', df.to_csv(index=False), file_name='molecules.csv')



