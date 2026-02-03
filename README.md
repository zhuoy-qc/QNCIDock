To use our method to perfrom docking, you need to prepare protanated protein in pbd format and ligand intial position in sdf format. 


🧬 Pi-cation-Dock 
Our code applys to any protein pocket contains at least one postively charge amino acid. This repository provides source code for our RingDock pipepline, focusing on pi-cation interactions (cations from protein interacts with ligand aromatic rings). Other non-colvaent interactions developing...

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

## Run with preprocess data 
In this section, we demonstrate how to use our codes on a proceessed dataset (DockGen dataset with all pi-cation complexes). First, unzip the .zip file. 


For demonstration, we provide preprocessed data (protein protanated, ligand in sdf format) for the Dockgen Dataset with all-pication interactions complexes included. This section will demonstrate how to run our docking pipeline and evaluat performance. 




## Protanate protein and prepare for out pipele
To run the full pipeline on a dataset like PoseBuster:

Download the dataset of interest.cd to the directory containing all PDB ID dirs.RUN move.py to move the dir containing PI-CATION interaction to "with_pication" dir. 
cd to "with_pication" dir


Run the following scripts in that directory:

python pi-cation-analysis.py, which finds all pi-cation interactions and list the distance,offset,Rz of these interactions.
python 1_sampling.py

python 2_model.py




## Run our pipepline example on a single protein docking task 
You can also analyze individual PDB files using the utilities provided:

Navigate to the utils/ directory.

We provide examples on several PDB files, and provide codes to reproduce our paper results.


📊 Output & Evaluation
The analysis codes include:

Compute Recovery rate for π-cation interactions

## Citation 
Please cite our paper if you find it helpful. Thank you!

## OS
The code has been tested on CentOS Linux Version 8.

## Acknowledgement


