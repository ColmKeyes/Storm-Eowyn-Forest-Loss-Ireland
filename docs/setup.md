# Setup Guide

## Prerequisites
- Conda/Miniconda installed
- SNAP 8.0+ installed with SNAPPY configured
- ASF and Earthdata accounts

## Installation Steps

1. **Clone repository**:
```bash
git clone <repository-url>
cd storm-eowyn-forest-loss-ireland
```

2. **Create conda environment**:
```bash
conda env create -f environment.yml
conda activate storm-eowyn
```

3. **Configure SNAP**:
```bash
# Verify SNAP installation
snap --version

# Configure SNAPPY (if not already done)
cd $SNAP_HOME/bin
./snappy-conf /path/to/conda/envs/storm-eowyn/bin/python
```

4. **Set up credentials**:
```bash
cp config.example.ini config.ini
# Edit config.ini with your credentials
```

5. **Test installation**:
```bash
python -c "import snappy; print('SNAPPY OK')"
python -c "import asf_search; print('ASF Search OK')"
```

## Configuration

Edit `config.ini` with:
- ASF/Earthdata credentials
- SNAP installation path
- Processing parameters
- Output directories

## Troubleshooting

### SNAP Issues
- Ensure SNAP_HOME environment variable is set
- Verify SNAPPY Python bindings are configured
- Check Java memory settings

### Memory Issues
- Increase JVM heap size in config
- Monitor system memory usage
- Use smaller processing batches
