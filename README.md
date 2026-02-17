## Overview
A method trained on DLPNO-CCSD(T) dimer interaction energies for quantitively evaluate pication interaction strength and guide docking aromatic ligand into  cationic protein binding pocket. 
To use our method to perfrom docking, you need to prepare protanated protein in pbd format and ligand intial position in sdf format. 

## Framework overview
![Workflow Illustration](workflow_illustration.png)



## Environments
First, clone our repo. Then, we recommend using Conda to set up the environment.
```bash
conda env create -f picationdock.yml
```
```bash
conda activate picationdock
```

## Data Organization
PicationDock requires a specific folder structure for proper execution. The dataset should be structured as follows:
should be placed under ***/pication/.../...

- **Folder Name:** A four-character identifier,  typically matching the PDB ID and ligand ID, e.g 6HA4_T3Y
- The following files are required in each folder named (e.g 6HA4_T3Y)
  - `<folder_name>_ligand.sdf`      --ligand file in sdf format, used for auto-generate a docking box (default +8 on all six sides)
  - `<folder_name>_protein_protonated.pdb ` --protonated protein file in pbd format 


Ensure that all required files are present before running.


## Docking on a single protein 
We first demonstrate how to dock 6HA4_T3Y from Dockgen Datset for you to try. first change into the directory '*replace with your path*'/pication/Example_6HA4_T3Y
### 1. Sample
```bash
python sample_vina.py
```
 this will generate exhaust50_dock.sdf which contains vina raw ranking of 50 sampled poses.
### 2. Compute RMSD of each sampled pose for later evaluation only
```bash
python compute_rmsd_for_docked_pose.py
```
this will compute RMSD of each sampled pose compared to reference experimental ligand pose and save results containing vina score into a csv. Reference ligand pose information only used to evluation of model performance, not used as model input.
### 3. Prediction dimer interaction energies.
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
This print the vina and model top-4 poses RMSD related to cyrstal ligand poses.

## Run with preprocess dataset (Reproduce paper key results, will take some time for Vina sampling run.) 
This section will demonstrate how to run our docking pipeline and evaluate performance for a dataset. 
```bash
unzip posebusters_all_cationic_binding_pockets_complexes.zip
cd PB_cationic_binding_pocket/
```
```bash
python protonate_all_proteins.py
```

'''reference_experimental_pication_interactions_report_with_pka_filtered.csv''' This contains the experimental pi-cation interactions and is used just for evaluating the pi-cation interaction recocery rate of the dataset, can be produced by PLIP see below sections.

This protonate all protein files. (skip this step if your proteins already protonated)

```bash
python protonate_all_proteins.py
```

As in the sinlge protein docking example, similar to the single protein complex docking, run the 4 python script in order. Then run the evaluate_RMSD.py and evlaute_pi_cation_interaction_recovery rate.py




## Protanate protein and prepare for out pipele
To run the full pipeline on a unprocessed dataset like PoseBuster raw dataset:

Download the dataset of interest.cd to the directory containing all PDB ID dirs.RUN move.py to move the dir containing PI-CATION interaction to "with_pication" dir. 
cd to "with_pication" dir


Run the following scripts in that directory:

python pi-cation-analysis.py, which finds all pi-cation interactions and list the distance,offset,Rz of these interactions.
python 1_sampling.py
python 2_model.py





## Citation 
Please cite our paper if you find it helpful. Thank you!

## OS
The code has been tested on CentOS Linux Version 8.



