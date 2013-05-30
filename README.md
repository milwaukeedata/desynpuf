# desynpuf

This repository creates and stores CSV (comma separated value) files containing Medicare data. The data has been anonymized by the Centers for Medicare & Medicaid Services, which is why they call it "data entrepreneur's synthetic public use files", or 'desynpuf' for short.

This README.md will do little to enlighten you, but it will point to other resources you might find useful. However, I will warn you that this is a large repository. You may wish to consider downloading limited data sets rather than cloning the whole repository.

The CMS.gov source data - which is not included in this repository, primarily because of the size of their complete data set - is available at this address:

http://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/SynPUFs/DE_Syn_PUF.html

This data represents benefits, claims, and prescription drug events for 2008 through 2010 for roughly 40 million people. The data is broken into 20 sample sets, each of which has 8 zip files each containing a portion of the data.

If you want to work with the source data, by all means do that. The CMS has a number of resources to help:

* CMS Data Disclaimer - User Agreement - Public Use Data [PDF, 124KB] (http://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/BSAPUFS/Downloads/PUF_Disclaimer.pdf)
* DE 1.0 Data Users Document [PDF, 988KB] (http://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/SynPUFs/Downloads/SynPUF_DUG.pdf)
* DE 1.0 Codebook [PDF, 801KB] (http://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/SynPUFs/Downloads/SynPUF_Codebook.pdf)
* DE 1.0 Frequently Asked Questions [PDF, 147KB] (http://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/SynPUFs/Downloads/SynPUF_FAQ.pdf)

The data that's actually in this repository represents twenty sample data sets, each a subset of the complete data set. Each sample data set contains all of the records from 2008, 2009, and 2010 for 20,000 patients. All records provided by the CMS data sets for each patient are included in the sample set that contains that patient. So for example, if you look at the (anonymized) patient data in the directory 1-sample-10000, you'll find all of the records for 10,000 patients. Any patient represented in the first sample set (1-sample-10000) will not reappear in any other sample set. 

UPDATE: There are only 18 sets at this point because samples 11 and 17 both contained corrupt Zip files, so I skipped them.

The Python code used to download and extract the data (sources.py), and create the sample data sets (make_samples.py) is provided for your review. If you see reason to suspect the selection protocol, please open an issue or a pull-request.

## Resources
These are helpful resources to help you translate the CPT, HCPCS (procedure) and ICD-9/10 (diagnostic) codes used by medical offices to obtain reimbursement for services.
* CMS/Medicare Physician Fee Schedule Data Base Relative Value files: http://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/PhysicianFeeSched/PFS-Relative-Value-Files.html
* CMS/Medicare Physician Fee Schedule lookup: http://www.cms.gov/apps/physician-fee-schedule/overview.aspx
* ICD-9-CM Diagnosis code lookup (CDC website): http://www.cdc.gov/nchs/icd/icd9cm.htm
* The CPT (procedure) codes are managed by the AMA and information about the codes can be found here: http://www.ama-assn.org/ama/pub/physician-resources/solutions-managing-your-practice/coding-billing-insurance/cpt.page
