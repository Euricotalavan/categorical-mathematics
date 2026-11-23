# 數學語言壓縮與自然分頁研究

> **公開整理 v1｜2026-11-18。** 本研究原先只做比較與隔離試驗；研究完成後，使用者另明確授權把結果提交 PR #1。本次只發布研究文字、結構化紀錄與診斷工具。正式 ReadFlow R1 已採納；以下新提案未採納，A／B 工作流與正式／凍結稿不變。
>
> 沒有新人類閱讀／理解／應用／保留測試，沒有「已穩定90分」的結論。本公開目錄不附私人原始PDF、完整教材、字型或恢復入口，不能單靠本目錄重建全部歷史頁面。固定比較基線仍為 `4076cc01c41106be449ccd02e9c494a829bdd5f2`。

## 先看這三個結果

1. P3把超過1750字元的頁數從164降到0，頁數841→886，使用者評價卻由70降至68。原PDF可定位短題解分離、表格與要求分頁、句中斷等代價。
2. 八案的符號化、刪重述、合併及限定版面條件，五份PDF都14頁。語義上可改，不等於一定省空間或更易讀。
3. 五組同正文版面對照有兩組2→1頁；去盒修補換到另一長例題失效且失去continued標示。成功和失敗均保存。

## 文件

- [完整研究結論](./RESULTS.md)：語言、敘事、自然分頁、AI診斷、跨卷策略及停止／採用條件。
- [實驗設計與結果](./EXPERIMENTS.md)：8案5條件、5組版面對照與57項局部數學義務。
- [實際頁面鑑識](./FORENSICS.md)：九組P2/P3案例，含來源、物理／印刷頁及前後文。
- [原創數學正反例](./LANGUAGE-EXAMPLES.md)：安全符號化、必要文字與須退數學角色的界線。
- [七組角色Prompt](./ROLE-PROMPTS.md)、[前綴審查結果](./PREFIX-REVIEW.md)與[缺陷Schema](./reading-defect.schema.json)。
- [公開交接](./HANDOFF.md)、[來源身份](./evidence/source-identities.json)、[文獻與實讀範圍](./evidence/literature.json)、[逐檔manifest](./MANIFEST.json)。

## 可執行的定位工具

需要Python與PyMuPDF。自行提供與map的SHA256相符的原始PDF：

```bash
python3 tools/reading_diagnostics.py /path/to/V0_ReadFlow_R7_P3_Reading.pdf --map tools/maps/P3-V0.json --out issues.json
```

請在本目錄執行，或加完整腳本路徑。map是檢查者看過案例後建立的定位資料，並非工具自己理解了全部數學。工具輸出CANDIDATE／UNKNOWN／身份BLOCKED；不修改PDF、不給可讀性總分。1750僅作歷史異常訊號，習題題目頁例外；混合頁仍須辨識區域。

公開檔案核驗可從repository根目錄執行：

```bash
python3 research/readability/language-pagination-20261118/verify.py
```

這只核本次公開檔身份、JSON／Python語法、相對連結與私人定位資料，不能替代數學審查或真人閱讀。

## 與先前研究的關係

[前輪S2.1／R3–R7研究](../study-20261118/RESULTS.md)保留原固定基線與結果。本研究比較基線為4076，不回寫前輪報告、原始規範或停止的候選。R1已正式採納；本研究操作提案未採納。PR繼續保持Draft，未授權合併main。
