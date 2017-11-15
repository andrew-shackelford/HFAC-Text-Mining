import download
import compare
import parse
import sys

def download_and_process(companyCode, cik=None):
    if cik is None:
        years = download.get_filings(companyCode)
    else:
        years = download.get_filings(companyCode, cik=cik)
    
    parse.parse_stock_multiple_years(companyCode, years)

    year_combinations = []
    for year_one in years:
        for year_two in years:
            if year_two > year_one:
                year_combinations.append((year_one, year_two))

    for year_one, year_two in year_combinations:
        compare.compare_stock(companyCode, year_one, year_two)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        download_and_process(sys.argv[1])
    else:
        download_and_process(sys.argv[1], cik=sys.argv[2])