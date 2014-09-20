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
    AllChem.EmbedMolecule( molH )
    mp = AllChem.MMFFGetMoleculeProperties(molH)
    field = AllChem.MMFFGetMoleculeForceField( molH, mp )
    field.Minimize()
    e = field.CalcEnergy()
    print('{0:}\t\t{1:.3f}'.format(molName, e))
    sdfWriter.write(molH)
sdfWriter.close()

