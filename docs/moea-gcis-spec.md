# 公司行號及有限合夥營業項目代碼表檢索系統

Company and Limited Partnership Business Scope Code Retrieving System

- 網站首頁 Website：https://gcis.nat.gov.tw/cod/codeSearch

## 營業項目分類 Business Scope Categories

營業項目代碼分為大類、中類、小類及細類四個層級，依序由左至右排列。

由 1 碼大寫英文字母及 6 碼數字組成，共 7 碼，定義如下：

| 中文名稱 | 網站英文名稱 | 說明                                                                           |
| -------- | ------------ | ------------------------------------------------------------------------------ |
| 大類     | Section      | 1 碼大寫英文字母                                                               |
| 中類     | Division     | 1 碼數字或大寫英文字母                                                         |
| 小類     | Group        | 2 碼數字                                                                       |
| 細類     | Class        | 3 碼數字。若尾碼為 0，表示一般業務；若尾碼為 1，表示特許業務（需先取得許可）。 |

## API Endpoints

API 的命名與網站呈現的名稱有所不同，請參考下方對應關係。

| API        | 網站                               |
| ---------- | ---------------------------------- |
| Main Code  | Section                            |
| Child Code | Section + Division + Group         |
| Full Code  | Section + Division + Group + Class |

### 取得大類代碼 Get All Main Codes

endpoint:

```
POST https://gcis.nat.gov.tw/elawCodAp/api/codeSearch/getAllMainCode
```

reponse example:

```json
[
  {
    "pkCode": 1,
    "code": "A",
    "codeName": "農、林、漁、牧業",
    "description": null,
    "codeNameE": "Agriculture, Forestry, Fishing and Animal Husbandry",
    "classMapping": null,
    "classMappingE": null,
    "permission": null,
    "link": null,
    "orgType": null,
    "orgTypeE": null,
    "descriptionE": null,
    "updateDate": null,
    "isStop": "F"
  }
]
```

### 取得中類及小類代碼 Get All Child Codes

endpoint:

```
POST https://gcis.nat.gov.tw/elawCodAp/api/codeSearch/getAllChildCode?mainCode={mainCode}
```

response example:

```json
{
  "code": "A",
  "codeName": "農、林、漁、牧業",
  "codeNameE": "Agriculture, Forestry, Fishing and Animal Husbandry",
  "description": null,
  "isStop": "F",
  "codeSearchDto": [
    {
      "code": "A1",
      "codeName": "農業",
      "codeNameE": "Agriculture",
      "description": null,
      "isStop": "F",
      "codeSearchDto": [
        {
          "code": "A101",
          "codeName": "農藝及園藝業",
          "codeNameE": null,
          "description": null,
          "isStop": "F",
          "codeSearchDto": []
        }
      ]
    }
  ]
}
```

### 取得完整代碼 Get All Full Codes

endpoint:

```
POST https://gcis.nat.gov.tw/elawCodAp/api/codeSearch/getAllFullCode?thiCode={group_code}
```

response example:

```json
[
  {
    "pkCode": 16,
    "code": "A101011",
    "codeName": "種苗業",
    "description": "依植物品種及種苗法規定，從事繁殖、輸出入、銷售種苗之事業者。",
    "codeNameE": "Seedling",
    "classMapping": "0119\t其他農作物栽培業",
    "classMappingE": "0119 Growing of Other Crops",
    "permission": "1",
    "link": "t70040",
    "orgType": null,
    "orgTypeE": null,
    "descriptionE": null,
    "updateDate": null,
    "isStop": "F"
  }
]
```
