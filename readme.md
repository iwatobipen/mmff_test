3D conformer generation using MMFF
===================================
This is test project to make 3D structure using RDKit, MMFF force-field.
gen3d_conf_from_smi_v2.py is main script.

Usage
------
### Data Preparation. ###
The script need smiles.
So, SDF to smi convereter in this repo.
To use it.
```
python sdf2smi.py <yourfile.sdf>
```


### generate 3D conf from smiles. ###
Need smiles files.
File format must be <smiles> tab <id>, and has header line.
```
python gen3d_conf_from_smi_v2.py <yoursmiles.smi>
```

Dependency
-----------
RDKit
