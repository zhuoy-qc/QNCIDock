# Evaluate top 1-4 for both Vina and Model - Simplified Output
import pandas as pd
import warnings

# Suppress the specific FutureWarning
warnings.filterwarnings("ignore", message="DataFrameGroupBy.apply operated on the grouping columns")

# Read the CSV file
df = pd.read_csv('predictions_with_model_scores.csv')

# Sort by PDB_ID and Vina_Rank to ensure proper ordering
df_sorted = df.sort_values(['PDB_ID', 'Vina_Rank'])

# Group by PDB_ID and get top poses for both Vina and Model
def get_top_poses_by_method(group):
    results = {}
    
    # Get Vina top 1-4 (using original Vina ranking)
    vina_top4 = group.nsmallest(4, 'Vina_Rank')  # Vina ranks are already 1,2,3,4...
    
    # Get Model top 1-4 (by Model_Probability, regardless of Vina rank)
    model_top4 = group.nlargest(4, 'Model_Probability')
    
    # Store Vina top 1-4 with their RMSD
    for i in range(1, 5):
        if i <= len(vina_top4):
            row = vina_top4.iloc[i-1]
            results[f'Vina_Top{i}_Rank'] = int(row['Vina_Rank'])  # Convert to int
            results[f'Vina_Top{i}_RMSD'] = row['RMSD']
            results[f'Vina_Top{i}_Model_Prob'] = row['Model_Probability']
        else:
            results[f'Vina_Top{i}_Rank'] = None
            results[f'Vina_Top{i}_RMSD'] = None
            results[f'Vina_Top{i}_Model_Prob'] = None
    
    # Store Model top 1-4 with their RMSD
    for i in range(1, 5):
        if i <= len(model_top4):
            row = model_top4.iloc[i-1]
            results[f'Model_Top{i}_Vina_Rank'] = int(row['Vina_Rank'])  # Convert to int
            results[f'Model_Top{i}_RMSD'] = row['RMSD']
            results[f'Model_Top{i}_Model_Prob'] = row['Model_Probability']
        else:
            results[f'Model_Top{i}_Vina_Rank'] = None
            results[f'Model_Top{i}_RMSD'] = None
            results[f'Model_Top{i}_Model_Prob'] = None
    
    return pd.Series(results)

# Group by PDB_ID and get top poses
top_poses = df_sorted.groupby('PDB_ID', group_keys=False).apply(get_top_poses_by_method)

# Print detailed results for each PDB
print("=" * 100)
print("VINA vs MODEL TOP 1-4 POSE COMPARISON")
print("=" * 100)

for pdb_id in df['PDB_ID'].unique():
    pdb_data = top_poses.loc[pdb_id]
    
    print(f"\nPDB ID: {pdb_id}")
    print("-" * 70)
    
    # Vina Top 1-4
    print("VINA TOP 1-4 (Original Vina Ranking):")
    print(f"{'Rank':<6} {'Vina Rank':<10} {'RMSD (Å)':<10} {'Model Prob':<12}")
    print("-" * 45)
    for i in range(1, 5):
        vina_rank = pdb_data[f'Vina_Top{i}_Rank']
        rmsd = pdb_data[f'Vina_Top{i}_RMSD']
        model_prob = pdb_data[f'Vina_Top{i}_Model_Prob']
        
        if pd.notna(vina_rank):
            print(f"Top{i:<4} {vina_rank:<10} {rmsd:<10.3f} {model_prob:<12.4f}")
        else:
            print(f"Top{i:<4} {'N/A':<10} {'N/A':<10} {'N/A':<12}")
    
    # Model Top 1-4
    print("\nMODEL TOP 1-4 (By Model Probability):")
    print(f"{'Rank':<6} {'Orig Vina Rank':<15} {'RMSD (Å)':<10} {'Model Prob':<12}")
    print("-" * 50)
    for i in range(1, 5):
        orig_vina_rank = pdb_data[f'Model_Top{i}_Vina_Rank']
        rmsd = pdb_data[f'Model_Top{i}_RMSD']
        model_prob = pdb_data[f'Model_Top{i}_Model_Prob']
        
        if pd.notna(orig_vina_rank):
            print(f"Top{i:<4} {orig_vina_rank:<15} {rmsd:<10.3f} {model_prob:<12.4f}")
        else:
            print(f"Top{i:<4} {'N/A':<15} {'N/A':<10} {'N/A':<12}")

# Restore warnings
warnings.resetwarnings()
