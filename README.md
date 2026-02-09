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

Folder Name: typically matching the PDB ID and ligand ID, e.g 6HA4_T3Y
The following files are required after rDock calculations:
<folder_name>_ligand.sdf  
<folder_name>_protein_protonated.pdb  --protonated protein file in pdb format 
Ensure that all required files are present before running.

## Docking on a single protein
We demonstrate how to dock 6HA4_T3Y from Dockgen Datset. 



## Run with preprocess data 
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



