## Overview
A method trained on DLPNO-CCSD(T) dimer interaction energies for quantitively evaluate pication interaction strength and guide docking aromatic ligand into  cationic protein binding pocket. 
To use our method to perfrom docking, you need to prepare protanated protein in pbd format and ligand intial position in sdf format. 

## Framework overview
![Workflow Illustration](workflow_illustration.png)



## Environments
First, clone our repo. Then, we recommend using Conda to set up the environment.
```bash
conda env create -f ringdock_pi-cation_env.yml
```
```bash
conda activate ringdock_pi-cation_env
```

## Data Organization
PicationDock requires a specific folder structure for proper execution. The dataset should be structured as follows:


- **Folder Name:** A four-character identifier,  typically matching the PDB ID and ligand ID, e.g 6HA4_T3Y
- The following files are required in each folder named (e.g 6HA4_T3Y)
  - `<folder_name>_ligand.sdf`      --ligand file in sdf format, used for auto-generate a docking box (default +8 on all six sides)
  - `<folder_name>_protein_protonated.pdb ` --protonated protein file in pbd format 


Ensure that all required files are present before running.


## Docking on a single protein
We first demonstrate how to dock 6HA4_T3Y from Dockgen Datset for you to try.
### 1.Sample
```bash
python vina_sample.py
```
 this will generate exhaust50_dock.sdf which contains vina raw ranking of 50 sampled poses.
 ### Compute RMSD of each sampled pose for later evaluation only
```bash
python  new_creat_rmsd_csv.py
```
this will compute RMSD of each sampled pose compared to reference experimental ligand pose and save results containing vina score into a csv. Reference ligand pose information only used to evluation of model performance, not used as model input.
### Prediction dimer interaction energies.
``bash
python  predict_interaction_energies.py
```
###Run final rerank
``bash
python  run_rerank.py
```
 this ouput final model ranking in `predictions_with_model_scores.csv`


## Run with preprocess dataset (Reproduce paper key results, will take some time for Vina sampling run.) 
For demonstration, we provide preprocessed data (protein protanated, ligand in sdf format) for the Dockgen Dataset with all-pication interactions complexes included. This section will demonstrate how to run our docking pipeline and evaluat performance.  First, unzip the .zip file. 
```bash
unzip Dockgen_all_with_pication_protein_protanated.zip
```

For demonstration, we provide preprocessed data (protein protanated, ligand in sdf format) for the Dockgen Dataset with all-pication interactions complexes included. This section will demonstrate how to run our docking pipeline and evaluat performance. 




## Protanate protein and prepare for out pipele
To run the full pipeline on a dataset like PoseBuster:

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



