import copy
from moea_gcis.core.utility import fetch_api, save_json_to_file


GCIS_HOST = "https://gcis.nat.gov.tw"


def fetch_cod_data(gcis_host: str = GCIS_HOST):
    """
    大類 Section
    中類 Division
    小類 Group
    細類 Class
    """
    print("\n=== Fetching COD Data ===")

    # fetch section codes
    section_code_list = fetch_section_codes(gcis_host)

    # fetch division, group
    child_list_by_section = fetch_child_codes(gcis_host, section_code_list)

    # fetch full codes


def fetch_section_codes(gcis_host):
    print("\n=== Fetching Section Codes ===")
    response = fetch_api(f"{gcis_host}/elawCodAp/api/codeSearch/getAllMainCode")

    # save raw response
    save_json_to_file(response, "data/cod/main_code/raw_main_code.json")

    # save processed section list
    section_full_list = response
    save_json_to_file(section_full_list, "data/cod/1_section_code.json")

    # extract section code list
    section_code_list = [item["code"] for item in section_full_list]
    print(section_code_list)
    return section_code_list


def fetch_child_codes(gcis_host, section_code_list):
    print("\n=== Fetching Child Codes ===")
    full_child_list = []
    for section_code in section_code_list:
        response = fetch_api(
            f"{gcis_host}/elawCodAp/api/codeSearch/getAllChildCode?mainCode={section_code}"
        )
        # save raw response
        save_json_to_file(
            response, f"data/cod/child_code/raw_child_code_{section_code}.json"
        )
        # append to full list
        full_child_list.append(response)
        print(
            f"Section {section_code} has {len(response['codeSearchDto'])} division codes"
        )

    # save full raw child list
    save_json_to_file(full_child_list, "data/cod/child_code/all_child_code.json")
