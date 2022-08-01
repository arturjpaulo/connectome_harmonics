import s3fs

fs = s3fs.S3FileSystem(anon=True)
subject_data = fs.ls('/fcp-indi/data/Projects/HBN/CPAC_preprocessed/sub-NDARAA075AMK_ses-1')
ll = fs.ls('/fcp-indi/data/Projects/HBN/CPAC_preprocessed/sub-NDARAA075AMK_ses-1/')
file_list = []
for folder in ll: 
    file_list.append(fs.ls(f"{folder}/"))


fs.get('fcp-indi/data/Projects/HBN/CPAC_preprocessed/sub-NDARAA075AMK_ses-1/anatomical_brain/sub-NDARAA075AMK_T1w_resample_calc.nii.gz',
       'sub-NDARAA075AMK_T1w_resample_calc.nii.gz')