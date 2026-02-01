# AIR CRE SuperSheet Parser

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Production-ready parser for AIR CRE SuperSheet PDF files. Extracts industrial & land listings with intelligent column alignment, address parsing, and data normalization.

## Features

✨ **Smart Column Alignment**
- Automatically detects and fixes shifted data columns
- Handles missing office space fields
- Corrects clear height in wrong columns

🏠 **Advanced Address Parsing**
- Splits into: St#1, St#2, StreetDir, StreetName, StreetType, Unit/Bldg, City, State, Zip
- Handles complex multi-unit addresses
- Preserves original full address

📊 **Data Normalization**
- DH/GL → Separate columns (Dock High / Ground Level)
- Parking → ParkingRatio + ParkingSpaces
- Rate → Rate value + RateType (NNN, MG, IG, etc.)
- All blank values → "N/A"

💾 **Multiple Export Formats**
- CSV
- Excel (XLSX)
- JSON

## Installation

```bash
# Clone the repository
git clone https://github.com/anthony81671/air-cre-supersheet-parser.git
cd air-cre-supersheet-parser

# Install dependencies
pip install -r requirements.txt

# Install package
pip install -e .
```

## Usage

### Command Line

```bash
# Parse a PDF and export to CSV
air-cre-parse -i "supersheet.pdf" -o "./output" -f csv

# Export to Excel
air-cre-parse -i "supersheet.pdf" -o "./output" -f xlsx

# Export to JSON
air-cre-parse -i "supersheet.pdf" -o "./output" -f json
```

### Python API

```python
from src.parsers.listing_parser import ListingParser
from src.parsers.pdf_extractor import PDFExtractor

# Extract text from PDF
extractor = PDFExtractor("supersheet.pdf")
text_data = extractor.extract()

# Parse listings
parser = ListingParser()
listings = parser.parse(text_data)

# Export to CSV
parser.to_csv(listings, "output.csv")
```

## Output Schema

34 columns including:

| Column | Description |
|--------|-------------|
| AIRLink | Listing identifier |
| Market | Market region (populated from region header) |
| Submarket | Sub-market area |
| PropertyLocation | Full address |
| St#1, St#2 | Street numbers |
| StreetDir | Street direction (N, S, E, W) |
| StreetName | Street name |
| StreetType | Street type (Ave, Rd, St, etc.) |
| UnitBldg | Unit/Building number |
| City, State, Zip | Location components |
| AvailableSF | Available square footage |
| Vacant | Vacancy status (Yes/No) |
| OfficeSF | Office space SF |
| BldgSF | Total building SF |
| ClearHt | Clear height |
| DH, GL | Dock High / Ground Level doors |
| Sprinkler | Sprinkler system (Yes/No) |
| Yard | Yard type (Fncd/Pvd, etc.) |
| ConstStatus | Construction status |
| ListingStatus | Listing availability |
| Possession | Possession timeline |
| Amps | Electrical amperage |
| ParkingRatio | Parking ratio (e.g., 1.0:1) |
| ParkingSpaces | Number of spaces |
| SalePrice | Sale price (if for sale) |
| PricePerSF | Price per square foot |
| Rate | Lease rate |
| RateType | Rate type (NNN, MG, IG, etc.) |
| ListingNotes | Combined notes |
| Broker | Broker contact information |
| MarketingFlyer | Marketing flyer link |

## Project Structure

```
air-cre-supersheet-parser/
├── src/
│   ├── parsers/
│   │   ├── pdf_extractor.py      # PDF text extraction
│   │   ├── listing_parser.py     # Main listing parser
│   │   ├── address_parser.py     # Address parsing
│   │   └── field_normalizer.py   # Data normalization
│   ├── utils/
│   │   ├── constants.py          # Constants & mappings
│   │   ├── helpers.py            # Helper functions
│   │   └── validators.py         # Data validation
│   └── main.py                   # CLI entry point
├── tests/                        # Test suite
├── docs/                         # Documentation
├── data/                         # Sample data
├── requirements.txt              # Dependencies
├── setup.py                      # Package setup
└── README.md                     # This file
```

## Requirements

- Python 3.8+
- pdfplumber >= 0.9.0
- pandas >= 2.0.0
- usaddress >= 0.5.10
- See [requirements.txt](requirements.txt) for full list

## Development

```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests
pytest

# Run with coverage
pytest --cov=src tests/

# Code formatting
black src/ tests/

# Linting
flake8 src/ tests/
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## Support

For issues and questions:
- Open an [issue](https://github.com/anthony81671/air-cre-supersheet-parser/issues)
- Check existing [discussions](https://github.com/anthony81671/air-cre-supersheet-parser/discussions)

## Acknowledgments

Built for processing AIR CRE (Commercial Real Estate) SuperSheet listings.
