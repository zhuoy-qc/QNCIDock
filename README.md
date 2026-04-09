## Overview
A method trained on DLPNO-CCSD(T) dimer interaction energies for quantitatively evaluating non—covalent interaction strength and guiding docking ligand into  cationic protein binding pocket. 
To use our docking method, you need to prepare the protonated protein in PDB format and the ligand's initial position in SDF format. 

## Framework overview

![Overview](workflow.png)




## Environments
First, clone our repo. 
```bash
gh repo clone zhuoy-qc/QNCIDock
```
Then, we recommend using Conda to set up the environment.
```bash
conda env create -f QNCIDock.yml
```
```bash
conda activate QNCIDock
```

## Data Organization
PicationDock requires a specific folder structure for proper execution. The dataset should be structured as follows:
should be placed under ***/pication/.../...

- **Folder Name:** A four-character identifier,  typically matching the PDB ID and ligand ID, e.g., 6HA4_T3Y
- The following files are required in each folder named (e.g., 6HA4_T3Y)
  - `<folder_name>_ligand.sdf`      --ligand file in sdf format, used for auto-generating a docking box (default +8 on all six sides)
  - `<folder_name>_protein_protonated.pdb ` --protonated protein file in pbd format 


Ensure that all required files are present before running.


## Docking on a single protein 
We first demonstrate how to dock 6HA4_T3Y from the DockGen Dataset for you to try. First, change into the directory '*replace with your path*'/pication/Example_6HA4_T3Y
### 1. Sample
```bash
python sample_vina.py
```
 This will generate exhaust50_dock.sdf, which contains the Vina raw ranking of 50 sampled poses.
### 2. Compute the RMSD of each sampled pose for later evaluation only
```bash
python compute_rmsd_for_docked_pose.py
```
This will compute the RMSD of each sampled pose relative to the reference experimental ligand pose and save the results, including the Vina score, in a CSV file. Reference ligand pose information is only used for the evaluation of model performance.
```bash
python run_energy_prediction.py
```
### 4. Run final rerank
```bash
python  run_model_rerank.py
```
### 5. Visualize docking results 
```bash
python  print_model_final.py
```
This prints the vina and model top-4 poses 'RMSD relative to the crystal ligand poses.

## Run with a dataset 
This section demonstrates how to run our docking pipeline and evaluate its performance on a dataset. The zip files contain the dataset and all scripts needed to reproduce key paper results.
```bash
unzip Posebusters_reproduce_paper_with_codes.zip
cd PB_cationic_binding_pocket/
```


'''reference_experimental_pication_interactions_report_with_pka_filtered.csv''' This contains the experimental pi-cation interactions and is used just for evaluating the pi-cation interaction recovery rate of the dataset, except for four failed during smina sampling, which can be produced by PLIP see below sections.
```bash
python protonate_all_proteins.py
```
This protonates all protein files. (skip this step if your proteins are already protonated)

As in the single protein docking example, similar to the single protein complex docking, run the sampling first(will take some time, depending on the CPU)

```bash
nohup python sample_vina.py &
python compute_rmsd_for_docked_pose.py 
python run_energy_prediction.py
python  run_model_rerank.py
```
Then run the remaining 3 Python scripts as in the single-protein docking demonstration.  # run_energy_prediction.py will generate many plipfixed_*.pdb and *_protonated.pdb files, you can delete them after the code finishes.

For evaluation performance: 
```bash
python  evaluation_recovery_rate.py
python  evaluation_rmsd.py
```




# To extract protein with cationic binding pockets from a raw dataset: 

Download the dataset of interest. CD into that dir. 


Run the following scripts in that directory:

python pi-cation-analysis.py, which finds all pi-cation interactions and lists the distance, offset, and Rz of these interactions. 



## Dock ligand aromatic rings only 
In this section, we demonstrate how to dock aromatic rings of ligands for the Dockgen dataset, and evaluation of ring docking False Positive Postive rate and Pi-cation interaction recovery rate of docked ring poses, and errors_relative_to_experimental_inteactions.py. (reproduce paper results)

```bash
unzip Dockgen_all_with_pication_protein_protonated.zip
cd Dockgen_all_with_pication_protein_protonated
```
Before running prepare_docking_tasks.py, change the ring sdf dir to match your correct path.

```bash
python prepare_docking_tasks.py    
python sample_aromatic_ring_poses.py 
python model_predict_energies.py
```
Model_predict_energies.py will generate many plipfixed_*.pdb and *_protonated.pdb files; you can delete them after the code finishes.
For evaluation :
```bash
python count_true_negatives.py
python tight_cutoff_evaluation.py
python loose_cutoff_evaluation.py
python errors_relative_to_experimental_inteactions.py
```



## Citation 
## Citation

If you use this work, please cite:

**Quantum chemical energy-based cation-π interaction recovers protein-ligand docking poses in cationic pocket**  
Zhuo Yin, Jun Yang  
*ChemRxiv*, 2026.  
DOI: [10.26434/chemrxiv.15001781/v1](https://chemrxiv.org/doi/abs/10.26434/chemrxiv.15001781/v1)  
[PDF Download](https://chemrxiv.org/doi/pdf/10.26434/chemrxiv.15001781/v1)

### BibTeX
```bibtex
@article{doi:10.26434/chemrxiv.15001781/v1,
  author  = {Zhuo Yin and Jun Yang},
  title   = {Quantum chemical energy-based cation-π interaction recovers protein-ligand docking poses in cationic pocket},
  journal = {ChemRxiv},
  volume  = {2026},
  number  = {0409},
  year    = {2026},
  doi     = {10.26434/chemrxiv.15001781/v1},
  url     = {https://chemrxiv.org/doi/abs/10.26434/chemrxiv.15001781/v1},
}
```


### OS
The code has been tested on CentOS Linux Version 8.



