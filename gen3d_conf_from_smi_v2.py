#! /usr/bin/python
# 
import sys
from rdkit import Chem
from rdkit.Chem import AllChem

supplier = Chem.SmilesMolSupplier( sys.argv[1], delimiter='\t', smilesColumn=0,nameColumn=1, titleLine=True )
sdfWriter = Chem.SDWriter( sys.argv[1][:-4] + "_MMFF_gen3D.sdf")

print("NAME\t\tMMFF ENERGY")
print supplier.next()
print 1111
for i in range( len(supplier) ):
    mol = supplier[i]
    if (mol.HasProp("_Name")):
        molName = mol.GetProp("_Name")
    molH = AllChem.AddHs( mol )
    cids = AllChem.EmbedMultipleConfs(molH, numConfs=100)
    mp = AllChem.MMFFGetMoleculeProperties(molH)
    for cid in cids:
        field = AllChem.MMFFGetMoleculeForceField( molH, mp, confId = cid )
        field.Minimize()
        e = field.CalcEnergy()
        print('{0:}\t\t{1:.3f}\t\t{2:}'.format(molName, e, cid))
        sdfWriter.write(molH, confId = cid)
sdfWriter.close()

