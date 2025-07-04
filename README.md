# Storm Eowyn Forest Loss Analysis - Ireland

<div align="center" style="background-color: #ffeb3b; padding: 10px; border-radius: 5px; margin-bottom: 20px;">
  <strong>🚧 Under Construction:</strong> This documentation page is being actively developed. Content may change frequently.
</div>

## Project Overview
Sentinel-1 InSAR coherence pipeline for quantifying forest cover loss in Ireland caused by Storm Eowyn (January 2025). Adapts an existing Borneo forest disturbance detection pipeline for Irish conditions.

## Key Features
- Automated Sentinel-1 scene catalog generation
- Optimized InSAR pair selection
- SNAP-based coherence processing
- Forest mask integration
- Change detection algorithms
- Geoparquet output catalog

## Quick Start
1. Install dependencies:
```bash
conda env create -f environment.yml
conda activate storm-eowyn
```

2. Configure credentials:
```bash
cp config.example.ini config.ini
# Edit with your ASF/Earthdata credentials
```

3. Verify setup:
```bash
python setup_check.py
```

4. Run processing:
```bash
python bin/1_generate_s1_catalog.py
```

## Directory Structure
```
├── bin/                    - Processing scripts
│   ├── 1_generate_s1_catalog.py
│   ├── 2_scene_pair_selector.py
│   └── data_preprocessing_sar/
├── src/                    - Core processing modules
│   └── sentinel1slc.py
├── data/                   - Input/output data (gitignored)
│   ├── input/             - Forest masks, reference data
│   ├── output/            - Processed results, catalogs
│   └── temp/              - Temporary processing files
├── docs/                   - Project documentation
│   └── setup.md           - Detailed setup guide
├── tests/                  - Unit and integration tests
├── config.example.ini      - Configuration template
├── environment.yml         - Conda environment
├── setup_check.py          - Setup verification script
├── .gitignore             - Git ignore rules
└── README.md              - This file
```

## Dependencies
- Python 3.9+
- SNAP 8.0+
- ESA SNAPPY Python bindings
- ASF Search API
- GeoPandas, PyArrow, Rasterio

## License
MIT
